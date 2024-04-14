import sys
import pygame as pg
import os 
pg.init()

WIDTH,HEIGHT=460,600
screen=pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Scientific Calculator")
clock=pg.time.Clock()
parent_dir=os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
normalButtons=os.path.join(parent_dir,"normalButtons")
pressedButtons=os.path.join(parent_dir,"pressedButtons")

normalButtons_img_path=[]
for file in os.listdir(normalButtons):
    if os.path.isfile(os.path.join(normalButtons, file)):
        normalButtons_img_path.append(file)
pressedButtons_img_path=[]
for file in os.listdir(pressedButtons):
    if os.path.isfile(os.path.join(pressedButtons, file)):
        pressedButtons_img_path.append(file)

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
    def __init__(self,x,y,normal_img,pressed_img):
        self.x=x
        self.y=y
        self.normal_img=normal_img
        self.pressed_img=pressed_img
        self.img=normal_img
        self.state="normal"
        self.rect=self.img.get_rect(topleft=(x,y))

    def draw(self,screen):
        screen.blit(self.img,self.rect)

    def update(self, mouse_pos,mouse_pressed):
        if self.rect.collidepoint(mouse_pos):
            self.img=self.pressed_img if mouse_pressed else self.normal_img
        else:
            self.img=self.normal_img
            


def main():

    NUM_ROWS=3
    NUM_COLS=3

    BUTTON_WIDTH=64
    BUTTON_HEIGHT=64
    
    BUTTON_PADDING_X=10
    BUTTON_PADDING_Y=10
    
    GRID_WIDTH=NUM_COLS*(BUTTON_WIDTH+BUTTON_PADDING_X)
    GRID_HEIGHT=NUM_ROWS*(BUTTON_HEIGHT+BUTTON_PADDING_Y)

    GRID_START_X=(WIDTH-GRID_WIDTH)//2
    GRID_START_Y=(HEIGHT-GRID_HEIGHT)//2
    buttons=[]
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            x = GRID_START_X + col * (BUTTON_WIDTH + BUTTON_PADDING_X)
            y = GRID_START_Y + row * (BUTTON_HEIGHT + BUTTON_PADDING_Y)
            index = row * NUM_COLS + col  # Calculate the index of the button image
            button = Button(x, y, normalButton_img[index], pressedButton_img[index])
            buttons.append(button)

    while True:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                sys.exit()
        
        mouse_pos=pg.mouse.get_pos()
        mouse_pressed=pg.mouse.get_pressed()[0]

        for button in buttons:
            button.update(mouse_pos,mouse_pressed)

        screen.fill((255,255,255))
        for button in buttons:
            button.draw(screen)
        pg.display.flip()
        clock.tick(30)

if __name__=="__main__":
    main()


