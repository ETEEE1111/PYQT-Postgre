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

from marketer import *

STYLE = """
        QWidget{
            background: #314054;
        }
        QLabel{
            color: #fff;
            border: 1px solid #fff;
            border-radius: 8px;
            padding: 2px;
        }
        QPushButton
        {
            color: white;
            background: #0577a8;
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
        QTableWidget{
            color: #fff;
            background-color: #50698a;
            gridline-color: #fff;
        }
        QGroupBox:title{
            color: white;
            subcontrol-origin: margin;
            subcontrol-position: top center;
            padding-left: 10px;
            padding-right: 10px; 
        }
        QTabWidget:pane {
            border: 1px solid #000;
        }
        QTabBar::tab {
            background:#314054 ; 
            border: 1px solid #000; 
            padding: 15px;  
            color: #fff
        } 
        QTabBar::tab:selected { 
            background: #fff; 
            margin-bottom: -1px; 
            color: #000
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

class marketer(Ui_marketer_w,QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_marketer_w,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Блок управления услугами")
        self.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.setStyleSheet(STYLE)
        self.col = []
        self.table = []
        self.get_table_inf()
        self.draw_table_wedgets()
        self.buttonhandler()
        
    def buttonhandler(self):
        self.del_btn.clicked.connect(self.delete)
        self.change_btn.clicked.connect(self.update)
        self.add_btn.clicked.connect(self.add)
    
    def get_table_inf(self):
        try:
            connection = connect_to_DB()
            connection.autocommit = True
            cursor = connection.cursor()
            getTablesColumnNames = f'''SELECT column_name FROM information_schema.columns WHERE table_name = 'services' AND table_schema = 'public' '''
            cursor.execute(getTablesColumnNames)
            self.col = cursor.fetchall()

            getTableItems = f'''SELECT * FROM services ORDER BY services_id'''
            cursor.execute(getTableItems)
            self.table = cursor.fetchall()
        except (Exception, Error) as error:
            pass

        finally:
            if connection:
                cursor.close()
                connection.close()
                
    
    def draw_table_wedgets(self):
        self.tableWidget.clear()
        self.tableWidget_2.clear()
        fixcol = []
        for elem in self.col:
            fixcol.append(elem[0])
        
        if (len(self.table) == 0):
            self.tableWidget.setRowCount(0)
        
        self.tableWidget.setColumnCount(len(fixcol))
        self.tableWidget.setHorizontalHeaderLabels(fixcol)
        self.tableWidget_2.setColumnCount(len(fixcol))
        self.tableWidget_2.setHorizontalHeaderLabels(fixcol)
        
        if (len(self.table) != 0):
            self.tableWidget.setRowCount(len(self.table) + 1)
            self.tableWidget_2.setRowCount(len(self.table) + 1)
            for i in range(len(self.table)):
                for j in range(len(self.table[i])):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(f"{self.table[i][j]}"))
                    self.tableWidget_2.setItem(i, j, QTableWidgetItem(f"{self.table[i][j]}"))
            self.tableWidget.setItem(len(self.table), 0, QTableWidgetItem(f"{int(self.tableWidget.item(len(self.table) - 1, 0).text()) + 1}"))
            self.tableWidget_2.setItem(len(self.table), 0, QTableWidgetItem(f"{int(self.tableWidget.item(len(self.table) - 1, 0).text()) + 1}"))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def delete(self):
        try:
            connection = connect_to_DB()
            connection.autocommit = True
            cursor = connection.cursor()
            DeleteRequest = f'''DELETE FROM services where services_id = {int(self.del_ln.text())}'''
            cursor.execute(DeleteRequest)
        except (Exception, Error) as error:
            return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
        finally:
            if connection:
                cursor.close()
                connection.close()
                self.get_table_inf()
                self.draw_table_wedgets()
                
                
    def update(self):
        try:
            connection = connect_to_DB()
            connection.autocommit = True
            cursor = connection.cursor()
            columnName = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentColumn()).text()
            changedValue = self.tableWidget.currentIndex().data()
            elementCode = self.tableWidget.item(self.tableWidget.currentRow(),0).text()
            UpdateRequest = f'''UPDATE services SET {columnName} = '{changedValue}' WHERE services_id = {elementCode} '''
            cursor.execute(UpdateRequest)
        except (Exception, Error) as error:
            return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
        finally:
            if connection:
                cursor.close()
                connection.close()
                self.get_table_inf()
                self.draw_table_wedgets()
    
    def add(self):
        try:
            connection = connect_to_DB()
            connection.autocommit = True
            cursor = connection.cursor()
            columnValues = []
            for i in range(1, self.tableWidget_2.columnCount()):
               columnValues.append(self.tableWidget_2.item(self.tableWidget_2.rowCount() - 1, i).text())
            addRequest = f'''INSERT INTO services (company_id, polygon_id, equipment_id, name_of_services, price)
                             VALUES ({int(columnValues[0])}, {int(columnValues[1])}, {int(columnValues[2])}, '{columnValues[3]}', '{int(columnValues[4])}')  '''
            cursor.execute(addRequest)
        except (Exception, Error) as error:
            return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
        finally:
            if connection:
                cursor.close()
                connection.close()
                self.get_table_inf()
                self.draw_table_wedgets()