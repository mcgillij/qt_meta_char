

class MetaChar:
    def __init__(self):
        self.name = ""
        self.history = ""
        self.brain = Brain()

class Brain:
    def __init__(self):
        # stats
        self.name = ""
        self.intelligence = 0
        self.reflex = 0
        self.technology = 0
        self.dexterity = 0
        self.cool = 0
        self.will = 0
        self.str = 0
        self.con = 0
        self.move = 0
        self.body = 0
        #derived stats
        self.luck = 0
        self.humanity = 0
        self.recovery = 0
        self.endurance = 0
        self.run = 0
        self.sprint = 0
        self.swim = 0
        self.leap = 0
        self.hits = 0
        self.stun = 0

