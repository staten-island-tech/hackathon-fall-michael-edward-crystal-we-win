import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
screen_center = 640, 360
#log in system

font = pygame.font.SysFont('Arial', 40)
text = 'Enter your username and password.'
text_surface = font.render(text, True, 'white')
text_rect = text_surface.get_rect(center=(640, 100))

def draw_text(surface, text, font, color, center_x, center_y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(center_x, center_y))
    surface.blit(text_surface, text_rect)

def draw_centered_rect(surface, color, width, height, center_x, center_y):
    rect_x = center_x - (width // 2)
    rect_y = center_y - (height // 2)
    pygame.draw.rect(surface, color, (rect_x, rect_y, width, height))

while running:
    screen.fill('black')
    draw_centered_rect(screen, 'white', 300, 200, 640, 360)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(text_surface, text_rect)
    pygame.display.flip()