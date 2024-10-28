import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import sys

def extract_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        return text.strip()
    else:
        return None

def text_to_speech(text, filename='output.mp3', lang='fr'):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    print(f"Audio sauvegardé sous le nom {filename}")

url = sys.argv[1]
text = extract_text_from_url(url)

if text:
    text_to_speech(text)
else:
    print("Échec de l'extraction du texte.")

