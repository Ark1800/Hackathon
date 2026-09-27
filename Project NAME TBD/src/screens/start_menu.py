import pygame
import sys
from pathlib import Path
from src.screens.base_state import BaseState
from src.modules.push_button import Push_Button
from src.modules.grid import Grid
from src.modules.label import Label
from src.modules.text_input import TextInput

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BROWN, BLACK, ORANGE

class MainMenu(BaseState):
    def __init__(self):
        super().__init__()
        self.btn_start_game = Push_Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100, 200, 100, "Setup", 36, "setup")
        self.btn_help = Push_Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 100, "Help", 36, "help")
        self.btn_exit = Push_Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 200, 200, 100, "Exit", 36, "exit")
        self.title = Label(SCREEN_WIDTH // 2, 100, 0, 100, "The Gambler's Nightmare", 100)
        self.lbl_title = Label(0, 0, SCREEN_WIDTH, 80, "TITLE", 48)
        self.txt_test1 = TextInput(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 300, 40, 24)  # Example TextInput
        self.txt_test1.set_prompt("Enter your name...")
        self.txt_test1.set_max_chars(50)
        self.txt_test1.set_text_color(BLACK)
        self.txt_test1.set_border_color(ORANGE)
        self.txt_test1.set_background_color(WHITE)
        self.txt_test1.set_cursor_color(BROWN)

    def handle_events(self, events, clock):
        for event in events:
            if self.btn_start_game.click(event):
                self.next_state = "SETUP"
                self.done = True
            elif self.btn_help.click(event):
                self.next_state = "HELP"
                self.done = True
            elif self.btn_exit.click(event):
                self.write_andclear_textfile("C:\Andrew C\\Hackathon\\presage_main_run.txt", "False")  # Write "False" to the text file
                pygame.quit()

        self.txt_test1.handle_events(events)  # Pass events to the TextInput for handling user input
        dt = clock.tick(60) / 1000.0  # Calculate delta time in seconds
        self.txt_test1.update(dt)  # Update the TextInput to handle cursor blinking and other updates

    def draw(self, screen):
        screen.fill((30, 30, 40)) 
        self.txt_test1.draw(screen) 
        self.title.draw(screen)
        self.btn_start_game.draw(screen)
        self.btn_help.draw(screen)
        self.btn_exit.draw(screen)
        self.lbl_title.draw(screen)
        self.txt_test1.draw(screen)  # Draw the TextInput on the screen
    
    @staticmethod
    def read_textfile(file_path):
        entries = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # .strip() removes the trailing newline character (\n)
                entry = line.strip()
                if entry:
                    entries.append(entry)
        return entries

    @staticmethod 
    def write_andclear_textfile(file_path, entry):
        with open(file_path, "w", encoding="utf-8") as file:
            pass  # Clear the file by opening it in write mode without writing anything
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(entry) #write the new entry to the file
        