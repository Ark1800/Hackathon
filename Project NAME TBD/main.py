'''
By: Andrew Campbell, Liam Johnston, Reese Houston, and Gabriel Abdalla
Date: 2026-09-26
Program Details: a functional screen management application that measures the users stress levels and authenticates who they are in order to let them into certain applications.
'''

# old main.py
'''
from src.engine import Game
import sys

if __name__ == "__main__":
    initial_state = "PRESAGE" if "--presage" in sys.argv else "MAIN_MENU"
    game = Game(initial_state)
    game.run()
'''
    
# new main.py
from src.engine import Game
from pathlib import Path
import subprocess
import sys

if __name__ == "__main__":
    if "--presage" in sys.argv:
        presage_script = Path(__file__).resolve().parent / "presage.py"
        raise SystemExit(subprocess.run(
            [sys.executable, str(presage_script), "--gui"],
            cwd=presage_script.parent,
        ).returncode)

    initial_state = "PRESAGE" if "--presage" in sys.argv else "MAIN_MENU"
    game = Game(initial_state)
    game.run()