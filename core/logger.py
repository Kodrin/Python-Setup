from core.base.scriptbase import ScriptBase
from core.entry import Entry

from random import randint, randrange
from core import entry

class Logger(ScriptBase):
    DATA_PATH = "/data"
    FILE_NAME = "log_file.txt"
    LOG_AMOUNT = 100

    # def __init__(self, filename):
    #     self.filename = filename

    def start(self):
        self.generate_logs(self.LOG_AMOUNT)
        print("## Generating Logs ##")

    def generate_logs(self, log_amount):
        LOG = ""
        for _ in range(log_amount):
            new_log = self.generate_entry()
            LOG += new_log

        write_file = open("./data/log_file.txt", "w")
        write_file.write(LOG)
        write_file.close()

    def generate_entry(self):
        entry = Entry()
        entry.randomize()

        entry_id = self.column_format(entry.id, 10)
        entry_desc = self.column_format(entry.desc, 30)
        entry_category = self.column_format(entry.category, 15)
        entry_timespent = self.column_format(entry.timespent, 10)

        return "\n" + entry_id + entry_category + entry_timespent + entry_desc
        # return Entry(id, description, category, time_spent)

    def column_format(self, value, length):
        column_length = length                      # how many characters wide
        string_value = str(value)
        string_value_len = len(string_value)

        if string_value_len > column_length:
            return string_value[0:column_length] #truncated value to column length
        elif string_value_len < column_length:
            difference = column_length - string_value_len
            for _ in range(difference):
                string_value += " "
            return string_value

        return string_value
