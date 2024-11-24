
# ChatGPT Coding Diary

## Project Name: hackathon rhtyythehm game

### Date: 11/22

---

## 1. **Make a map of a song based on its mp3**

Mapping songs takes to long :(. need to do it automatically


---

## 2. **Initial Approach/Code**

I needed to make a spectogram and graph it. Apparently librosa has fourier trnasforms that might be useful.

```python
class MAP:
    def __init__(self,name, mp3path: str,* , songStruct: dict = None, customKeys: list[str] = None) -> None:
        self.name = name
        self.mp3path = mp3path
        self.songStruct = songStruct or None
        self.KEYS = customKeys or ["Q"]

    def fourier_transform(self) -> list: #what type is a db scaled spectogram ???????>
        y, sr = librosa.load(self.mp3path, sr=None) 
        D = librosa.stft(y) #returns matrix (scary), abs is just doing linear algebra (thats also scary) (determinant of big scary matrix)
        return [librosa.amplitude_to_db(np.abs(D), ref=np.max), sr]
```

---

## 3. **Interaction with ChatGPT**

### Questions/Requests to ChatGPT
Write down the questions or requests you made to ChatGPT. 

- "How do I automatically make a map for a rhytyhme game in python based on the mp3 file?
- "How do I get the tempo of a song using librosa?

---

## 4. **ChatGPT's Suggestions/Code Changes**

Record the code or suggestions ChatGPT provided. Include any changes or improvements ChatGPT suggested and how it influenced your approach.

```python

def get_tempo_beats(self) -> list[int]:
        y, sr = librosa.load(self.mp3path, sr=None) 
        tempo, beatTimes = librosa.beat.beat_track(y=y, sr=sr)
        return tempo, librosa.frames_to_time(beatTimes, sr=sr) 

```

- What was ChatGPT's solution or suggestion? -> use librosa.getbeats()
- How did it differ from your original approach? -> it doesnt overcomplicate things HOW DID I MISS THAT

---

## 5. **Reflection on Changes**

Reflect on the changes made to your code after ChatGPT's suggestions. Answer the following questions:

- Why do you think ChatGPT's suggestions are helpful or relevant? -> Allowed me to get the proj done usings builtin functions and save time
- Did the suggestions improve your code? How? -> Yes for the above reason
- Did you understand why the changes were made, or are you still uncertain about some parts? -> I need to review the librosa docs in order to understand how exactly the function works

---

## 6. **Testing and Results**

Tested it on megalovania, its imperfect but it works pretty well



- Did you encounter any bugs or issues during testing?

no
---

## 7. **What Did You Learn?**

In this section, reflect on what you learned from this coding session. Did you gain any new insights, or were there areas you still struggled with? 

Example:
> I learned how to use Librosas features in order to automattically generate a map for a rhythm game.

---

## (CHatgpt was also used for starting me with a "template" for loadmap.py and refactoring some code)
