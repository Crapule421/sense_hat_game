#Initialisation du SenseHat
from sense_hat import SenseHat
sense = SenseHat()

#Si le SenseHat est bien initialisé alors je récupère les informations
#du joystick et les print en console.
while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
