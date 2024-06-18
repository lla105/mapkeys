import time
import pyautogui
import threading
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID

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
            x = window['kCGWindowBounds']['X']
            y = window['kCGWindowBounds']['Y']
            width = window['kCGWindowBounds']['Width']
            height = window['kCGWindowBounds']['Height']
            return (x,y,width,height)
        
def print_pos():
    while True:
        pos = get_scrcpy_window_pos()
        print(f' scrcpy pos @ ({pos[0]},{pos[1]}) , w: {pos[2]} h: {pos[3]}')
        time.sleep(1)

# Main script logic
if __name__ == "__main__":
    # Get center of scrcpy window
    scrcpy_center = get_scrcpy_window_center()

    thread1 = threading.Thread(target=print_pos)
    thread1.start()

    print( 'scrcpy cetner : ', scrcpy_center)
    if scrcpy_center:
        print(f"Clicking at the center of scrcpy window: {scrcpy_center}")
        for i in range(7):
            # pyautogui.moveTo(scrcpy_center[0], scrcpy_center[1])
            pyautogui.click(scrcpy_center[0], scrcpy_center[1])
            # pyautogui.dragTo(100, 200, button='left')
            print('click....')
            time.sleep(1)        

    else:
        print("scrcpy window not found or not visible on screen.")
