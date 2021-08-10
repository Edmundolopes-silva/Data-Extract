import moviepy as mp
import imageio
from moviepy.editor import *
import speech_recognition as sr

sound = AudioFileClip("/content/drive/MyDrive/video.mp4")
newsound = sound.subclip("00:00:10","00:01:50")   #cut audio from video at 10-25 seconds
newsound.write_audiofile("sound2.wav", 44100, 2, 2000,"pcm_s32le")  #save inn '/content/Drive/MyDrive'


r = sr.Recognizer()
with sr.AudioFile('/content/drive/MyDrive/sound2.wav') as source:
    audio = r.record(source)

try:
  s = r.recognize_google(audio)
  print("Text: " + s)
except Exception as e:
  print("EXception: " + str(e))