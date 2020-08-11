from core.entry import Entry

from random import randint, randrange
from core import entry

class Logger:
    DATA_PATH = "/data"

    def __init__(self, filename):
        self.filename = filename


    def generate_logs(self, log_amount):
        LOG = ""
        for _ in range(log_amount):
            new_log = self.generate_entry()
            LOG += new_log

        write_file = open("./data/log_file.txt", "w")
        write_file.write(LOG)
        write_file.close()

    def generate_entry(self):
        id = randint(0,1000)
        description = "I am running!"
        category = "GAMING"
        time_spent = randrange(0.0,3.0)
        return "\n" + str(id) + description + category + str(time_spent)
        # return Entry(id, description, category, time_spent)
