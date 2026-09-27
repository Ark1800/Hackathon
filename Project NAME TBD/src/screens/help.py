import pygame
from pathlib import Path
from src.screens.base_state import BaseState
from src.settings import WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class Help(BaseState):
    def __init__(self):
        super().__init__()
        image_path = Path(__file__).resolve().parents[2] / "assets" / "Black_Background_2.png"
        self.background = pygame.image.load(str(image_path)).convert_alpha()
        self.background_rect = self.background.get_rect(topleft=(0, 0))
        self.font = pygame.font.SysFont(None, 36)

    def handle_events(self, events, clock):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Return to menu on Escape
                self.next_state = "MAIN_MENU"
                self.done = True

    def draw(self, screen):
        screen.fill((30, 30, 40))
        screen.blit(self.background, self.background_rect)
        message = self.font.render("HELP - Press ESC to return to menu", True, WHITE)
        message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(message, message_rect)