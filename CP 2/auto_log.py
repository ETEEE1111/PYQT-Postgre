from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox

import psycopg2
import psycopg2.extras
import urllib.parse
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from config import *

import sys

from auto import *
from manager_log import *
from marketer_log import *
from comapny_log import *

STYLE = """
        QWidget{
            background: #314054;
        }
        QLabel{
            color: #fff;
        }
        QLabel#login, QLabel#password{
            border: 1px solid #fff;
            border-radius: 8px;
            padding: 2px;
        }
        QPushButton
        {
            color: white;
            background: #0577a8;
            border: 1px #DADADA solid;
            padding: 5px 10px;
            border-radius: 2px;
            font-weight: bold;
            font-size: 9pt;
            outline: none;
        }
        QPushButton:hover{
            border: 1px #C6C6C6 solid;
            color: #fff;
            background: #0892D0;
        }
        QLineEdit {
            padding: 1px;
            color: #fff;
            border-style: solid;
            border: 2px solid #fff;
            border-radius: 8px;
        }
        QRadioButton{
         color: #fff   
        }
    """

def connect_to_DB():
    urllib.parse.uses_netloc.append("postgres")
    url = urllib.parse.urlparse(databaseUrl)
    connection = psycopg2.connect(user=url.username,
                                  password=url.password,
                                  host=url.hostname,
                                  port=url.port,
                                  database=url.path[1:])
    return connection

class autoh(Ui_AutoWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_AutoWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Авторизация")
        self.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.setStyleSheet(STYLE)
        self.button_handler()
        self.w1 = company()
        self.w2 = logic()
        self.w3 = marketer()
        
    def button_handler(self):
        self.radioButton.clicked.connect(self.echo_mode_off)
        self.authorisation.clicked.connect(self.authorisat)
        self.pushButton.clicked.connect(self.quit)
            
    def echo_mode_off(self):
        if(not self.radioButton.isChecked()):
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        else:    
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
    
    def authorisat(self):
        try:
            connection = connect_to_DB()
            connection.autocommit = True
            cursor = connection.cursor()
            getLevelOfAccess = f"""SELECT level_of_access
                                   FROM authorisation
                                   WHERE login = '{self.login.text()}' AND password = '{self.password.text()}'"""
            cursor.execute(getLevelOfAccess)
            LevelOfAccess = cursor.fetchall()
        except (Exception, Error) as error:
            return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
        finally:
            if connection:
                cursor.close()
                connection.close()
                if(len(LevelOfAccess) == 0):
                   return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
                if(LevelOfAccess[0][0] == 1):
                    self.w1.show()
                    self.close()
                if(LevelOfAccess[0][0] == 2):
                    self.w2.show()
                    self.close()
                if(LevelOfAccess[0][0] == 3):
                    self.w3.show()
                    self.close()
    
    def quit(self):
        self.close()         

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mwindow = autoh()
    mwindow.show()
    sys.exit(app.exec())