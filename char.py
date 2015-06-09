from PyQt4 import QtGui
from PyQt4.QtCore import *
import sys
from pprint import pprint
import char_window
from classes import Char
from xhtml2pdf import pisa

class MainApp(QtGui.QMainWindow, char_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.char = Char()
        self.init_ui()
        self.init_menu()
    #main
    def main(self):
        self.show()

    def init_menu(self):
        exit_action = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(QtGui.qApp.quit)

        save_action = QtGui.QAction(QtGui.QIcon('save.png'), '&Save', self)
        save_action.setShortcut('Ctrl+s')
        save_action.setStatusTip('Save To Disk')
        save_action.triggered.connect(self.showSaveDialog)

        load_action = QtGui.QAction(QtGui.QIcon('load.png'), '&Load', self)
        load_action.setShortcut('Ctrl+o')
        load_action.setStatusTip('Load From Disk')
        load_action.triggered.connect(self.showOpenDialog)

        export_html_action = QtGui.QAction(QtGui.QIcon('export.png'), 'E&xport HTML', self)
        export_html_action.setShortcut('Ctrl+t')
        export_html_action.setStatusTip('Export to HTML')
        export_html_action.triggered.connect(self.export_to_html)

        export_pdf_action = QtGui.QAction(QtGui.QIcon('export.png'), 'E&xport PDF', self)
        export_pdf_action.setShortcut('Ctrl+p')
        export_pdf_action.setStatusTip('Export to PDF')
        export_pdf_action.triggered.connect(self.export_to_pdf)
        #test_action = QtGui.QAction(QtGui.QIcon('test.png'), '&Test', self)
        #test_action.setShortcut('Ctrl+T')
        #test_action.setStatusTip('TestAction')
        #test_action.triggered.connect(self.showTestDialog)
        menubar = self.menuBar()

        file_menu = menubar.addMenu('&File')
        file_menu.addAction(load_action)
        file_menu.addAction(save_action)
        #file_menu.addAction(test_action)
        file_menu.addAction(export_html_action)
        file_menu.addAction(export_pdf_action)
        file_menu.addAction(exit_action)

    def export_to_html(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Export to HTML', "*.html")
        if filename:
            html = open('meta_char_sheet.html', 'r')
            html_str = html.read()
            html.close()
            #html = '<h1>${name}Hi there</h1><p>${pants}hi2<br/></p>hi3'
            from string import Template
            s = Template(html_str)
            d = self.create_dict()
            s = s.safe_substitute(d)
            output = open(filename, 'w')
            output.write(str(s))
            output.close()
            print file(filename).read()

    def export_to_pdf(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Export to PDF', "*.pdf")
        if filename:
            html = open('meta_char_sheet.html', 'r')
            html_str = html.read()
            html.close()
            from string import Template
            s = Template(html_str)
            d = self.create_dict()
            s = s.safe_substitute(d)
            convert_html_to_pdf(s, filename)

    def create_dict(self):
        #shortcuts
        b = self.meta_char.brain
        l = self.meta_char.left_hand
        r = self.meta_char.right_hand
        bd = self.meta_char.body
        my_dict = dict(
                name=self.meta_char.name,
                history=self.meta_char.history,
                b_name=b.name,
                b_int=b.intelligence,
                b_ref=b.reflex,
                b_tech=b.technology,
                b_dex=b.dexterity,
                b_cool=b.cool,
                b_will=b.will,
                b_str=b.strength,
                b_con=b.constitution,
                b_move=b.move,
                b_body=b.body,
                b_luck=b.luck,
                b_hum=b.humanity,
                b_rec=b.recovery,
                b_end=b.endurance,
                b_run=b.run,
                b_spr=b.sprint,
                b_swim=b.swim,
                b_leap=b.leap,
                b_hits=b.hits,
                b_stun=b.stun,
                b_ks1=b.key_skill_1,
                b_ks1_lvl=b.key_skill_1_lvl,
                b_ks2=b.key_skill_2,
                b_ks2_lvl=b.key_skill_2_lvl,
                b_kp1=b.key_perk_1,
                b_kp1_lvl=b.key_perk_1_lvl,
                b_kp2=b.key_perk_2,
                b_kp2_lvl=b.key_perk_2_lvl,
                b_lp=b.lifepath,
                b_goals=b.goals,

                l_name=l.name,
                l_int=l.intelligence,
                l_ref=l.reflex,
                l_tech=l.technology,
                l_dex=l.dexterity,
                l_cool=l.cool,
                l_will=l.will,
                l_str=l.strength,
                l_con=l.constitution,
                l_move=l.move,
                l_body=l.body,
                l_luck=l.luck,
                l_hum=l.humanity,
                l_rec=l.recovery,
                l_end=l.endurance,
                l_run=l.run,
                l_spr=l.sprint,
                l_swim=l.swim,
                l_leap=l.leap,
                l_hits=l.hits,
                l_stun=l.stun,
                l_ks1=l.key_skill_1,
                l_ks1_lvl=l.key_skill_1_lvl,
                l_ks2=l.key_skill_2,
                l_ks2_lvl=l.key_skill_2_lvl,
                l_kp1=l.key_perk_1,
                l_kp1_lvl=l.key_perk_1_lvl,
                l_kp2=l.key_perk_2,
                l_kp2_lvl=l.key_perk_2_lvl,
                l_lp=l.lifepath,
                l_goals=l.goals,

                r_name=r.name,
                r_int=r.intelligence,
                r_ref=r.reflex,
                r_tech=r.technology,
                r_dex=r.dexterity,
                r_cool=r.cool,
                r_will=r.will,
                r_str=r.strength,
                r_con=r.constitution,
                r_move=r.move,
                r_body=r.body,
                r_luck=r.luck,
                r_hum=r.humanity,
                r_rec=r.recovery,
                r_end=r.endurance,
                r_run=r.run,
                r_spr=r.sprint,
                r_swim=r.swim,
                r_leap=r.leap,
                r_hits=r.hits,
                r_stun=r.stun,
                r_ks1=r.key_skill_1,
                r_ks1_lvl=r.key_skill_1_lvl,
                r_ks2=r.key_skill_2,
                r_ks2_lvl=r.key_skill_2_lvl,
                r_kp1=r.key_perk_1,
                r_kp1_lvl=r.key_perk_1_lvl,
                r_kp2=r.key_perk_2,
                r_kp2_lvl=r.key_perk_2_lvl,
                r_lp=r.lifepath,
                r_goals=r.goals,

                bd_leaders=bd.leaders,
                bd_soldiers=bd.soldiers,
                bd_grunts=bd.grunts,
                bd_assets=bd.assets,
                bd_vehicles=bd.vehicles

                )
        return my_dict

    def showTestDialog(self):
        print "From Test Action:", self.meta_char.name, self.meta_char.history, "brain: ", self.meta_char.brain.intelligence

    def showOpenDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '/home')
        print "opening", filename, "\n"
        if filename:
            meta_char = self.meta_char.load_from_disk(filename)
            self.meta_char = meta_char
            self.update_all_mc_fields()
            self.update_body_fields()
            self.update_all_brain_derived_fields()
            self.update_all_right_hand_derived_fields()
            self.update_all_left_hand_derived_fields()

    def showSaveDialog(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', "*")
        print "saving", filename, "\n"
        if filename:
            self.meta_char.save_to_disk(filename)
    def onNameTextChanged(self, text):
        print text
        self.char.name = str(text)
    def onReputationTextChanged(self, text):
        print text
        self.char.reputation= int(text)
    def onIPTextChanged(self, text):
        print text
        self.char.ip = int(text)
    def onLifepathTextChanged(self, text):
        print text
        self.char.lifepath = str(text)
    def onTraitsTextChanged(self, text):
        print text
        self.char.traits = str(text)
    def onFeelAboutPeopleTextChanged(self, text):
        print text
        self.char.feel_about_people= str(text)
    def onYouValueMostTextChanged(self, text):
        print text
        self.char.you_value_most= str(text)
    def onValuedPersonTextChanged(self, text):
        print text
        self.char.valued_person = str(text)
    def onValuedPossesionTextChanged(self, text):
        print text
        self.char.valued_possesion= str(text)
    def onClothesTextChanged(self, text):
        print text
        self.char.clothes = str(text)
    def onHairTextChanged(self, text):
        print text
        self.char.hair= str(text)
    def onAffectationsTextChanged(self, text):
        print text
        self.char.affectations = str(text)
    def onOriginsTextChanged(self, text):
        print text
        self.char.origins = str(text)
    def onLanguagesTextChanged(self, text):
        print text
        self.char.languages= str(text)
    def onBackgroundTextChanged(self):
        text = self.plainTextEditBackground.toPlainText()
        print text
        self.char.background = str(text)
    def onOutfitTextChanged(self):
        text = self.plainTextEditOutfit.toPlainText()
        print text
        self.char.outfit= str(text)
    def onWeaponsTextChanged(self):
        text = self.plainTextEditWeapons.toPlainText()
        print text
        self.char.weapons = str(text)

    # hooks up all the textfields / areas
    def init_ui(self):
        self.lineEditName.textChanged.connect(self.onNameTextChanged)
        self.lineEditReputation.textChanged.connect(self.onReputationTextChanged)
        self.lineEditIP.textChanged.connect(self.onIPTextChanged)
        self.lineEditLifepath.textChanged.connect(self.onLifepathTextChanged)
        self.lineEditTraits.textChanged.connect(self.onTraitsTextChanged)
        self.lineEditFeelAboutPeople.textChanged.connect(self.onFeelAboutPeopleTextChanged)
        self.lineEditYouValueMost.textChanged.connect(self.onYouValueMostTextChanged)
        self.lineEditValuedPerson.textChanged.connect(self.onValuedPersonTextChanged)
        self.lineEditValuedPossesion.textChanged.connect(self.onValuedPossesionTextChanged)
        self.lineEditClothes.textChanged.connect(self.onClothesTextChanged)
        self.lineEditHair.textChanged.connect(self.onHairTextChanged)
        self.lineEditAffectations.textChanged.connect(self.onAffectationsTextChanged)
        self.lineEditOrigins.textChanged.connect(self.onOriginsTextChanged)
        self.lineEditLanguages.textChanged.connect(self.onLanguagesTextChanged)
        self.plainTextEditBackground.textChanged.connect(self.onBackgroundTextChanged)
        #outfit
        self.plainTextEditOutfit.textChanged.connect(self.onOutfitTextChanged)
        #weapons
        self.plainTextEditWeapons.textChanged.connect(self.onWeaponsTextChanged)
        # stats
        self.lineEditInt.textChanged.connect(self.onIntTextChanged)
        self.lineEditRef.textChanged.connect(self.onRefTextChanged)
        self.lineEditTech.textChanged.connect(self.onTechTextChanged)
        self.lineEditDex.textChanged.connect(self.onDexTextChanged)
        self.lineEditCool.textChanged.connect(self.onCoolTextChanged)
        self.lineEditWill.textChanged.connect(self.onWillTextChanged)
        self.lineEditStr.textChanged.connect(self.onStrTextChanged)
        self.lineEditCon.textChanged.connect(self.onConTextChanged)
        self.lineEditMove.textChanged.connect(self.onMoveTextChanged)
        self.lineEditBody.textChanged.connect(self.onBodyTextChanged)

        # skills
        self.cb_skill_1.activated[str].connect(self.onSkill1Activated)
        self.cb_skill_2.activated[str].connect(self.onSkill2Activated)
        self.cb_skill_3.activated[str].connect(self.onSkill3Activated)
        self.cb_skill_4.activated[str].connect(self.onSkill4Activated)
        self.cb_skill_5.activated[str].connect(self.onSkill5Activated)
        self.cb_skill_6.activated[str].connect(self.onSkill6Activated)
        self.cb_skill_7.activated[str].connect(self.onSkill7Activated)
        self.cb_skill_8.activated[str].connect(self.onSkill8Activated)
        self.cb_skill_9.activated[str].connect(self.onSkill8Activated)
        self.cb_skill_10.activated[str].connect(self.onSkill10Activated)
        self.cb_skill_11.activated[str].connect(self.onSkill11Activated)
        self.cb_skill_12.activated[str].connect(self.onSkill12Activated)
        self.cb_skill_13.activated[str].connect(self.onSkill13Activated)
        self.cb_skill_14.activated[str].connect(self.onSkill14Activated)
        self.cb_skill_15.activated[str].connect(self.onSkill15Activated)
        self.cb_skill_16.activated[str].connect(self.onSkill16Activated)
        self.skill_1_lvl.textChanged.connect(self.onSkill1LVLTextChanged)
        self.skill_2_lvl.textChanged.connect(self.onSkill2LVLTextChanged)
        self.skill_3_lvl.textChanged.connect(self.onSkill3LVLTextChanged)
        self.skill_4_lvl.textChanged.connect(self.onSkill4LVLTextChanged)
        self.skill_5_lvl.textChanged.connect(self.onSkill5LVLTextChanged)
        self.skill_6_lvl.textChanged.connect(self.onSkill6LVLTextChanged)
        self.skill_7_lvl.textChanged.connect(self.onSkill7LVLTextChanged)
        self.skill_8_lvl.textChanged.connect(self.onSkill8LVLTextChanged)
        self.skill_9_lvl.textChanged.connect(self.onSkill9LVLTextChanged)
        self.skill_10_lvl.textChanged.connect(self.onSkill10LVLTextChanged)
        self.skill_11_lvl.textChanged.connect(self.onSkill11LVLTextChanged)
        self.skill_12_lvl.textChanged.connect(self.onSkill12LVLTextChanged)
        self.skill_13_lvl.textChanged.connect(self.onSkill13LVLTextChanged)
        self.skill_14_lvl.textChanged.connect(self.onSkill14LVLTextChanged)
        self.skill_15_lvl.textChanged.connect(self.onSkill15LVLTextChanged)
        self.skill_16_lvl.textChanged.connect(self.onSkill16LVLTextChanged)
        #perks
        self.cb_perk_1.activated[str].connect(self.onPerk1Activated)
        self.cb_perk_2.activated[str].connect(self.onPerk2Activated)
        self.cb_perk_3.activated[str].connect(self.onPerk3Activated)
        self.cb_perk_4.activated[str].connect(self.onPerk4Activated)
        self.cb_perk_5.activated[str].connect(self.onPerk5Activated)
        self.cb_perk_6.activated[str].connect(self.onPerk6Activated)
        self.cb_perk_7.activated[str].connect(self.onPerk7Activated)
        self.cb_perk_8.activated[str].connect(self.onPerk8Activated)
        self.cb_perk_9.activated[str].connect(self.onPerk8Activated)
        self.cb_perk_10.activated[str].connect(self.onPerk10Activated)
        self.cb_perk_11.activated[str].connect(self.onPerk11Activated)
        self.cb_perk_12.activated[str].connect(self.onPerk12Activated)
        self.cb_perk_13.activated[str].connect(self.onPerk13Activated)
        self.cb_perk_14.activated[str].connect(self.onPerk14Activated)
        self.cb_perk_15.activated[str].connect(self.onPerk15Activated)
        self.cb_perk_16.activated[str].connect(self.onPerk16Activated)
        self.perk_1_lvl.textChanged.connect(self.onPerk1LVLTextChanged)
        self.perk_2_lvl.textChanged.connect(self.onPerk2LVLTextChanged)
        self.perk_3_lvl.textChanged.connect(self.onPerk3LVLTextChanged)
        self.perk_4_lvl.textChanged.connect(self.onPerk4LVLTextChanged)
        self.perk_5_lvl.textChanged.connect(self.onPerk5LVLTextChanged)
        self.perk_6_lvl.textChanged.connect(self.onPerk6LVLTextChanged)
        self.perk_7_lvl.textChanged.connect(self.onPerk7LVLTextChanged)
        self.perk_8_lvl.textChanged.connect(self.onPerk8LVLTextChanged)
        self.perk_9_lvl.textChanged.connect(self.onPerk9LVLTextChanged)
        self.perk_10_lvl.textChanged.connect(self.onPerk10LVLTextChanged)
        self.perk_11_lvl.textChanged.connect(self.onPerk11LVLTextChanged)
        self.perk_12_lvl.textChanged.connect(self.onPerk12LVLTextChanged)
        self.perk_13_lvl.textChanged.connect(self.onPerk13LVLTextChanged)
        self.perk_14_lvl.textChanged.connect(self.onPerk14LVLTextChanged)
        self.perk_15_lvl.textChanged.connect(self.onPerk15LVLTextChanged)
        self.perk_16_lvl.textChanged.connect(self.onPerk16LVLTextChanged)
    #skills
    def onSkill1Activated(self, text):
        self.char.skill_1 = str(text)
    def onSkill2Activated(self, text):
        self.char.skill_2 = str(text)
    def onSkill3Activated(self, text):
        self.char.skill_3 = str(text)
    def onSkill4Activated(self, text):
        self.char.skill_4 = str(text)
    def onSkill5Activated(self, text):
        self.char.skill_5 = str(text)
    def onSkill6Activated(self, text):
        self.char.skill_6 = str(text)
    def onSkill7Activated(self, text):
        self.char.skill_7 = str(text)
    def onSkill8Activated(self, text):
        self.char.skill_8 = str(text)
    def onSkill9Activated(self, text):
        self.char.skill_9 = str(text)
    def onSkill10Activated(self, text):
        self.char.skill_10 = str(text)
    def onSkill11Activated(self, text):
        self.char.skill_11 = str(text)
    def onSkill12Activated(self, text):
        self.char.skill_12 = str(text)
    def onSkill13Activated(self, text):
        self.char.skill_13 = str(text)
    def onSkill14Activated(self, text):
        self.char.skill_14 = str(text)
    def onSkill15Activated(self, text):
        self.char.skill_15 = str(text)
    def onSkill16Activated(self, text):
        self.char.skill_16 = str(text)
    def onSkill1LVLTextChanged(self, text):
        self.skill_1_lvl = int(text)
    def onSkill2LVLTextChanged(self, text):
        self.skill_2_lvl = int(text)
    def onSkill3LVLTextChanged(self, text):
        self.skill_3_lvl = int(text)
    def onSkill4LVLTextChanged(self, text):
        self.skill_4_lvl = int(text)
    def onSkill5LVLTextChanged(self, text):
        self.skill_5_lvl = int(text)
    def onSkill6LVLTextChanged(self, text):
        self.skill_6_lvl = int(text)
    def onSkill7LVLTextChanged(self, text):
        self.skill_7_lvl = int(text)
    def onSkill8LVLTextChanged(self, text):
        self.skill_8_lvl = int(text)
    def onSkill9LVLTextChanged(self, text):
        self.skill_9_lvl = int(text)
    def onSkill10LVLTextChanged(self, text):
        self.skill_10_lvl = int(text)
    def onSkill11LVLTextChanged(self, text):
        self.skill_11_lvl = int(text)
    def onSkill12LVLTextChanged(self, text):
        self.skill_12_lvl = int(text)
    def onSkill13LVLTextChanged(self, text):
        self.skill_13_lvl = int(text)
    def onSkill14LVLTextChanged(self, text):
        self.skill_14_lvl = int(text)
    def onSkill15LVLTextChanged(self, text):
        self.skill_15_lvl = int(text)
    def onSkill16LVLTextChanged(self, text):
        self.skill_16_lvl = int(text)
    #perks
    def onPerk1Activated(self, text):
        self.char.perk_1 = str(text)
    def onPerk2Activated(self, text):
        self.char.perk_2 = str(text)
    def onPerk3Activated(self, text):
        self.char.perk_3 = str(text)
    def onPerk4Activated(self, text):
        self.char.perk_4 = str(text)
    def onPerk5Activated(self, text):
        self.char.perk_5 = str(text)
    def onPerk6Activated(self, text):
        self.char.perk_6 = str(text)
    def onPerk7Activated(self, text):
        self.char.perk_7 = str(text)
    def onPerk8Activated(self, text):
        self.char.perk_8 = str(text)
    def onPerk9Activated(self, text):
        self.char.perk_9 = str(text)
    def onPerk10Activated(self, text):
        self.char.perk_10 = str(text)
    def onPerk11Activated(self, text):
        self.char.perk_11 = str(text)
    def onPerk12Activated(self, text):
        self.char.perk_12 = str(text)
    def onPerk13Activated(self, text):
        self.char.perk_13 = str(text)
    def onPerk14Activated(self, text):
        self.char.perk_14 = str(text)
    def onPerk15Activated(self, text):
        self.char.perk_15 = str(text)
    def onPerk16Activated(self, text):
        self.char.perk_16 = str(text)
    def onPerk1LVLTextChanged(self, text):
        self.perk_1_lvl = int(text)
    def onPerk2LVLTextChanged(self, text):
        self.perk_2_lvl = int(text)
    def onPerk3LVLTextChanged(self, text):
        self.perk_3_lvl = int(text)
    def onPerk4LVLTextChanged(self, text):
        self.perk_4_lvl = int(text)
    def onPerk5LVLTextChanged(self, text):
        self.perk_5_lvl = int(text)
    def onPerk6LVLTextChanged(self, text):
        self.perk_6_lvl = int(text)
    def onPerk7LVLTextChanged(self, text):
        self.perk_7_lvl = int(text)
    def onPerk8LVLTextChanged(self, text):
        self.perk_8_lvl = int(text)
    def onPerk9LVLTextChanged(self, text):
        self.perk_9_lvl = int(text)
    def onPerk10LVLTextChanged(self, text):
        self.perk_10_lvl = int(text)
    def onPerk11LVLTextChanged(self, text):
        self.perk_11_lvl = int(text)
    def onPerk12LVLTextChanged(self, text):
        self.perk_12_lvl = int(text)
    def onPerk13LVLTextChanged(self, text):
        self.perk_13_lvl = int(text)
    def onPerk14LVLTextChanged(self, text):
        self.perk_14_lvl = int(text)
    def onPerk15LVLTextChanged(self, text):
        self.perk_15_lvl = int(text)
    def onPerk16LVLTextChanged(self, text):
        self.perk_16_lvl = int(text)

    def onIntTextChanged(self, text):
        print 'onIntTextChanged', text
        self.char.intelligence = int(text)
        self.update_all_derived_fields()

    def onRefTextChanged(self, text):
        print 'onRefTextChanged', text
        self.char.reflex = int(text)
        self.update_all_derived_fields()

    def onTechTextChanged(self, text):
        print 'onTechTextChanged', text
        self.char.technology = int(text)
        self.update_all_derived_fields()

    def onDexTextChanged(self, text):
        print 'onDexTextChanged', text
        self.char.dexterity = int(text)
        self.update_all_derived_fields()

    def onCoolTextChanged(self, text):
        print 'onCoolTextChanged', text
        self.char.cool = int(text)
        self.update_all_derived_fields()

    def onWillTextChanged(self, text):
        print 'onWillTextChanged', text
        self.char.will= int(text)
        self.update_all_derived_fields()

    def onStrTextChanged(self, text):
        print 'onStrTextChanged', text
        self.char.strength = int(text)
        self.update_all_derived_fields()

    def onConTextChanged(self, text):
        print 'onConTextChanged', text
        self.char.constitution = int(text)
        self.update_all_derived_fields()

    def onMoveTextChanged(self, text):
        print 'onMoveTextChanged', text
        self.char.move = int(text)
        self.update_all_derived_fields()

    def onBodyTextChanged(self, text):
        print 'onBodyTextChanged', text
        self.char.body = int(text)
        self.update_all_derived_fields()

    def update_all_derived_fields(self):
        # key skills
        self.lineEditName.setText(str(self.char.name))
        self.lineEditInt.setText(str(self.char.intelligence))
        self.lineEditRef.setText(str(self.char.reflex))
        self.lineEditTech.setText(str(self.char.technology))
        self.lineEditDex.setText(str(self.char.dexterity))
        self.lineEditCool.setText(str(self.char.cool))
        self.lineEditWill.setText(str(self.char.will))
        self.lineEditStr.setText(str(self.char.strength))
        self.lineEditCon.setText(str(self.char.constitution))
        self.lineEditMove.setText(str(self.char.move))
        self.lineEditBody.setText(str(self.char.body))

        self.char.luck = self.char.intelligence + self.char.reflex / 2
        self.lineROLuck.setText(str(self.char.luck))
        print str(self.char.luck)
        #humanity
        self.char.humanity = self.char.will * 10
        self.lineROHum.setText(str(self.char.humanity))
        print str(self.char.humanity)
        #recovery
        self.char.recovery = self.char.strength + self.char.constitution / 2
        self.lineRORec.setText(str(self.char.recovery))
        print str(self.char.recovery)
        #endurance
        self.char.endurance = self.char.constitution * 2
        self.lineROEnd.setText(str(self.char.endurance))
        print str(self.char.endurance)
        #run
        self.char.run = self.char.move * 2
        self.lineRORun.setText(str(self.char.run))
        print str(self.char.run)
        #sprint
        self.char.sprint = self.char.move * 3
        self.lineROSpr.setText(str(self.char.sprint))
        print str(self.char.sprint)
        #swim
        self.char.swim = self.char.move
        self.lineROSwim.setText(str(self.char.swim))
        print str(self.char.swim)
        #leap
        self.char.leap = self.char.move
        self.lineROLeap.setText(str(self.char.leap))
        print str(self.char.leap)
        #hits
        self.char.hits = self.char.body * 2
        self.lineROHits.setText(str(self.char.hits))
        print str(self.char.hits)
        #stun
        self.char.stun = self.char.body * 5
        self.lineROStun.setText(str(self.char.stun))
        print str(self.char.stun)

def convert_html_to_pdf(source, output):
    output_file = open(output, "w+b")
    pisa_status = pisa.CreatePDF(source, output_file)
    output_file.close()
    return pisa_status

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    MA = MainApp()
    MA.main()
    app.exec_()
