#installed processes
import win32gui
import win32process
import win32con
import psutil
import socket
import json 
import pygetwindow as gw
import sys
import subprocess
import time
from pathlib import Path

#TO RUN SCRIPT: python.exe "C:\Andrew C\Hackathon\Script Tests\app_monitor.py"

#host data
HOST = "127.0.0.1"
PORT = 5000
PROJECT_DIR = Path(r"C:\Andrew C\\Hackathon\\Project NAME TBD")
PROJECT_MAIN = PROJECT_DIR / "main.py"
LOCKED_APPS_FILE = PROJECT_DIR / "locked_apps.txt"

global apps_blocking
apps_blocking = [] #receiving all apps

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

def minimize_by_keyword(keyword):
    windows = gw.getWindowsWithTitle(keyword)
    for window in windows:
        if window.isMinimized:
            continue  # Skip if the window is already minimized
        window.minimize()
        print(f"Minimized window: {window.title}")
        
def open_presage_process():
    #Pause monitoring until the Presage Pygame process closes.
    print("Opening Presage authentication...")
    presage_process = subprocess.Popen(
        [sys.executable, str(PROJECT_MAIN), "--presage"],
        cwd=PROJECT_DIR,
    )
    presage_main_run = read_textfile("C:\\Andrew C\\Hackathon\\presage_main_run.txt")[0]  # Read the value from the text file
    while presage_main_run == "True":
        for i in range(len(apps_blocking)):
            minimize_by_keyword(apps_blocking[i]["window"])  # Minimize the locked application window
        presage_main_run = read_textfile("C:\\Andrew C\\Hackathon\\presage_main_run.txt")[0]  # Read the value from the text file
    presage_process.wait()  # Wait for the Presage process to finish

def get_open_applications():
    applications = []

    def callback(hwnd, _):
        if not win32gui.IsWindowVisible(hwnd):
            return #if window isnt visible skip it (removes background processes)
            
        title = win32gui.GetWindowText(hwnd) #title of window

        if not title:
            return

        try: #try to get the application name and window title, if it fails skip it
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            process = psutil.Process(pid)

            applications.append({
                "name": process.name(), #OPERATION NAME i.e. "chrome.exe"
                "window": title #WINDOW TITLE i.e. "Hackathon - Google Docs"
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    win32gui.EnumWindows(callback, None)

    return applications

def main():

    while True:
        applications = get_open_applications()
        valid = False
        locked_application = None
        apps_blocking = []
        locked_apps = read_textfile(LOCKED_APPS_FILE)  # Read the locked
        for application in applications:
            (app_name, end) = application["name"].split(".exe")  # Split the application name at ".exe"
            app_window = application["window"]
           # print(f"Checking application: {app_name}, Window: {app_window}")  # Debugging output
            if app_name in locked_apps:
                valid = True
                locked_application = application
                break  # Exit the loop if a locked application is found
            for locked_app in locked_apps:
                if locked_app.lower() in app_window.lower():
                    valid = True
                    locked_application = application
                    break  # Exit the loop if a locked application is found
        if valid == True:
            write_andclear_textfile("C:\\Andrew C\\Hackathon\\presage_main_run.txt", "True")  # Write "True" to the text file
            minimize_by_keyword(locked_application["window"])  # Minimize the locked application window
            apps_blocking.append(locked_application)  # Add the locked application to the blocking list
        time.sleep(2)

if __name__ == "__main__":
    main()