import sys

import PyQt5 as Qt

import data_management
import interface

class Application:
    def __init__(self):
        self.__current_base = 'EUR'

    def set_main_window(self, window):
        self.__main_window = window

    def set_current_base(self, new_base):
        self.__current_base = str(new_base)
    
    def update_rates(self):
        try:
            rates = data_management.get_latest_exchange_rates(self.__current_base)
            self.__main_window.update_rates(rates['rates'], rates['base'])
        except Exception as err:
            self.__main_window.warn(err)
        
        

def main():
    qt_application = Qt.QtWidgets.QApplication(sys.argv)
    app = Application()
    window = interface.Gui(app)
    app.set_main_window(window)
    sys.exit(qt_application.exec_())

if __name__ == '__main__':
    main()