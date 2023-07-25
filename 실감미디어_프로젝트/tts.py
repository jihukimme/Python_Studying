from gtts import gTTS
from playsound import playsound

text = "안녕하세요. 실감미디어 프로젝트 벡터팀 입니다. 저희는 영상처리를 이용하여 시각장애인의 일상생활 안전향상을 위한 프로그램을 개발중입니다."

tts = gTTS(text = text, lang="ko")
tts.save(r"실감미디어_프로젝트\실감미디어.mp3")

playsound(r"실감미디어_프로젝트\실감미디어.mp3")