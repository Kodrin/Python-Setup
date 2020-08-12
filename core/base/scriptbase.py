class ScriptBase():
    AWAKE_CALLED = False
    START_CALLED = False
    EXIT_CALLED = False

    # called once before start
    def awake(self):
        self.AWAKE_CALLED = True
        return 1

    # called once after awake
    def start(self):
        self.START_CALLED = True
        return 1

    # main loop
    def update(self):
        return 1

    # called once on last frame
    def exit(self):
        self.EXIT_CALLED = True
        return 1
