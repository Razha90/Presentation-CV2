from keyboardReact import macros
import keyboard as key

check = True

while check:
    if (key.is_pressed('b')):
        macros.leftarrow()
        
    if (key.is_pressed('c')):
        macros.rightarrow()
        
    if (key.is_pressed('z')):
        macros.rightup()
        
    if (key.is_pressed('x')):
        macros.rightbottom()
        
    if(key.is_pressed('q')):
        check = False
  