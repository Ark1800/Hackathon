import pygame
from src.screens.base_state import BaseState
from src.settings import WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class Help(BaseState):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont(None, 36)

    def handle_events(self, events, clock):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Return to menu on Escape
                self.next_state = "MAIN_MENU"
                self.done = True

    def draw(self, screen):
        screen.fill((30, 30, 40))
        message = self.font.render("HELP - Press ESC to return to menu", True, WHITE)
        message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(message, message_rect)