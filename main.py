from machine import Pin
from time import sleep
from BLE import BLEUART
import bluetooth

nombre= 'ESP32'
ble=bluetooth.BLE()
misuart=BLEUART(ble, nombre)

def transmito():
    buffer=misuart.read(),decode().strip()
    print(buffer)
    misuart.write("la entrega bluetooth es dentro de 8 diaas")

misuart.iqr(handler=transmito)


# Solo ejemplo de encender BLE
# Para enviar datos, deberías crear un servicio GATT personalizado
