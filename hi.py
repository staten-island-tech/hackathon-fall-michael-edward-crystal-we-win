import pygame

pygame.init()
backgroundcolor = (30, 37, 50)
size = (800, 800)  
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game')
x = 1
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(backgroundcolor)
    pygame.draw.rect(screen, (255, 0, 0), (200, 200, 1000, 100)) # color,  (x, y, width, height)


    pygame.draw.circle(screen, (0, 255, 0), (300, 300), 50) # color, coordinates, size


    pygame.draw.line(screen, (0, 0, 255), (1000, 50), (200, 200), 5)  # color, coordinates of one point, coordinates of other, thickness
    
    pygame.display.update()
    x += 1
    
print(x)
   