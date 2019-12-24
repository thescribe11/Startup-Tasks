import os
import shutil
import getpass

code = r"""
import subprocess
import webbrowser
import sys, os
import pyautogui
import tkinter as tk
import getpass
import psutil
from time import *

is_going = True

def OpenGitHub(*args):
    webbrowser.open('https://github.com/thescribe11')

def TaskManager(*args):
    global ProcessEntry

    PROCNAME = ProcessEntry.get()
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()

def RunCommand(*args):
    os.system(f'code C:\\Users\\Adam\\AppData\\Local\\Programs\\Python\\Python38\\Office_2019\\Mail2019.py')

root = tk.Tk()
root.title("Automated tasks")

GitHubButton = tk.Button(root, text = "Open GitHub", font="Times 16", command=OpenGitHub)
GitHubButton.grid(padx=50, pady=(50, 0))

KillFrame = tk.Frame(root, relief='solid', borderwidth=1)
KillFrame.grid(pady=30)

ProcessEntry = tk.Entry(KillFrame, font="Times 12")
ProcessEntry.grid(pady=5)

Killer = tk.Button(KillFrame, text="Kill process", font="Times 16", command=TaskManager)
Killer.grid(padx=50, pady=10)

Projecter = tk.Button(root, text="Run shell command", font="Times 16", command=RunCommand)
Projecter.grid(padx=50, pady=(0,50))

root.mainloop()
"""

run_code = """ECHO ON
REM Executing StartTasks.py...
python StartTasks.py
PAUSE"""

with open(f"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\StartTasks.py", 'w') as f:
    f.write(code)

with open(f"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\StartTasksRunner.bat", "w") as f:
    f.write(run_code)
