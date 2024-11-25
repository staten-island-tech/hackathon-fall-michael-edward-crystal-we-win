import librosa #https://librosa.org/doc/latest/index.html
import numpy as np
import matplotlib.pyplot as plt
import random
import bisect
import asyncio

class MAP:
    def __init__(self,name, mp3path: str,* , songStruct: dict = None, customKeys: list[str] = None) -> None:
        self.name = name
        self.mp3path = mp3path
        self.songStruct = songStruct or None
        self.KEYS = customKeys or ["W","A","S","D"]

    def fourier_transform(self) -> list: #what type is a db scaled spectogram ???????>
        y, sr = librosa.load(self.mp3path, sr=None) 
        D = librosa.stft(y) #returns matrix (scary), abs is just doing linear algebra (thats also scary) (determinant of big scary matrix)
        return [librosa.amplitude_to_db(np.abs(D), ref=np.max), sr]
        
    def plot_fourier(self) -> None:
        fourier = self.fourier_transform()
        plt.figure(figsize=(12, 8))
        librosa.display.specshow(fourier[0], x_axis='time', y_axis='log', sr=fourier[1])
        plt.colorbar(format='%+2.0f dB')
        plt.title('Spectrogram of the MP3 File')
        plt.show()
    
    def get_tempo_beats(self) -> list[int]:
        y, sr = librosa.load(self.mp3path, sr=None) 
        tempo, beatTimes = librosa.beat.beat_track(y=y, sr=sr)
        return tempo, librosa.frames_to_time(beatTimes, sr=sr) 

    def map(self) -> list[dict]:
        gmap = []
        
        tempo,clicktimes = self.get_tempo_beats()
        tempo = int(tempo[0])

        for i, time in enumerate(clicktimes):
            gmap.append((round(float(time),3) - 1280/750 ,random.choice(self.KEYS)))

        difficulty = 'filler'
        note_density =  (int(clicktimes[-1]) if clicktimes.size > 0 else 0)/500
        key_diversity =  max(0, len(set(self.KEYS)) / 4 - 0.5) 

        if key_diversity > 0.5:
            key_diversity = float(round(1 - np.exp(-0.916 * (len(self.KEYS) - 4)), 2))

        difficultyValue =  float(0.6 * (tempo / 180) +   0.3 * note_density +  0.1 * key_diversity)  
        difficulties = [('Cakewalk',0),('Easy',0.3),("Medium",0.45),("Hard",0.65),("Hell",0.85),(":(",0.925),("Arbitary Max",1.01)]
        
        for i in difficulties:
            if difficultyValue > i[1]: difficulty = i[0]
            else: pass
            
        return [
            {
              "Name": self.name,
              "Tempo": tempo,
              "Difficulty": {difficulty: difficultyValue}
            },
            gmap
        ]
    
async def check_input(time: float, key: str, map: list[tuple[float, str]]) -> float | None: #runtime 5ms i think thats ok
    PERFECT = 0.05
    GOOD = 0.1
    OK = 0.15
    BAD = 0.2

    beat_times = [beat_time for beat_time, beat_key in map if beat_key == key]

    if not beat_times:
        return -1, None

    # Binary search for the closest time (i didnt do this, chatgpt did.)
    idx = bisect.bisect_left(beat_times, time)

    closest_diff = float('inf')
    if idx < len(beat_times):
        closest_diff = abs(time - beat_times[idx])
    if idx > 0:
        closest_diff = min(closest_diff, abs(time - beat_times[idx - 1]))

    if closest_diff <= PERFECT:
        return 1.0, beat_times[idx]
    elif closest_diff <= GOOD:
        return 0.8, beat_times[idx]
    elif closest_diff <= OK:
        return 0.5, beat_times[idx]
    elif closest_diff <= BAD:
        return 0.2, beat_times[idx]
    else:
        return -1, beat_times[idx]

    

    