import serial
import time
import numpy as np
import pandas as pd
from datetime import datetime

PUERTO = 'COM3'  # Asegúrate de que sea tu puerto COM
BAUDIOS = 115200

# Constantes para termistor NTC de 10k (Coeficientes Steinhart-Hart)
R_FIJA = 10000.0
A = 0.001129148
B = 0.000234125
C = 0.0000000876741

registros = []

try:
    esp32 = serial.Serial(PUERTO, BAUDIOS, timeout=1)
    time.sleep(2)
    esp32.reset_input_buffer()  # Limpia datos basura iniciales
    print("Conectado al ESP32. Midiendo temperatura... (Presiona Ctrl+C o Stop para detener)")

    ultimo_guardado = time.time()

    while True:
        if esp32.in_waiting > 0:
            linea = esp32.readline().decode('utf-8', errors='ignore').strip()

            # Si viene separado por coma (ej. '716,848'), tomamos el primer valor
            if ',' in linea:
                partes = linea.split(',')
                valor_str = partes[0].strip()
            else:
                valor_str = linea

            if valor_str.isdigit():
                adc = int(valor_str)

                if 0 < adc < 4095:
                    # 1. Calcular resistencia del termistor
                    r_ntc = R_FIJA * (4095.0 / adc - 1.0)

                    # 2. Ecuación de Steinhart-Hart con NumPy
                    ln_r = np.log(r_ntc)
                    temp_kelvin = 1.0 / (A + B * ln_r + C * (ln_r ** 3))
                    temp_celsius = round(temp_kelvin - 273.15, 2)

                    # 3. Evaluar estado de fiebre y activar alarma
                    if temp_celsius >= 30:
                        estado_fiebre = "FIEBRE"
                        esp32.write(b'1')
                    else:
                        estado_fiebre = "Normal"
                        esp32.write(b'0')

                    print(f"ADC: {adc} | Temp actual: {temp_celsius} °C | Estado: {estado_fiebre}")

                    # 4. Guardar en tabla cada 60 segundos (1 minuto)
                    if time.time() - ultimo_guardado >= 60:
                        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        registros.append({
                            "Fecha_Hora": ahora,
                            "Temperatura_C": temp_celsius,
                            "Estado": estado_fiebre
                        })

                        df = pd.DataFrame(registros)
                        df.to_csv("registro_fiebre.csv", index=False)
                        print("\n--- Registro guardado en registro_fiebre.csv ---")
                        print(df.tail(5))
                        print("----------------------------------------------\n")

                        ultimo_guardado = time.time()

except KeyboardInterrupt:
    print("\nPrograma detenido por el usuario.")
finally:
    if 'esp32' in locals() and esp32.is_open:
        esp32.close()