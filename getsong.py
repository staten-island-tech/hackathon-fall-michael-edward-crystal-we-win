import pytube
from pytubefix import YouTube
from pytubefix.cli import on_progress

import moviepy
import os
import inspect

def get_path() -> str: #i found this monstorsity on stackoverflow
    return os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0])))

def getSong(query, dir=f'{get_path()}\\songs') -> str:
    os.makedirs(dir, exist_ok=True)
    
    file_safe_query = "".join(c if c.isalnum() or c in " _-" else "_" for c in query)
    mp3_path = os.path.join(dir, f"{file_safe_query}.mp3")

    if os.path.exists(mp3_path):
        return mp3_path

    searched = pytube.Search(query + ' song')
    if not searched.results: return None
    
    video = searched.results[0]
    video_url = video.watch_url

    yt = YouTube(video_url, on_progress_callback = on_progress)

    video_stream = yt.streams.filter(only_audio=True).first()
    audio_path = video_stream.download(output_path=dir)
    
    with moviepy.AudioFileClip(audio_path) as audio_clip:
        audio_clip.write_audiofile(mp3_path)

    os.remove(audio_path)

    return mp3_path



