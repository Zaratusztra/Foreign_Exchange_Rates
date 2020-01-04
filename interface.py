from PyQt5.QtWidgets import *

class Gui(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(400,220)
        self.center()
        self.setWindowTitle("Foreign Exchange Rates")
        #self.setWindowIcon(QIcon("FER.png"))

        self.button_update = QPushButton('Update rates', self)
        self.button_update.setToolTip("Push to pull the latest<i> exchange rates</i>.")
        self.button_update.resize(self.button_update.sizeHint())
        self.button_update.move(25,25)
        self.button_update.clicked.connect(self.update_rates)

        self.show()

    def update_rates(self):
        print("test")

    def center(self):
        geometry_of_window = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        geometry_of_window.moveCenter(screen_center)
        self.move(geometry_of_window.topLeft())

    # def closeEvent(self, event): # Inherited method
    #     reply = QMessageBox.question(self, \
    #         'Quit application?', 'Are you sure, you want to quit?'\
    #         , QMessageBox.Yes|QMessageBox.No, QMessageBox.No) # Button to appear and default button.
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()
