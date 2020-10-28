from core.base.scriptbase import ScriptBase
from core.entry import Entry

class Logger(ScriptBase):
    DATA_PATH = "./data/"
    FILE_NAME = "log_file.txt"
    PATH_TO_FILE = DATA_PATH + FILE_NAME
    LOG_AMOUNT = 50
    IDENTIFIER = "#"
    ENTRIES = []

    def start(self):
        self.generate_logs(self.LOG_AMOUNT)
        # self.read_logs()

    def generate_logs(self, log_amount):
        print("## Generating Logs ##")
        log_file = ""
        for _ in range(log_amount):
            new_log = self.generate_entry(_)
            log_file += new_log

        write_file = open(self.PATH_TO_FILE, "w")
        write_file.write(log_file)
        write_file.close()
        print("~~ Generated Logs ~~")

    def read_logs(self):
        print("## Reading Logs ##")
        read_file = open(self.PATH_TO_FILE, "r")

        lines = read_file.readlines()
        for line in lines:
            self.ENTRIES.append(self.decode_entry(line))

        read_file.close()
        print("~~ Done Reading Logs ~~")

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
        entry = Entry()
        string_value = str(value)               # stringify data
        decoded_data_list = []                  # list for out decoded data
        data_list = string_value.split(self.IDENTIFIER)     # separate based on identifier

        for element in data_list:               # trim out whitespace and insert to new list
            element = element.rstrip()
            decoded_data_list.append(element)

        decoded_data_list.remove("")            # remove empty elements from list

        entry.id = decoded_data_list[0]
        entry.category = decoded_data_list[1]
        entry.timespent = decoded_data_list[2]
        entry.desc = decoded_data_list[3]

        return entry
