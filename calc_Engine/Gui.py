import pygame as pg
from pygame.locals import *


class GUI:
    def __init__(self):
        pg.init()
        # self.surface = pg.display.get_surface()
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
            ["𝑥ʸ", "7", "8", "9", "𝑥"],
            ["10ⁿ", "4", "5", "6", "-"],
            ["log", "1", "2", "3", "+"],
            ["ln", "∓", "0", ".", "="],
        ]

        self.buttons = None
        self.button_w = (self.WIDTH / 5) - 3
        self.button_h = (self.HEIGHT / 18) - 3
        self.button_rect = None
        self.button_position = []
        self.button_matrix()

    def Trig_func_dropdown(self):
        pg.draw.line(
            self.screen,
            self.GUI_Colors["WHITE"],
            (0, (self.HEIGHT / 2) - (self.HEIGHT / 14)),
            (self.WIDTH, (self.HEIGHT / 2) - (self.HEIGHT / 14)),
            2,
        )

        # self.button_matrix()

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
                rect = pg.Rect(x + 1, y + 2, button_width - 3, button_height - 3)
                row_buttons.append({"rect": rect, "clicked": False, "label": label})

            self.buttons.append(row_buttons)

        # print(self.buttons)

    def SetUp(self):
        self.screen.fill(self.GUI_Colors["BACKGROUND"])
        self.Trig_func_dropdown()
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
