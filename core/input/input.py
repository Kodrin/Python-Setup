# this is the input module for detecting key inputs
import macro
import keyboard as key              # for keyboard input
from core.base.scriptbase import ScriptBase

class Input(ScriptBase):

    def init(self):
        global execute_logger
        execute_logger = False

    def update(self):
        self.controls()
        if key.is_pressed("e"):
            macro.APP_RUNNING = False

    def controls(self):
        execute_logger = key.is_pressed("l")
        if execute_logger is True:
            print("Logger is executing")
