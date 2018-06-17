import sys
import serial
import time
#compurter inteligence system goes here

#if ect


 
# Define message complete with
# carriage return at the end
message1 = input("")
 
# Configure Pi serial port
s = serial.Serial()
s.baudrate = 9600
s.timeout = 0
s.port = ("/dev/ttyAMA0")
 

s.open()
 
 
# Clear display
s.write("$$$ALL,ON\r")
time.sleep(5)
s.write("$$$ALL,OFF\r")
 
# Send message 1 to the Pi-Lite
for i in range (1,1):
	time.sleep(2)	
	s.write(message1)
