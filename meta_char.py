from PyQt4 import QtGui
from PyQt4.QtCore import *
import sys
from pprint import pprint
import meta_char_window
from classes import MetaChar, Brain

class MainApp(QtGui.QMainWindow, meta_char_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.meta_char = MetaChar()
        self.lineEditInt.textChanged.connect(self.onIntTextChanged)
        self.lineEditRef.textChanged.connect(self.onRefTextChanged)
    def main(self):
        self.show()

    def onRefTextChanged(self, text):
        print 'onRefTextChanged', text
        self.meta_char.brain.reflex = int(text)
        self.meta_char.brain.luck = self.meta_char.brain.intelligence + self.meta_char.brain.reflex / 2
        print dir(self.lineROLuck)
        self.lineROLuck.setText(str(self.meta_char.brain.luck))
        print str(self.meta_char.brain.luck)
        pass

    def onIntTextChanged(self, text):
        print 'onIntTextChanged', text
        self.meta_char.brain.intelligence = int(text)
        print dir(text)
        self.meta_char.brain.luck = self.meta_char.brain.intelligence + self.meta_char.brain.reflex / 2
        print str(self.meta_char.brain.luck)
        pass

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    MA = MainApp()
    MA.main()
    app.exec_()
