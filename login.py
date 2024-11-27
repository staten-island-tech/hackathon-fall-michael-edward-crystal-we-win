import pygame
import json
import time
import os
import inspect
print(f'{os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0])))}\\userdata.json')
with open(f'{os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0])))}\\userdata.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
 
pygame.init()

screen = pygame.display.set_mode((1280, 720))
screen.fill('black')

running = True
lastChange = 0

font = pygame.font.SysFont('Arial', 40)

page = 'Beginning'
max_text_width = 135

class Button:
    def __init__(self, x, y, width, height, bgcolor, text, text_color, font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.bgcolor = bgcolor
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.SysFont('Arial', font_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.bgcolor, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, mouse_pressed):
        if self.is_hovered(mouse_pos) and mouse_pressed[0]:
            return True
        return False


class Text:
    def __init__(self, font, text, color, x, y):
        self.font = font
        self.color = color
        self.text = text
        self.x = x
        self.y = y 
    
    def draw(self):
        text_surface = font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.x, self.y) 
        screen.blit(text_surface, text_rect)


class Login_SignUp:
    def __init__(self, signup_or_login):
        self.signup_or_login = signup_or_login

    def show(self):
        global page
        
        screen.fill('black')

        Text(font, 'Username', 'white', 540, 20).draw() 
        pygame.draw.rect(screen, 'white', username_box)

        Text(font, 'Password', 'white', 540, 300).draw()
        pygame.draw.rect(screen, 'white', password_box)

        global lastChange

        if self.signup_or_login == 'Log in' :
            go_to_signup = Button(490, 570, 300, 50, 'white', 'Go to Sign Up', 'black')
            go_to_signup.draw(screen) 
            if go_to_signup.is_clicked(mouse_pos, mouse_pressed) and time.time() - lastChange >= 1:
                page = 'Sign up'
                lastChange = time.time()
                
        elif self.signup_or_login == 'Sign up' :
            go_to_login = Button(490, 570, 300, 50, 'white', 'Go to Log In', 'black')
            go_to_login.draw(screen)
            if go_to_login.is_clicked(mouse_pos, mouse_pressed) and time.time() - lastChange >= 1:
                page = 'Log in'
                lastChange = time.time()
                  
    def handle_events(self, event):
        global input_username, input_password, writing_username, writing_password
        if event.type == pygame.MOUSEBUTTONDOWN:
            if username_box.collidepoint(event.pos):
                writing_username = True
                writing_password = False
            elif password_box.collidepoint(event.pos):
                writing_password = True
                writing_username = False
            else:
                writing_username = False
                writing_password = False
           
        elif event.type == pygame.KEYDOWN:
            if writing_username:
                if event.key == pygame.K_BACKSPACE:
                    input_username = input_username[:-1]
                else:
                    temp_text = input_username + event.unicode
                    text_surface = pygame.font.SysFont('Arial', 20).render(temp_text, True, 'black')
                    if text_surface.get_width() <= max_text_width:
                        input_username += event.unicode

            elif writing_password:
                if event.key == pygame.K_BACKSPACE:
                    input_password = input_password[:-1]
                else:
                    temp_text = input_password + event.unicode
                    text_surface = pygame.font.SysFont('Arial', 20).render(temp_text, True, 'black')
                    if text_surface.get_width() <= max_text_width:
                        input_password += event.unicode

       
username_box =  pygame.Rect(490, 120, 300, 50)
password_box = pygame.Rect(490, 375, 300, 50)

log_in = Button(320, 180, 200, 100, 'white', 'Log In', 'black')
sign_up = Button(760, 180, 200, 100, 'white', 'Sign Up', 'black')

confirm = Button(490, 500, 300, 50, 'white', 'Confirm', 'black')

input_username = ''
input_password = ''
writing_username = False
writing_password = False

def loginFlow():
    running = True
    global page
    global mouse_pos
    global mouse_pressed
    global user

    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if page == 'Log in' or page == 'Sign up':
                Login_SignUp(page).handle_events(event)


        if page == 'Beginning':
            Text(font, 'Our Super Awesome Game!', 'white', 400, 40).draw()
            log_in.draw(screen)
            sign_up.draw(screen)
            if log_in.is_clicked(mouse_pos, mouse_pressed):
                page = 'Log in'
            elif sign_up.is_clicked(mouse_pos, mouse_pressed):
                page = 'Sign up'
        
        elif page == 'Log in':
            login_screen = Login_SignUp('Log in')
            login_screen.show()

            Text(pygame.font.SysFont('Arial', 20), input_username, 'black', 500, 120).draw()
            Text(pygame.font.SysFont('Arial', 20), input_password, 'black', 500, 375).draw()
            
            confirm.draw(screen)

            if confirm.is_clicked(mouse_pos, mouse_pressed):
                    user_found = False 
                    for user in data:
                        if user['Username'] == input_username:
                            user_found = True
                        
                        if user['Password'] == input_password and user_found:
                             #pygame.quit()
                             return user
                        elif input_username.strip() == '' or input_password.strip() == ''and user_found:
                            Text(font, 'Blank Input', 'white', 535, 225).draw()
                        elif not user_found:
                            Text(font, 'Username not found', 'white', 500, 225).draw()
                        
        elif page == 'Sign up':
            user_taken = False
            signup_screen = Login_SignUp('Sign up')
            signup_screen.show()

            Text(pygame.font.SysFont('Arial', 20), input_username, 'black', 500, 120).draw()
            Text(pygame.font.SysFont('Arial', 20), input_password, 'black', 500, 375).draw()
            
            confirm.draw(screen)

            if confirm.is_clicked(mouse_pos, mouse_pressed):
                for user in data:
                    if user['Username'] == input_username:
                        user_taken = True
                        Text(font, 'Username taken', 'white', 500, 225).draw()

                if not user_taken and input_username != '' and input_password != '':
                    new_data = {"Username": input_username, "Password": input_password}
                    data.append(new_data)
                    with open(f'{os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0])))}\\userdata.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    #pygame.quit()
                    return new_data
                elif input_username.strip() == '' or input_password.strip() == '':
                    Text(font, 'Blank Input', 'white', 535, 225).draw()
                
        pygame.display.flip()


