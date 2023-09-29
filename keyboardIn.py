import keyboard

def main():
    while True:
        try:
            key_event = keyboard.read_event()
            if key_event.event_type == keyboard.KEY_DOWN:
                if key_event.name == 'z':
                    keyboard.press_and_release('right')
                elif key_event.name == 'x':
                    keyboard.press_and_release('left')
                elif key_event.name == 'c':
                    keyboard.press_and_release('up')
                elif key_event.name == 'v':
                    keyboard.press_and_release('down')
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
