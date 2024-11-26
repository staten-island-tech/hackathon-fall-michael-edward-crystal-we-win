import pygame
import mapping
import random
import time
import asyncio
import math
asyncio.sleep(2)

qwerty = 'qwertyuiopasdfghjklzxcvbnm'.upper()

key_positions = {}
for i in range(len(qwerty)):
      key_positions[qwerty[i]] = 700*i/len(qwerty)  

print(key_positions)
def play_music(mp3path: str) -> None:
    pygame.mixer.music.load(mp3path)
    pygame.mixer.music.play(loops=0, start=0.0)

def load_map(map: mapping.MAP) -> None:
    pygame.init()
    screen = pygame.display.set_mode((1310, 720))
    clock = pygame.time.Clock()

    map_info, beatMap = map.map()
    play_music(map.mp3path)
    hit_text = "Waiting..."
    toUpdateAsHit = []
    start_time = time.time()
    player_score = 0.0
    current_beat_index = 0
    in_map = True
    key_pressed = None
    streak = 0
    streak_multiplier = math.floor(math.log(streak + 1, 2)) if streak > 0 else 1 #floor(log2(streak + 2))
    accuracy = 1
    netscore = 0
    notespassed = 0

    notes = []
    scores = {"1.0": 'PERFECT', "0.9": 'GOOD', "0.75": "OK", "0.5": 'BAD', "-3": "MISS"} 
    font = pygame.font.SysFont("Arial", 24)  
    
    while in_map:
        timePlaying = time.time() - start_time

        while current_beat_index < len(beatMap) and beatMap[current_beat_index][0] <= timePlaying:
            beat_time, beat_key = beatMap[current_beat_index]

            y_pos = key_positions.get(beat_key.upper(), 100) 

            notes.append({
                'beat_time': beat_time,
                'beat_key': beat_key,
                'spawned_at': timePlaying, 
                'y_pos': y_pos,
                'color': [random.randint(135, 255), random.randint(50, 200), random.randint(135, 255)],
                'hit': False
            })

            current_beat_index += 1

        screen.fill((0, 0, 0))

      
        for note in notes:
        
            time_since_spawned = timePlaying - note['spawned_at']
            if note['beat_time'] + 1/(clock.get_fps() if clock.get_fps() != 0 else 1) >= timePlaying >= note['beat_time']: notespassed += 1 #im not sure what happened here

            if note['beat_time'] in toUpdateAsHit:
                note['hit'] = True

            if not note['hit'] and timePlaying > note['beat_time'] + 0.2:
                streak = 0 
                player_score = max(player_score * 0.9, player_score - 50)
                hit_text = 'MISS'
                note['hit'] = True

            x_pos = time_since_spawned * 750  
            
            pygame.draw.rect(
                screen,
                tuple([min(255, i * random.uniform(0.95, 1.05)) for i in note['color']]),
                (x_pos, note['y_pos'], 40, 15)
            )

            key_label = font.render(note['beat_key'], True, (255, 255, 255))
            screen.blit(key_label, (1280, note['y_pos']))

    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_map = False
            elif event.type == pygame.KEYDOWN:
                if pygame.K_a <= event.key <= pygame.K_z:  
                    key_pressed = chr(event.key).upper()

     
        if key_pressed:
            score, keyTime = asyncio.run(mapping.check_input(timePlaying, key_pressed, beatMap))
            netscore += score  if score != -1 else 0
            if score and score != -1 and note not in toUpdateAsHit:
                streak_multiplier = 2 * (math.floor(math.log(streak + 1, 2)) if streak > 0 else 0.5) 
                toUpdateAsHit.append(keyTime)
                player_score += 50 * score * min(streak_multiplier, 8) 
                player_score *= accuracy/100 
                streak += 1
            elif score == -1 and note not in toUpdateAsHit:
                streak = 0
                streak_multiplier = 1
                player_score = 0.8*player_score
                toUpdateAsHit.append(keyTime)

            key_pressed = None  
            hit_text = scores[str(score)]
        
        accuracy = round(100*netscore/notespassed,2) if notespassed != 0 else 0
        score_text = font.render(f"Score: {player_score:.2f}", True, (255, 255, 255))
        streak_text = font.render(f"Streak: {streak} (Multiplier: {min(streak_multiplier,8)})",True, (255,255,255))
        #hit_text = font.render(hit_text, True, (random.randint(100,255),random.randint(100,255),random.randint(100,255)))
        screen.blit(score_text, (10, 10))
        screen.blit(streak_text, (10,30))
        screen.blit(font.render(f"{hit_text} ({accuracy}%)", True, (random.randint(100,255),random.randint(100,255),random.randint(100,255))), (10,50))
        pygame.display.flip()
        clock.tick(60)  
        if timePlaying >= map_info['Length']+0.5: return [score, accuracy]


load_map(mapping.MAP('The only thing I know for real', r"C:\Users\mmati\OneDrive\Documents\GitHub\hackathon-fall-michael-edward-crystal-we-win\songs\The only thing I know for real.mp3"))
