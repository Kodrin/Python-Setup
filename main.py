# LIBRARIES IMPORT
import macro
import keyboard as key              # for keyboard input
from core.input.input import Input
from core.logger import Logger      # logging module

# CLASS INSTANCES
macro.init()
input = Input()
logger = Logger()


# EXECUTION FLOW
# called once before start
def awake():
    if macro.AWAKE_CALLED is False:
        macro.AWAKE_CALLED = True
        print("[AWAKE HAS BEEN CALLED]")

# called once after awake
def start():
    if macro.START_CALLED is False:
        macro.START_CALLED = True
        logger.start()
        print("[START HAS BEEN CALLED]")
        # do something here

# main loop
def update():
    while macro.APP_RUNNING is True:
        input.update()

# called once on last framee
def exit():
    if macro.APP_RUNNING is False:
        if macro.EXIT_CALLED is False:
            macro.EXIT_CALLED = True
            print("[APP HAS EXITED]")


# EXCECUTION
awake()
start()
update()
exit()

