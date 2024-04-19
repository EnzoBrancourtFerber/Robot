import os

def transcribe_text(file_path):
    try:
        with open(file_path, "r") as file:
            text = file.read()
            print("Texte transcrit :", text)
            return text
    except FileNotFoundError:
        print("Fichier introuvable :", file_path)
        return None

def analyze_command(text):
    text = text.lower()
    keywords = {
        "avancer": ["avance", "avancer", "avancez", "aller en avant"],
        "reculer": ["recule", "reculer", "reculez", "aller en arrière"],
        "droite": ["droite", "à droite", "tourne à droite"],
        "gauche": ["gauche", "à gauche", "tourne à gauche"],
        "stop": ["stop", "arrêt"]
    }

    for command, key_list in keywords.items():
        for key in key_list:
            if key in text:
                return command
    return "stop"

def generate_command(text):
    command = analyze_command(text)
    if command != "stop":
        return f"Je vais {command}"
    else:
        return "Arrêt"

# Nom du dossier contenant le fichier texte d'entrée
folder_name = "dossier_test_2_texttocommand"
# Nom du fichier texte d'entrée
input_file_name = "test2.TXT"
# Chemin vers le fichier texte d'entrée
input_file_path = os.path.join(folder_name, input_file_name)
# Chemin vers le fichier texte de sortie
output_file_path = os.path.join(folder_name, "command_output.txt")

# Transcrire le texte du fichier d'entrée
transcribed_text = transcribe_text(input_file_path)

# Générer la commande en fonction du texte transcrit
command = generate_command(transcribed_text)

# Écrire la commande dans le fichier de sortie
try:
    with open(output_file_path, "w") as output_file:
        output_file.write(command)
    print("Commande générée :", command)
except Exception as e:
    print("Erreur lors de l'écriture du fichier de sortie :", e)