import librosa #https://librosa.org/doc/latest/index.html
import numpy as np
import matplotlib.pyplot as plt

class MAP:
    def __init__(self, mp3path: str,songStruct: dict = None) -> None:
        self.mp3path = mp3path
        self.songStruct = songStruct or None
        self.KEYS = ["W","A","S","D"]

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
    
    def get_tempo_beats(self) -> [int,int]:
        y, sr = librosa.load(self.mp3path, sr=None) 
        tempo, beatTimes = librosa.beat.beat_track(y=y, sr=sr)
        return tempo, librosa.frames_to_time(beatTimes, sr=sr) 

    def map(self):
        gmap = []
        
        tempo,clicktimes = self.get_tempo_beats()
        for i, time in enumerate(clicktimes):
            gmap.append(
                {
                  "Key": random.choice(self.KEYS),
                  'Time': time  
                }
            )

    
Megalovania = MAP(r"C:\Users\mike.mat\Documents\GitHub\hackathon-fall-michael-edward-crystal-we-win\songs\Toby Fox - Megalovania.mp3")
print(Megalovania.get_tempo()[0])

    