import pygame
import mapping
import random
import time
import asyncio
import math

from moviepy.editor import VideoFileClip


def play_music(mp3path: str) -> None:
    pygame.mixer.music.load(mp3path)
    pygame.mixer.music.play(loops=0, start=0.0)


def load_map(map: mapping.MAP) -> None:
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    # Get map information and the beatmap
    map_info, beatMap = map.map()
    play_music(map.mp3path)

    start_time = time.time()
    player_score = 0.0
    current_beat_index = 0
    in_map = True
    key_pressed = None
    streak = 0

    # Create a list of notes to track their position over time
    notes = []

    while in_map:
        timePlaying = time.time() - start_time

        # Spawn new notes based on the beat map
        while current_beat_index < len(beatMap) and beatMap[current_beat_index][0] <= timePlaying:
            beat_time, beat_key = beatMap[current_beat_index]
            
            # Track each note's start time and key
            notes.append({
                'beat_time': beat_time,
                'beat_key': beat_key,
                'spawned_at': timePlaying,  # Time when this note was spawned
                'y_pos': 100 + (ord(beat_key) - ord("A")) * 50,  # Vertical position based on key
            })
            
            current_beat_index += 1

        # Clear screen and redraw notes
        screen.fill((0, 0, 0))

        # Update and draw each note
        for note in notes:
            # Calculate how much time has passed since the note spawned
            time_since_spawned = timePlaying - note['spawned_at']

            # Move the note horizontally across the screen (left to right)
            x_pos = time_since_spawned * 100  # Adjust the multiplier for note speed
 
            # Draw the note as a red rectangle 
            print(f"Spawned note at ({x_pos}, {note['y_pos']})")
            pygame.draw.rect(screen, (255, 0, 0), (x_pos, note['y_pos'], 30, 30))

        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_map = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    key_pressed = "W"
                elif event.key == pygame.K_a:
                    key_pressed = "A"
                elif event.key == pygame.K_s:
                    key_pressed = "S"
                elif event.key == pygame.K_d:
                    key_pressed = "D"

        # Check if the player pressed a key
        if key_pressed:
            score = asyncio.run(mapping.check_input(timePlaying, key_pressed, beatMap))
            if score:
                streak_multiplier = math.floor(math.log(streak + 1, 2)) if streak > 0 else 1
                player_score += score * min(streak_multiplier, 8)  # Limit max multiplier
                streak += 1
            key_pressed = None  # Reset key press after checking

        # Display score
        font = pygame.font.SysFont("Arial", 36)
        score_text = font.render(f"Score: {player_score:.2f}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)  # Limit FPS to 60


# Start the game with a map
load_map(mapping.MAP('Megalovania', r"C:\Users\mike.mat\Documents\GitHub\hackathon-fall-michael-edward-crystal-we-win\songs\Toby Fox - Megalovania.mp3"))
