# #!/usr/bin/python2.7

from pynput.mouse import Button, Controller


import subprocess
import time
import pyautogui  # Used for simulating mouse clicks


mouse = Controller()

while True:
    print(f' position : {mouse.position}')