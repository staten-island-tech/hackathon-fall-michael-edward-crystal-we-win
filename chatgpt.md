
# ChatGPT Coding Diary

## Project Name: _Rhythm Game_

### Date: _11/22/24_

I DID NOT PUT EVERYTHING I ASKED CHATGPT HERE BECAUSE IT'D TAKE FOREVER TO WRITE DOWN AND IT WOULDN'T BE VERY CLEAR. 

---

## 1. **Task/Problem Description**

Briefly describe the problem you're trying to solve or the task you're working on.

`I'm trying to make a sign up and log in system using a json files and pygame `

---

## 2. **Initial Approach/Code**

Describe the initial approach you took to solving the problem. If you started writing code, include it here.

```
1. Have 'log in' and 'sign up' as big text near the top.
2. Make button - Get the rectangles that surrounds the texts in step 1 and make it so if there's a click on the rectangle, it does something. (pygame buttons are weird)
3. If logging in, look through the json file to see if the username and password is there.
4. If signing up, write the data to a json file.

```

- What was your plan for solving the problem?
- Did you have any initial thoughts or strategies before using ChatGPT?

---

## 3. **Interaction with ChatGPT**

### Questions/Requests to ChatGPT
Write down the questions or requests you made to ChatGPT. 
Also include what code from ChatGPT you are unsure of and craft a question that asks for further clarification. 

```text

How to make buttons in pygame?
How to show user input on screen while their cursor is in certain boxes and they're typing in pygame?

```

---

## 4. **ChatGPT's Suggestions/Code Changes**

Record the code or suggestions ChatGPT provided. Include any changes or improvements ChatGPT suggested and how it influenced your approach.

```python

#for question 1
class Button:
    def __init__(self, x, y, width, height, color, text, text_color, font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.SysFont('Arial', font_size)

    def draw(self, screen):
        # Draw the button
        pygame.draw.rect(screen, self.color, self.rect)
        # Draw the text on the button
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_hovered(self, mouse_pos):
        # Check if the mouse is hovering over the button
        return self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, mouse_pressed):
        # Check if the button was clicked
        if self.is_hovered(mouse_pos) and mouse_pressed[0]:
            return True
        return False

#for question 2
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if mouse is inside the input box
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    # Remove last character on backspace
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    # You can add logic for submitting the text
                    print(f'User typed: {input_text}')
                    input_text = ''  # Clear input after submit
                else:
                    # Append the character to the input text
                    input_text += event.unicode
```

- What was ChatGPT's solution or suggestion?

`Question 1: Have the button be a class and its actions be methods within the class`
`Question 2: It used active to know when the user input should be on the screen and provided the commands`

- How did it differ from your original approach?

`Question 1: My original plan was to do a function for making the button and have the actions be put in the event loop, but ChatGPT's approach is way more readable`
`Question 2: I hadn't thought of using active. I planned to do something like 'If touching box and typing, show stuff on screen'`

---

## 5. **Reflection on Changes**

Reflect on the changes made to your code after ChatGPT's suggestions. Answer the following questions:

- Why do you think ChatGPT's suggestions are helpful or relevant?

`Yeah, it provides more readable code and provides stuff like pygame's attributes and methods, so I don't have to go back to the documentation`
 
- Did the suggestions improve your code? How?

`It did because it formatted its code very logically, so it made mine more readable.`

- Did you understand why the changes were made, or are you still uncertain about some parts?

`I understand.`

Example:
>                                                             

---

## 6. **Testing and Results**

After making the changes, did you test your code? What were the results?


- Did you run any tests (e.g., unit tests, edge cases)?\

`Yeah. I just ran it and saw if everything worked as intended` 
 
- Did the code work as expected after incorporating ChatGPT's changes?
- Did you encounter any bugs or issues during testing?

`It mostly worked as intended. I needed to edit ChatGPt's code in its showing user input on screen suggestion because it printed the input on the terminal rather than on the screen.`

---

## 7. **What Did You Learn?**

In this section, reflect on what you learned from this coding session. Did you gain any new insights, or were there areas you still struggled with? 

```
1. I need to start using classes more. I usualy default to functions.
2. My normal code is usually pretty unreadable--I need to write more comments and format my code better (more classes and functions).
 ```
---
