from PyQt5.QtWidgets import *

import data_management

class Gui(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app

        self.resize(600,240)
        self.center()
        self.setWindowTitle("Foreign Exchange Rates")
        #self.setWindowIcon(QIcon("FER.png"))

        self.button_update = QPushButton(self)
        self.button_update.setText('Update rates')
        self.button_update.setToolTip("Push to pull the latest<i> exchange rates</i>.")
        self.button_update.resize(self.button_update.sizeHint())
        self.button_update.move(25,25)
        self.button_update.clicked.connect(app.update_rates)

        self.label_rates = QTextEdit(self)
        self.label_rates.move(125,26)
        self.label_rates.setStyleSheet("font-size: 16px")
        self.label_rates.setText('Val 1 = Val 2')
        self.label_rates.resize(450, 200)

        self.base_choice_widget = QComboBox(self)
        self.base_choice_widget.insertItem(1,'EUR')
        self.base_choice_widget.insertItem(2,'USD')
        self.base_choice_widget.insertItem(3,'PLN')
        self.base_choice_widget.resize(self.base_choice_widget.sizeHint())
        self.base_choice_widget.move(25, 65)
        self.base_choice_widget.currentIndexChanged.connect(self.send_new_base)

        self.show()

    def update_rates(self, new_rates, base):
        all_rates = list()
        for key in new_rates.keys():
            if key != base:
                all_rates.append("{}={} {}\n".format(key,new_rates[key],base))
        all_rates.sort()
        new_text = str()
        for l in all_rates:
            new_text += l
        self.label_rates.setText(new_text)

    def send_new_base(self):
        self.app.set_current_base(self.base_choice_widget.currentText())

    def center(self):
        geometry_of_window = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        geometry_of_window.moveCenter(screen_center)
        self.move(geometry_of_window.topLeft())

    def warn(self, error):
        message = "Sorry, some problem occured:\n {}".format(error)
        warning_window = QMessageBox()
        warning_window.setText(message)
        warning_window.exec_()
