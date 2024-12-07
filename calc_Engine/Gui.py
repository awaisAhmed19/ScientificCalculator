import pygame as pg
from pygame.locals import *
import sys

pg.init()


class GUI:
    def __init__(self):
        self.WIDTH = 450
        self.HEIGHT = 720
        self.SIZE = (self.WIDTH, self.HEIGHT)
        self.font = pg.font.SysFont("Arial", 16)
        self.screen = pg.display.set_mode(self.SIZE)
        self.clock = pg.time.Clock()
        self.GUI_Colors = {
            "WHITE": (255, 255, 255),
            "BACKGROUND": (128, 128, 128),
            "DARK_GREY": (100, 100, 100),
            "LIGHT_GREY": (192, 192, 192),
            "BLACK": (0, 0, 0),
        }
        self.clicked = False
        self.button_rect = None
        self.button_pressed = False
        self.SetUp()

    def SetUp(self):
        self.screen.fill(self.GUI_Colors["BACKGROUND"])
        self.Button(30, 30, 50, 50, "1")
        # pg.display.flip()

    def Button(self, x, y, Width, Height, Text):
        self.button_rect = pg.Rect(x, y, Width, Height)
        color = (
            self.GUI_Colors["LIGHT_GREY"]
            if not self.clicked
            else self.GUI_Colors["DARK_GREY"]
        )
        self.screen.fill(color, self.button_rect)
        text_surface = self.font.render(Text, True, self.GUI_Colors["BLACK"])
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        self.screen.blit(text_surface, text_rect)
        self.draw_Border(self.button_rect)

    def draw_Border(self, rect):
        outer_color = (
            self.GUI_Colors["BLACK"] if self.clicked else self.GUI_Colors["WHITE"]
        )

        inner_color = (
            self.GUI_Colors["WHITE"] if self.clicked else self.GUI_Colors["BLACK"]
        )

        # Draw the border lines
        pg.draw.line(self.screen, outer_color, rect.topleft, rect.topright, 2)  # Top
        pg.draw.line(
            self.screen, outer_color, rect.topright, rect.bottomright, 2
        )  # Right
        pg.draw.line(
            self.screen, inner_color, rect.bottomright, rect.bottomleft, 2
        )  # Bottom
        pg.draw.line(self.screen, inner_color, rect.bottomleft, rect.topleft, 2)  # Left

    def update(self, events):
        for e in events:
            if e.type == pg.MOUSEBUTTONDOWN and self.button_rect.collidepoint(
                pg.mouse.get_pos()
            ):
                print("clicked")
                self.clicked = not self.clicked
                self.SetUp()
            else:
                print("not clicked")


g = GUI()  # Initialize once
run = True
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        g.update(pg.event.get())
        pg.display.flip()
        g.clock.tick(60)
pg.quit()
