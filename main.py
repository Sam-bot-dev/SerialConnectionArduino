# This is for led
import serial
import time

# Replace 'COM5' with your actual port (check in Arduino IDE > Tools > Port)
arduino = serial.Serial('COM5', 9600)
time.sleep(2)  # Wait for Arduino to reset

def turn_on():
    arduino.write(b'1')  # Send byte '1'
    print("LED turned ON")
def blink():
    count=int(input("enter the times you want it to blink \n"))
    n=1
    while n<=count:
        arduino.write(b'1')
        time.sleep(1)
        arduino.write(b'0')
        time.sleep(1)
        n=n+1
def turn_off():
    arduino.write(b'0')  # Send byte '0'
    print("LED turned OFF")

# Control loop
while True:
    cmd = input("Enter command (on/off/blink/exit): ").strip().lower()
    if cmd == "on":
        turn_on()
    elif cmd == "off":
        turn_off()
    elif cmd =="blink":
        blink()
    elif cmd == "exit":
        print("Exiting...")
        break
    else:
        print("Invalid command.")
