CATEGORIES = [
    "R&D",
    "COOKING",
    "CODING",
    "PHOTOGRAPHY",
    "GAMING"
]


class Entry:

    def __init__(self, id, desc, category, timespent):
        self.id = id
        self.desc = desc
        self.category = category
        self.timespent = timespent