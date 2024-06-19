import time
import pyautogui
import threading
from pynput import keyboard

from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID

windowwidth = 0
windowheight= 0
windowPOSx = 0
windowPOSy = 0

# Function to get scrcpy window position and size
def get_scrcpy_window_center():
    options = kCGWindowListOptionOnScreenOnly
    window_list = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
    for window in window_list:
        if window.get('kCGWindowOwnerName') == 'scrcpy':
            x = window['kCGWindowBounds']['X']
            y = window['kCGWindowBounds']['Y']
            width = window['kCGWindowBounds']['Width']
            height = window['kCGWindowBounds']['Height']
            # Calculate center of scrcpy window
            center_x = x + width // 2
            center_y = y + height // 2
            return (center_x, center_y)
    return None

def get_scrcpy_window_pos():
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
            print()
            return (windowPOSx, windowPOSy, windowwidth, windowheight)
        
def print_pos():
    while True:
        xx,yy = pyautogui.position()
        pos = get_scrcpy_window_pos()
        # print(f' scrcpy pos @ ({pos[0]},{pos[1]}) , w: {pos[2]} h: {pos[3]}')
        print(f' scrcpy pos @ ({windowPOSx},{windowPOSy}) , w: {windowwidth} h: {windowheight}')
        time.sleep(0.5)


def listen_for_keys():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
def scale_coordinates(x,y):
    x = x/1080*windowwidth
    y = y/1920*windowheight
def on_press(key):
    try:
        # Convert key to string representation
        key_str = key.char
        print('Key pressed:', key_str)
        if key_str in coordinates:
            x, y = coordinates[key_str]

            print(' >>>> converting :::: ', x , y)
            scrcpy_rect = get_scrcpy_window_center()
            if scrcpy_rect:
                print('Scrcpy window detected.')
                # click_in_scrcpy(x, y, scrcpy_rect)
            else:
                print("Scrcpy window not found or not visible on screen.")
    except AttributeError:
        # Key is not a character key
        pass



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
               '1' : (125,1485),
               '2' : (379, 1500),
               '3' : (616, 1500),
               '5' : (365, 1515),
               '0' : (375, 1849),
               'selectbuilding' : (151,1040),
               'selectunit' : (237,1140),
               'enter' : (897, 1784),
               'small' : (158, 1087),
               'medium' : (760,1070),
               'large' : (140, 1310),
               'confirm': (520, 1747),
               'backtohomescreen' : (320,1675)
               }


# Main script logic
if __name__ == "__main__":
    # Get center of scrcpy window
    # scrcpy_center = get_scrcpy_window_center()

    thread1 = threading.Thread(target=print_pos)
    thread1.start()
    thread2 = threading.Thread(target=listen_for_keys)
    thread2.start()

    print( 'scrcpy cetner : ', scrcpy_center)
    # if scrcpy_center:
    #     print(f"Clicking at the center of scrcpy window: {scrcpy_center}")
    #     for i in range(7):
    #         # pyautogui.moveTo(scrcpy_center[0], scrcpy_center[1])
    #         pyautogui.click(scrcpy_center[0], scrcpy_center[1])
    #         # pyautogui.dragTo(100, 200, button='left')
    #         print('click....')
    #         time.sleep(1)        

    # else:
    #     print("scrcpy window not found or not visible on screen.")
