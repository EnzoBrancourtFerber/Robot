import speech_recognition as sr

def transcrire_audio():
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
        return None
    except sr.RequestError as e:
        print("Erreur lors de la reconnaissance vocale: ", e)
        return None
