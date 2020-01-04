import sys

import PyQt5 as Qt

import data_management
import interface

def main():
    application = Qt.QtWidgets.QApplication(sys.argv)
    main_window = interface.Gui()
    sys.exit(application.exec_())

if __name__ == '__main__':
    main()