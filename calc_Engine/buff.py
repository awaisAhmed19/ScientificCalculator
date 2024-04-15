import os,sys,pygame as pg
pg.init()

WIDTH,HEIGHT=460,600
screen=pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Scientific Calculator")
clock=pg.time.Clock()

button_types=[
        "sin","cos","tan","rad","deg",
        "log","ln","(",")","inv",
        "!","AC","%","back","div",
        "^","7","8","9","mul",
        "sqrt","4","5","6","sub",
        "pie","1","2","3","add",
        "e","00","0","dot","equal",
        
    ]
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
normalButtons_img_path=[f"{normalButtons}/{i}.png" for i in button_types]
normalButton_img=[]
pressedButton_img=[]
for button in normalButtons_img_path:
    img_path=os.path.join(normalButtons,button)
    buttons=pg.image.load(img_path).convert_alpha()
    normalButton_img.append(buttons)

print(normalButton_img)
print(normalButtons_img_path)

for button in pressedButtons_img_path:
    img_path=os.path.join(pressedButtons,button)
    buttons=pg.image.load(img_path).convert_alpha()
    pressedButton_img.append(buttons)

print(normalButton_img[0].get_width())

def main():
    while True:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                sys.exit()
        

        screen.fill((255,255,255))
        
        pg.display.flip()
        clock.tick(30)

if __name__=="__main__":
    main()


