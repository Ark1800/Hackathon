import pygame
from pathlib import Path
from src.screens.base_state import BaseState
from src.modules.listview import ListView
from src.settings import WHITE, BLACK, GREEN, BROWN, RED, SCREEN_WIDTH, SCREEN_HEIGHT
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
        image_path = Path(__file__).resolve().parents[2] / "assets" / "Black_Background_3.png"
        self.background = pygame.image.load(str(image_path)).convert_alpha()
        self.background_rect = self.background.get_rect(topleft=(0, 0))
        self.lst_blockedprograms = ListView(self.items, SCREEN_WIDTH * 0.25, 100, 30)
        self.lst_blockedprograms.set_max_visible_items(15)
        self.lst_blockedprograms.set_width_override(SCREEN_WIDTH // 2)  # Set the width of the ListView to half the screen width
        self.lbl_title = Label(0, 0, SCREEN_WIDTH, 80, "The Gambler's Nightmare", 50)
        self.add_program_label = Label(SCREEN_WIDTH * 0.08, 110, 0, 0, "Add Program", 24)
        self.remove_program_label = Label(SCREEN_WIDTH * 0.09, 300, 0, 0, "Remove Program", 24)
        self.btn_return = Push_Button(SCREEN_WIDTH - 110, SCREEN_HEIGHT - 50, 100, 40, "Return", 24, "return")

        self.add_text = TextInput(SCREEN_WIDTH * 0.025, 130, 150, 30, 18)  # Example TextInput
        self.add_text.set_prompt("Enter program name...")
        self.add_text.set_max_chars(50)
        self.add_text.set_text_color(BLACK)
        self.add_text.set_border_color(GREEN)
        self.add_text.set_background_color(WHITE)
        self.add_text.set_cursor_color(BROWN)

        self.remove_text = TextInput(SCREEN_WIDTH * 0.025, 320, 150, 30, 18)  # Example TextInput
        self.remove_text.set_prompt("Enter program name...")
        self.remove_text.set_max_chars(50)
        self.remove_text.set_text_color(BLACK)
        self.remove_text.set_border_color(RED)
        self.remove_text.set_background_color(WHITE)
        self.remove_text.set_cursor_color(BROWN)

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
        self.add_text.handle_events(events)
        self.add_text.update(clock.get_time() / 1000.0)
        self.remove_text.handle_events(events)
        self.remove_text.update(clock.get_time() / 1000.0)

    def draw(self, screen):
        screen.fill((10, 50, 10))
        #message = self.font.render("SETUP - Press ESC to return to menu", True, WHITE)
        #message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
        screen.blit(self.background, self.background_rect)
        self.lst_blockedprograms.draw(screen)
        self.lbl_title.draw(screen)
        self.add_program_label.draw(screen)
        self.remove_program_label.draw(screen)
        self.btn_return.draw(screen)
        self.add_text.draw(screen)  # Draw the TextInput on the screen
        self.remove_text.draw(screen)  # Draw the TextInput on the screen
        #screen.blit(message, message_rect)
        