# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'marketer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_marketer_w(object):
    def setupUi(self, marketer_w):
        marketer_w.setObjectName("marketer_w")
        marketer_w.resize(784, 667)
        self.centralwidget = QtWidgets.QWidget(marketer_w)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.name_lb_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.name_lb_2.setFont(font)
        self.name_lb_2.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lb_2.setObjectName("name_lb_2")
        self.verticalLayout_4.addWidget(self.name_lb_2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_8.addWidget(self.tableWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.change_lb = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.change_lb.setFont(font)
        self.change_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.change_lb.setWordWrap(True)
        self.change_lb.setObjectName("change_lb")
        self.verticalLayout_2.addWidget(self.change_lb)
        self.change_btn = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.change_btn.setFont(font)
        self.change_btn.setObjectName("change_btn")
        self.verticalLayout_2.addWidget(self.change_btn)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.del_ln = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.del_ln.setFont(font)
        self.del_ln.setObjectName("del_ln")
        self.verticalLayout.addWidget(self.del_ln)
        self.del_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.del_btn.setObjectName("del_btn")
        self.verticalLayout.addWidget(self.del_btn)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.name_lb = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.name_lb.setFont(font)
        self.name_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lb.setObjectName("name_lb")
        self.verticalLayout_6.addWidget(self.name_lb)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.verticalLayout_6.addWidget(self.tableWidget_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.add_lb = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.add_lb.setFont(font)
        self.add_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.add_lb.setWordWrap(True)
        self.add_lb.setObjectName("add_lb")
        self.horizontalLayout_2.addWidget(self.add_lb)
        self.add_btn = QtWidgets.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.add_btn.setFont(font)
        self.add_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.add_btn.setAutoDefault(False)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_2.addWidget(self.add_btn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        marketer_w.setCentralWidget(self.centralwidget)

        self.retranslateUi(marketer_w)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(marketer_w)

    def retranslateUi(self, marketer_w):
        _translate = QtCore.QCoreApplication.translate
        marketer_w.setWindowTitle(_translate("marketer_w", "MainWindow"))
        self.name_lb_2.setText(_translate("marketer_w", "Блок управления услугами"))
        self.groupBox.setTitle(_translate("marketer_w", "Изменение"))
        self.change_lb.setText(_translate("marketer_w", "Выберети ячейку которую хотите изменить и нажмите кнопку "))
        self.change_btn.setText(_translate("marketer_w", "Изменить"))
        self.groupBox_3.setTitle(_translate("marketer_w", "Удаление"))
        self.del_ln.setPlaceholderText(_translate("marketer_w", "Введите id строки, которую хотите удалить"))
        self.del_btn.setText(_translate("marketer_w", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("marketer_w", "Изменение и удаление существующих заказов"))
        self.name_lb.setText(_translate("marketer_w", "Блок управления услугами"))
        self.add_lb.setText(_translate("marketer_w", "Добавьте новые значения в пустую строку  "))
        self.add_btn.setText(_translate("marketer_w", "Добавить в таблицу"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("marketer_w", "Добавление новых заказов"))
