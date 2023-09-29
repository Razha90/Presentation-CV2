import keyboard as key
import time

class macros():
    def leftarrow():
        key.press_and_release('left')        
        print('left')
        time.sleep(1)
    def rightarrow():
        key.press_and_release('right')
        print('right')
        time.sleep(1)
        
    def rightup():
        key.press_and_release('up')
        print('up')
        time.sleep(1)
        
    def rightbottom():
        key.press_and_release('down')
        print('down')
        time.sleep(1)
   