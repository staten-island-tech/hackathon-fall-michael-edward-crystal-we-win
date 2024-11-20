import pygame
pygame.init()

COLORbackground = (10, 15, 26)
SIZEbackground = (1200, 800)  
screen = pygame.display.set_mode(SIZEbackground)
screen.fill(COLORbackground)

TEXTtitle = "RHYTHM game"
pygame.display.set_caption('Give Us 100. Please.')
class Game():
    def StartGame():
        pass
    
    
    
    
class TitleScreen():
    def DrawButton(screen, text, rect, font, base_color, hover_color, action=None):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        mouse_release = pygame.MOUSEBUTTONUP
    
        if rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, hover_color, rect)
            if mouse_click[0] and action:  # Left mouse click
                action()
        else:
            pygame.draw.rect(screen, base_color, rect)
    
        text_surf = font.render(text, True, (150, 180, 200))
        text_rect = text_surf.get_rect(center=rect.center)
        screen.blit(text_surf, text_rect)

    def ButtonAction(rect):
        pygame.draw.rect(screen, (10, 15, 26), rect)
    
    def OpenScreen():
        RUNNINGtitlescreen = True
        while RUNNINGtitlescreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNINGtitlescreen = False
    
            font = pygame.font.Font(None, 75)
            lilfont = pygame.font.Font(None, 30)
    
            rect = pygame.Rect(400, 100, 400, 100)
            startbutton = pygame.draw.rect(screen, (105, 120, 155), (400, 100, 100, 100))
            textbox = pygame.draw.rect(screen, (30, 45, 78), rect) 
            titletext = font.render(TEXTtitle, True, (135, 225, 240))
            bytext = lilfont.render("By Michael (mostly), Edward, and Crystal", True, (255, 255, 255))
    
            circle = pygame.draw.circle(screen, (235, 243, 255), (600, 800), 350, 200) 
            circleoutline = pygame.draw.circle(screen, (0, 200, 255), (600, 800), 350, 10) 
            circleoutline2 = pygame.draw.circle(screen, (0, 200, 255), (600, 800), 150, 10) 
    
            text_rect = titletext.get_rect(center=(rect.centerx, rect.bottom + 50))
            bytextmap = bytext.get_rect(center=(rect.centerx, rect.bottom + 150))
            button = TitleScreen.DrawButton(screen, "Start Game", rect, font, (60, 90, 100), (80, 120, 130), TitleScreen.ButtonAction(rect))

            
            screen.blit(titletext, text_rect) 
            screen.blit(bytext, bytextmap)
    
            pygame.display.update()
        
TitleScreen.OpenScreen()