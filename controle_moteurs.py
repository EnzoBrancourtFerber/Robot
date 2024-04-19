from gpiozero import Motor, OutputDevice
import time

# Configuration des broches GPIO pour les moteurs
PIN_MOTEUR_DROIT_AVANT = 17
PIN_MOTEUR_DROIT_ARRIERE = 18
PIN_MOTEUR_GAUCHE_AVANT = 19
PIN_MOTEUR_GAUCHE_ARRIERE = 20

# Initialisation des moteurs
moteur_droit = Motor(forward=PIN_MOTEUR_DROIT_AVANT, backward=PIN_MOTEUR_DROIT_ARRIERE)
moteur_gauche = Motor(forward=PIN_MOTEUR_GAUCHE_AVANT, backward=PIN_MOTEUR_GAUCHE_ARRIERE)

# Fonction pour avancer
def avancer():
    moteur_droit.forward()
    moteur_gauche.forward()

# Fonction pour reculer
def reculer():
    moteur_droit.backward()
    moteur_gauche.backward()

# Fonction pour tourner à droite
def tourner_droite():
    moteur_droit.forward()
    moteur_gauche.backward()

# Fonction pour tourner à gauche
def tourner_gauche():
    moteur_droit.backward()
    moteur_gauche.forward()

# Fonction pour arrêter
def stop():
    moteur_droit.stop()
    moteur_gauche.stop()

# Fonction pour exécuter la commande appropriée en fonction de la direction spécifiée
def executer_commande(direction):
    if direction == "avancer":
        avancer()
    elif direction == "reculer":
        reculer()
    elif direction == "droite":
        tourner_droite()
    elif direction == "gauche":
        tourner_gauche()
    elif direction == "stop":
        stop()
    else:
        print("Commande non reconnue")

# Appels de fonctions de contrôle des moteurs lorsqu'elles sont appelées directement
if __name__ == "__main__":
    executer_commande("avancer")
    time.sleep(2)
    executer_commande("stop")