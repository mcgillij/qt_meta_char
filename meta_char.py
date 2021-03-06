from PyQt4 import QtGui
from PyQt4.QtCore import *
import sys
import meta_char_window
from classes import MetaChar, Brain, RightHand, LeftHand
from xhtml2pdf import pisa

class MainApp(QtGui.QMainWindow, meta_char_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.meta_char = MetaChar()
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
        menubar = self.menuBar()

        file_menu = menubar.addMenu('&File')
        file_menu.addAction(load_action)
        file_menu.addAction(save_action)
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
            #print file(filename).read()

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

    def showOpenDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '/home')
        #print "opening", filename, "\n"
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
        #print "saving", filename, "\n"
        if filename:
            self.meta_char.save_to_disk(filename)

    # hooks up all the textfields / areas
    def init_ui(self):
        self.lineEditName.textChanged.connect(self.onMCNameTextChanged)
        self.plainTextEditHistory.textChanged.connect(self.onMCHistoryTextChanged)
        # brain related actions
        self.lineEditBrainName.textChanged.connect(self.onBrainNameTextChanged)
        self.lineEditBrainInt.textChanged.connect(self.onBrainIntTextChanged)
        self.lineEditBrainRef.textChanged.connect(self.onBrainRefTextChanged)
        self.lineEditBrainTech.textChanged.connect(self.onBrainTechTextChanged)
        self.lineEditBrainDex.textChanged.connect(self.onBrainDexTextChanged)
        self.lineEditBrainCool.textChanged.connect(self.onBrainCoolTextChanged)
        self.lineEditBrainWill.textChanged.connect(self.onBrainWillTextChanged)
        self.lineEditBrainStr.textChanged.connect(self.onBrainStrTextChanged)
        self.lineEditBrainCon.textChanged.connect(self.onBrainConTextChanged)
        self.lineEditBrainMove.textChanged.connect(self.onBrainMoveTextChanged)
        self.lineEditBrainBody.textChanged.connect(self.onBrainBodyTextChanged)
        self.lineEditBrainKSOne.textChanged.connect(self.onBrainKSOneTextChanged)
        self.lineEditBrainKSOneLVL.textChanged.connect(self.onBrainKSOneLVLTextChanged)
        self.lineEditBrainKSTwo.textChanged.connect(self.onBrainKSTwoTextChanged)
        self.lineEditBrainKSTwoLVL.textChanged.connect(self.onBrainKSTwoLVLTextChanged)
        self.lineEditBrainKPOne.textChanged.connect(self.onBrainKPOneTextChanged)
        self.lineEditBrainKPOneLVL.textChanged.connect(self.onBrainKPOneLVLTextChanged)
        self.lineEditBrainKPTwo.textChanged.connect(self.onBrainKPTwoTextChanged)
        self.lineEditBrainKPTwoLVL.textChanged.connect(self.onBrainKPTwoLVLTextChanged)
        self.plainTextEditBrainLP.textChanged.connect(self.onBrainLPTextChanged)
        self.plainTextEditBrainGoals.textChanged.connect(self.onBrainGoalsTextChanged)

        # right hand related actions
        self.lineEditRHName.textChanged.connect(self.onRHNameTextChanged)
        self.lineEditRHInt.textChanged.connect(self.onRHIntTextChanged)
        self.lineEditRHRef.textChanged.connect(self.onRHRefTextChanged)
        self.lineEditRHTech.textChanged.connect(self.onRHTechTextChanged)
        self.lineEditRHDex.textChanged.connect(self.onRHDexTextChanged)
        self.lineEditRHCool.textChanged.connect(self.onRHCoolTextChanged)
        self.lineEditRHWill.textChanged.connect(self.onRHWillTextChanged)
        self.lineEditRHStr.textChanged.connect(self.onRHStrTextChanged)
        self.lineEditRHCon.textChanged.connect(self.onRHConTextChanged)
        self.lineEditRHMove.textChanged.connect(self.onRHMoveTextChanged)
        self.lineEditRHBody.textChanged.connect(self.onRHBodyTextChanged)
        self.lineEditRHKSOne.textChanged.connect(self.onRHKSOneTextChanged)
        self.lineEditRHKSOneLVL.textChanged.connect(self.onRHKSOneLVLTextChanged)
        self.lineEditRHKSTwo.textChanged.connect(self.onRHKSTwoTextChanged)
        self.lineEditRHKSTwoLVL.textChanged.connect(self.onRHKSTwoLVLTextChanged)
        self.lineEditRHKPOne.textChanged.connect(self.onRHKPOneTextChanged)
        self.lineEditRHKPOneLVL.textChanged.connect(self.onRHKPOneLVLTextChanged)
        self.lineEditRHKPTwo.textChanged.connect(self.onRHKPTwoTextChanged)
        self.lineEditRHKPTwoLVL.textChanged.connect(self.onRHKPTwoLVLTextChanged)
        self.plainTextEditRHLP.textChanged.connect(self.onRHLPTextChanged)
        self.plainTextEditRHGoals.textChanged.connect(self.onRHGoalsTextChanged)
        # left hand related actions
        self.lineEditLHName.textChanged.connect(self.onLHNameTextChanged)
        self.lineEditLHInt.textChanged.connect(self.onLHIntTextChanged)
        self.lineEditLHRef.textChanged.connect(self.onLHRefTextChanged)
        self.lineEditLHTech.textChanged.connect(self.onLHTechTextChanged)
        self.lineEditLHDex.textChanged.connect(self.onLHDexTextChanged)
        self.lineEditLHCool.textChanged.connect(self.onLHCoolTextChanged)
        self.lineEditLHWill.textChanged.connect(self.onLHWillTextChanged)
        self.lineEditLHStr.textChanged.connect(self.onLHStrTextChanged)
        self.lineEditLHCon.textChanged.connect(self.onLHConTextChanged)
        self.lineEditLHMove.textChanged.connect(self.onLHMoveTextChanged)
        self.lineEditLHBody.textChanged.connect(self.onLHBodyTextChanged)
        self.lineEditLHKSOne.textChanged.connect(self.onLHKSOneTextChanged)
        self.lineEditLHKSOneLVL.textChanged.connect(self.onLHKSOneLVLTextChanged)
        self.lineEditLHKSTwo.textChanged.connect(self.onLHKSTwoTextChanged)
        self.lineEditLHKSTwoLVL.textChanged.connect(self.onLHKSTwoLVLTextChanged)
        self.lineEditLHKPOne.textChanged.connect(self.onLHKPOneTextChanged)
        self.lineEditLHKPOneLVL.textChanged.connect(self.onLHKPOneLVLTextChanged)
        self.lineEditLHKPTwo.textChanged.connect(self.onLHKPTwoTextChanged)
        self.lineEditLHKPTwoLVL.textChanged.connect(self.onLHKPTwoLVLTextChanged)
        self.plainTextEditLHLP.textChanged.connect(self.onLHLPTextChanged)
        self.plainTextEditLHGoals.textChanged.connect(self.onLHGoalsTextChanged)

        # body related actions
        self.lineEditBodyLeaders.textChanged.connect(self.onBodyLeadersTextChanged)
        self.lineEditBodySoldiers.textChanged.connect(self.onBodySoldiersTextChanged)
        self.lineEditBodyGrunts.textChanged.connect(self.onBodyGruntsTextChanged)
        self.plainTextEditBodyAssets.textChanged.connect(self.onBodyAssetsTextChanged)
        self.plainTextEditBodyVehicles.textChanged.connect(self.onBodyVehiclesTextChanged)

    def update_body_fields(self):
        self.lineEditBodyLeaders.setText(str(self.meta_char.body.leaders))
        self.lineEditBodySoldiers.setText(str(self.meta_char.body.soldiers))
        self.lineEditBodyGrunts.setText(str(self.meta_char.body.grunts))
        self.plainTextEditBodyAssets.setPlainText(str(self.meta_char.body.assets))
        self.plainTextEditBodyVehicles.setPlainText(str(self.meta_char.body.vehicles))
    # body related events
    def onBodyLeadersTextChanged(self, text):
        #print 'onBodyLeadersTextChanged', text
        self.meta_char.body.leaders = str(text)
        #print self.meta_char.body.leaders
    def onBodySoldiersTextChanged(self, text):
        #print 'onBodySoldiersTextChanged', text
        self.meta_char.body.soldiers = str(text)
        #print self.meta_char.body.soldiers
    def onBodyGruntsTextChanged(self, text):
        #print 'onBodyGruntsTextChanged', text
        self.meta_char.body.grunts = str(text)
        #print self.meta_char.body.grunts
    def onBodyAssetsTextChanged(self):
        text = self.plainTextEditBodyAssets.toPlainText()
        #print 'onBodyAssetsTextChanged', text
        self.meta_char.body.assets = str(text)
        #print self.meta_char.body.assets
    def onBodyVehiclesTextChanged(self):
        text = self.plainTextEditBodyVehicles.toPlainText()
        #print 'onBodyVehiclesTextChanged', text
        self.meta_char.body.vehicles= str(text)
        #print self.meta_char.body.vehicles

    # meta_char base level attributes
    def onMCNameTextChanged(self, text):
        #print 'onMCNameTextChanged', text
        self.meta_char.name = str(text)
        #print self.meta_char.name
    def onMCHistoryTextChanged(self):
        text = self.plainTextEditHistory.toPlainText()
        #print 'onMCHistoryTextChanged', text
        self.meta_char.history = str(text)
        #print self.meta_char.history
    # brain page related functions
    def onBrainGoalsTextChanged(self):
        text = self.plainTextEditBrainGoals.toPlainText()
        #print 'onBrainGoalsTextChanged', text
        self.meta_char.brain.goals = str(text)
        #print self.meta_char.brain.goals
    def onBrainLPTextChanged(self):
        text = self.plainTextEditBrainLP.toPlainText()
        #print 'onBrainLPTextChanged', text
        self.meta_char.brain.lifepath = str(text)
        #print self.meta_char.brain.lifepath
    def onBrainKSOneTextChanged(self, text):
        #print 'onBrainKSOneTextChanged', text
        self.meta_char.brain.key_skill_1 = str(text)
        #print self.meta_char.brain.key_skill_1

    def onBrainKSOneLVLTextChanged(self, text):
        #print 'onBrainKSOneLVLTextChanged', text
        self.meta_char.brain.key_skill_1_lvl = int(text)
        #print self.meta_char.brain.key_skill_1_lvl
    def onBrainKSTwoTextChanged(self, text):
        #print 'onBrainKSTwoTextChanged', text
        self.meta_char.brain.key_skill_2 = str(text)
        #print self.meta_char.brain.key_skill_2

    def onBrainKSTwoLVLTextChanged(self, text):
        #print 'onBrainKSTwoLVLTextChanged', text
        self.meta_char.brain.key_skill_2_lvl = int(text)
        #print self.meta_char.brain.key_skill_2_lvl
    def onBrainKPOneTextChanged(self, text):
        #print 'onBrainKPOneTextChanged', text
        self.meta_char.brain.key_perk_1 = str(text)
        #print self.meta_char.brain.key_perk_1

    def onBrainKPOneLVLTextChanged(self, text):
        #print 'onBrainKPOneLVLTextChanged', text
        self.meta_char.brain.key_perk_1_lvl = int(text)
        #print self.meta_char.brain.key_perk_1_lvl
    def onBrainKPTwoTextChanged(self, text):
        #print 'onBrainKPTwoTextChanged', text
        self.meta_char.brain.key_perk_2 = str(text)
        #print self.meta_char.brain.key_perk_2

    def onBrainKPTwoLVLTextChanged(self, text):
        #print 'onBrainKPTwoLVLTextChanged', text
        self.meta_char.brain.key_perk_2_lvl = int(text)
        #print self.meta_char.brain.key_perk_2_lvl

    def onBrainIntTextChanged(self, text):
        #print 'onBrainIntTextChanged', text
        self.meta_char.brain.intelligence = int(text)
        self.update_all_brain_derived_fields()

    def onBrainRefTextChanged(self, text):
        #print 'onBrainRefTextChanged', text
        self.meta_char.brain.reflex = int(text)
        self.update_all_brain_derived_fields()

    def onBrainTechTextChanged(self, text):
        #print 'onBrainTechTextChanged', text
        self.meta_char.brain.technology = int(text)
        self.update_all_brain_derived_fields()

    def onBrainDexTextChanged(self, text):
        #print 'onBrainDexTextChanged', text
        self.meta_char.brain.dexterity = int(text)
        self.update_all_brain_derived_fields()

    def onBrainCoolTextChanged(self, text):
        #print 'onBrainCoolTextChanged', text
        self.meta_char.brain.cool = int(text)
        self.update_all_brain_derived_fields()

    def onBrainWillTextChanged(self, text):
        #print 'onBrainWillTextChanged', text
        self.meta_char.brain.will= int(text)
        self.update_all_brain_derived_fields()

    def onBrainStrTextChanged(self, text):
        #print 'onBrainStrTextChanged', text
        self.meta_char.brain.strength = int(text)
        self.update_all_brain_derived_fields()

    def onBrainConTextChanged(self, text):
        #print 'onBrainConTextChanged', text
        self.meta_char.brain.constitution = int(text)
        self.update_all_brain_derived_fields()

    def onBrainMoveTextChanged(self, text):
        #print 'onBrainMoveTextChanged', text
        self.meta_char.brain.move = int(text)
        self.update_all_brain_derived_fields()

    def onBrainBodyTextChanged(self, text):
        #print 'onBrainBodyTextChanged', text
        self.meta_char.brain.body = int(text)
        self.update_all_brain_derived_fields()

    def onBrainNameTextChanged(self, text):
        #print 'onBrainNameTextChanged', text
        self.meta_char.brain.name= str(text)

    def update_all_mc_fields(self):
        self.lineEditName.setText(str(self.meta_char.name))
        self.plainTextEditHistory.setPlainText(str(self.meta_char.history))

    def update_all_brain_derived_fields(self):
        # key skills
        self.lineEditBrainName.setText(str(self.meta_char.brain.name))
        self.lineEditBrainInt.setText(str(self.meta_char.brain.intelligence))
        self.lineEditBrainRef.setText(str(self.meta_char.brain.reflex))
        self.lineEditBrainTech.setText(str(self.meta_char.brain.technology))
        self.lineEditBrainDex.setText(str(self.meta_char.brain.dexterity))
        self.lineEditBrainCool.setText(str(self.meta_char.brain.cool))
        self.lineEditBrainWill.setText(str(self.meta_char.brain.will))
        self.lineEditBrainStr.setText(str(self.meta_char.brain.strength))
        self.lineEditBrainCon.setText(str(self.meta_char.brain.constitution))
        self.lineEditBrainMove.setText(str(self.meta_char.brain.move))
        self.lineEditBrainBody.setText(str(self.meta_char.brain.body))
        self.lineEditBrainKSOne.setText(str(self.meta_char.brain.key_skill_1))
        self.lineEditBrainKSOneLVL.setText(str(self.meta_char.brain.key_skill_1_lvl))
        self.lineEditBrainKSTwo.setText(str(self.meta_char.brain.key_skill_2))
        self.lineEditBrainKSTwoLVL.setText(str(self.meta_char.brain.key_skill_2_lvl))
        self.lineEditBrainKPOne.setText(str(self.meta_char.brain.key_perk_1))
        self.lineEditBrainKPOneLVL.setText(str(self.meta_char.brain.key_perk_1_lvl))
        self.lineEditBrainKPTwo.setText(str(self.meta_char.brain.key_perk_2))
        self.lineEditBrainKPTwoLVL.setText(str(self.meta_char.brain.key_perk_2_lvl))
        self.plainTextEditBrainLP.setPlainText(str(self.meta_char.brain.lifepath))
        self.plainTextEditBrainGoals.setPlainText(str(self.meta_char.brain.goals))
        #luck
        self.meta_char.brain.luck = self.meta_char.brain.intelligence + self.meta_char.brain.reflex / 2
        self.lineROBrainLuck.setText(str(self.meta_char.brain.luck))
        #print str(self.meta_char.brain.luck)
        #humanity
        self.meta_char.brain.humanity = self.meta_char.brain.will * 10
        self.lineROBrainHum.setText(str(self.meta_char.brain.humanity))
        #print str(self.meta_char.brain.humanity)
        #recovery
        self.meta_char.brain.recovery = self.meta_char.brain.strength + self.meta_char.brain.constitution / 2
        self.lineROBrainRec.setText(str(self.meta_char.brain.recovery))
        #print str(self.meta_char.brain.recovery)
        #endurance
        self.meta_char.brain.endurance = self.meta_char.brain.constitution * 2
        self.lineROBrainEnd.setText(str(self.meta_char.brain.endurance))
        #print str(self.meta_char.brain.endurance)
        #run
        self.meta_char.brain.run = self.meta_char.brain.move * 2
        self.lineROBrainRun.setText(str(self.meta_char.brain.run))
        #print str(self.meta_char.brain.run)
        #sprint
        self.meta_char.brain.sprint = self.meta_char.brain.move * 3
        self.lineROBrainSpr.setText(str(self.meta_char.brain.sprint))
        #print str(self.meta_char.brain.sprint)
        #swim
        self.meta_char.brain.swim = self.meta_char.brain.move
        self.lineROBrainSwim.setText(str(self.meta_char.brain.swim))
        #print str(self.meta_char.brain.swim)
        #leap
        self.meta_char.brain.leap = self.meta_char.brain.move
        self.lineROBrainLeap.setText(str(self.meta_char.brain.leap))
        #print str(self.meta_char.brain.leap)
        #hits
        self.meta_char.brain.hits = self.meta_char.brain.body * 2
        self.lineROBrainHits.setText(str(self.meta_char.brain.hits))
        #print str(self.meta_char.brain.hits)
        #stun
        self.meta_char.brain.stun = self.meta_char.brain.body * 5
        self.lineROBrainStun.setText(str(self.meta_char.brain.stun))
        #print str(self.meta_char.brain.stun)

    # right hand page related functions
    def onRHGoalsTextChanged(self):
        text = self.plainTextEditRHGoals.toPlainText()
        #print 'onRHGoalsTextChanged', text
        self.meta_char.right_hand.goals = str(text)
        #print self.meta_char.right_hand.goals
    def onRHLPTextChanged(self):
        text = self.plainTextEditRHLP.toPlainText()
        #print 'onRHLPTextChanged', text
        self.meta_char.right_hand.lifepath = str(text)
        #print self.meta_char.right_hand.lifepath
    def onRHKSOneTextChanged(self, text):
        #print 'onRHKSOneTextChanged', text
        self.meta_char.right_hand.key_skill_1 = str(text)
        #print self.meta_char.right_hand.key_skill_1

    def onRHKSOneLVLTextChanged(self, text):
        #print 'onRHKSOneLVLTextChanged', text
        self.meta_char.right_hand.key_skill_1_lvl = int(text)
        #print self.meta_char.right_hand.key_skill_1_lvl
    def onRHKSTwoTextChanged(self, text):
        #print 'onRHKSTwoTextChanged', text
        self.meta_char.right_hand.key_skill_2 = str(text)
        #print self.meta_char.right_hand.key_skill_2

    def onRHKSTwoLVLTextChanged(self, text):
        #print 'onRHKSTwoLVLTextChanged', text
        self.meta_char.right_hand.key_skill_2_lvl = int(text)
        #print self.meta_char.right_hand.key_skill_2_lvl
    def onRHKPOneTextChanged(self, text):
        #print 'onRHKPOneTextChanged', text
        self.meta_char.right_hand.key_perk_1 = str(text)
        #print self.meta_char.right_hand.key_perk_1

    def onRHKPOneLVLTextChanged(self, text):
        #print 'onRHKPOneLVLTextChanged', text
        self.meta_char.right_hand.key_perk_1_lvl = int(text)
        #print self.meta_char.right_hand.key_perk_1_lvl
    def onRHKPTwoTextChanged(self, text):
        #print 'onRHKPTwoTextChanged', text
        self.meta_char.right_hand.key_perk_2 = str(text)
        #print self.meta_char.right_hand.key_perk_2

    def onRHKPTwoLVLTextChanged(self, text):
        #print 'onRHKPTwoLVLTextChanged', text
        self.meta_char.right_hand.key_perk_2_lvl = int(text)
        #print self.meta_char.right_hand.key_perk_2_lvl
    def onRHIntTextChanged(self, text):
        #print 'onRHIntTextChanged', text
        self.meta_char.right_hand.intelligence = int(text)
        self.update_all_right_hand_derived_fields()

    def onRHRefTextChanged(self, text):
        #print 'onRHRefTextChanged', text
        self.meta_char.right_hand.reflex = int(text)
        self.update_all_right_hand_derived_fields()

    def onRHTechTextChanged(self, text):
        #print 'onRHTechTextChanged', text
        self.meta_char.right_hand.technology = int(text)
        self.update_all_right_hand_derived_fields()

    def onRHDexTextChanged(self, text):
        #print 'onRHDexTextChanged', text
        self.meta_char.right_hand.dexterity = int(text)
        self.update_all_right_hand_derived_fields()

    def onRHCoolTextChanged(self, text):
        #print 'onRHCoolTextChanged', text
        self.meta_char.right_hand.cool = int(text)
        self.update_all_right_hand_derived_fields()

    def onRHWillTextChanged(self, text):
        #print 'onRHWillTextChanged', text
        self.meta_char.right_hand.will= int(text)
        self.update_all_right_hand_derived_fields()

    def onRHStrTextChanged(self, text):
        #print 'onRHStrTextChanged', text
        self.meta_char.right_hand.strength = int(text)
        self.update_all_right_hand_derived_fields()

    def onRHConTextChanged(self, text):
        #print 'onRHConTextChanged', text
        self.meta_char.right_hand.constitution = int(text)
        self.update_all_right_hand_derived_fields()

    def onRHMoveTextChanged(self, text):
        #print 'onRHMoveTextChanged', text
        self.meta_char.right_hand.move = int(text)
        self.update_all_right_hand_derived_fields()

    def onRHBodyTextChanged(self, text):
        #print 'onRHBodyTextChanged', text
        self.meta_char.right_hand.body = int(text)
        self.update_all_right_hand_derived_fields()

    def onRHNameTextChanged(self, text):
        #print 'onRHNameTextChanged', text
        self.meta_char.right_hand.name= str(text)

    def update_all_right_hand_derived_fields(self):
        # key skills
        self.lineEditRHName.setText(str(self.meta_char.right_hand.name))
        self.lineEditRHInt.setText(str(self.meta_char.right_hand.intelligence))
        self.lineEditRHRef.setText(str(self.meta_char.right_hand.reflex))
        self.lineEditRHTech.setText(str(self.meta_char.right_hand.technology))
        self.lineEditRHDex.setText(str(self.meta_char.right_hand.dexterity))
        self.lineEditRHCool.setText(str(self.meta_char.right_hand.cool))
        self.lineEditRHWill.setText(str(self.meta_char.right_hand.will))
        self.lineEditRHStr.setText(str(self.meta_char.right_hand.strength))
        self.lineEditRHCon.setText(str(self.meta_char.right_hand.constitution))
        self.lineEditRHMove.setText(str(self.meta_char.right_hand.move))
        self.lineEditRHBody.setText(str(self.meta_char.right_hand.body))
        self.lineEditRHKSOne.setText(str(self.meta_char.right_hand.key_skill_1))
        self.lineEditRHKSOneLVL.setText(str(self.meta_char.right_hand.key_skill_1_lvl))
        self.lineEditRHKSTwo.setText(str(self.meta_char.right_hand.key_skill_2))
        self.lineEditRHKSTwoLVL.setText(str(self.meta_char.right_hand.key_skill_2_lvl))
        self.lineEditRHKPOne.setText(str(self.meta_char.right_hand.key_perk_1))
        self.lineEditRHKPOneLVL.setText(str(self.meta_char.right_hand.key_perk_1_lvl))
        self.lineEditRHKPTwo.setText(str(self.meta_char.right_hand.key_perk_2))
        self.lineEditRHKPTwoLVL.setText(str(self.meta_char.right_hand.key_perk_2_lvl))
        self.plainTextEditRHLP.setPlainText(str(self.meta_char.right_hand.lifepath))
        self.plainTextEditRHGoals.setPlainText(str(self.meta_char.right_hand.goals))
        #luck
        self.meta_char.right_hand.luck = self.meta_char.right_hand.intelligence + self.meta_char.right_hand.reflex / 2
        self.lineRORHLuck.setText(str(self.meta_char.right_hand.luck))
        #print str(self.meta_char.right_hand.luck)
        #humanity
        self.meta_char.right_hand.humanity = self.meta_char.right_hand.will * 10
        self.lineRORHHum.setText(str(self.meta_char.right_hand.humanity))
        #print str(self.meta_char.right_hand.humanity)
        #recovery
        self.meta_char.right_hand.recovery = self.meta_char.right_hand.strength + self.meta_char.right_hand.constitution / 2
        self.lineRORHRec.setText(str(self.meta_char.right_hand.recovery))
        #print str(self.meta_char.right_hand.recovery)
        #endurance
        self.meta_char.right_hand.endurance = self.meta_char.right_hand.constitution * 2
        self.lineRORHEnd.setText(str(self.meta_char.right_hand.endurance))
        #print str(self.meta_char.right_hand.endurance)
        #run
        self.meta_char.right_hand.run = self.meta_char.right_hand.move * 2
        self.lineRORHRun.setText(str(self.meta_char.right_hand.run))
        #print str(self.meta_char.right_hand.run)
        #sprint
        self.meta_char.right_hand.sprint = self.meta_char.right_hand.move * 3
        self.lineRORHSpr.setText(str(self.meta_char.right_hand.sprint))
        #print str(self.meta_char.right_hand.sprint)
        #swim
        self.meta_char.right_hand.swim = self.meta_char.right_hand.move
        self.lineRORHSwim.setText(str(self.meta_char.right_hand.swim))
        #print str(self.meta_char.right_hand.swim)
        #leap
        self.meta_char.right_hand.leap = self.meta_char.right_hand.move
        self.lineRORHLeap.setText(str(self.meta_char.right_hand.leap))
        #print str(self.meta_char.right_hand.leap)
        #hits
        self.meta_char.right_hand.hits = self.meta_char.right_hand.body * 2
        self.lineRORHHits.setText(str(self.meta_char.right_hand.hits))
        #print str(self.meta_char.right_hand.hits)
        #stun
        self.meta_char.right_hand.stun = self.meta_char.right_hand.body * 5
        self.lineRORHStun.setText(str(self.meta_char.right_hand.stun))
        #print str(self.meta_char.right_hand.stun)

    # left hand page related functions
    def onLHGoalsTextChanged(self):
        text = self.plainTextEditLHGoals.toPlainText()
        #print 'onLHGoalsTextChanged', text
        self.meta_char.left_hand.goals = str(text)
        #print self.meta_char.left_hand.goals
    def onLHLPTextChanged(self):
        text = self.plainTextEditLHLP.toPlainText()
        #print 'onLHLPTextChanged', text
        self.meta_char.left_hand.lifepath = str(text)
        #print self.meta_char.left_hand.lifepath
    def onLHKSOneTextChanged(self, text):
        #print 'onLHKSOneTextChanged', text
        self.meta_char.left_hand.key_skill_1 = str(text)
        #print self.meta_char.left_hand.key_skill_1

    def onLHKSOneLVLTextChanged(self, text):
        #print 'onLHKSOneLVLTextChanged', text
        self.meta_char.left_hand.key_skill_1_lvl = int(text)
        #print self.meta_char.left_hand.key_skill_1_lvl
    def onLHKSTwoTextChanged(self, text):
        #print 'onLHKSTwoTextChanged', text
        self.meta_char.left_hand.key_skill_2 = str(text)
        #print self.meta_char.left_hand.key_skill_2

    def onLHKSTwoLVLTextChanged(self, text):
        #print 'onLHKSTwoLVLTextChanged', text
        self.meta_char.left_hand.key_skill_2_lvl = int(text)
        #print self.meta_char.left_hand.key_skill_2_lvl
    def onLHKPOneTextChanged(self, text):
        #print 'onLHKPOneTextChanged', text
        self.meta_char.left_hand.key_perk_1 = str(text)
        #print self.meta_char.left_hand.key_perk_1

    def onLHKPOneLVLTextChanged(self, text):
        #print 'onLHKPOneLVLTextChanged', text
        self.meta_char.left_hand.key_perk_1_lvl = int(text)
        #print self.meta_char.left_hand.key_perk_1_lvl
    def onLHKPTwoTextChanged(self, text):
        #print 'onLHKPTwoTextChanged', text
        self.meta_char.left_hand.key_perk_2 = str(text)
        #print self.meta_char.left_hand.key_perk_2

    def onLHKPTwoLVLTextChanged(self, text):
        #print 'onLHKPTwoLVLTextChanged', text
        self.meta_char.left_hand.key_perk_2_lvl = int(text)
        #print self.meta_char.left_hand.key_perk_2_lvl

    def onLHIntTextChanged(self, text):
        #print 'onLHIntTextChanged', text
        self.meta_char.left_hand.intelligence = int(text)
        self.update_all_left_hand_derived_fields()

    def onLHRefTextChanged(self, text):
        #print 'onLHRefTextChanged', text
        self.meta_char.left_hand.reflex = int(text)
        self.update_all_left_hand_derived_fields()

    def onLHTechTextChanged(self, text):
        #print 'onLHTechTextChanged', text
        self.meta_char.left_hand.technology = int(text)
        self.update_all_left_hand_derived_fields()

    def onLHDexTextChanged(self, text):
        #print 'onLHDexTextChanged', text
        self.meta_char.left_hand.dexterity = int(text)
        self.update_all_left_hand_derived_fields()

    def onLHCoolTextChanged(self, text):
        #print 'onLHCoolTextChanged', text
        self.meta_char.left_hand.cool = int(text)
        self.update_all_left_hand_derived_fields()

    def onLHWillTextChanged(self, text):
        #print 'onLHWillTextChanged', text
        self.meta_char.left_hand.will= int(text)
        self.update_all_left_hand_derived_fields()

    def onLHStrTextChanged(self, text):
        #print 'onLHStrTextChanged', text
        self.meta_char.left_hand.strength = int(text)
        self.update_all_left_hand_derived_fields()

    def onLHConTextChanged(self, text):
        #print 'onLHConTextChanged', text
        self.meta_char.left_hand.constitution = int(text)
        self.update_all_left_hand_derived_fields()

    def onLHMoveTextChanged(self, text):
        #print 'onLHMoveTextChanged', text
        self.meta_char.left_hand.move = int(text)
        self.update_all_left_hand_derived_fields()

    def onLHBodyTextChanged(self, text):
        #print 'onLHBodyTextChanged', text
        self.meta_char.left_hand.body = int(text)
        self.update_all_left_hand_derived_fields()

    def onLHNameTextChanged(self, text):
        #print 'onLNNameTextChanged', text
        self.meta_char.left_hand.name= str(text)

    def update_all_left_hand_derived_fields(self):
        # key skills
        self.lineEditLHName.setText(str(self.meta_char.left_hand.name))
        self.lineEditLHInt.setText(str(self.meta_char.left_hand.intelligence))
        self.lineEditLHRef.setText(str(self.meta_char.left_hand.reflex))
        self.lineEditLHTech.setText(str(self.meta_char.left_hand.technology))
        self.lineEditLHDex.setText(str(self.meta_char.left_hand.dexterity))
        self.lineEditLHCool.setText(str(self.meta_char.left_hand.cool))
        self.lineEditLHWill.setText(str(self.meta_char.left_hand.will))
        self.lineEditLHStr.setText(str(self.meta_char.left_hand.strength))
        self.lineEditLHCon.setText(str(self.meta_char.left_hand.constitution))
        self.lineEditLHMove.setText(str(self.meta_char.left_hand.move))
        self.lineEditLHBody.setText(str(self.meta_char.left_hand.body))
        self.lineEditLHKSOne.setText(str(self.meta_char.left_hand.key_skill_1))
        self.lineEditLHKSOneLVL.setText(str(self.meta_char.left_hand.key_skill_1_lvl))
        self.lineEditLHKSTwo.setText(str(self.meta_char.left_hand.key_skill_2_lvl))
        self.lineEditLHKSTwoLVL.setText(str(self.meta_char.left_hand.key_skill_2_lvl))
        self.lineEditLHKPOne.setText(str(self.meta_char.left_hand.key_perk_1))
        self.lineEditLHKPOneLVL.setText(str(self.meta_char.left_hand.key_perk_1_lvl))
        self.lineEditLHKPTwo.setText(str(self.meta_char.left_hand.key_perk_2_lvl))
        self.lineEditLHKPTwoLVL.setText(str(self.meta_char.left_hand.key_perk_2_lvl))
        self.plainTextEditLHLP.setPlainText(str(self.meta_char.left_hand.lifepath))
        self.plainTextEditLHGoals.setPlainText(str(self.meta_char.left_hand.goals))
        #luck
        self.meta_char.left_hand.luck = self.meta_char.left_hand.intelligence + self.meta_char.left_hand.reflex / 2
        self.lineROLHLuck.setText(str(self.meta_char.left_hand.luck))
        #print str(self.meta_char.left_hand.luck)
        #humanity
        self.meta_char.left_hand.humanity = self.meta_char.left_hand.will * 10
        self.lineROLHHum.setText(str(self.meta_char.left_hand.humanity))
        #print str(self.meta_char.left_hand.humanity)
        #recovery
        self.meta_char.left_hand.recovery = self.meta_char.left_hand.strength + self.meta_char.left_hand.constitution / 2
        self.lineROLHRec.setText(str(self.meta_char.left_hand.recovery))
        #print str(self.meta_char.left_hand.recovery)
        #endurance
        self.meta_char.left_hand.endurance = self.meta_char.left_hand.constitution * 2
        self.lineROLHEnd.setText(str(self.meta_char.left_hand.endurance))
        #print str(self.meta_char.left_hand.endurance)
        #run
        self.meta_char.left_hand.run = self.meta_char.left_hand.move * 2
        self.lineROLHRun.setText(str(self.meta_char.left_hand.run))
        #print str(self.meta_char.left_hand.run)
        #sprint
        self.meta_char.left_hand.sprint = self.meta_char.left_hand.move * 3
        self.lineROLHSpr.setText(str(self.meta_char.left_hand.sprint))
        #print str(self.meta_char.left_hand.sprint)
        #swim
        self.meta_char.left_hand.swim = self.meta_char.left_hand.move
        self.lineROLHSwim.setText(str(self.meta_char.left_hand.swim))
        #print str(self.meta_char.left_hand.swim)
        #leap
        self.meta_char.left_hand.leap = self.meta_char.left_hand.move
        self.lineROLHLeap.setText(str(self.meta_char.left_hand.leap))
        #print str(self.meta_char.left_hand.leap)
        #hits
        self.meta_char.left_hand.hits = self.meta_char.left_hand.body * 2
        self.lineROLHHits.setText(str(self.meta_char.left_hand.hits))
        #print str(self.meta_char.left_hand.hits)
        #stun
        self.meta_char.left_hand.stun = self.meta_char.left_hand.body * 5
        self.lineROLHStun.setText(str(self.meta_char.left_hand.stun))
        #print str(self.meta_char.left_hand.stun)

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
