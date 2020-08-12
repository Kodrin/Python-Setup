import random

CATEGORIES = [
    "R&D",
    "READING",
    "DESIGN",
    "LEARNING",
    "EXERCISE",
    "TRAVEL",
    "COMMUTE",
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

TIMESPENT = [
    0.25,
    0.5,
    0.75,
    1.0,
    1.25,
    1.5,
    1.75,
    2.0,
    2.25,
    2.5,
    2.75,
    3.0
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
        self.timespent = random.choice(TIMESPENT)

