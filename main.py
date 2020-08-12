import keyboard as key              # for keyboard input
from core.logger import Logger      # logging module

APP_RUNNING = True                  # app macros
AWAKE_CALLED = False
START_CALLED = False

# called once before start
def awake():
    global AWAKE_CALLED
    if AWAKE_CALLED is False:
        AWAKE_CALLED = True
        print("[AWAKE HAS BEEN CALLED]")

# called once after awake
def start():
    global START_CALLED
    if START_CALLED is False:
        START_CALLED = True
        print("[START HAS BEEN CALLED]")
        # do something here

# main loop
def update():
    global APP_RUNNING
    while APP_RUNNING is True:
        # my_name = input()
        # print(my_name)
        if key.is_pressed("e"):
            APP_RUNNING = False

# called once on last framee
def exit():
    global APP_RUNNING
    if APP_RUNNING is False:
        print("[APP HAS EXITED]")


# execution
awake()
start()
update()
exit()

# print("Hello, World!")
# print("my name is codrin!")
# print("this is a basic python learning project")
# print("just for fun!")
