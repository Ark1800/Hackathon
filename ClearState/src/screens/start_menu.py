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
        self.background = pygame.image.load("ClearState\\assets\\Black_Background.png").convert_alpha()
        self.background_rect = self.background.get_rect()
        self.background_rect.topleft = (0, 0)  # Set the top-left corner of the background image to (0, 0)
        self.btn_start_game = Push_Button(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 250, 300, 150, "Setup", 60, "setup")
        self.btn_help = Push_Button(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, 300, 150, "Help", 60, "help")
        self.btn_exit = Push_Button(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 150, 300, 150, "Exit", 60, "exit")
        self.lbl_title = Label(0, 0, SCREEN_WIDTH, 80, "ClearState", 50)

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

    

    def draw(self, screen):
        screen.fill((30, 30, 40)) 
        self.background.blit(screen, self.background_rect)
        self.lbl_title.draw(screen)
        self.btn_start_game.draw(screen)
        self.btn_help.draw(screen)
        self.btn_exit.draw(screen)
        self.lbl_title.draw(screen)
    
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
        