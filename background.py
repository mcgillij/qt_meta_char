import random

class CharInfo():
    def __init__(self, age, traits, feel_people, value_most, valued_person, valued_possession, clothes, hair, affectations, origins, background, parent=None):
        self.age = int(age)
        self.traits = traits
        self.feel_people = feel_people
        self.value_most = value_most
        self.valued_person = valued_person
        self.valued_possession = valued_possession
        self.clothes = clothes
        self.hair = hair
        self.affectations = affectations
        self.origins = origins
        self.background = background

    def return_me(self):
        output =  "Age: " + str(self.age) + "\n"
        output +=  "Traits: " + self.traits + "\n"
        output +=  "Feels about people: " + self.feel_people + "\n"
        output +=  "Value Most: " + self.value_most + "\n"
        output +=  "Valued Person: " + self.valued_person + "\n"
        output +=  "Valued Possession: " + self.valued_possession + "\n"
        output +=  "Clothes: " + self.clothes + "\n"
        output +=  "Hair: " + self.hair + "\n"
        output +=  "Affectations: " + self.affectations + "\n"
        output +=  "Origins: " + self.origins + "\n"
        output +=  str(self.background)
        return output

    def print_me(self):
        print "Age: " + str(self.age) + "\n"
        print "Traits: " + self.traits + "\n"
        print "Feels about people: " + self.feel_people + "\n"
        print "Value Most: " + self.value_most + "\n"
        print "Valued Person: " + self.valued_person + "\n"
        print "Valued Possession: " + self.valued_possession + "\n"
        print "Clothes: " + self.clothes + "\n"
        print "Hair: " + self.hair + "\n"
        print "Affectations: " + self.affectations + "\n"
        print "Origins: " + self.origins + "\n"
        print self.background

