import pygame
pygame.init()

COLORbackground = (10, 15, 26)
SIZEbackground = (1200, 800)  
screen = pygame.display.set_mode(SIZEbackground)
screen.fill(COLORbackground)

TEXTtitle = "RHYTHM game"
pygame.display.set_caption('Give Us 100. Please.')



class TitleScreen():
    def OpenScreen():
        RUNNINGtitlescreen = True
        while RUNNINGtitlescreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNINGtitlescreen = False
    
            font = pygame.font.Font(None, 75)
            lilfont = pygame.font.Font(None, 30)
    
            rect = pygame.Rect(400, 100, 400, 100)
            textbox = pygame.draw.rect(screen, (30, 45, 78), rect) 
            titletext = font.render(TEXTtitle, True, (135, 225, 240))
            bytext = lilfont.render("By Michael (mostly), Edward, and Crystal", True, (255, 255, 255))
    
            circle = pygame.draw.circle(screen, (235, 243, 255), (600, 800), 350, 200) 
            circleoutline = pygame.draw.circle(screen, (0, 200, 255), (600, 800), 350, 10) 
            circleoutline2 = pygame.draw.circle(screen, (0, 200, 255), (600, 800), 150, 10) 
    
            text_rect = titletext.get_rect(center=rect.center)
            bytextmap = bytext.get_rect(center=(rect.centerx, rect.bottom + 50))
     
            screen.blit(titletext, text_rect) 
            screen.blit(bytext, bytextmap)
    
            pygame.display.update()
        
TitleScreen.OpenScreen()