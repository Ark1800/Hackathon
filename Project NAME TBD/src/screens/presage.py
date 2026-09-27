import pygame
from src.screens.base_state import BaseState
from src.modules.push_button import Push_Button
from src.modules.grid import Grid
from src.modules.label import Label

from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BROWN

class Presage(BaseState):
    def __init__(self):
        super().__init__()
        self.grid = Grid(50, BROWN)

    def handle_events(self, events, clock):
        pass

    def draw(self, screen):
        screen.fill((30, 30, 40)) 
        self.grid.draw(screen)  