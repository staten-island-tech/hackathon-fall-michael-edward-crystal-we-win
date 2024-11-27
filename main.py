import login
import mapping
import loadmap
import getsong
import realtitlescreen as rts
import random
import displayscore as dp

print("Starting Login Flow...")
user = login.loginFlow()
print("Fin")

while True:
    song,path = rts.TitleScreen.PickaDamnSong()
    score,accuracy = loadmap.load_map(mapping.MAP(song,path, customKeys=random.choice((['W',"A","S","D"],['Q','W','E','R'],['Q','G','M']))))
    dp.display_results(score,accuracy)
 
