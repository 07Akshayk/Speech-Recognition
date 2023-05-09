from gtts import gTTS
import os

mytext = "I am dead!"
audio = gTTS('hello', lang="en", slow=True)

audio.save("example.mp3")
os.system("start example.mp3")