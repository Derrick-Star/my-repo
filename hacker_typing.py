
import string
import random
import time
import os

# Open Notpad
os.system("start notepad.exe")
time.sleep(2)  # Wait for Notepad to open

#duration to run (in seconds)
RUN_TIME = 7 * 60  # 7 minutes

#all hacker-looking characters
characters = string.ascii_letters + string.digits + string.punctuation + " " * 10

# Start typing random characters
while True:
    start_time = time.time()
    stroke_count = 0

    while time.time() - start_time < RUN_TIME:
        # Generate a random character
        char = random.choice(characters)
        pyautogui.typewrite(char)
        stroke_count += 1

        if stroke_count % 700 == 0:
            pyautogui.press('enter')
        
        time.sleep(0.1)
        
    pyautogui.press('enter')  
    pyautogui.typewrite("<<<<<>>>>>>>Restarting sequence<<<<<<>>>>>>>")
    pyautogui.press('enter')
    time.sleep(1)  # Wait before restarting the sequence