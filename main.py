# basic library for mathematical operations
# import tkinter as tk
import math
from core.logger import Logger

sample_file = open("data/sample.txt", "r+")

for line in sample_file.readlines():
    print(line)

sample_file.close()

LOGGER = Logger("something")
LOGGER.generate_logs(10)

# print("Hello, World!")
# print("my name is codrin!")
# print("this is a basic python learning project")
# print("just for fun!")
