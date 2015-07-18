from PyQt4 import QtGui
from PyQt4.QtCore import *
import bg_helper
import sys
from background import CharInfo, Roller

class BGHelper(QtGui.QDialog, bg_helper.Ui_Dialog):
    def __init__(self, parent=None):
        super(BGHelper, self).__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.roller = Roller()

    def generate(self):
        value = self.spinBoxAge.value()
        c = self.roller.roll_personality(value)
        text = c.return_me()
        self.plainTextEditResults.setPlainText(text)
    #main
    def main(self):
        self.show()

    # hooks up all the textfields / areas
    def init_ui(self):
        self.pushButtonGenerate.clicked.connect(self.generate)

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    MA = BGHelper()
    MA.main()
    app.exec_()
