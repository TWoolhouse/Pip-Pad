import socket
import _thread
from time import sleep

server_addr = "109.156.206.253"
sever_port = 53337

class Client:

    def __init__(self, name):
        self.name = name
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.client_socket:
            self.client_socket.connect((server_addr, sever_port))
            self.setup = self.client_socket.recv(1024).decode().split("!#!")
            self.command_char = self.setup[0]
            self.commands = self.setup[1]
            print(self.setup[-1])
            self.client_socket.send(self.name.encode())

            _thread.start_new_thread(self.send, tuple())
            self.recv()
            self.client_socket.close()

    def send(self):
        while True:
            self.user_input = input("> ")
            self.client_socket.send(self.user_input.encode())
            if self.user_input == self.command_char+"close":
                break
            sleep(0.1)

    def recv(self):
        while True:
            self.data = self.client_socket.recv(1024).decode()
            if self.data != "":
                self.data = self.data.split("!#!")
                print("\n[{}]: {}".format(self.data[0], self.data[1]))
                if self.data[0] == "TCP_TD":
                    break


def main():
    Client(input("Please enter your name:\n"))

