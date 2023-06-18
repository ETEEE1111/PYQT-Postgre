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

import pandas as pd

import easygui

from company import *

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
        QComboBox{
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

class company(Ui_Comapany,QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Comapany,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Блок управления компанией")
        self.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.setStyleSheet(STYLE)
        self.comboBox.addItem("Менеджер")
        self.comboBox.addItem("Маркетолог")
        self.comboBox.addItem("Инструктор")
        self.col = []
        self.table = []
        self.types = []
        self.button_handller()
        self.update_table_inf()
        self.get_table_inf(name='polygon')
        self.draw_table_polygon()
        self.get_table_inf(name='type')
        self.draw_table_type()
        self.get_table_inf(name="authorisation")
        self.draw_table_auto()
        
    def button_handller(self):
        self.comboBox.currentTextChanged.connect(self.update_table_inf)
        self.pushButton_6.clicked.connect(self.del_for_emp)
        self.pushButton_5.clicked.connect(self.update_for_emp)
        self.pushButton_7.clicked.connect(self.add_for_emp)
        self.pushButton_9.clicked.connect(self.del_for_polygon)
        self.pushButton_8.clicked.connect(self.update_for_polygon)
        self.pushButton_10.clicked.connect(self.add_for_polygon)
        self.pushButton_14.clicked.connect(self.update_for_type)
        self.pushButton_15.clicked.connect(self.del_for_type)
        self.pushButton_16.clicked.connect(self.add_for_type)
        self.pushButton_17.clicked.connect(self.update_for_auto)
        self.pushButton_18.clicked.connect(self.del_for_auto)
        self.pushButton_19.clicked.connect(self.add_for_auto)
        self.pushButton_3.clicked.connect(self.report_polygon)
        self.pushButton_2.clicked.connect(self.report_type)
        self.pushButton.clicked.connect(self.report_autohorisation)
    
    def get_table_inf(self, name):
        try:
            connection = connect_to_DB()
            connection.autocommit = True
            cursor = connection.cursor()
            getTablesColumnNames = f'''SELECT column_name FROM information_schema.columns WHERE table_name = '{name}' AND table_schema = 'public' '''
            cursor.execute(getTablesColumnNames)
            self.col = cursor.fetchall()

            getTableItems = f'''SELECT * FROM {name} ORDER BY {name}_id'''
            cursor.execute(getTableItems)
            self.table = cursor.fetchall()
        except (Exception, Error) as error:
            pass

        finally:
            if connection:
                cursor.close()
                connection.close()
                
    def update_table_inf(self):
        if(self.comboBox.currentText() == "Менеджер"):
            self.get_table_inf(name = "manager")
        if(self.comboBox.currentText() == "Маркетолог"):
            self.get_table_inf(name = "marketer")
        if(self.comboBox.currentText() == "Инструктор"):
            self.get_table_inf(name = "instructor")
        
        self.tableWidget_3.clear()
        fixcol = []
        for elem in self.col:
            fixcol.append(elem[0])
        
        self.tableWidget_3.setColumnCount(len(fixcol))
        self.tableWidget_3.setHorizontalHeaderLabels(fixcol)
        if (len(self.table) != 0):
            self.tableWidget_3.setRowCount(len(self.table) + 1)
            for i in range(len(self.table)):
                for j in range(len(self.table[i])):
                    self.tableWidget_3.setItem(i, j, QTableWidgetItem(f"{self.table[i][j]}"))
            self.tableWidget_3.setItem(len(self.table), 0, QTableWidgetItem(f"{int(self.tableWidget_3.item(len(self.table) - 1, 0).text()) + 1}"))
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
    def del_for_emp(self):
        if(self.comboBox.currentText() == "Менеджер"):
            try:
                connection = connect_to_DB()
                connection.autocommit = True
                cursor = connection.cursor()
                DeleteRequest = f'''DELETE FROM manager where manager_id = {int(self.lineEdit.text())}'''
                cursor.execute(DeleteRequest)
            except (Exception, Error) as error:
                return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    self.update_table_inf()
                    self.lineEdit.setText("")
        
        if(self.comboBox.currentText() == "Маркетолог"):
            try:
                connection = connect_to_DB()
                connection.autocommit = True
                cursor = connection.cursor()
                DeleteRequest = f'''DELETE FROM marketer where marketer_id = {int(self.lineEdit.text())}'''
                cursor.execute(DeleteRequest)
            except (Exception, Error) as error:
                return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    self.update_table_inf()
                    self.lineEdit.setText("")
                    
        if(self.comboBox.currentText() == "Инструктор"):
            try:
                connection = connect_to_DB()
                connection.autocommit = True
                cursor = connection.cursor()
                DeleteRequest = f'''DELETE FROM instructor where instructor_id = {int(self.lineEdit.text())}'''
                cursor.execute(DeleteRequest)
            except (Exception, Error) as error:
                return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    self.update_table_inf()
                    self.lineEdit.setText("")
                    
    def update_for_emp(self):
        if(self.comboBox.currentText() == "Менеджер"):
            try:
                connection = connect_to_DB()
                connection.autocommit = True
                cursor = connection.cursor()
                columnName = self.tableWidget_3.horizontalHeaderItem(self.tableWidget_3.currentColumn()).text()
                changedValue = self.tableWidget_3.currentIndex().data()
                elementCode = self.tableWidget_3.item(self.tableWidget_3.currentRow(),0).text()
                UpdateRequest = f'''UPDATE manager SET {columnName} = '{changedValue}' WHERE manager_id = {elementCode} '''
                cursor.execute(UpdateRequest)
            except (Exception, Error) as error:
                return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    self.update_table_inf()
                    
        if(self.comboBox.currentText() == "Маркетолог"):     
            try:
                connection = connect_to_DB()
                connection.autocommit = True
                cursor = connection.cursor()
                columnName = self.tableWidget_3.horizontalHeaderItem(self.tableWidget_3.currentColumn()).text()
                changedValue = self.tableWidget_3.currentIndex().data()
                elementCode = self.tableWidget_3.item(self.tableWidget_3.currentRow(),0).text()
                UpdateRequest = f'''UPDATE marketer SET {columnName} = '{changedValue}' WHERE marketer_id = {elementCode} '''
                cursor.execute(UpdateRequest)
            except (Exception, Error) as error:
                return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    self.update_table_inf()
                
        if(self.comboBox.currentText() == "Инструктор"):
            try:
                connection = connect_to_DB()
                connection.autocommit = True
                cursor = connection.cursor()
                columnName = self.tableWidget_3.horizontalHeaderItem(self.tableWidget_3.currentColumn()).text()
                changedValue = self.tableWidget_3.currentIndex().data()
                elementCode = self.tableWidget_3.item(self.tableWidget_3.currentRow(),0).text()
                UpdateRequest = f'''UPDATE instructor SET {columnName} = '{changedValue}' WHERE instructor_id = {elementCode} '''
                cursor.execute(UpdateRequest)
            except (Exception, Error) as error:
                return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    self.update_table_inf()
                    
    def add_for_emp(self):
        if(self.comboBox.currentText() == "Менеджер"):
            try:
                connection = connect_to_DB()
                connection.autocommit = True
                cursor = connection.cursor()
                columnValues = []
                for i in range(1, self.tableWidget_3.columnCount()):
                    columnValues.append(self.tableWidget_3.item(self.tableWidget_3.rowCount() - 1, i).text())
                print(columnValues)
                addRequest = f'''INSERT INTO manager (company_id, fullname_manager, date_of_birth, phone_number)
                                VALUES ({int(columnValues[0])}, '{columnValues[1]}', '{columnValues[2]}', '{columnValues[3]}')  '''
                cursor.execute(addRequest)
            except (Exception, Error) as error:
                return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    self.update_table_inf()
        
        if(self.comboBox.currentText() == "Маркетолог"):
            try:
                connection = connect_to_DB()
                connection.autocommit = True
                cursor = connection.cursor()
                columnValues = []
                for i in range(1, self.tableWidget_3.columnCount()):
                    columnValues.append(self.tableWidget_3.item(self.tableWidget_3.rowCount() - 1, i).text())
                addRequest = f'''INSERT INTO marketer (company_id, fullname_marketer, phone_number, date_of_birth)
                                VALUES ({int(columnValues[0])}, '{columnValues[1]}', '{columnValues[2]}', '{columnValues[3]}')  '''
                cursor.execute(addRequest)
            except (Exception, Error) as error:
                return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    self.update_table_inf()
            
        if(self.comboBox.currentText() == "Инструктор"):
            try:
                connection = connect_to_DB()
                connection.autocommit = True
                cursor = connection.cursor()
                columnValues = []
                for i in range(1, self.tableWidget_3.columnCount()):
                    columnValues.append(self.tableWidget_3.item(self.tableWidget_3.rowCount() - 1, i).text())
                addRequest = f'''INSERT INTO instructor (company_id, fullname_instructor, date_of_birth, phone_number, experience)
                                VALUES ({int(columnValues[0])}, '{columnValues[1]}', '{columnValues[2]}', '{columnValues[3]}', {int(columnValues[4])})  '''
                cursor.execute(addRequest)
            except (Exception, Error) as error:
                return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    self.update_table_inf()
    
    
    def draw_table_polygon(self):
        self.tableWidget_4.clear()
        fixcol = []
        for elem in self.col:
            fixcol.append(elem[0])
        
        self.tableWidget_4.setColumnCount(len(fixcol))
        self.tableWidget_4.setHorizontalHeaderLabels(fixcol)
        
        if (len(self.table) != 0):
            self.tableWidget_4.setRowCount(len(self.table) + 1)
            for i in range(len(self.table)):
                for j in range(len(self.table[i])):
                    self.tableWidget_4.setItem(i, j, QTableWidgetItem(f"{self.table[i][j]}"))
            self.tableWidget_4.setItem(len(self.table), 0, QTableWidgetItem(f"{int(self.tableWidget_4.item(len(self.table) - 1, 0).text()) + 1}"))
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def del_for_polygon(self):
        try:
            connection = connect_to_DB()
            connection.autocommit = True
            cursor = connection.cursor()
            DeleteRequest = f'''DELETE FROM polygon where polygon_id = {int(self.lineEdit_2.text())}'''
            cursor.execute(DeleteRequest)
        except (Exception, Error) as error:
            return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
        finally:
            if connection:
                cursor.close()
                connection.close()
                self.get_table_inf(name="polygon")
                self.draw_table_polygon()
                self.lineEdit_2.setText("")
                
                
    def update_for_polygon(self):
        try:
            connection = connect_to_DB()
            connection.autocommit = True
            cursor = connection.cursor()
            columnName = self.tableWidget_4.horizontalHeaderItem(self.tableWidget_4.currentColumn()).text()
            changedValue = self.tableWidget_4.currentIndex().data()
            elementCode = self.tableWidget_4.item(self.tableWidget_4.currentRow(),0).text()
            UpdateRequest = f'''UPDATE polygon 
                                SET {columnName} = '{changedValue}' 
                                WHERE polygon_id = {elementCode} '''
            cursor.execute(UpdateRequest)
        except (Exception, Error) as error:
            return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
        finally:
            if connection:
                cursor.close()
                connection.close()
                self.get_table_inf(name="polygon")
                self.draw_table_polygon()
    
    def add_for_polygon(self):
        try:
            connection = connect_to_DB()
            connection.autocommit = True
            cursor = connection.cursor()
            columnValues = []
            for i in range(1, self.tableWidget_4.columnCount()):
               columnValues.append(self.tableWidget_4.item(self.tableWidget_4.rowCount() - 1, i).text())
            addRequest = f'''INSERT INTO polygon (company_id, name_polygon)
                             VALUES ({int(columnValues[0])}, '{columnValues[1]}' )  '''
            cursor.execute(addRequest)
        except (Exception, Error) as error:
            return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
        finally:
            if connection:
                cursor.close()
                connection.close()
                self.get_table_inf(name="polygon")
                self.draw_table_polygon()
    
    
    def draw_table_type(self):
        self.tableWidget_5.clear()
        fixcol = []
        for elem in self.col:
            fixcol.append(elem[0])
        
        self.tableWidget_5.setColumnCount(len(fixcol))
        self.tableWidget_5.setHorizontalHeaderLabels(fixcol)
        
        if (len(self.table) != 0):
            self.tableWidget_5.setRowCount(len(self.table) + 1)
            for i in range(len(self.table)):
                for j in range(len(self.table[i])):
                    self.tableWidget_5.setItem(i, j, QTableWidgetItem(f"{self.table[i][j]}"))
            self.tableWidget_5.setItem(len(self.table), 0, QTableWidgetItem(f"{int(self.tableWidget_5.item(len(self.table) - 1, 0).text()) + 1}"))
        self.tableWidget_5.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def del_for_type(self):
        try:
            connection = connect_to_DB()
            connection.autocommit = True
            cursor = connection.cursor()
            DeleteRequest = f'''DELETE FROM type where type_id = {int(self.lineEdit_5.text())}'''
            cursor.execute(DeleteRequest)
        except (Exception, Error) as error:
            return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
        finally:
            if connection:
                cursor.close()
                connection.close()
                self.get_table_inf(name="type")
                self.draw_table_type()
                self.lineEdit_5.setText("")
                
                
    def update_for_type(self):
        try:
            connection = connect_to_DB()
            connection.autocommit = True
            cursor = connection.cursor()
            columnName = self.tableWidget_5.horizontalHeaderItem(self.tableWidget_5.currentColumn()).text()
            changedValue = self.tableWidget_5.currentIndex().data()
            elementCode = self.tableWidget_5.item(self.tableWidget_5.currentRow(),0).text()
            UpdateRequest = f'''UPDATE type 
                                SET {columnName} = '{changedValue}' 
                                WHERE type_id = {elementCode} '''
            cursor.execute(UpdateRequest)
        except (Exception, Error) as error:
            return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
        finally:
            if connection:
                cursor.close()
                connection.close()
                self.get_table_inf(name="type")
                self.draw_table_type()
    
    def add_for_type(self):
        try:
            connection = connect_to_DB()
            connection.autocommit = True
            cursor = connection.cursor()
            columnValues = []
            for i in range(1, self.tableWidget_5.columnCount()):
               columnValues.append(self.tableWidget_5.item(self.tableWidget_5.rowCount() - 1, i).text())
            addRequest = f'''INSERT INTO type (type_name)
                             VALUES ('{columnValues[0]}')  '''
            cursor.execute(addRequest)
        except (Exception, Error) as error:
            return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
        finally:
            if connection:
                cursor.close()
                connection.close()
                self.get_table_inf(name="type")
                self.draw_table_type()
    
    
    def draw_table_auto(self):
        self.tableWidget_6.clear()
        fixcol = []
        for elem in self.col:
            fixcol.append(elem[0])
        
        self.tableWidget_6.setColumnCount(len(fixcol))
        self.tableWidget_6.setHorizontalHeaderLabels(fixcol)
        
        if (len(self.table) != 0):
            self.tableWidget_6.setRowCount(len(self.table) + 1)
            for i in range(len(self.table)):
                for j in range(len(self.table[i])):
                    self.tableWidget_6.setItem(i, j, QTableWidgetItem(f"{self.table[i][j]}"))
            self.tableWidget_6.setItem(len(self.table), 0, QTableWidgetItem(f"{int(self.tableWidget_6.item(len(self.table) - 1, 0).text()) + 1}"))
        self.tableWidget_6.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def del_for_auto(self):
        try:
            connection = connect_to_DB()
            connection.autocommit = True
            cursor = connection.cursor()
            DeleteRequest = f'''DELETE FROM authorisation where authorisation_id = {int(self.lineEdit_7.text())}'''
            cursor.execute(DeleteRequest)
        except (Exception, Error) as error:
            return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
        finally:
            if connection:
                cursor.close()
                connection.close()
                self.get_table_inf(name="authorisation")
                self.draw_table_auto()
                self.lineEdit_7.setText("")
                
                
    def update_for_auto(self):
        try:
            connection = connect_to_DB()
            connection.autocommit = True
            cursor = connection.cursor()
            columnName = self.tableWidget_6.horizontalHeaderItem(self.tableWidget_6.currentColumn()).text()
            changedValue = self.tableWidget_6.currentIndex().data()
            elementCode = self.tableWidget_6.item(self.tableWidget_6.currentRow(),0).text()
            UpdateRequest = f'''UPDATE authorisation 
                                SET {columnName} = '{changedValue}' 
                                WHERE authorisation_id = {elementCode} '''
            cursor.execute(UpdateRequest)
        except (Exception, Error) as error:
            return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
        finally:
            if connection:
                cursor.close()
                connection.close()
                self.get_table_inf(name="authorisation")
                self.draw_table_auto()
    
    def add_for_auto(self):
        try:
            connection = connect_to_DB()
            connection.autocommit = True
            cursor = connection.cursor()
            columnValues = []
            for i in range(1, self.tableWidget_6.columnCount()):
               columnValues.append(self.tableWidget_6.item(self.tableWidget_6.rowCount() - 1, i).text())
            addRequest = f'''INSERT INTO authorisation (login, password, level_of_access)
                             VALUES ('{columnValues[0]}', '{columnValues[1]}', {int(columnValues[2])})  '''
            cursor.execute(addRequest)
        except (Exception, Error) as error:
            return QMessageBox.critical(self, "Ошибка ", f"Неправильно введены данные!", QMessageBox.Ok)
        finally:
            if connection:
                cursor.close()
                connection.close()
                self.get_table_inf(name="authorisation")
                self.draw_table_auto()            
    def report_polygon(self):
        connection = connect_to_DB()        
        df = pd.read_sql('select * from polygon', connection)
        df = df.drop(columns = 'polygon_id')
        df = df.drop(columns = 'company_id')
        dir =  easygui.diropenbox()
        name = '\polygon_report.xlsx'
        df.to_excel(dir+name)
    
    def report_type(self):
        connection = connect_to_DB()        
        df = pd.read_sql('select * from type', connection)
        df = df.drop(columns = 'type_id')
        dir =  easygui.diropenbox()
        name = '\\type_report.xlsx'
        df.to_excel(dir+name)
    
    def report_autohorisation(self):
        connection = connect_to_DB()        
        df = pd.read_sql('select * from authorisation', connection)
        df = df.drop(columns = 'authorisation_id')
        dir =  easygui.diropenbox()
        name = '\\autohorisation_report.xlsx'
        df.to_excel(dir+name)
