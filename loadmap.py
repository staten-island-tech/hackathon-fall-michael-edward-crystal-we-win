import pygame
import mapping
import pytube
import os
import random

from moviepy.editor import VideoFileClip

def vid_gif(vidurl: str) -> str:
    yt = pytube.YouTube(vidurl)
    stream = yt.streams.filter(file_extension='mp4').first()
    name = f'{random.randint(1, 10**10)}.mp4'
    stream.download(filename=name)
    clip = VideoFileClip(name)
    name = name.replace('mp4','gif')
    clip.write_gif(name)
    return name

print(vid_gif(r'https://www.youtube.com/watch?v=wDgQdr8ZkTw'))


