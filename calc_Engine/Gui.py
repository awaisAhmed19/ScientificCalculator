import pygame as pg
from pygame.locals import *
import math
from Postfix_Evaluation import Post_Evaluation

p = Post_Evaluation()


class GUI:
    def __init__(self):
        pg.init()
        self.WIDTH, self.HEIGHT = 310, 530
        self.SIZE = (self.WIDTH, self.HEIGHT)
        self.font = pg.font.SysFont("Segoe UI Symbol ", 20)
        self.screen = pg.display.set_mode(self.SIZE, pg.RESIZABLE)
        pg.display.set_caption("Scientific Calculator")
        self.clock = pg.time.Clock()
        self.GUI_Colors = {
            "WHITE": (255, 255, 255),
            "BACKGROUND": (128, 128, 128),
            "DARK_GREY": (100, 100, 100),
            "LIGHT_GREY": (192, 192, 192),
            "BLACK": (0, 0, 0),
        }
        self.button_array = [
            ["MC", "MR", "M+", "M-", "MS", "M"],
            ["Trig", "Func"],
            ["2nd", "π", "e", "C", "→"],
            ["𝑥²", "¹/𝑥", "|𝑥|", "exp", "mod"],
            ["²√𝑥", "(", ")", "n!", "÷"],
            ["𝑥ʸ", "7", "8", "9", "x"],
            ["10ⁿ", "4", "5", "6", "-"],
            ["log", "1", "2", "3", "+"],
            ["ln", "∓", "0", ".", "="],
        ]
        self.display_text = ""
        self.buttons = None
        self.button_rect = None
        self.button_position = []
        self.button_matrix()

        # self.button_matrix()

    def text_Display(self):
        text_box = pg.Rect(1, 1, self.WIDTH - 3, (self.HEIGHT / 4) - 3)
        text_surface = self.font.render(
            self.display_text, True, self.GUI_Colors["BLACK"]
        )
        text_rect = text_surface.get_rect(right=text_box.right)
        self.screen.blit(text_surface, text_rect)
        pg.draw.line(
            self.screen,
            self.GUI_Colors["WHITE"],
            text_box.topleft,
            text_box.bottomleft,
            4,
        )
        pg.draw.line(
            self.screen,
            self.GUI_Colors["WHITE"],
            text_box.bottomleft,
            text_box.bottomright,
            4,
        )
        pg.draw.line(
            self.screen,
            self.GUI_Colors["BLACK"],
            text_box.topleft,
            text_box.topright,
            4,
        )
        pg.draw.line(
            self.screen,
            self.GUI_Colors["BLACK"],
            text_box.topright,
            text_box.bottomright,
            4,
        )

    def button_matrix(self):
        self.buttons = []
        rows = len(self.button_array)
        for rowi, row in enumerate(self.button_array):
            cols = len(row)
            button_width = self.WIDTH / cols
            button_height = (3 * self.HEIGHT / 4) / rows
            y_offset = self.HEIGHT / 4  # Top margin

            row_buttons = []
            for colj, label in enumerate(row):
                x = colj * button_width
                y = rowi * button_height + y_offset
                rect = pg.Rect(x + 2, y + 2, button_width - 3, button_height - 3)
                row_buttons.append({"rect": rect, "clicked": False, "label": label})

            self.buttons.append(row_buttons)

    def preprocessed(self, text):
        match (text):
            case "2nd":
                pass
            case "π":
                self.display_text += str(math.pi)
            case "e":
                self.display_text += str(math.e)
            case "C":
                self.display_text = ""
            case "→":
                if self.display_text != "":
                    self.display_text = self.display_text[:-1]
            case "𝑥²":
                self.display_text += "^2"
            case "¹/𝑥":
                self.display_text = "1/" + self.display_text
            case "|𝑥|":
                number = float(self.display_text)
                if number < 0:
                    number *= -1
                self.display_text = str(number)
            case "exp":
                pass
            case "mod":
                self.display_text += "%"

            case "²√𝑥":
                self.display_text = f"√({self.display_text})"
            case "(":
                if self.display_text == "":
                    self.display_text += "("
                else:
                    self.display_text += "*("
            case ")":
                self.display_text += ")"
            case "n!":
                self.display_text += "!"
            case "÷":
                self.display_text += "÷"
            case "𝑥ʸ":
                self.display_text += "^"
            case "x":
                self.display_text += "*"
            case "10ⁿ":
                self.display_text = f"10^({self.display_text})"
            case "-":
                self.display_text += "-"
            case "log":
                self.display_text = f"log({self.display_text})"
            case "+":
                self.display_text += "+"
            case "ln":
                self.display_text = f"ln({self.display_text})"
            case "∓":
                self.display_text = str(float(self.display_text) * (-1))
            case "=":
                if self.display_text == "":
                    self.display_text += "enter a number"
                else:
                    input_text = self.display_text
                    self.display_text = ""
                    result = p.Post_Evaluation(input_text)
                    print(f"Post_Evaluation returned: {result}")  # Debug
                    if result is None:
                        self.display_text += " Error: Invalid Expression"
                    else:
                        self.display_text += str(self.isfloating(result))
                        print(self.display_text)
            case _:
                self.display_text += text
        return self.display_text

    def isfloating(self, num):
        if num.is_integer():
            print("done")
            return int(num)

        return float(num)

    def SetUp(self):
        self.screen.fill(self.GUI_Colors["BACKGROUND"])
        self.text_Display()
        for i, row in enumerate(self.buttons):
            for j, pos in enumerate(row):
                self.Button(
                    pos["rect"].x,
                    pos["rect"].y,
                    pos["rect"].width,
                    pos["rect"].height,
                    self.button_array[i][j],
                    pos["clicked"],
                )
        pg.display.flip()

    def Button(self, x, y, Width, Height, Text, clicked):
        button_rect = pg.Rect(x, y, Width, Height)
        color = (
            self.GUI_Colors["LIGHT_GREY"]
            if not clicked
            else self.GUI_Colors["DARK_GREY"]
        )
        self.screen.fill(color, button_rect)
        text_surface = self.font.render(Text, True, self.GUI_Colors["BLACK"])
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.screen.blit(text_surface, text_rect)
        self.draw_Border(button_rect, clicked)

    def draw_Border(self, rect, clicked):
        outer_color = self.GUI_Colors["BLACK"] if clicked else self.GUI_Colors["WHITE"]
        inner_color = self.GUI_Colors["WHITE"] if clicked else self.GUI_Colors["BLACK"]

        # Draw the border lines
        pg.draw.line(self.screen, outer_color, rect.topleft, rect.topright, 2)  # Top
        pg.draw.line(
            self.screen, inner_color, rect.topright, rect.bottomright, 2
        )  # Right
        pg.draw.line(
            self.screen, inner_color, rect.bottomright, rect.bottomleft, 2
        )  # Bottom
        pg.draw.line(self.screen, outer_color, rect.bottomleft, rect.topleft, 2)  # Left

    def update(self):
        mouse_pos = pg.mouse.get_pos()
        mosue_pressed = pg.mouse.get_pressed()[0]

        for row in self.buttons:
            for button in row:
                if button["rect"].collidepoint(mouse_pos):
                    if mosue_pressed and not button["clicked"]:
                        button["clicked"] = True
                        self.Button(
                            button["rect"].x,
                            button["rect"].y,
                            button["rect"].width,
                            button["rect"].height,
                            self.button_array[self.buttons.index(row)][
                                row.index(button)
                            ],
                            button["clicked"],
                        )
                        self.preprocessed(button["label"])
                    elif not mosue_pressed and button["clicked"]:
                        button["clicked"] = False
                        self.Button(
                            button["rect"].x,
                            button["rect"].y,
                            button["rect"].width,
                            button["rect"].height,
                            self.button_array[self.buttons.index(row)][
                                row.index(button)
                            ],
                            button["clicked"],
                        )
                        print("unclicked")


g = GUI()
run = True

while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
    g.update()
    g.SetUp()
    pg.display.flip()
    g.clock.tick(60)
pg.quit()
