import pygame
from pathlib import Path
from src.modules.label import Label
from src.screens.base_state import BaseState
from src.settings import BLACK, SCREEN_WIDTH, SCREEN_HEIGHT

class Help(BaseState):
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load("ClearState/assets/White_Background_3.jpg").convert()
        self.font = pygame.font.SysFont(None, 36)
        self.subtitlefont = pygame.font.SysFont(None, 28)
        self.bodyfont = pygame.font.SysFont(None, 15)
        self.title1 = self.font.render("Instuctions to setup Clearstate:", True, BLACK)
        self.title1_rect = self.title1.get_rect(center=(SCREEN_WIDTH // 2 - 75, 75))
        self.subtitle1 = self.subtitlefont.render("How to add a program:", True, BLACK)
        self.subtitle1_rect = self.title1.get_rect(center=(SCREEN_WIDTH // 2 - 75, 125))
        self.subtitle2 = self.subtitlefont.render("How to remove a program:", True, BLACK)
        self.subtitle2_rect = self.title1.get_rect(center=(SCREEN_WIDTH // 2 - 75, 300))
        self.title2 = self.font.render("How to pass Clearstate test:", True, BLACK)
        self.title2_rect = self.title1.get_rect(center=(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT - 300))
        self.body1 = self.bodyfont.render("1. Click Setup \n 2. Type program name to be blocked in Add Program field \n 3. Click on the Add Program button \n 4. Return to the main menu to save", True, BLACK)
        self.body1_rect = self.body1.get_rect(center=(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT - 300))
    
    
    def handle_events(self, events, clock):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Return to menu on Escape
                self.next_state = "MAIN_MENU"
                self.done = True

    def draw(self, screen):
        screen.fill((30, 30, 40))
        screen.blit(self.background, (0, 0))
        message = self.font.render("HELP - Press ESC to return to menu", True, BLACK)
        message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        screen.blit(message, message_rect)
        screen.blit(self.title1, self.title1_rect)
        screen.blit(self.title2, self.title2_rect)
        screen.blit(self.subtitle1, self.subtitle1_rect)
        screen.blit(self.subtitle2, self.subtitle2_rect)
        screen.blit(self.body1, self.body1_rect)