class Roller():
    def __init__(self, parent=None):
        self.age = 0
        self.background_edgerunner = [
                "Edge Runner Leader",
                "Corporates",
                "Corporates",
                "Combat Freelancers",
                "Combat Freelancers",
                "Middle Class",
                "Smugglers",
                "Gang Family",
                "Crime Family",
                "Combat Zone Poor",
                "Urban Homeless",
                "Arcology Family"
                ]
        self.background_desnai = [
                "Park Managers",
                "Imaginators",
                "Technicians",
                "Idol Family",
                "General Workers",
                "General Workers",
                "Park Security Ops",
                "Mechjocks",
                "Park Regional Manager",
                "Park Maintenance"
                ]
        self.background_reef = [
                "Community Leaders",
                "Dive Team",
                "Technicians",
                "Subjocks",
                "Ex-Pirates",
                "Security Forces",
                "Sea Farmers",
                "Sea Farmers",
                "Traders",
                "Explorers"
                ]
        self.background_rip = [
                "City Leaders",
                "City Managers",
                "City Technicians",
                "Trader Family",
                "Sea Gatherers",
                "Sea Gatherers",
                "Bioform Techs",
                "Sea Farmers",
                "City Fighters",
                "Surfriders"
                ]
        self.background_ceemetal = [
                "Council Wisemen",
                "Body Technician",
                "Protectors",
                "Transporters",
                "Dragoons",
                "Artisans",
                "Archivists",
                "Everyday Citizens",
                "Everyday Citizens",
                "Wealthy Citizens"
                ]
        self.background_roller = [
                "Council Leaders",
                "Shamen",
                "Warriors",
                "Warriors",
                "Family Leaders",
                "Pirates",
                "Go-Gangers",
                "Traders",
                "Traders",
                "Migrant Farmers",
                "Scouts"
                ]

        self.parents_status = [
                "Both parents are living",
                "Both parents are living",
                "Both parents are living",
                "Both parents are living",
                "Both parents are living",
                "Both parents are living",
                "Something has happened to one or both parents",
                "Something has happened to one or both parents",
                "Something has happened to one or both parents"
                ]

        self.family_status = [
                "Family status in danger, and you risk losing everything(if you haven't already)",
                "Family status in danger, and you risk losing everything(if you haven't already)",
                "Family status in danger, and you risk losing everything(if you haven't already)",
                "Family status in danger, and you risk losing everything(if you haven't already)",
                "Family status in danger, and you risk losing everything(if you haven't already)",
                "Family status in danger, and you risk losing everything(if you haven't already)",
                "Family status is OK, even if parents are missing or dead",
                "Family status is OK, even if parents are missing or dead",
                "Family status is OK, even if parents are missing or dead"
                ]

        self.family_tragedy = [
                "Family lost everything through betrayal",
                "Family lost everything through bad management",
                "Family exiled or otherwise driven out from their original home/nation/corporation",
                "Family is imprisoned and you alone escaped",
                "Family vanished. You are the only remaining member",
                "Family was murdered / killed and you were the only survivor",
                "Family was involved in a longterm conspiracy, organization or association such as a crime family or revolutionary group",
                "Family was scattered to the winds due to misfortune",
                "Family is cursed with a hereditary feud that has lasted generations",
                "You are the inheritor of a family debt; you must honor this debt before moving on with your life"
                ]

        self.family_happened = [
                "Your parents died in warfare",
                "Your parents died in an accident",
                "Your parents were murdered",
                "Your parents have amnesia and don't remember you",
                "You never knew your parents",
                "Your parents are in hiding to protect you",
                "Your parents left with relatives for safe-keeping",
                "You grew up on the Street and never had parents",
                "Your parents gave you up for adoption",
                "Your parents sold you for money"
                ]

        self.childhood_environment = [
                "Spent on the Street with no adult supervision",
                "Spent in a safe, stable CorpZone, Enclave or Roller City",
                "On the run from enemies, always moving from place to place",
                "In a decaying, once upscale part of the MidCity",
                "In an Enclave in the MidCity always under attack",
                "In the ruins of the Undercity",
                "In a small Enclave or town far from the city",
                "On the glittering High City Levels",
                "In an OceanZone environment",
                "Traveling on or near the RoadZones"
                ]

        # roll even for each sibling is male otherwise female
        self.sibling_age = [
                "older than you",
                "older than you",
                "older than you",
                "older than you",
                "older than you",
                "younger than you",
                "younger than you",
                "younger than you",
                "your twin"
                ]
        # for each sibling roll how they feel about you
        self.sibling_feel = [
                "dislike you",
                "dislike you",
                "like you",
                "like you",
                "is neutral",
                "is neutral",
                "they hero worship you",
                "they hero worship you",
                "they hate you",
                "they hate you"
                ]

        self.life_events = [
                "Big Problems, Big Wins",
                "Big Problems, Big Wins",
                "Big Problems, Big Wins",
                "Friends & Enemies",
                "Friends & Enemies",
                "Romantic Involvement",
                "Romantic Involvement",
                "Nothing happened that year",
                "Nothing happened that year"
                ]

        # even lucky
        self.life_events_lucky = [
                "Made a Powerful Connection in the Local Government. Roll 1D10. 1-4 Local Security Forces, 5-7 Local Altcult Leader's Office, 8-10 City Manager's Office",
                "Financial Windfall: Roll 1D10 x 100 for amount of NCD",
                "Big Score on the job or deal! Roll 1D10 x 100 for amount of NCD",
                "Find a Sensei (teacher) Begin at +2 or add +1 to a Martial Arts skill of your choice",
                "Find a teacher: Add +1 to any INT based skill, or begin a new INT based skill at +2",
                "Powerful Altcult member owes you a favor",
                "Local Nomad Pack befriends you. You can call upon them for one favor a month, equivalent to a Family Perk of +2",
                "Made a friend in a local Altcult. You may use him for inside information at a level of +2 Streetwise on any situation relating to that Altcult",
                "Local Boostergang likes you (Who knows why. These are Boosters right?) You can call upon them for 1 favor a month, equivalent to Family Perk of +2. But don't push your luck",
                "Find a Combat Teacher. Add +1 to any weapon skill with the exception of Martial Arts or Brawling, or begin a new combat skill at +2"
                ]

        # odd disaster
        self.life_events_disaster = [
                "Financial Loss or Debt: Roll 1D10 x 100. You have lost this much in Night City Dollars. If you can't pay this now, you have a debt to pay, in cash or in blood",
                "Imprisonment. You have been in prison, or possibly held hostage (your choice). Roll 1D10 for length of imprisonment in months",
                "Illness or addiction. You have contracted either an illness or a drug habit in this time. Lost 1 pt of REF permanently as a result",
                "Betrayal: you have been backstabbed in some manner. Roll another D10, 1-3 you are being blackmailed. 4-7 a secret was exposed, 8-10 you were betrayed by a close friend in either romance or career(you choose)",
                "Accident: You were in some kind of terrible accident. Roll 1D10. 1-4 you were terribly maimed and must substract -2 from your DEX. 5-6, you were hospitalized for 1D10 months that year. 7-8, you have lost 1D10 months of memory of that year. 9-10, you constantly relive nightmares (8 in 10 chance each night) of the accident and wake up screaming",
                "Lover, friend or relative killed. You lost someone you really cared about. 1-5, they died accidentally. 6-8, they were murdered by an unknown parties. 9-10, they were murdered and you know who did it. You just need proof",
                "False Accusation: You were setup. Roll 1D10. 1-3, the accusation is theft, 4-5, it's cowardice, 6-8, it's murder, 9, it's rape, 10, its lying or betrayal",
                "Hunted by the Law: You are hunted by the law for crimes you may or may not have commited (your choice). Roll 1D10. 1-3, only a couple of local renta-cops want you. 4-6, it's an entire local Security Force. 7-8, it's an Altcult Militia, 9-10, it's the FBI or equiv national police force",
                "Hunted by Neo-Corp: You have angered some Corporate Honcho. Roll 1D10. 1-3, it's a small local firm. 4-6, it's a larger corp with offices Citywide, 7-8, it's a big, national corp with agents in most major cities. 9-10; it's a huge multinational with armies, ninja's and spies everywhere",
                "Mental or Physical Incapacitation: You have experienced some type of mental or physical breakdown. Roll 1D10. 1-3, it's some type of nervous disorder. probably from a bioplague -- lose 1 pt REF. 4-7, it's some kind of mental problem; you suffer anxiety attacks and phobias. Lose 1 pt from your COOL stat. 8-10. it's a major psychosis. You hear voices, are violent, irrational, depressive. Lose 1 pt from COOL and REF stats"
                ]
        # what are you going to do about it
        self.life_events_waygdai = [
                "Clear your name",
                "Clear your name",
                "Live it down and try to forget it",
                "Live it down and try to forget it",
                "Hunt down those responsible and make them pay!",
                "Hunt down those responsible and make them pay!",
                "Get whats rightfully yours",
                "Get whats rightfully yours",
                "Save, if possible, anyone else involved in the situation",
                "Save, if possible, anyone else involved in the situation"
                ]

        self.friends_and_enemies = [
                "You made a friend",
                "You made a friend",
                "You made a friend",
                "You made a friend",
                "You made a friend",
                "You made an enemy",
                "You made an enemy",
                "You made an enemy",
                "You made an enemy",
                "You made an enemy",
                ]
        # even male, odd female
        self.friend_relationship = [
                "Like a big brother/sister to you",
                "Like a kid sister / brother to you",
                "A teacher or mentor",
                "A partner / co-worker",
                "An old lover (choose which one)",
                "An old enemy (choose which one)",
                "Like a foster parent to you",
                "A relative",
                "Reconnect with a childhood friend",
                "Met through common interest"
                ]
        # even male, odd female
        self.enemies_relationship = [
                "Ex friend",
                "Ex Lover",
                "Relative",
                "Childhood enemy",
                "Person working for you",
                "Person you work for",
                "Partner or co-worker",
                "Boostergan member",
                "Neo-Corporate Exec",
                "Government Official or Altcult Leader"
                ]
        # the cause
        self.enemies_cause = [
                "Caused the other to lose face or status",
                "Caused the loss of a lover, friend or relative",
                "Caused a major humiliation",
                "Accused the other of cowardice or some other personal flaw",
                "Caused a physical disability: Roll 1D6. 1-2, lose eye. 3-4, lose arm. 5-6, badly scarred",
                "Deserted or betrayed the other",
                "Turned down job offer or romantic involvement",
                "You just didn't like eachother",
                "Was romantic rival",
                "Foiled a plan of the other"
                ]
        # who is frakked off
        self.enemies_frakked = [
                "They hate you",
                "They hate you",
                "They hate you",
                "They hate you",
                "You hate them",
                "You hate them",
                "You hate them",
                "The feelings mutual",
                "The feelings mutual"
                ]
        # whatcha gonna do about it
        self.enemies_wgdabi = [
                "Go into a murderous, killing rage and rip his face off!",
                "Go into a murderous, killing rage and rip his face off!",
                "Avoid the scum",
                "Avoid the scum",
                "Backstab him indirectly",
                "Backstab him indirectly",
                "Ignore the scum",
                "Ignore the scum",
                "Rip into him verbally",
                "Rip into him verbally"
                ]
        # what can they throw against you
        self.enemies_forces = [
                "Just themselves",
                "Just themselves",
                "Just themselves",
                "Themselves and a few friends",
                "Themselves and a few friends",
                "An entire gang",
                "An entire gang",
                "A small Corp or local Altcult",
                "A large Corp or Entire Enclave",
                "An entire Altcult (your'e a one man kulturekampf!)"
                ]

        # romantic life
        self.romantic_how_it_worked_out = [
                "Happy love affair",
                "Happy love affair",
                "Happy love affair",
                "Happy love affair",
                "Tragic love affair",
                "Love Affair with problems",
                "Love Affair with problems",
                "Fast Affairs and Hot Dates",
                "Fast Affairs and Hot Dates",
                "Life got COMPLICATED"
                ]

        self.tragic_love_affair = [
                "Lover died in accident",
                "Lover mysteriously vanished",
                "It didn't work out",
                "A personal goal or vendetta came between you",
                "Lover kidnapped",
                "Lover went insane",
                "Lover committed suicide",
                "Lover killed in a fight",
                "Rival cut you out of the action",
                "Lover  imprisoned or exiled"
                ]
        self.mutual_feelings = [
                "They still love you",
                "You still love them",
                "You still love eachother",
                "You hate them",
                "They hate you",
                "You hate eachother",
                "You're friends",
                "No feelings either way; it's over",
                "You like them, they hate you",
                "They like you, you hate them"
                ]

        self.complicated = [
                "Someone got pregnant and now you have a kid",
                "Someone got pregnant and now you have a kid",
                "Your old lover just secretly showed up",
                "Their old Lover just secretly showed up",
                "One of you had a kid in the past and they just showed up",
                "One of you had a kid in the past and they just showed up",
                "One of you had a kid in the past and they just showed up",
                "You have a terrible secret your hiding from them",
                "An old enemy of yours just showed up",
                "An old enemy of theirs just showed up"
                ]

        self.love_affair_with_problems = [
                "Your lovers friends / family hate you",
                "Your lovers friends / family would use any means to get rid of you",
                "Your friends / family hate your lover",
                "One of you has a romantic rival",
                "You are seperated in some way",
                "You fight constantly",
                "You're professional rivals",
                "One of you is insanely jealous",
                "One of you is messing around",
                "You have conflicting backgrounds and families"
                ]

        self.personality_traits = [
                "Shy and secretive",
                "Rebellious, antisocial, violent",
                "Arrogant, proud and aloof",
                "Moody, rash and headstrong",
                "Picky, fussy and nervous",
                "Stable and serious",
                "Silly and fluffheaded",
                "Sneaky and deceptive",
                "Intellectual and detached",
                "Friendly and outgoing"
                ]

        self.how_do_you_feel_about_people = [
                "Neutral",
                "Neutral",
                "I like almost everyone",
                "I hate almost everyone",
                "People are tools. Use them for your own goals and discard them",
                "Every person is a valuable individual",
                "People are obstacles to be destroyed if they cross me",
                "People are untrustworthy, don't depend on anyone",
                "Wipe'em all out and give the place to cockroaches",
                "People are wonderful"
                ]

        self.what_do_you_value_most = [
                "Money",
                "Honor",
                "Your word",
                "Honesty",
                "Knowledge",
                "Vengeance",
                "Love",
                "Power",
                "Having a good time",
                "Friendship"
                ]
        self.what_person_do_you_value_most = [
                "A parent",
                "Brother or sister",
                "Lover",
                "Friend",
                "Yourself",
                "A pet",
                "Teacher or mentor",
                "Public Figure",
                "A personal hero",
                "No one"
                ]

        self.your_most_valued_possession = [
                "a weapon",
                "a tool",
                "a piece of clothing",
                "a photograph",
                "a book or diary",
                "a recording",
                "a musical instrument",
                "a piece of jewelry",
                "a toy",
                "a letter"
                ]

        self.personal_style_clothes = [
                "Biker leathers",
                "Blue jeans",
                "Corpoate Suits",
                "Jumpsuits",
                "Miniskirts",
                "High fashion",
                "Cammos",
                "Normal",
                "Nude",
                "Bag lady chic"
                ]
        self.personal_style_hair = [
                "Mowhawk",
                "Long & Ratty",
                "Short & Spiked",
                "Wild & all over",
                "Bald",
                "Striped",
                "Tinted",
                "Neat, short",
                "Short, curly",
                "Long, straight"
                ]
        self.personal_affectations = [
                "Tattoos",
                "Mirrorshades",
                "Ritual Scars",
                "Spiked Gloves",
                "Nose ring",
                "Earrings",
                "Long fingernails",
                "Spiked heeled boots",
                "Weird Contact Lenses",
                "Fingerless gloves"
                ]
        # automagically know your base lang at level 8, and "streetslang" (common in dnd)
        self.personal_origins = [
                "Anglo-American (English)",
                "African (Bantu, Hongo, Ashanti, Zulu, Swahili)",
                "Japanese or Korean",
                "Central European / Soviet (Bulgarian, Russian, Czech, Polish, Ukrainian, Slovak)",
                "Pacific Islander (Micronesian, Tagalog, Polynesian, Malayan, Sudanese, Indonesian, Hawaiian)",
                "Chinese / Southeast Asian (Burmese, Caontonese, Mandarin, Thai, Tibetan, Vietnamese)",
                "Black American (English, Blackfolk)",
                "Hispanic American (Spanish, English)",
                "Central / South American (Spanish, Portuguese)",
                "European (French, German, English, Spanish, Italian, Greek, Danish, Dutch, Norwegian, Swedish, Finnish)"
                ]

    def roll_personality(self, age):
        age = age 
        num_years = age - 16
        traits = random.choice(self.personality_traits)
        how_do_you_feel_about_people = random.choice(self.how_do_you_feel_about_people)
        value_most = random.choice(self.what_do_you_value_most)
        what_person_do_you_value_most = random.choice(self.what_person_do_you_value_most)
        possession = random.choice(self.your_most_valued_possession)
        clothes = random.choice(self.personal_style_clothes)
        hair = random.choice(self.personal_style_hair)
        affectations = random.choice(self.personal_affectations)
        origins = random.choice(self.personal_origins)
        background = self.roll_background(num_years)
        c = CharInfo(age, traits, how_do_you_feel_about_people, value_most, what_person_do_you_value_most, possession, clothes, hair, affectations, origins, background)
        #c.print_me()
        return c

    def roll_background(self, num_years):
        backgrounds = []
        backgrounds.extend(self.background_edgerunner)
        backgrounds.extend(self.background_desnai)
        backgrounds.extend(self.background_reef)
        backgrounds.extend(self.background_rip)
        backgrounds.extend(self.background_ceemetal)
        backgrounds.extend(self.background_roller)
        background = "Background: " + random.choice(backgrounds) + "\n"

        parents_status = random.choice(self.parents_status)
        if parents_status == "Both parents are living":
            background += "Parent Status: " + parents_status + "\n"
            family_status = random.choice(self.family_status)
            background += "Family Status: " + family_status + "\n"
            if family_status == "Family status in danger, and you risk losing everything(if you haven't already)":
                family_tragedy = random.choice(self.family_tragedy)
                background += "Family Tragedy: " + family_tragedy + "\n"
            else:
                family_happened = random.choice(self.family_happened)
                background += "Family Happened: " + family_happened + "\n"
        else:
            background += "Parent Status: " + parents_status + "\n"
            family_happened = random.choice(self.family_happened)
            background += "Family Happened: " + family_happened + "\n"

        childhood_environment = random.choice(self.childhood_environment)
        background += "Childhood Environment: " + childhood_environment + "\n"

        siblings = random.randint(1,10)
        if siblings <= 7:
            num_siblings = siblings
        elif siblings >= 8:
            num_siblings = 0 # only child

        background += "Siblings: " + str(num_siblings) + "\n"
        for i in range(num_siblings):
            sibling_gender = random.randint(1,10)
            sibling_age = random.choice(self.sibling_age)
            sibling_feel = random.choice(self.sibling_feel)
            if is_even(sibling_gender):
                sibling_gender = "Male"
            else:
                sibling_gender = "Female"

            background += "Sibling #" + str(i+1) + " is " + sibling_gender + " and " + sibling_age + " and " + sibling_feel + "\n"

        background += "Life Events: \n"
        background += "Years 1-16: Growing up\n";
        # 1 major event for each year after 16
        for i in range(num_years):
            event = random.choice(self.life_events)
            if event == "Big Problems, Big Wins":
                num = random.randint(1,10)
                if is_even(num):
                    # big win
                    event = random.choice(self.life_events_lucky)
                else:
                    event = random.choice(self.life_events_disaster)
                    what_you_gonna_do = random.choice(self.life_events_waygdai)
                    event = event + " and you want to " + what_you_gonna_do 

            elif event == "Friends & Enemies":
                friend_or_enemy = random.choice(self.friends_and_enemies)
                if friend_or_enemy == "You made a friend":
                    num = random.randint(1,10)
                    if is_even(num):
                        friend_gender = "Male"
                    else:
                        friend_gender = "Female"
                    friend_status = random.choice(self.friend_relationship)
                    friend_clothes = random.choice(self.personal_style_clothes)
                    friend_hair = random.choice(self.personal_style_hair)
                    friend_affectations = random.choice(self.personal_affectations)
                    friend_motivation = random.choice(self.personality_traits)
                    event = "You made a " + friend_gender + " friend and he/she's an " + friend_status + "\n" + "They usually wear " + friend_clothes + " clothes, and they rock a " + friend_hair + " haircut and also like " + friend_affectations + "\n" + "Your buddy also has the following motivation: " + friend_motivation
                else:
                    # enemy
                    num = random.randint(1,10)
                    if is_even(num):
                        enemy_gender = "Male"
                    else:
                        enemy_gender = "Female"

                    enemy_relation = random.choice(self.enemies_relationship)
                    enemy_cause = random.choice(self.enemies_cause)
                    whos_frakked = random.choice(self.enemies_frakked)
                    what_you_gonna_do = random.choice(self.enemies_wgdabi)
                    enemy_forces = random.choice(self.enemies_forces)
                    event = "You made a " + enemy_gender + " enemy and he/she's an " + enemy_relation + " and also " + enemy_cause + " and " + whos_frakked + " and you intend to " + what_you_gonna_do + " but they may have some extra influence from " + enemy_forces

            elif event == "Romantic Involvement":
                relationship = random.choice(self.romantic_how_it_worked_out)
                if relationship == "Tragic love affair":
                    tragic = random.choice(self.tragic_love_affair)
                    mutual_feelings = random.choice(self.mutual_feelings)
                    event = relationship + ": " + tragic + " and your feelings on the matter are " + mutual_feelings
                elif relationship == "Love Affair with problems":
                    problems = random.choice(self.love_affair_with_problems)
                    event = relationship + ": " + problems
                elif relationship == "Life got COMPLICATED":
                    complication = random.choice(self.complicated)
                    event = relationship + ": " + complication
                else:
                    event = event + ": " + relationship


            background += str(i+17)+ ": " + event + "\n"
        return background

    def main(self):
        self.roll_personality(25)

def is_even(num):
    return num % 2 == 0

if __name__=='__main__':
    app = Roller()
    app.main()
