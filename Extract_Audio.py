import moviepy as mp
import imageio
from moviepy.editor import *

sound = AudioFileClip("/content/drive/MyDrive/video.mp4")
newsound = sound.subclip("00:00:10","00:01:50")   #cut audio from video at 10-25 seconds
newsound.write_audiofile("sound2.wav", 44100, 2, 2000,"pcm_s32le")