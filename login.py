import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

font = pygame.font.SysFont('Arial', 40)
text = 'Enter your username and password.'
text_surface = font.render(text, True, 'white')
text_rect = text_surface.get_rect(center=(640, 100))

user_input = ''

active = False

def draw_text(surface, text, font, color, center_x, center_y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(center_x, center_y))
    text_surface.blit(text_surface, text_rect)

def draw_centered_rect(surface, color, width, height, center_x, center_y):
    rect_x = center_x - (width // 2)
    rect_y = center_y - (height // 2)
    pygame.draw.rect(surface, color, (rect_x, rect_y, width, height))

input_box = pygame.Rect(100, 100, 200, 32)

while running:
    screen.fill('black')
    draw_centered_rect(screen, 'white', 300, 200, 640, 360)
    draw_text(screen, user_input, font, 'white', input_box.centerx, input_box.centery)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = True  
            else:
                active = False
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]  
                elif event.key == pygame.K_RETURN:
                    print(f"Username entered: {user_input}")
                else:
                    user_input += event.unicode
                    

    screen.blit(text_surface, text_rect)
 
    pygame.draw.rect(text_surface, 'white', input_box)
    pygame.display.flip()
    