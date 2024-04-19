import speech_recognition as sr
from nltk.metrics import jaccard_distance

# Transcription audio en texte
def transcrire_audio(fichier_audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(fichier_audio) as source:
        audio_data = recognizer.record(source)

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

# Enregistrer la transcription dans un fichier texte
def enregistrer_transcription(texte, nom_fichier):
    try:
        with open(nom_fichier, "w") as f:
            f.write(texte)
        print("Transcription enregistrée dans", nom_fichier)
    except Exception as e:
        print("Erreur lors de l'enregistrement de la transcription:", e)

# Comparaison du texte transcrit avec le texte de référence
def comparer_texte(reference_text, transcribed_text):
    jaccard_similarity = 1 - jaccard_distance(set(reference_text.split()), set(transcribed_text.split()))
    if jaccard_similarity >= 0.8:
        note = "Excellent"
    elif 0.6 <= jaccard_similarity < 0.8:
        note = "Bon"
    elif 0.4 <= jaccard_similarity < 0.6:
        note = "Moyen"
    else:
        note = "Faible"

    print("Similarité de Jaccard :", jaccard_similarity)
    print("Note attribuée :", note)

# Fichier audio de test
fichier_audio = "test3.wav"

# Transcription du fichier audio
transcribed_text = transcrire_audio(fichier_audio)

# Enregistrer la transcription dans un fichier texte
if transcribed_text:
    enregistrer_transcription(transcribed_text, "test1.txt")

# Texte de référence
reference_text = "J'aimerai bien avoir du doliprane"

# Comparaison du texte transcrit avec le texte de référence
if transcribed_text:
    comparer_texte(reference_text, transcribed_text)
