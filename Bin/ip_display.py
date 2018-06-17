import matrix_control as m_c
import socket
from time import sleep as s

def main():
    s(5)
    mc =  m_c.MatrixControl()
    mc.set_speed(75)
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.connect(("8.8.8.8", 80))
    ip = soc.getsockname()[0]
    soc.close()
    mc.send(ip)
    s(6)
    mc.set_speed(100)
    mc.send(ip)
