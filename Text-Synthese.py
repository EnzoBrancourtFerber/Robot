import requests
import json

api_key = "sk-proj-tK99HqsNsH7OgUeNgZX2T3BlbkFJ0tEnv3o3joooEhNN6ZQt"
fichier_txt = "texte_entree.txt"

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

texte = read_text_file(fichier_txt)

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": f"Résumer ce texte: {texte}"}],
    "max_tokens": 100
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)

if response.status_code == 200:
    response_data = response.json()
    fichier = open("resume.txt", "w")
    fichier.write(response_data["choices"][0]["message"]["content"])
    fichier.close()
    print("Le résumé à été crée")
else:
    print(f"Failed with status code {response.status_code}")
    print("Response text:", response.text)