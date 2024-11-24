import pygame
pygame.init()

COLORbackground = (10, 15, 26)
SIZEbackground = (1200, 800)  
screen = pygame.display.set_mode(SIZEbackground)
screen.fill(COLORbackground)
TEXTtitle = "RHYTHM game"
running = True
pygame.display.set_caption('Give Us 100. Please.')
class Game():
    def StartGame():
        pass
    
class TitleScreen():
    def DrawButton(screen, text, rect, font, base_color, hover_color, action=None):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
                
        if rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, hover_color, rect)
            for event in pygame.event.get():
                if mouse_click == True and action:  # Left mouse click
                    TitleScreen.ButtonAction(rect)
        else:
            pygame.draw.rect(screen, base_color, rect)

    
        text_surf = font.render(text, True, (150, 180, 200))
        text_rect = text_surf.get_rect(center=rect.center)
        screen.blit(text_surf, text_rect)

    def ButtonAction(rect):
        global RUNNINGtitlescreen, startbuttonclicked
        screen.fill(COLORbackground)
        RUNNINGtitlescreen = False
        pygame.display.update()
        startbuttonclicked = True
        TitleScreen.SelectMenuScreen()
    
    def OpenScreen(running):
        font = pygame.font.Font(None, 75)
        lilfont = pygame.font.Font(None, 30)
        while running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                    running = False
                    break
            rect = pygame.Rect(400, 100, 400, 100)
        
            titletext = font.render(TEXTtitle, True, (135, 225, 240))
            bytext = lilfont.render("By Michael (mostly), Edward, and Crystal", True, (255, 255, 255))
    
            circle = pygame.draw.circle(screen, (235, 243, 255), (600, 800), 350, 200) 
            circleoutline = pygame.draw.circle(screen, (0, 200, 255), (600, 800), 350, 10) 
            circleoutline2 = pygame.draw.circle(screen, (0, 200, 255), (600, 800), 150, 10) 
            
            rect = pygame.Rect(400, 100, 400, 100)  
            
            text_rect = titletext.get_rect(center=(rect.centerx, rect.bottom + 50))
            bytextmap = bytext.get_rect(center=(rect.centerx, rect.bottom + 150))
            screen.blit(titletext, text_rect) 
            screen.blit(bytext, bytextmap)
            
            buttonrect = pygame.Rect(400, 400, 400, 100)
            TitleScreen.DrawButton(screen, "Start Game", buttonrect, font, (60, 90, 100), (80, 120, 130), action=TitleScreen.ButtonAction(rect))
            pygame.display.update()
    
    def SelectMenuScreen():
        global RUNNINGmenuscreen, gamebuttonclicked
        RUNNINGmenuscreen = True
        gamebuttonclicked = False
        screen.fill(COLORbackground)
        songs = [{
                'name' : 'hi'
            }, {
                'name' : 'hey'
            }] 
        
        while RUNNINGmenuscreen == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNINGtitlescreen = False
                    RUNNINGmenuscreen = False
                    break
            
            ycoordinate = 10
            rect = pygame.Rect(400, 10, 400, 100)
            buttonfont = pygame.font.Font(None, 30)
        
            # replace this with loading the json
            
            TitleScreen.LoadSongButtons()
    
    
    def LoadSongButtons():
        y = 10
        songs = [{'name': 'hi'}, {'name': 'hey'}]
        mouse_pos = pygame.mouse.get_pos()  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1:  
                    for i, song in enumerate(songs):
                        rect = pygame.Rect(400, 10 + (i * 100), 400, 100)
                        if rect.collidepoint(mouse_pos):  
                            print(f"Starting song: {song['name']}")
                            TitleScreen.SongStart(song)  

        for i, song in enumerate(songs):
            rect = pygame.Rect(400, 10 + (i * 100), 400, 100)  
            if rect.collidepoint(mouse_pos):
                color = (80, 120, 130) 
            else:
                color = (60, 100, 110)
            pygame.draw.rect(screen, color, rect) 
            font = pygame.font.Font(None, 36)
            text = font.render(song['name'], True, (255, 255, 255))
            screen.blit(text, (rect.x + 10, rect.y + 30)) 
        
    def SongStart(song):
        screen.fill(COLORbackground)
        pygame.display.update()
        print(song['name'])    
        
TitleScreen.OpenScreen(running)