import speech_recognition as sr

def transcribe_audio():
    recognizer = sr.Recognizer()

    # Utiliser le microphone comme source audio
    with sr.Microphone() as source:
        print("Parlez maintenant...")
        recognizer.adjust_for_ambient_noise(source)  # Ajuster le niveau de bruit du microphone
        audio_data = recognizer.listen(source)  # Capturer l'audio en temps réel

    try:
        # Transcrire l'audio en texte
        text = recognizer.recognize_google(audio_data, language="fr-FR")
        print("Transcription: ", text)
        return text

    except sr.UnknownValueError:
        print("Impossible de comprendre l'audio")
    except sr.RequestError as e:
        print("Erreur lors de la reconnaissance vocale: ", e)

def analyze_command(text):
    # Convertir le texte en minuscules pour faciliter la manipulation
    text = text.lower()

    # Définir les mots clés associés à chaque commande de mouvement
    keywords = {
        "avancer": ["avance", "avancer", "avancez", "aller en avant"],
        "reculer": ["recule", "reculer", "reculez", "aller en arrière"],
        "droite": ["droite", "à droite", "tourne à droite"],
        "gauche": ["gauche", "à gauche", "tourne à gauche"],
        "stop": ["stop", "arrêt"]
    }

    # Parcourir les mots clés et identifier la commande de mouvement
    for command, key_list in keywords.items():
        for key in key_list:
            if key in text:
                return command

    # Si aucun mot clé n'est trouvé, retourner "stop" par défaut
    return "stop"


def respond_to_command(text):
    # Interpréter la commande à partir du texte transcrit
    command = analyze_command(text)
    return command
