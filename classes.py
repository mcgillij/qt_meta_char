import os, glob, pickle

class MetaChar:
    def __init__(self):
        self.name = ""
        self.history = ""
        self.brain = Brain()
        self.right_hand = RightHand()
        self.left_hand = LeftHand()
        self.body = Body()
    def save_to_disk(self, filename):
        print "Attempting to save to disk with pickle"
        save_file = file(filename, "wb")
        pickle.dump(self, save_file, 2)
        save_file.close()

    def load_from_disk(self, filename):
        print "Attempting to load from disk with pickle"
        load_file = file(filename, "rb")
        meta_char = pickle.load(load_file)
        load_file.close()
        return meta_char

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
        self.strength = 0
        self.constitution = 0
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
        # key skills
        self.key_skill_1 = ""
        self.key_skill_1_lvl = 0
        self.key_skill_2 = ""
        self.key_skill_2_lvl = 0
        self.key_perk_1 = ""
        self.key_perk_1_lvl = 0
        self.key_perk_2 = ""
        self.key_perk_2_lvl = 0
        self.lifepath = ""
        self.goals = ""

class RightHand:
    def __init__(self):
        # stats
        self.name = ""
        self.intelligence = 0
        self.reflex = 0
        self.technology = 0
        self.dexterity = 0
        self.cool = 0
        self.will = 0
        self.strength = 0
        self.constitution = 0
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
        # key skills
        self.key_skill_1 = ""
        self.key_skill_1_lvl = 0
        self.key_skill_2 = ""
        self.key_skill_2_lvl = 0
        self.key_perk_1 = ""
        self.key_perk_1_lvl = 0
        self.key_perk_2 = ""
        self.key_perk_2_lvl = 0
        self.lifepath = ""
        self.goals = ""

class LeftHand:
    def __init__(self):
        # stats
        self.name = ""
        self.intelligence = 0
        self.reflex = 0
        self.technology = 0
        self.dexterity = 0
        self.cool = 0
        self.will = 0
        self.strength = 0
        self.constitution = 0
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
        # key skills
        self.key_skill_1 = ""
        self.key_skill_1_lvl = 0
        self.key_skill_2 = ""
        self.key_skill_2_lvl = 0
        self.key_perk_1 = ""
        self.key_perk_1_lvl = 0
        self.key_perk_2 = ""
        self.key_perk_2_lvl = 0
        self.lifepath = ""
        self.goals = ""

class Body:
    def __init__(self):
        self.leaders = ""
        self.soldiers = ""
        self.grunts = ""
        self.assets = ""
        self.vehicles = ""
