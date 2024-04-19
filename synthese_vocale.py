import os
import speech_recognition as sr

class SyntheseVocale:
    def __init__(self):
        self.directory = os.path.dirname(os.path.abspath(__file__))  # Chemin absolu du répertoire du fichier en cours
        self.index = 1

    def transcrire_audio(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Parlez maintenant...")
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio_data, language="fr-FR")
            print("Transcription: ", text)
            return text
        except sr.UnknownValueError:
            print("Impossible de comprendre l'audio")
            return None
        except sr.RequestError as e:
            print("Erreur lors de la reconnaissance vocale: ", e)
            return None

    def enregistrer_synthese(self, texte):
        filename = f"patient-text{self.index}.txt"
        filepath = os.path.join(self.directory, filename)
        
        # Vérifier si le fichier existe déjà
        while os.path.exists(filepath):
            self.index += 1
            filename = f"synthese_{self.index}.txt"
            filepath = os.path.join(self.directory, filename)

        with open(filepath, "w") as f:  # Utiliser le mode "w" pour créer un nouveau fichier
            f.write(texte + "\n")
