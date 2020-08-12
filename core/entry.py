import random

CATEGORIES = [
    "R&D",
    "COOKING",
    "CODING",
    "PHOTOGRAPHY",
    "GAMING"
]

DESCRIPTIONS = [
    "refactored some code",
    "made coconut curry",
    "researched how to walk",
    "took pics of my feet",
    "played chess with myself"
]


class Entry:

    def __init__(self, id = 0, desc = "null", category = "null", timespent = 0.0):
        self.id = id
        self.desc = desc
        self.category = category
        self.timespent = timespent

    def randomize(self):
        self.id = random.randint(0,1000)
        self.desc = random.choice(DESCRIPTIONS)
        self.category = random.choice(CATEGORIES)
        self.timespent = random.randint(0, 3)

