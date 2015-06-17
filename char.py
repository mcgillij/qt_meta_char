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
        test_action = QtGui.QAction(QtGui.QIcon('test.png'), '&Test', self)
        test_action.setShortcut('Ctrl+T')
        test_action.setStatusTip('TestAction')
        test_action.triggered.connect(self.showTestDialog)
        menubar = self.menuBar()

        file_menu = menubar.addMenu('&File')
        file_menu.addAction(load_action)
        file_menu.addAction(save_action)
        file_menu.addAction(test_action)
        file_menu.addAction(export_html_action)
        file_menu.addAction(export_pdf_action)
        file_menu.addAction(exit_action)

    def export_to_html(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Export to HTML', "*.html")
        if filename:
            html = open('char_sheet.html', 'r')
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
            html = open('char_sheet.html', 'r')
            html_str = html.read()
            html.close()
            from string import Template
            s = Template(html_str)
            d = self.create_dict()
            s = s.safe_substitute(d)
            convert_html_to_pdf(s, filename)

    def create_dict(self):
        #shortcuts
        c = self.char
        my_dict = dict(
                name=c.name,
                age=c.age,
                sex=c.sex,
                image_path = c.image_path,
                reputation = c.reputation,
                ip = c.ip,
                lifepath = c.lifepath,
                traits = c.traits,
                feel_about_people = c.feel_about_people,
                you_value_most = c.you_value_most,
                valued_person = c.valued_person,
                valued_possesion = c.valued_possesion,
                clothes = c.clothes,
                hair = c.hair,
                affectations = c.affectations,
                origins = c.origins,
                languages = c.languages,
                background = c.background,
                int=c.intelligence,
                ref=c.reflex,
                tech=c.technology,
                dex=c.dexterity,
                cool=c.cool,
                will=c.will,
                str=c.strength,
                con=c.constitution,
                move=c.move,
                body=c.body,
                luck=c.luck,
                hum=c.humanity,
                rec=c.recovery,
                end=c.endurance,
                run=c.run,
                spr=c.sprint,
                swim=c.swim,
                leap=c.leap,
                hits=c.hits,
                stun=c.stun,
                skill_1 = c.skill_1,
                skill_1_lvl = c.skill_1_lvl,
                skill_2 = c.skill_2,
                skill_2_lvl = c.skill_2_lvl,
                skill_3 = c.skill_3,
                skill_3_lvl = c.skill_3_lvl,
                skill_4 = c.skill_4,
                skill_4_lvl = c.skill_4_lvl,
                skill_5 = c.skill_5,
                skill_5_lvl = c.skill_5_lvl,
                skill_6 = c.skill_6,
                skill_6_lvl = c.skill_6_lvl,
                skill_7 = c.skill_7,
                skill_7_lvl = c.skill_7_lvl,
                skill_8 = c.skill_8,
                skill_8_lvl = c.skill_8_lvl,
                skill_9 = c.skill_9,
                skill_9_lvl = c.skill_9_lvl,
                skill_10 = c.skill_10,
                skill_10_lvl = c.skill_10_lvl,
                skill_11 = c.skill_11,
                skill_11_lvl = c.skill_11_lvl,
                skill_12 = c.skill_12,
                skill_12_lvl = c.skill_12_lvl,
                skill_13 = c.skill_13,
                skill_13_lvl = c.skill_13_lvl,
                skill_14 = c.skill_14,
                skill_14_lvl = c.skill_14_lvl,
                skill_15 = c.skill_15,
                skill_15_lvl = c.skill_15_lvl,
                skill_16 = c.skill_16,
                skill_16_lvl = c.skill_16_lvl,
                perk_1 = c.perk_1,
                perk_1_lvl = c.perk_1_lvl,
                perk_2 = c.perk_2,
                perk_2_lvl = c.perk_2_lvl,
                perk_3 = c.perk_3,
                perk_3_lvl = c.perk_3_lvl,
                perk_4 = c.perk_4,
                perk_4_lvl = c.perk_4_lvl,
                perk_5 = c.perk_5,
                perk_5_lvl = c.perk_5_lvl,
                perk_6 = c.perk_6,
                perk_6_lvl = c.perk_6_lvl,
                perk_7 = c.perk_7,
                perk_7_lvl = c.perk_7_lvl,
                perk_8 = c.perk_8,
                perk_8_lvl = c.perk_8_lvl,
                perk_9 = c.perk_9,
                perk_9_lvl = c.perk_9_lvl,
                perk_10 = c.perk_10,
                perk_10_lvl = c.perk_10_lvl,
                perk_11 = c.perk_11,
                perk_11_lvl = c.perk_11_lvl,
                perk_12 = c.perk_12,
                perk_12_lvl = c.perk_12_lvl,
                perk_13 = c.perk_13,
                perk_13_lvl = c.perk_13_lvl,
                perk_14 = c.perk_14,
                perk_14_lvl = c.perk_14_lvl,
                perk_15 = c.perk_15,
                perk_15_lvl = c.perk_15_lvl,
                perk_16 = c.perk_16,
                perk_16_lvl = c.perk_16_lvl,
                outfit = c.outfit,
                weapons = c.weapons

)
        return my_dict
    #diag windows
    def showTestDialog(self):
        pprint(dir(self.char))
    def showOpenDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '/home')
        print "opening", filename, "\n"
        if filename:
            char = self.char.load_from_disk(filename)
            self.char = char
            self.update_all_derived_fields()
            scene = QtGui.QGraphicsScene()
            scene.addPixmap(QtGui.QPixmap(self.char.image_path))
            self.graphicsView.setScene(scene)
            self.graphicsView.show()

    def showSaveDialog(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', "*")
        print "saving", filename, "\n"
        if filename:
            self.char.save_to_disk(filename)
    def showChooseImageDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Choose Image', "*.png")
        print "trying to load up", filename, "as an image \n"
        if filename:
            self.char.image_path = filename
            self.lineROImagePath.setText(str(filename))
            scene = QtGui.QGraphicsScene()
            scene.addPixmap(QtGui.QPixmap(filename))
            self.graphicsView.setScene(scene)
            self.graphicsView.show()
    # onChange events
    def onNameTextChanged(self, text):
        print text
        self.char.name = str(text)
    def onAgeTextChanged(self, text):
        print text
        self.char.age = int(text)
    def onSexTextChanged(self, text):
        print text
        self.char.sex = str(text)
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
        self.pushButtonChooseImage.clicked.connect(self.showChooseImageDialog)
        self.lineEditName.textChanged.connect(self.onNameTextChanged)
        self.lineEditAge.textChanged.connect(self.onAgeTextChanged)
        self.lineEditSex.textChanged.connect(self.onSexTextChanged)
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
        self.cb_skill_9.activated[str].connect(self.onSkill9Activated)
        self.cb_skill_10.activated[str].connect(self.onSkill10Activated)
        self.cb_skill_11.activated[str].connect(self.onSkill11Activated)
        self.cb_skill_12.activated[str].connect(self.onSkill12Activated)
        self.cb_skill_13.activated[str].connect(self.onSkill13Activated)
        self.cb_skill_14.activated[str].connect(self.onSkill14Activated)
        self.cb_skill_15.activated[str].connect(self.onSkill15Activated)
        self.cb_skill_16.activated[str].connect(self.onSkill16Activated)
        self.le_skill_1_lvl.textChanged.connect(self.onSkill1LVLTextChanged)
        self.le_skill_2_lvl.textChanged.connect(self.onSkill2LVLTextChanged)
        self.le_skill_3_lvl.textChanged.connect(self.onSkill3LVLTextChanged)
        self.le_skill_4_lvl.textChanged.connect(self.onSkill4LVLTextChanged)
        self.le_skill_5_lvl.textChanged.connect(self.onSkill5LVLTextChanged)
        self.le_skill_6_lvl.textChanged.connect(self.onSkill6LVLTextChanged)
        self.le_skill_7_lvl.textChanged.connect(self.onSkill7LVLTextChanged)
        self.le_skill_8_lvl.textChanged.connect(self.onSkill8LVLTextChanged)
        self.le_skill_9_lvl.textChanged.connect(self.onSkill9LVLTextChanged)
        self.le_skill_10_lvl.textChanged.connect(self.onSkill10LVLTextChanged)
        self.le_skill_11_lvl.textChanged.connect(self.onSkill11LVLTextChanged)
        self.le_skill_12_lvl.textChanged.connect(self.onSkill12LVLTextChanged)
        self.le_skill_13_lvl.textChanged.connect(self.onSkill13LVLTextChanged)
        self.le_skill_14_lvl.textChanged.connect(self.onSkill14LVLTextChanged)
        self.le_skill_15_lvl.textChanged.connect(self.onSkill15LVLTextChanged)
        self.le_skill_16_lvl.textChanged.connect(self.onSkill16LVLTextChanged)
        #perks
        self.cb_perk_1.activated[str].connect(self.onPerk1Activated)
        self.cb_perk_2.activated[str].connect(self.onPerk2Activated)
        self.cb_perk_3.activated[str].connect(self.onPerk3Activated)
        self.cb_perk_4.activated[str].connect(self.onPerk4Activated)
        self.cb_perk_5.activated[str].connect(self.onPerk5Activated)
        self.cb_perk_6.activated[str].connect(self.onPerk6Activated)
        self.cb_perk_7.activated[str].connect(self.onPerk7Activated)
        self.cb_perk_8.activated[str].connect(self.onPerk8Activated)
        self.cb_perk_9.activated[str].connect(self.onPerk9Activated)
        self.cb_perk_10.activated[str].connect(self.onPerk10Activated)
        self.cb_perk_11.activated[str].connect(self.onPerk11Activated)
        self.cb_perk_12.activated[str].connect(self.onPerk12Activated)
        self.cb_perk_13.activated[str].connect(self.onPerk13Activated)
        self.cb_perk_14.activated[str].connect(self.onPerk14Activated)
        self.cb_perk_15.activated[str].connect(self.onPerk15Activated)
        self.cb_perk_16.activated[str].connect(self.onPerk16Activated)
        self.le_perk_1_lvl.textChanged.connect(self.onPerk1LVLTextChanged)
        self.le_perk_2_lvl.textChanged.connect(self.onPerk2LVLTextChanged)
        self.le_perk_3_lvl.textChanged.connect(self.onPerk3LVLTextChanged)
        self.le_perk_4_lvl.textChanged.connect(self.onPerk4LVLTextChanged)
        self.le_perk_5_lvl.textChanged.connect(self.onPerk5LVLTextChanged)
        self.le_perk_6_lvl.textChanged.connect(self.onPerk6LVLTextChanged)
        self.le_perk_7_lvl.textChanged.connect(self.onPerk7LVLTextChanged)
        self.le_perk_8_lvl.textChanged.connect(self.onPerk8LVLTextChanged)
        self.le_perk_9_lvl.textChanged.connect(self.onPerk9LVLTextChanged)
        self.le_perk_10_lvl.textChanged.connect(self.onPerk10LVLTextChanged)
        self.le_perk_11_lvl.textChanged.connect(self.onPerk11LVLTextChanged)
        self.le_perk_12_lvl.textChanged.connect(self.onPerk12LVLTextChanged)
        self.le_perk_13_lvl.textChanged.connect(self.onPerk13LVLTextChanged)
        self.le_perk_14_lvl.textChanged.connect(self.onPerk14LVLTextChanged)
        self.le_perk_15_lvl.textChanged.connect(self.onPerk15LVLTextChanged)
        self.le_perk_16_lvl.textChanged.connect(self.onPerk16LVLTextChanged)
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
        self.char.skill_1_lvl = int(text)
    def onSkill2LVLTextChanged(self, text):
        self.char.skill_2_lvl = int(text)
    def onSkill3LVLTextChanged(self, text):
        self.char.skill_3_lvl = int(text)
    def onSkill4LVLTextChanged(self, text):
        self.char.skill_4_lvl = int(text)
    def onSkill5LVLTextChanged(self, text):
        self.char.skill_5_lvl = int(text)
    def onSkill6LVLTextChanged(self, text):
        self.char.skill_6_lvl = int(text)
    def onSkill7LVLTextChanged(self, text):
        self.char.skill_7_lvl = int(text)
    def onSkill8LVLTextChanged(self, text):
        self.char.skill_8_lvl = int(text)
    def onSkill9LVLTextChanged(self, text):
        self.char.skill_9_lvl = int(text)
    def onSkill10LVLTextChanged(self, text):
        self.char.skill_10_lvl = int(text)
    def onSkill11LVLTextChanged(self, text):
        self.char.skill_11_lvl = int(text)
    def onSkill12LVLTextChanged(self, text):
        self.char.skill_12_lvl = int(text)
    def onSkill13LVLTextChanged(self, text):
        self.char.skill_13_lvl = int(text)
    def onSkill14LVLTextChanged(self, text):
        self.char.skill_14_lvl = int(text)
    def onSkill15LVLTextChanged(self, text):
        self.char.skill_15_lvl = int(text)
    def onSkill16LVLTextChanged(self, text):
        self.char.skill_16_lvl = int(text)
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
        self.char.perk_1_lvl = int(text)
    def onPerk2LVLTextChanged(self, text):
        self.char.perk_2_lvl = int(text)
    def onPerk3LVLTextChanged(self, text):
        self.char.perk_3_lvl = int(text)
    def onPerk4LVLTextChanged(self, text):
        self.char.perk_4_lvl = int(text)
    def onPerk5LVLTextChanged(self, text):
        self.char.perk_5_lvl = int(text)
    def onPerk6LVLTextChanged(self, text):
        self.char.perk_6_lvl = int(text)
    def onPerk7LVLTextChanged(self, text):
        self.char.perk_7_lvl = int(text)
    def onPerk8LVLTextChanged(self, text):
        self.char.perk_8_lvl = int(text)
    def onPerk9LVLTextChanged(self, text):
        self.char.perk_9_lvl = int(text)
    def onPerk10LVLTextChanged(self, text):
        self.char.perk_10_lvl = int(text)
    def onPerk11LVLTextChanged(self, text):
        self.char.perk_11_lvl = int(text)
    def onPerk12LVLTextChanged(self, text):
        self.char.perk_12_lvl = int(text)
    def onPerk13LVLTextChanged(self, text):
        self.char.perk_13_lvl = int(text)
    def onPerk14LVLTextChanged(self, text):
        self.char.perk_14_lvl = int(text)
    def onPerk15LVLTextChanged(self, text):
        self.char.perk_15_lvl = int(text)
    def onPerk16LVLTextChanged(self, text):
        self.char.perk_16_lvl = int(text)

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
        self.lineEditName.setText(str(self.char.name))
        self.lineEditAge.setText(str(self.char.age))
        self.lineEditSex.setText(str(self.char.sex))
        self.lineEditReputation.setText(str(self.char.reputation))
        self.lineEditIP.setText(str(self.char.ip))
        self.lineROImagePath.setText(str(self.char.image_path))
        self.lineEditLifepath.setText(str(self.char.lifepath))
        self.lineEditTraits.setText(str(self.char.traits))
        self.lineEditFeelAboutPeople.setText(str(self.char.feel_about_people))
        self.lineEditYouValueMost.setText(str(self.char.you_value_most))
        self.lineEditValuedPerson.setText(str(self.char.valued_person))
        self.lineEditValuedPossesion.setText(str(self.char.valued_possesion))
        self.lineEditClothes.setText(str(self.char.clothes))
        self.lineEditHair.setText(str(self.char.hair))
        self.lineEditAffectations.setText(str(self.char.affectations))
        self.lineEditOrigins.setText(str(self.char.origins))
        self.lineEditLanguages.setText(str(self.char.languages))
        self.plainTextEditBackground.setPlainText(str(self.char.background))
        #outfit
        self.plainTextEditOutfit.setPlainText(str(self.char.outfit))
        #weapons
        self.plainTextEditWeapons.setPlainText(str(self.char.weapons))
        #stats
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
        self.char.humanity = self.char.will * 10
        self.lineROHum.setText(str(self.char.humanity))
        self.char.recovery = self.char.strength + self.char.constitution / 2
        self.lineRORec.setText(str(self.char.recovery))
        self.char.endurance = self.char.constitution * 2
        self.lineROEnd.setText(str(self.char.endurance))
        self.char.run = self.char.move * 2
        self.lineRORun.setText(str(self.char.run))
        self.char.sprint = self.char.move * 3
        self.lineROSpr.setText(str(self.char.sprint))
        self.char.swim = self.char.move
        self.lineROSwim.setText(str(self.char.swim))
        self.char.leap = self.char.move
        self.lineROLeap.setText(str(self.char.leap))
        self.char.hits = self.char.body * 2
        self.lineROHits.setText(str(self.char.hits))
        self.char.stun = self.char.body * 5
        self.lineROStun.setText(str(self.char.stun))
        # skills
        self.cb_skill_1.setCurrentIndex(self.cb_skill_1.findText(self.char.skill_1))
        self.cb_skill_2.setCurrentIndex(self.cb_skill_2.findText(self.char.skill_2))
        self.cb_skill_3.setCurrentIndex(self.cb_skill_3.findText(self.char.skill_3))
        self.cb_skill_4.setCurrentIndex(self.cb_skill_4.findText(self.char.skill_4))
        self.cb_skill_5.setCurrentIndex(self.cb_skill_5.findText(self.char.skill_5))
        self.cb_skill_6.setCurrentIndex(self.cb_skill_6.findText(self.char.skill_6))
        self.cb_skill_7.setCurrentIndex(self.cb_skill_7.findText(self.char.skill_7))
        self.cb_skill_8.setCurrentIndex(self.cb_skill_8.findText(self.char.skill_8))
        self.cb_skill_9.setCurrentIndex(self.cb_skill_9.findText(self.char.skill_9))
        self.cb_skill_10.setCurrentIndex(self.cb_skill_10.findText(self.char.skill_10))
        self.cb_skill_11.setCurrentIndex(self.cb_skill_11.findText(self.char.skill_11))
        self.cb_skill_12.setCurrentIndex(self.cb_skill_12.findText(self.char.skill_12))
        self.cb_skill_13.setCurrentIndex(self.cb_skill_13.findText(self.char.skill_13))
        self.cb_skill_14.setCurrentIndex(self.cb_skill_14.findText(self.char.skill_14))
        self.cb_skill_15.setCurrentIndex(self.cb_skill_15.findText(self.char.skill_15))
        self.cb_skill_16.setCurrentIndex(self.cb_skill_16.findText(self.char.skill_16))
        self.le_skill_1_lvl.setText(str(self.char.skill_1_lvl))
        self.le_skill_2_lvl.setText(str(self.char.skill_2_lvl))
        self.le_skill_3_lvl.setText(str(self.char.skill_3_lvl))
        self.le_skill_4_lvl.setText(str(self.char.skill_4_lvl))
        self.le_skill_5_lvl.setText(str(self.char.skill_5_lvl))
        self.le_skill_6_lvl.setText(str(self.char.skill_6_lvl))
        self.le_skill_7_lvl.setText(str(self.char.skill_7_lvl))
        self.le_skill_8_lvl.setText(str(self.char.skill_8_lvl))
        self.le_skill_9_lvl.setText(str(self.char.skill_9_lvl))
        self.le_skill_10_lvl.setText(str(self.char.skill_10_lvl))
        self.le_skill_11_lvl.setText(str(self.char.skill_11_lvl))
        self.le_skill_12_lvl.setText(str(self.char.skill_12_lvl))
        self.le_skill_13_lvl.setText(str(self.char.skill_13_lvl))
        self.le_skill_14_lvl.setText(str(self.char.skill_14_lvl))
        self.le_skill_15_lvl.setText(str(self.char.skill_15_lvl))
        self.le_skill_16_lvl.setText(str(self.char.skill_16_lvl))
        #perks
        self.cb_perk_1.setCurrentIndex(self.cb_perk_1.findText(self.char.perk_1))
        self.cb_perk_2.setCurrentIndex(self.cb_perk_2.findText(self.char.perk_2))
        self.cb_perk_3.setCurrentIndex(self.cb_perk_3.findText(self.char.perk_3))
        self.cb_perk_4.setCurrentIndex(self.cb_perk_4.findText(self.char.perk_4))
        self.cb_perk_5.setCurrentIndex(self.cb_perk_5.findText(self.char.perk_5))
        self.cb_perk_6.setCurrentIndex(self.cb_perk_6.findText(self.char.perk_6))
        self.cb_perk_7.setCurrentIndex(self.cb_perk_7.findText(self.char.perk_7))
        self.cb_perk_8.setCurrentIndex(self.cb_perk_8.findText(self.char.perk_8))
        self.cb_perk_9.setCurrentIndex(self.cb_perk_9.findText(self.char.perk_9))
        self.cb_perk_10.setCurrentIndex(self.cb_perk_10.findText(self.char.perk_10))
        self.cb_perk_11.setCurrentIndex(self.cb_perk_11.findText(self.char.perk_11))
        self.cb_perk_12.setCurrentIndex(self.cb_perk_12.findText(self.char.perk_12))
        self.cb_perk_13.setCurrentIndex(self.cb_perk_13.findText(self.char.perk_13))
        self.cb_perk_14.setCurrentIndex(self.cb_perk_14.findText(self.char.perk_14))
        self.cb_perk_15.setCurrentIndex(self.cb_perk_15.findText(self.char.perk_15))
        self.cb_perk_16.setCurrentIndex(self.cb_perk_16.findText(self.char.perk_16))
        self.le_perk_1_lvl.setText(str(self.char.perk_1_lvl))
        self.le_perk_2_lvl.setText(str(self.char.perk_2_lvl))
        self.le_perk_3_lvl.setText(str(self.char.perk_3_lvl))
        self.le_perk_4_lvl.setText(str(self.char.perk_4_lvl))
        self.le_perk_5_lvl.setText(str(self.char.perk_5_lvl))
        self.le_perk_6_lvl.setText(str(self.char.perk_6_lvl))
        self.le_perk_7_lvl.setText(str(self.char.perk_7_lvl))
        self.le_perk_8_lvl.setText(str(self.char.perk_8_lvl))
        self.le_perk_9_lvl.setText(str(self.char.perk_9_lvl))
        self.le_perk_10_lvl.setText(str(self.char.perk_10_lvl))
        self.le_perk_11_lvl.setText(str(self.char.perk_11_lvl))
        self.le_perk_12_lvl.setText(str(self.char.perk_12_lvl))
        self.le_perk_13_lvl.setText(str(self.char.perk_13_lvl))
        self.le_perk_14_lvl.setText(str(self.char.perk_14_lvl))
        self.le_perk_15_lvl.setText(str(self.char.perk_15_lvl))
        self.le_perk_16_lvl.setText(str(self.char.perk_16_lvl))

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
