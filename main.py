import transcription_vocale
import analyse_commande
import controle_moteurs
from synthese_vocale import SyntheseVocale

def main():
    print("Attente de la commande vocale...")

    synthese = SyntheseVocale()

    while True:
        texte = transcription_vocale.transcrire_audio()
        commande = analyse_commande.analyze_command(texte)

        if commande not in ["avancer", "reculer", "droite", "gauche"]:
            synthese.enregistrer_synthese(texte)

        if commande == "stop":
            print("Le robot s'arrête.")
            controle_moteurs.stop()
            break

        print("Commande détectée :", commande)
        controle_moteurs.executer_commande(commande)

if __name__ == "__main__":
    main()
