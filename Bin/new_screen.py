from os import system, name
from time import strftime
def new_screen():
    system('cls' if name=='nt' else 'clear') #turn on for non IDLE use
    print("Aperture industries terminal V.0.3	",strftime("%I:%M %p"),"\nThis program is currently experimental do 'CTRL+D' to terminate.\n")
