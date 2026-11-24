# Proyecto_Final_Termometro
En este repositorio desarrollamos la siguiente idea:
Termometro Medico Digital con Alarma y Registro de Fiebre

Por lo que decidimos en primer lugar dividir el proyecto en dos partes:
- Circuitos Electronicos: Diseñar un divisor de voltaje simple usando un Termistor NTC.
- Programacion Estructurada (Python + ESP32): El ESP32 lee el valor analogico y lo transmite por puerto serial. 
En Python, usas NumPy para convertir la lectura a grados Celsius mediante la ecuacion de Steinhart-Hart y
Pandas para generar una tabla que registre la temperatura cada minuto e indique si hay estado de fiebre.

# Materiales:
- Computadora (Para realizar el codigo)
- Cable USB
- Cables Dupont
- ESP32
- Termistor NTC 10 kOhms
- Resistencias 10 kOhms
- Buzzer activo
- Protoboard

# Circuitos Electronicos:
En esta seccion se explicara el como hacer la conexion sobre el protoboard:
1. Ocupas poner el ESP32 sobre el protoboard de tal manera que puedas hacer conexion en sus pines por ambos lados,
en caso de no poder hacerlo entonces usa dos protoboards.
2. Conecta el termistor de tal manera que una pata este conectada sobre el pin 3v3 del ESP32 y la otra pata quede
conectada en una franja libre del protoboard.
3. A continuacion conecta una resistencia de manera que una pata quede en el pin GNC del ESP32 y la otra quede 
conectada sobre la franja que estaba libre donde esta la pata del termistor colocada.
4. Despues ocupas poner un cable que conecte el pin D34 del ESP32 a la franja donde esta la union entre la
resistencia y el termistor.
5. Por ultimo se necesita conectar el Buzzer de tal manera que el pin positivo del componente se conecte al D2
del ESP32 y el pin negativo se conecte al pin GNC del ESP32.

# Programacion Estructurada:
Esta seccion es la mas extensa ya que es necesario primero instalar y preparar el entorno donde se va a desarrollar
el programa.
1. Primero se tiene que instalar visual studio y arduino en el equipo de computo.
2. Necesitas instalar los drivers del ESP32 para que el computador lo detecte.
3. En Arduino debes de autorizar las URL para actualizar el ESP32 y encontrar el modelo que utilizas.
4. Ocupas abrir el documento sketch_nov22a en Arduino y subir los datos la ESP32 mediante el cable USB.
5. Por ultimo abres el archivo script.py y lo ejecutas mientras tengas el ESP32 conectado al equipo de computo 
usando nuevamente el cable USB
