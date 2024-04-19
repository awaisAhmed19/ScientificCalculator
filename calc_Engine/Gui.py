import sys
import pygame as pg
import os 
pg.init()

WIDTH,HEIGHT=68*7,68*6
screen=pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Scientific Calculator")
clock=pg.time.Clock()
base_font=pg.font.Font(None,32)
user_text=''

input_rect=pg.Rect(5,5,WIDTH-10,64)

color_active=pg.Color(190,190,190)
color_passive=pg.Color(155,155,155)

color=color_passive 

parent_dir=os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
normalButtons=os.path.join(parent_dir,"normalButtons")
pressedButtons=os.path.join(parent_dir,"pressedButtons")

button_types=[
        "sin","rad","deg","AC","%","back","div",
        "cos","tan","inv","7","8","9","mul",
        "log","ln","!","4","5","6","sub",
        "pie","e","^","1","2","3","add",
        "sqrt","(",")","00","0","dot","equal", 
]

buttonLookup=[
        "sin(",
        "rad(",
        "deg(",
        "AC",
        "%",
        "back",
        "/",
        "cos(",
        "tan(",
        "inv(",
        "7",
        "8",
        "9",
        "*",
        "log(",
        "ln(",
        "!",
        "4",
        "5",
        "6",
        "-",
        "3.14",
        "2.7682",
        "^",
        "1",
        "2",
        "3",
        "-",
        "sqrt",
        "(",
        ")",
        "00",
        "0",
        ".",
        "=", 
]

normalButtons_img_path=[]
for file in os.listdir(normalButtons):
    if os.path.isfile(os.path.join(normalButtons, file)):
        normalButtons_img_path.append(file)
pressedButtons_img_path=[]
for file in os.listdir(pressedButtons):
    if os.path.isfile(os.path.join(pressedButtons, file)):
        pressedButtons_img_path.append(file)

normalButtons_img_path=[f"{i}.png" for i in button_types]
pressedButtons_img_path=[f"{i}.png" for i in button_types]

normalButton_img=[]
pressedButton_img=[]
for button in normalButtons_img_path:
    img_path=os.path.join(normalButtons,button)
    buttons=pg.image.load(img_path).convert_alpha()
    normalButton_img.append(buttons)

for button in pressedButtons_img_path:
    img_path=os.path.join(pressedButtons,button)
    buttons=pg.image.load(img_path).convert_alpha()
    pressedButton_img.append(buttons)

class Button:
    def __init__(self, write, x, y, normal_img, pressed_img):
        self.x = x
        self.y = y
        self.normal_img = normal_img
        self.pressed_img = pressed_img
        self.img = normal_img
        self.state = "normal"
        self.rect = self.img.get_rect(topleft=(x,y))
        self.write = write
        self.prev_state = False  # Previous state of mouse button

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    def update(self, mouse_pos, mouse_pressed):
        if self.rect.collidepoint(mouse_pos):
            self.img = self.pressed_img if mouse_pressed else self.normal_img
            if mouse_pressed and not self.prev_state:  # Check if button was just pressed
                self.handle_input()
        else:
            self.img = self.normal_img
        self.prev_state = mouse_pressed  # Update previous state

    def handle_input(self):
        global user_text
        if self.write in ['AC', 'back', '=']:
            if self.write == "AC":
                user_text = ''
            elif self.write == 'back':
                user_text = user_text[:-1]
            elif self.write == '=':
                pass
        else:
            user_text += self.write



    
    
def main():
    global user_text

    NUM_ROWS=5
    NUM_COLS=7

    screen.fill((182,182,182))

    BUTTON_WIDTH=64
    BUTTON_HEIGHT=64
    
    BUTTON_PADDING_X=2
    BUTTON_PADDING_Y=0
    
    GRID_WIDTH=NUM_COLS*(BUTTON_WIDTH+BUTTON_PADDING_X)
    GRID_HEIGHT=NUM_ROWS*(BUTTON_HEIGHT+BUTTON_PADDING_Y)

    GRID_START_X=(WIDTH-GRID_WIDTH)//2
    GRID_START_Y=(HEIGHT-GRID_HEIGHT)
    buttons=[]
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            for text in buttonLookup:
                index=row*NUM_COLS+col
                x = GRID_START_X + col * (BUTTON_WIDTH + BUTTON_PADDING_X)
                y = GRID_START_Y + row * (BUTTON_HEIGHT + BUTTON_PADDING_Y)
                button = Button(text,x, y, normalButton_img[index], pressedButton_img[index])
                buttons.append(button)

    active=False
    while True:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                sys.exit()
            

        if active:
            color=color_active
        else: color=color_passive

        pg.draw.rect(screen,color,input_rect)
        text_surface=base_font.render(user_text,False,(0,0,0))
        screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))
        #input_rect.w=WIDTH-10
        mouse_pos=pg.mouse.get_pos()
        mouse_pressed=pg.mouse.get_pressed()[0]

        for button in buttons:
            button.update(mouse_pos,mouse_pressed)

        for button in buttons:
            button.draw(screen)
        pg.display.flip()
        clock.tick(30)

if __name__=="__main__":
    main()


