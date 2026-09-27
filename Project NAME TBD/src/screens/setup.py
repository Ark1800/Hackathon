import pygame
from src.screens.base_state import BaseState
from src.modules.listview import ListView
from src.settings import WHITE, SCREEN_WIDTH, SCREEN_HEIGHT
from src.modules.label import Label
from src.modules.push_button import Push_Button
from src.modules.text_input import TextInput


def create_programs(count):
    programs = []
    for number in range(1, count + 1):
        programs.append(f"Program {number}")
    return programs

class Setup(BaseState):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont(None, 36)
        self.items = create_programs(50)
        self.lst_blockedprograms = ListView(self.items, SCREEN_WIDTH * 0.25, 100, 30)
        self.lst_blockedprograms.set_max_visible_items(15)
        self.lst_blockedprograms.set_width_override(SCREEN_WIDTH // 2)  # Set the width of the ListView to half the screen width
        self.lbl_title = Label(0, 0, SCREEN_WIDTH, 80, "The Gambler's Nightmare", 48)
        self.add_program_label = Label(SCREEN_WIDTH * 0.1, 110, 0, 0, "Add Program", 24)
        self.remove_program_label = Label(SCREEN_WIDTH * 0.1, 300, 0, 0, "Remove Program", 24)
        self.btn_return = Push_Button(SCREEN_WIDTH - 110, SCREEN_HEIGHT - 50, 100, 40, "Return", 24, "return")

    def handle_events(self, events, clock):
        self.lst_blockedprograms.handle_events(events)
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Return to menu on Escape
                self.next_state = "MAIN_MENU"
                self.done = True
            elif self.btn_return.click(event):
                self.next_state = "MAIN_MENU"
                self.done = True

    def draw(self, screen):
        screen.fill((10, 50, 10))
        #message = self.font.render("SETUP - Press ESC to return to menu", True, WHITE)
        #message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
        self.lst_blockedprograms.draw(screen)
        self.lbl_title.draw(screen)
        self.add_program_label.draw(screen)
        self.remove_program_label.draw(screen)
        self.btn_return.draw(screen)
        #screen.blit(message, message_rect)
        