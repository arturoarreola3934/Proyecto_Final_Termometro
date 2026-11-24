const int pinTermistor = 34; // Pin analógico donde conectamos el sensor
const int pinAlarma = 2;     // LED integrado en la placa ESP32

void setup() {
  Serial.begin(115200); // Inicia la comunicación serial a 115200 baudios
  pinMode(pinAlarma, OUTPUT);
}

void loop() {

  if (Serial.available() > 0) {
    char estado = Serial.read();
    if (estado == '1') {
      tone(pinAlarma, 2000); // Genera un pitido agudo de 2000 Hz
    } else if (estado == '0') {
      noTone(pinAlarma);     // Silencia el buzzer
    }
  }
  
  // Leemos el valor crudo del ADC (0 a 4095)
  int lecturaADC = analogRead(pinTermistor);
  
  // Enviamos el dato a la computadora por USB
  Serial.println(lecturaADC);
  
  // Revisamos si Python nos mandó una señal de alerta ('1' = fiebre, '0' = normal)
  if (Serial.available() > 0) {
    char estado = Serial.read();
    if (estado == '1') {
      digitalWrite(pinAlarma, HIGH); // Enciende alarma/LED
    } else if (estado == '0') {
      digitalWrite(pinAlarma, LOW);  // Apaga alarma/LED
    }
  }
  
  delay(1000); // Espera 1 segundo antes de la siguiente lectura
}