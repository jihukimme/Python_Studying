from gtts import gTTS
from playsound import playsound

file_path = r'실감미디어_프로젝트\텍스트.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')
tts.save(r'실감미디어_프로젝트\텍스트.mp3')

playsound(r'실감미디어_프로젝트\텍스트.mp3')