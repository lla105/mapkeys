import time
import pyautogui
import threading
from pynput import keyboard

from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID

windowwidth = 0
windowheight= 0
windowPOSx = 0
windowPOSy = 0

def get_scrcpy_window_pos():
    global windowPOSx, windowPOSy, windowwidth, windowheight

    options = kCGWindowListOptionOnScreenOnly
    window_list = CGWindowListCopyWindowInfo(options, kCGNullWindowID)

    for window in window_list:
        if window.get('kCGWindowOwnerName') == 'scrcpy':
            windowPOSx = window['kCGWindowBounds']['X']
            windowPOSy = window['kCGWindowBounds']['Y']
            windowwidth = window['kCGWindowBounds']['Width']
            windowheight = window['kCGWindowBounds']['Height']
            # for i in range(7):
            # print( ' >>>> CLICKING: ', width//2,height//2)
            # pyautogui.click(width/22, height//2)
                # time.sleep(1)
            # print()
            return (windowPOSx, windowPOSy, windowwidth, windowheight)
        
def print_pos():
    while True:
        xx,yy = pyautogui.position()
        pos = get_scrcpy_window_pos()
        # print(f' scrcpy pos @ ({pos[0]},{pos[1]}) , w: {pos[2]} h: {pos[3]}')
        # print(f' scrcpy pos @ ({windowPOSx},{windowPOSy}) , w: {windowwidth} h: {windowheight}')
        time.sleep(0.5)


def listen_for_keys():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
def scale_coordinates(x,y):
    x = x/1080*windowwidth
    y = y/1920*windowheight
    return (x,y)
def on_press(key):
    try:
        key_str = key.char
        print('>>>Key pressed:', key_str)
        if (isinstance(key, keyboard.KeyCode) and key.vk == 76):
            send_click_command('enter')
        if key_str in coordinates:
            send_click_command(key_str)

    except AttributeError:
        # Key is not a character key
        if key == keyboard.Key.enter :
            send_click_command('enter')
        elif key == keyboard.Key.backspace :
            send_click_command('backspace')
        pass
# Function to click within scrcpy window
def click_in_scrcpy(x, y, scrcpy_rect):
    scrcpy_x, scrcpy_y, _, _ = scrcpy_rect
    print('Clicking at:', scrcpy_x + x, scrcpy_y + y)
    pyautogui.click(scrcpy_x + x, scrcpy_y + y)
def send_click_command(command):
    x,y = coordinates[command]
    x,y = scale_coordinates(x,y)
    scrcpy_rect = get_scrcpy_window_pos()
    if scrcpy_rect:
        click_in_scrcpy(x, y, scrcpy_rect)

coordinates = {'backbutton' : (81,660), 
               'startbutton': (769, 1556),
               'quickstart' : (810, 1800),
               'english' : (290 , 1150),
               'deposit' : (270, 1024),
               'collect' : (530, 1355),
               'fedex' : (604, 1400),
               'canadapost' : (850,1430),
               'DHL' : (850, 1125),
               'unit#' : (542, 1074),
               '1' : (125,1455),
               '2' : (379, 1455),
               '3' : (616, 1455),
               '4' : (125, 1570),
               '5' : (365, 1570),
               '6' : (616, 1570),
               '7' : (125, 1687),
               '8' : (380, 1687),
               '9' : (616, 1687),
               '0' : (375, 1800),
               'backspace' : (900, 1465),
               'enter' : (897, 1790),
               'selectbuilding' : (151,1040),
               'selectunit' : (237,1140),
               'small' : (158, 1087),
               'medium' : (760,1070),
               'large' : (140, 1310),
               'confirm': (520, 1747),
               'backtohomescreen' : (320,1675)
               }


# Main script logic
if __name__ == "__main__":
    thread1 = threading.Thread(target=print_pos)
    thread1.start()
    thread2 = threading.Thread(target=listen_for_keys)
    thread2.start()

