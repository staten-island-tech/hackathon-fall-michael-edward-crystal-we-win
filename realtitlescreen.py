import pygame
import json
import os
pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Game')

print(os.path.abspath('songs.json'))

class TitleScreen():
    def CreateStartGameButton():
        global running
        basecolor = (60, 100, 110)
        hovercolor = (100, 140, 150)
        buttonrect = pygame.Rect(440, 225, 400, 100)
        mouseposition = pygame.mouse.get_pos()
        buttonfont = pygame.font.Font(None, 50)
        buttontext = 'Start Game'
        buttontextsurface = buttonfont.render(buttontext, True, (235, 245, 255))
        buttontextrect = buttontextsurface.get_rect(center=buttonrect.center)   
        mouseclicked = False
             
        if buttonrect.collidepoint(mouseposition):
            print('JUMPSCARE!')
            running = False
            TitleScreen.OpenMenuScreen()
            pygame.draw.rect(screen, hovercolor, buttonrect)
            pygame.draw.rect(screen, (30, 70, 80), buttonrect, 5)

        else:
            pygame.draw.rect(screen, basecolor, buttonrect)
            pygame.draw.rect(screen, (30, 70, 80), buttonrect, 5)
        

        
        screen.blit(buttontextsurface, buttontextrect)   
    
    def OpenTitleScreen():
        global running
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
            screen.fill((0, 0, 0))
            
            pygame.draw.rect(screen, (10, 40, 50), (290, 100, 700, 100))
            pygame.draw.rect(screen, (0, 30, 40), (290, 100, 700, 100), 5)
            pygame.draw.circle(screen, (15, 15, 25), (640, 720), 300, 200)
            pygame.draw.circle(screen, (245, 245, 255), (640, 720), 300, 10)
            pygame.draw.circle(screen, (245, 245, 255), (640, 720), 100, 10)
            
            textbox = pygame.Rect(200, 150, 400, 100)
            
            titlefont = pygame.font.Font(None, 36)
            titletext = 'RHYTHM GAME by MICHAEL (edward and crystal as well)'
            titletextsurface = titlefont.render(titletext, True, (255, 255, 255))
            titletextrect = titletextsurface.get_rect(center=(640, 150))
            
            screen.blit(titletextsurface, titletextrect)
            TitleScreen.CreateStartGameButton()
            
            pygame.display.update()
    
    def OpenMenuScreen():
        newrunning = True
        while newrunning == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    newrunning = False
                    pygame.quit()
                    
            screen.fill((0, 0, 0))
            songsfont = pygame.font.Font(None, 50)
            songsrect = pygame.Rect(10, 60, 400, 50)
            songssurface = songsfont.render(f'Available Songs', True, (255, 255, 255))
            songstextrect = songssurface.get_rect(center=songsrect.center)
            pygame.draw.rect(screen, (60, 140, 150), songsrect)
            screen.blit(songssurface, songstextrect)
            
            ycoordinate = 150
            songs = [
                {'name': 'hello'}, {'name': 'hey'}
            ]
            
            for song in songs:
                songfont = pygame.font.Font(None, 30)
                songrect = pygame.Rect(10, ycoordinate, 200, 50)
                mouseposition = pygame.mouse.get_pos()
                if songrect.collidepoint(mouseposition):
                    newrunning = False
                    TitleScreen.SongConfirm(song)
                    break
                else:
                    pygame.draw.rect(screen, (60, 100, 110), songrect)
                songnamesurface = songfont.render(song['name'], True, (255, 255, 255))
                songnamerect = songnamesurface.get_rect(center=songrect.center)
                screen.blit(songnamesurface, songnamerect)
                ycoordinate += 100
            
            pygame.draw.circle(screen, (15, 15, 25), (750, 360), 300, 280)
            pygame.draw.circle(screen, (245, 245, 255), (750, 360), 320, 20)
            pygame.draw.circle(screen, (245, 245, 255), (750, 360), 40, 20)
            
            returnfont = pygame.font.Font(None, 50)
            returnrect = pygame.Rect(10, ycoordinate, 400, 50)
            returnsurface = returnfont.render(f'Return To Menu', True, (255, 255, 255))
            returntextrect = returnsurface.get_rect(center=returnrect.center)
            pygame.draw.rect(screen, (60, 140, 150), returnrect)
            screen.blit(returnsurface, returntextrect)
            if returnrect.collidepoint(mouseposition):
                screen.fill((0, 0, 0))
                newrunning = False
                TitleScreen.OpenTitleScreen()
                
            pygame.display.update()
            
    def SongConfirm(song):
        newnewrunning = True
        while newnewrunning == True:
            mouseposition = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    newnewrunning = False
                    pygame.quit()
                
            screen.fill((0, 0, 0))

            askfont = pygame.font.Font(None, 50)
            askrect = pygame.Rect(830, 20, 400, 100)
            asksurface = askfont.render(f'Start the song {song['name']}?', True, (255, 255, 255))
            asktextrect = asksurface.get_rect(center=askrect.center)
            pygame.draw.rect(screen, (60, 140, 150), askrect)
            screen.blit(asksurface, asktextrect)

            pygame.draw.circle(screen, (15, 15, 25), (350, 360), 300, 280)
            pygame.draw.circle(screen, (245, 245, 255), (350, 360), 320, 20)
            pygame.draw.circle(screen, (245, 245, 255), (350, 360), 40, 20)
            
            
            
            yesfont = pygame.font.Font(None, 30)
            yesrect = pygame.Rect(830, 130, 400, 100)  
            yessurface = yesfont.render('YES', True, (255, 255, 255))
            yestextrect = yessurface.get_rect(center=yesrect.center)  
            if yesrect.collidepoint(mouseposition):
                screen.fill((0, 0, 0))
                print(f'starting the song {song['name']}')
                newnewrunning = False
                # start game function
            else:
                pygame.draw.rect(screen, (60, 100, 110), yesrect)
            screen.blit(yessurface, yestextrect)

            nofont = pygame.font.Font(None, 30)
            norect = pygame.Rect(830, 300, 400, 100)  
            nosurface = nofont.render('NO', True, (255, 255, 255))
            notextrect = nosurface.get_rect(center=norect.center)  
            if norect.collidepoint(mouseposition):
                screen.fill((0, 0, 0))
                TitleScreen.OpenMenuScreen()
                newnewrunning = False
            else:
                pygame.draw.rect(screen, (60, 100, 110), norect)
            screen.blit(nosurface, notextrect)
                
            pygame.display.update()

TitleScreen.OpenTitleScreen()