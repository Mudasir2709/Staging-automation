
import time
from pynput.keyboard import Controller, Key


def enter_text_in_os_dialog(file_path):
    keyboard = Controller()
    time.sleep(1)
    keyboard.type(file_path)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)