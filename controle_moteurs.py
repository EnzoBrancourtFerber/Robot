# Définition des fonctions de contrôle des moteurs (simulation)
def avancer():
    return "Simulation : Avancer"

def reculer():
    return "Simulation : Reculer"

def tourner_droite():
    return "Simulation : Tourner à droite"

def tourner_gauche():
    return "Simulation : Tourner à gauche"

def stop():
    return "Simulation : Stop"

# Fonction pour exécuter la commande appropriée en fonction de la direction spécifiée
def executer_commande(direction):
    if direction == "avancer":
        return avancer()
    elif direction == "reculer":
        return reculer()
    elif direction == "droite":
        return tourner_droite()
    elif direction == "gauche":
        return tourner_gauche()
    elif direction == "stop":
        return stop()
    else:
        return "Commande non reconnue"

# Appels de fonctions de contrôle des moteurs (simulation) lorsqu'elles sont appelées directement
if __name__ == "__main__":
    print(executer_commande("avancer"))
    print(executer_commande("reculer"))
    print(executer_commande("droite"))
    print(executer_commande("gauche"))
    print(executer_commande("stop"))
