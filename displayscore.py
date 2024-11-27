import pygame
import time

def display_results(score, accuracy, window_size=(800, 600), font_name='Arial', font_size=50):
    pygame.init()

    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Rhythm Game Results")

    font = pygame.font.SysFont(font_name, font_size)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    accuracy_text = font.render(f"Accuracy: {accuracy:.2f}%", True, (255, 255, 255))

    prompt_text = font.render("Press ENTER to return to main screen", True, (125, 0, 200))

    score_pos = score_text.get_rect(center=(window_size[0] // 2, window_size[1] // 3))
    accuracy_pos = accuracy_text.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
    prompt_pos = prompt_text.get_rect(center=(window_size[0] // 2, window_size[1] * 3 // 4))

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Press Enter to return
                    return None

        # Clear screen
        screen.fill((0, 0, 0))  # Black background

        # Draw text
        screen.blit(score_text, score_pos)
        screen.blit(accuracy_text, accuracy_pos)
        screen.blit(prompt_text, prompt_pos)

        # Update display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()
