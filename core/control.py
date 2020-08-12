# this is the control module for awake start update and exit functions

APP_RUNNING = True
AWAKE_CALLED = False
START_CALLED = False

def awake():
    return 1


def start():
    return 1


def update():
    while True:
        return 1

def exit():
    if APP_RUNNING is False:
        return 1