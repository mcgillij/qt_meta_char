import os, glob, pickle


class Char:
    def __init__(self):
        self.name = ""
        self.reputation = 0
        self.ip = 0
        self.lifepath = ""
        self.traits = ""
        self.feel_about_people = ""
        self.you_value_most = ""
        self.valued_person = ""
        self.valued_possession = ""
        self.clothes = ""
        self.hair = ""
        self.affectations = ""
        self.origins = ""
        self.languages = ""
        self.background = ""
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
        self.skill_1 = ""
        self.skill_1_lvl = 0
        self.skill_2 = ""
        self.skill_2_lvl = 0
        self.skill_3 = ""
        self.skill_3_lvl = 0
        self.skill_4 = ""
        self.skill_4_lvl = 0
        self.skill_5 = ""
        self.skill_5_lvl = 0
        self.skill_6 = ""
        self.skill_6_lvl = 0
        self.skill_7 = ""
        self.skill_7_lvl = 0
        self.skill_8 = ""
        self.skill_8_lvl = 0
        self.skill_9 = ""
        self.skill_9_lvl = 0
        self.skill_10 = ""
        self.skill_10_lvl = 0
        self.skill_11 = ""
        self.skill_11_lvl = 0
        self.skill_12 = ""
        self.skill_12_lvl = 0
        self.skill_13 = ""
        self.skill_13_lvl = 0
        self.skill_14 = ""
        self.skill_14_lvl = 0
        self.skill_15 = ""
        self.skill_15_lvl = 0
        self.skill_16 = ""
        self.skill_16 = 0
        self.perk_1 = ""
        self.perk_1_lvl = 0
        self.perk_2 = ""
        self.perk_2_lvl = 0
        self.perk_3 = ""
        self.perk_3_lvl = 0
        self.perk_4 = ""
        self.perk_4_lvl = 0
        self.perk_5 = ""
        self.perk_5_lvl = 0
        self.perk_6 = ""
        self.perk_6_lvl = 0
        self.perk_7 = ""
        self.perk_7_lvl = 0
        self.perk_8 = ""
        self.perk_8_lvl = 0
        self.perk_9 = ""
        self.perk_9_lvl = 0
        self.perk_10 = ""
        self.perk_10_lvl = 0
        self.perk_11 = ""
        self.perk_11_lvl = 0
        self.perk_12 = ""
        self.perk_12_lvl = 0
        self.perk_13 = ""
        self.perk_13_lvl = 0
        self.perk_14 = ""
        self.perk_14_lvl = 0
        self.perk_15 = ""
        self.perk_15_lvl = 0
        self.perk_16 = ""
        self.perk_16 = 0
        self.outfit = ""
        self.weapons = ""


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
