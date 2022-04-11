import pyautogui, sys
import time
print('Press "q" to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        time.sleep(3)
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
