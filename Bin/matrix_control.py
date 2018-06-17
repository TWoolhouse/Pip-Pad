import sys
import serial

class MatrixControl:

    def __init__(self):
        self.s = serial.Serial()
        self.s.baudrate = 9600
        self.s.timeout = 0
        self.s.port = "/dev/ttyAMA0"
        try:
            self.s.open()
        except serial.SerialException:  print("Sorry. Can not open serial\n")

    def send(self, text):
        self.s.write(text.encode())

    def send_cmd(self, text):
        self.send("$$$"+str(text)+"\r")

    def all_on(self):
        self.send_cmd("ALL,ON")

    def all_off(self):
        self.send_cmd("ALL,OFF")

    def set_speed(self, speed):
        self.send_cmd("SPEED"+str(speed))
