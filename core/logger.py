from core.base.scriptbase import ScriptBase
from core.entry import Entry

class Logger(ScriptBase):
    DATA_PATH = "./data/"
    FILE_NAME = "log_file.txt"
    PATH_TO_FILE = DATA_PATH + FILE_NAME
    LOG_AMOUNT = 5
    IDENTIFIER = "#"

    def start(self):
        print("## Generating Logs ##")
        # self.generate_logs(self.LOG_AMOUNT)
        self.read_logs()
        print("~~ Generated Logs ~~")

    def generate_logs(self, log_amount):
        LOG = ""
        for _ in range(log_amount):
            new_log = self.generate_entry(_)
            LOG += new_log

        write_file = open(self.PATH_TO_FILE, "w")
        write_file.write(LOG)
        write_file.close()

    def read_logs(self):
        read_file = open(self.PATH_TO_FILE, "r")
        lines = read_file.readlines()
        for line in lines:
            self.decode_entry(line)

        read_file.close()

    def generate_entry(self, index):
        entry = Entry()
        entry.randomize()

        entry_id = self.encode_entry(index, 10)
        entry_desc = self.encode_entry(entry.desc, 30)
        entry_category = self.encode_entry(entry.category, 15)
        entry_timespent = self.encode_entry(entry.timespent, 10)

        if index == 0:
            return entry_id + entry_category + entry_timespent + entry_desc
        else:
            return "\n" + entry_id + entry_category + entry_timespent + entry_desc
        # return Entry(id, description, category, time_spent)

    def encode_entry(self, value, length):
        column_length = length                              # how many characters wide
        string_value = str(value)
        string_value = self.IDENTIFIER + string_value
        string_value_len = len(string_value)

        if string_value_len > column_length:
            return string_value[0:column_length]            # truncated value to column length
        elif string_value_len < column_length:
            difference = column_length - string_value_len
            for _ in range(difference):
                string_value += " "
            return string_value

        return string_value

    def decode_entry(self, value):
        string_value = str(value)               # stringify data
        decoded_data_list = []                  # list for out decoded data
        data_list = string_value.split(self.IDENTIFIER)     # separate based on identifier

        for element in data_list:               # trim out whitespace and insert to new list
            element = element.rstrip()
            decoded_data_list.append(element)

        decoded_data_list.remove("")            # remove empty elements from list
        print (decoded_data_list)

