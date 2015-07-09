from PyQt4 import QtGui
from PyQt4.QtCore import *
import background_generator
import sys
from background import CharInfo, Roller

class MainApp(QtGui.QMainWindow, background_generator.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
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
    MA = MainApp()
    MA.main()
    app.exec_()
