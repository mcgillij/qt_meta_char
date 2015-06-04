from PyQt4 import QtGui
from PyQt4.QtCore import *
import sys
from pprint import pprint
import meta_char_window
from classes import MetaChar, Brain, RightHand, LeftHand

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
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(QtGui.qApp.quit)

        save_action = QtGui.QAction(QtGui.QIcon('save.png'), '&Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save To Disk')
        save_action.triggered.connect(self.showSaveDialog)

        load_action = QtGui.QAction(QtGui.QIcon('load.png'), '&Load', self)
        load_action.setShortcut('Ctrl+O')
        load_action.setStatusTip('Load From Disk')
        load_action.triggered.connect(self.showOpenDialog)

        test_action = QtGui.QAction(QtGui.QIcon('test.png'), '&Test', self)
        test_action.setShortcut('Ctrl+T')
        test_action.setStatusTip('TestAction')
        test_action.triggered.connect(self.showTestDialog)
        menubar = self.menuBar()

        file_menu = menubar.addMenu('&File')
        file_menu.addAction(load_action)
        file_menu.addAction(save_action)
        file_menu.addAction(test_action)
        file_menu.addAction(exit_action)
    def showTestDialog(self):
        print "From Test Action:", self.meta_char.name, self.meta_char.history, "brain: ", self.meta_char.brain.intelligence

    def showOpenDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '/home')
        print "opening", filename, "\n"
        if filename:
            meta_char = self.meta_char.load_from_disk(filename)
            self.meta_char = meta_char
            self.update_all_brain_derived_fields()


    def showSaveDialog(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', "*")
        print "saving", filename, "\n"
        if filename:
            self.meta_char.save_to_disk(filename)

    # hooks up all the textfields / areas
    def init_ui(self):
        self.lineEditName.textChanged.connect(self.onMCNameTextChanged)
        self.plainTextEditHistory.textChanged.connect(self.onMCHistoryTextChanged)
        # brain related actions
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
    # body related events
    def onBodyLeadersTextChanged(self, text):
        print 'onBodyLeadersTextChanged', text
        self.meta_char.body.leaders = str(text)
        print self.meta_char.body.leaders
        pass
    def onBodySoldiersTextChanged(self, text):
        print 'onBodySoldiersTextChanged', text
        self.meta_char.body.soldiers = str(text)
        print self.meta_char.body.soldiers
        pass
    def onBodyGruntsTextChanged(self, text):
        print 'onBodyGruntsTextChanged', text
        self.meta_char.body.grunts = str(text)
        print self.meta_char.body.grunts
        pass
    def onBodyAssetsTextChanged(self):
        text = self.plainTextEditBodyAssets.toPlainText()
        print 'onBodyAssetsTextChanged', text
        self.meta_char.body.assets = str(text)
        print self.meta_char.body.assets
        pass
    def onBodyVehiclesTextChanged(self):
        text = self.plainTextEditBodyVehicles.toPlainText()
        print 'onBodyVehiclesTextChanged', text
        self.meta_char.body.vehicles= str(text)
        print self.meta_char.body.vehicles
        pass

    # meta_char base level attributes
    def onMCNameTextChanged(self, text):
        print 'onMCNameTextChanged', text
        self.meta_char.name = str(text)
        print self.meta_char.name
        pass
    def onMCHistoryTextChanged(self):
        text = self.plainTextEditHistory.toPlainText()
        print 'onMCHistoryTextChanged', text
        self.meta_char.history = str(text)
        print self.meta_char.history
        pass
    # brain page related functions
    def onBrainGoalsTextChanged(self):
        text = self.plainTextEditBrainGoals.toPlainText()
        print 'onBrainGoalsTextChanged', text
        self.meta_char.brain.goals = str(text)
        print self.meta_char.brain.goals
        pass
    def onBrainLPTextChanged(self):
        text = self.plainTextEditBrainLP.toPlainText()
        print 'onBrainLPTextChanged', text
        self.meta_char.brain.lifepath = str(text)
        print self.meta_char.brain.lifepath
        pass
    def onBrainKSOneTextChanged(self, text):
        print 'onBrainKSOneTextChanged', text
        self.meta_char.brain.key_skill_1 = str(text)
        print self.meta_char.brain.key_skill_1
        pass

    def onBrainKSOneLVLTextChanged(self, text):
        print 'onBrainKSOneLVLTextChanged', text
        self.meta_char.brain.key_skill_1_lvl = int(text)
        print self.meta_char.brain.key_skill_1_lvl
        pass
    def onBrainKSTwoTextChanged(self, text):
        print 'onBrainKSTwoTextChanged', text
        self.meta_char.brain.key_skill_2 = str(text)
        print self.meta_char.brain.key_skill_2
        pass

    def onBrainKSTwoLVLTextChanged(self, text):
        print 'onBrainKSTwoLVLTextChanged', text
        self.meta_char.brain.key_skill_2_lvl = int(text)
        print self.meta_char.brain.key_skill_2_lvl
        pass
    def onBrainKPOneTextChanged(self, text):
        print 'onBrainKPOneTextChanged', text
        self.meta_char.brain.key_perk_1 = str(text)
        print self.meta_char.brain.key_perk_1
        pass

    def onBrainKPOneLVLTextChanged(self, text):
        print 'onBrainKPOneLVLTextChanged', text
        self.meta_char.brain.key_perk_1_lvl = int(text)
        print self.meta_char.brain.key_perk_1_lvl
        pass
    def onBrainKPTwoTextChanged(self, text):
        print 'onBrainKPTwoTextChanged', text
        self.meta_char.brain.key_perk_2 = str(text)
        print self.meta_char.brain.key_perk_2
        pass

    def onBrainKPTwoLVLTextChanged(self, text):
        print 'onBrainKPTwoLVLTextChanged', text
        self.meta_char.brain.key_perk_2_lvl = int(text)
        print self.meta_char.brain.key_perk_2_lvl
        pass

    def onBrainIntTextChanged(self, text):
        print 'onBrainIntTextChanged', text
        self.meta_char.brain.intelligence = int(text)
        self.update_all_brain_derived_fields()
        pass

    def onBrainRefTextChanged(self, text):
        print 'onBrainRefTextChanged', text
        self.meta_char.brain.reflex = int(text)
        self.update_all_brain_derived_fields()
        pass

    def onBrainTechTextChanged(self, text):
        print 'onBrainTechTextChanged', text
        self.meta_char.brain.technology = int(text)
        self.update_all_brain_derived_fields()
        pass

    def onBrainDexTextChanged(self, text):
        print 'onBrainDexTextChanged', text
        self.meta_char.brain.dexterity = int(text)
        self.update_all_brain_derived_fields()
        pass

    def onBrainCoolTextChanged(self, text):
        print 'onBrainCoolTextChanged', text
        self.meta_char.brain.cool = int(text)
        self.update_all_brain_derived_fields()
        pass

    def onBrainWillTextChanged(self, text):
        print 'onBrainWillTextChanged', text
        self.meta_char.brain.will= int(text)
        self.update_all_brain_derived_fields()
        pass

    def onBrainStrTextChanged(self, text):
        print 'onBrainStrTextChanged', text
        self.meta_char.brain.strength = int(text)
        self.update_all_brain_derived_fields()
        pass

    def onBrainConTextChanged(self, text):
        print 'onBrainConTextChanged', text
        self.meta_char.brain.constitution = int(text)
        self.update_all_brain_derived_fields()
        pass

    def onBrainMoveTextChanged(self, text):
        print 'onBrainMoveTextChanged', text
        self.meta_char.brain.move = int(text)
        self.update_all_brain_derived_fields()
        pass

    def onBrainBodyTextChanged(self, text):
        print 'onBrainBodyTextChanged', text
        self.meta_char.brain.body = int(text)
        self.update_all_brain_derived_fields()
        pass

    def update_all_brain_derived_fields(self):
        # key skills 
        self.lineEditBrainKSOne.setText(str(self.meta_char.brain.key_skill_1))
        self.lineEditBrainKSOneLVL.setText(str(self.meta_char.brain.key_skill_1_lvl))
        self.lineEditBrainKSTwo.setText(str(self.meta_char.brain.key_skill_2_lvl))
        self.lineEditBrainKSTwoLVL.setText(str(self.meta_char.brain.key_skill_2_lvl))
        self.lineEditBrainKPOne.setText(str(self.meta_char.brain.key_perk_1))
        self.lineEditBrainKPOneLVL.setText(str(self.meta_char.brain.key_perk_1_lvl))
        self.lineEditBrainKPTwo.setText(str(self.meta_char.brain.key_perk_2_lvl))
        self.lineEditBrainKPTwoLVL.setText(str(self.meta_char.brain.key_perk_2_lvl))

        #luck
        self.meta_char.brain.luck = self.meta_char.brain.intelligence + self.meta_char.brain.reflex / 2
        self.lineROBrainLuck.setText(str(self.meta_char.brain.luck))
        print str(self.meta_char.brain.luck)
        #humanity
        self.meta_char.brain.humanity = self.meta_char.brain.will * 10
        self.lineROBrainHum.setText(str(self.meta_char.brain.humanity))
        print str(self.meta_char.brain.humanity)
        #recovery
        self.meta_char.brain.recovery = self.meta_char.brain.strength + self.meta_char.brain.constitution / 2
        self.lineROBrainRec.setText(str(self.meta_char.brain.recovery))
        print str(self.meta_char.brain.recovery)
        #endurance
        self.meta_char.brain.endurance = self.meta_char.brain.constitution * 2
        self.lineROBrainEnd.setText(str(self.meta_char.brain.endurance))
        print str(self.meta_char.brain.endurance)
        #run
        self.meta_char.brain.run = self.meta_char.brain.move * 2
        self.lineROBrainRun.setText(str(self.meta_char.brain.run))
        print str(self.meta_char.brain.run)
        #sprint
        self.meta_char.brain.sprint = self.meta_char.brain.move * 3
        self.lineROBrainSpr.setText(str(self.meta_char.brain.sprint))
        print str(self.meta_char.brain.sprint)
        #swim
        self.meta_char.brain.swim = self.meta_char.brain.move
        self.lineROBrainSwim.setText(str(self.meta_char.brain.swim))
        print str(self.meta_char.brain.swim)
        #leap
        self.meta_char.brain.leap = self.meta_char.brain.move
        self.lineROBrainLeap.setText(str(self.meta_char.brain.leap))
        print str(self.meta_char.brain.leap)
        #hits
        self.meta_char.brain.hits = self.meta_char.brain.body * 2
        self.lineROBrainHits.setText(str(self.meta_char.brain.hits))
        print str(self.meta_char.brain.hits)
        #stun
        self.meta_char.brain.stun = self.meta_char.brain.body * 5
        self.lineROBrainStun.setText(str(self.meta_char.brain.stun))
        print str(self.meta_char.brain.stun)
        pass

    # right hand page related functions
    def onRHGoalsTextChanged(self):
        text = self.plainTextEditRHGoals.toPlainText()
        print 'onRHGoalsTextChanged', text
        self.meta_char.right_hand.goals = str(text)
        print self.meta_char.right_hand.goals
        pass
    def onRHLPTextChanged(self):
        text = self.plainTextEditRHLP.toPlainText()
        print 'onRHLPTextChanged', text
        self.meta_char.right_hand.lifepath = str(text)
        print self.meta_char.right_hand.lifepath
        pass
    def onRHKSOneTextChanged(self, text):
        print 'onRHKSOneTextChanged', text
        self.meta_char.right_hand.key_skill_1 = str(text)
        print self.meta_char.right_hand.key_skill_1
        pass

    def onRHKSOneLVLTextChanged(self, text):
        print 'onRHKSOneLVLTextChanged', text
        self.meta_char.right_hand.key_skill_1_lvl = int(text)
        print self.meta_char.right_hand.key_skill_1_lvl
        pass
    def onRHKSTwoTextChanged(self, text):
        print 'onRHKSTwoTextChanged', text
        self.meta_char.right_hand.key_skill_2 = str(text)
        print self.meta_char.right_hand.key_skill_2
        pass

    def onRHKSTwoLVLTextChanged(self, text):
        print 'onRHKSTwoLVLTextChanged', text
        self.meta_char.right_hand.key_skill_2_lvl = int(text)
        print self.meta_char.right_hand.key_skill_2_lvl
        pass
    def onRHKPOneTextChanged(self, text):
        print 'onRHKPOneTextChanged', text
        self.meta_char.right_hand.key_perk_1 = str(text)
        print self.meta_char.right_hand.key_perk_1
        pass

    def onRHKPOneLVLTextChanged(self, text):
        print 'onRHKPOneLVLTextChanged', text
        self.meta_char.right_hand.key_perk_1_lvl = int(text)
        print self.meta_char.right_hand.key_perk_1_lvl
        pass
    def onRHKPTwoTextChanged(self, text):
        print 'onRHKPTwoTextChanged', text
        self.meta_char.right_hand.key_perk_2 = str(text)
        print self.meta_char.right_hand.key_perk_2
        pass

    def onRHKPTwoLVLTextChanged(self, text):
        print 'onRHKPTwoLVLTextChanged', text
        self.meta_char.right_hand.key_perk_2_lvl = int(text)
        print self.meta_char.right_hand.key_perk_2_lvl
        pass
    def onRHIntTextChanged(self, text):
        print 'onRHIntTextChanged', text
        self.meta_char.right_hand.intelligence = int(text)
        self.update_all_right_hand_derived_fields()
        pass

    def onRHRefTextChanged(self, text):
        print 'onRHRefTextChanged', text
        self.meta_char.right_hand.reflex = int(text)
        self.update_all_right_hand_derived_fields()
        pass

    def onRHTechTextChanged(self, text):
        print 'onRHTechTextChanged', text
        self.meta_char.right_hand.technology = int(text)
        self.update_all_right_hand_derived_fields()
        pass

    def onRHDexTextChanged(self, text):
        print 'onRHDexTextChanged', text
        self.meta_char.right_hand.dexterity = int(text)
        self.update_all_right_hand_derived_fields()
        pass

    def onRHCoolTextChanged(self, text):
        print 'onRHCoolTextChanged', text
        self.meta_char.right_hand.cool = int(text)
        self.update_all_right_hand_derived_fields()
        pass

    def onRHWillTextChanged(self, text):
        print 'onRHWillTextChanged', text
        self.meta_char.right_hand.will= int(text)
        self.update_all_right_hand_derived_fields()
        pass

    def onRHStrTextChanged(self, text):
        print 'onRHStrTextChanged', text
        self.meta_char.right_hand.strength = int(text)
        self.update_all_right_hand_derived_fields()
        pass

    def onRHConTextChanged(self, text):
        print 'onRHConTextChanged', text
        self.meta_char.right_hand.constitution = int(text)
        self.update_all_right_hand_derived_fields()
        pass

    def onRHMoveTextChanged(self, text):
        print 'onRHMoveTextChanged', text
        self.meta_char.right_hand.move = int(text)
        self.update_all_right_hand_derived_fields()
        pass

    def onRHBodyTextChanged(self, text):
        print 'onRHBodyTextChanged', text
        self.meta_char.right_hand.body = int(text)
        self.update_all_right_hand_derived_fields()
        pass

    def update_all_right_hand_derived_fields(self):
        #luck
        self.meta_char.right_hand.luck = self.meta_char.right_hand.intelligence + self.meta_char.right_hand.reflex / 2
        self.lineRORHLuck.setText(str(self.meta_char.right_hand.luck))
        print str(self.meta_char.right_hand.luck)
        #humanity
        self.meta_char.right_hand.humanity = self.meta_char.right_hand.will * 10
        self.lineRORHHum.setText(str(self.meta_char.right_hand.humanity))
        print str(self.meta_char.right_hand.humanity)
        #recovery
        self.meta_char.right_hand.recovery = self.meta_char.right_hand.strength + self.meta_char.right_hand.constitution / 2
        self.lineRORHRec.setText(str(self.meta_char.right_hand.recovery))
        print str(self.meta_char.right_hand.recovery)
        #endurance
        self.meta_char.right_hand.endurance = self.meta_char.right_hand.constitution * 2
        self.lineRORHEnd.setText(str(self.meta_char.right_hand.endurance))
        print str(self.meta_char.right_hand.endurance)
        #run
        self.meta_char.right_hand.run = self.meta_char.right_hand.move * 2
        self.lineRORHRun.setText(str(self.meta_char.right_hand.run))
        print str(self.meta_char.right_hand.run)
        #sprint
        self.meta_char.right_hand.sprint = self.meta_char.right_hand.move * 3
        self.lineRORHSpr.setText(str(self.meta_char.right_hand.sprint))
        print str(self.meta_char.right_hand.sprint)
        #swim
        self.meta_char.right_hand.swim = self.meta_char.right_hand.move
        self.lineRORHSwim.setText(str(self.meta_char.right_hand.swim))
        print str(self.meta_char.right_hand.swim)
        #leap
        self.meta_char.right_hand.leap = self.meta_char.right_hand.move
        self.lineRORHLeap.setText(str(self.meta_char.right_hand.leap))
        print str(self.meta_char.right_hand.leap)
        #hits
        self.meta_char.right_hand.hits = self.meta_char.right_hand.body * 2
        self.lineRORHHits.setText(str(self.meta_char.right_hand.hits))
        print str(self.meta_char.right_hand.hits)
        #stun
        self.meta_char.right_hand.stun = self.meta_char.right_hand.body * 5
        self.lineRORHStun.setText(str(self.meta_char.right_hand.stun))
        print str(self.meta_char.right_hand.stun)
        pass

    # left hand page related functions
    def onLHGoalsTextChanged(self):
        text = self.plainTextEditLHGoals.toPlainText()
        print 'onLHGoalsTextChanged', text
        self.meta_char.left_hand.goals = str(text)
        print self.meta_char.left_hand.goals
        pass
    def onLHLPTextChanged(self):
        text = self.plainTextEditLHLP.toPlainText()
        print 'onLHLPTextChanged', text
        self.meta_char.left_hand.lifepath = str(text)
        print self.meta_char.left_hand.lifepath
        pass
    def onLHKSOneTextChanged(self, text):
        print 'onLHKSOneTextChanged', text
        self.meta_char.left_hand.key_skill_1 = str(text)
        print self.meta_char.left_hand.key_skill_1
        pass

    def onLHKSOneLVLTextChanged(self, text):
        print 'onLHKSOneLVLTextChanged', text
        self.meta_char.left_hand.key_skill_1_lvl = int(text)
        print self.meta_char.left_hand.key_skill_1_lvl
        pass
    def onLHKSTwoTextChanged(self, text):
        print 'onLHKSTwoTextChanged', text
        self.meta_char.left_hand.key_skill_2 = str(text)
        print self.meta_char.left_hand.key_skill_2
        pass

    def onLHKSTwoLVLTextChanged(self, text):
        print 'onLHKSTwoLVLTextChanged', text
        self.meta_char.left_hand.key_skill_2_lvl = int(text)
        print self.meta_char.left_hand.key_skill_2_lvl
        pass
    def onLHKPOneTextChanged(self, text):
        print 'onLHKPOneTextChanged', text
        self.meta_char.left_hand.key_perk_1 = str(text)
        print self.meta_char.left_hand.key_perk_1
        pass

    def onLHKPOneLVLTextChanged(self, text):
        print 'onLHKPOneLVLTextChanged', text
        self.meta_char.left_hand.key_perk_1_lvl = int(text)
        print self.meta_char.left_hand.key_perk_1_lvl
        pass
    def onLHKPTwoTextChanged(self, text):
        print 'onLHKPTwoTextChanged', text
        self.meta_char.left_hand.key_perk_2 = str(text)
        print self.meta_char.left_hand.key_perk_2
        pass

    def onLHKPTwoLVLTextChanged(self, text):
        print 'onLHKPTwoLVLTextChanged', text
        self.meta_char.left_hand.key_perk_2_lvl = int(text)
        print self.meta_char.left_hand.key_perk_2_lvl
        pass

    def onLHIntTextChanged(self, text):
        print 'onLHIntTextChanged', text
        self.meta_char.left_hand.intelligence = int(text)
        self.update_all_left_hand_derived_fields()
        pass

    def onLHRefTextChanged(self, text):
        print 'onLHRefTextChanged', text
        self.meta_char.left_hand.reflex = int(text)
        self.update_all_left_hand_derived_fields()
        pass

    def onLHTechTextChanged(self, text):
        print 'onLHTechTextChanged', text
        self.meta_char.left_hand.technology = int(text)
        self.update_all_left_hand_derived_fields()
        pass

    def onLHDexTextChanged(self, text):
        print 'onLHDexTextChanged', text
        self.meta_char.left_hand.dexterity = int(text)
        self.update_all_left_hand_derived_fields()
        pass

    def onLHCoolTextChanged(self, text):
        print 'onLHCoolTextChanged', text
        self.meta_char.left_hand.cool = int(text)
        self.update_all_left_hand_derived_fields()
        pass

    def onLHWillTextChanged(self, text):
        print 'onLHWillTextChanged', text
        self.meta_char.left_hand.will= int(text)
        self.update_all_left_hand_derived_fields()
        pass

    def onLHStrTextChanged(self, text):
        print 'onLHStrTextChanged', text
        self.meta_char.left_hand.strength = int(text)
        self.update_all_left_hand_derived_fields()
        pass

    def onLHConTextChanged(self, text):
        print 'onLHConTextChanged', text
        self.meta_char.left_hand.constitution = int(text)
        self.update_all_left_hand_derived_fields()
        pass

    def onLHMoveTextChanged(self, text):
        print 'onLHMoveTextChanged', text
        self.meta_char.left_hand.move = int(text)
        self.update_all_left_hand_derived_fields()
        pass

    def onLHBodyTextChanged(self, text):
        print 'onLHBodyTextChanged', text
        self.meta_char.left_hand.body = int(text)
        self.update_all_left_hand_derived_fields()
        pass

    def update_all_left_hand_derived_fields(self):
        #luck
        self.meta_char.left_hand.luck = self.meta_char.left_hand.intelligence + self.meta_char.left_hand.reflex / 2
        self.lineROLHLuck.setText(str(self.meta_char.left_hand.luck))
        print str(self.meta_char.left_hand.luck)
        #humanity
        self.meta_char.left_hand.humanity = self.meta_char.left_hand.will * 10
        self.lineROLHHum.setText(str(self.meta_char.left_hand.humanity))
        print str(self.meta_char.left_hand.humanity)
        #recovery
        self.meta_char.left_hand.recovery = self.meta_char.left_hand.strength + self.meta_char.left_hand.constitution / 2
        self.lineROLHRec.setText(str(self.meta_char.left_hand.recovery))
        print str(self.meta_char.left_hand.recovery)
        #endurance
        self.meta_char.left_hand.endurance = self.meta_char.left_hand.constitution * 2
        self.lineROLHEnd.setText(str(self.meta_char.left_hand.endurance))
        print str(self.meta_char.left_hand.endurance)
        #run
        self.meta_char.left_hand.run = self.meta_char.left_hand.move * 2
        self.lineROLHRun.setText(str(self.meta_char.left_hand.run))
        print str(self.meta_char.left_hand.run)
        #sprint
        self.meta_char.left_hand.sprint = self.meta_char.left_hand.move * 3
        self.lineROLHSpr.setText(str(self.meta_char.left_hand.sprint))
        print str(self.meta_char.left_hand.sprint)
        #swim
        self.meta_char.left_hand.swim = self.meta_char.left_hand.move
        self.lineROLHSwim.setText(str(self.meta_char.left_hand.swim))
        print str(self.meta_char.left_hand.swim)
        #leap
        self.meta_char.left_hand.leap = self.meta_char.left_hand.move
        self.lineROLHLeap.setText(str(self.meta_char.left_hand.leap))
        print str(self.meta_char.left_hand.leap)
        #hits
        self.meta_char.left_hand.hits = self.meta_char.left_hand.body * 2
        self.lineROLHHits.setText(str(self.meta_char.left_hand.hits))
        print str(self.meta_char.left_hand.hits)
        #stun
        self.meta_char.left_hand.stun = self.meta_char.left_hand.body * 5
        self.lineROLHStun.setText(str(self.meta_char.left_hand.stun))
        print str(self.meta_char.left_hand.stun)
        pass
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    MA = MainApp()
    MA.main()
    app.exec_()
