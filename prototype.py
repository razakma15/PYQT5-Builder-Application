# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototype.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import newest_images

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os
import requests
from bs4 import BeautifulSoup
from multiprocessing import Process, Queue, Pool, Manager
import threading

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "stock_prices.db")
connect = sqlite3.connect(db_path)
c = connect.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        # Central Widget Where all widgets are instantated on
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        # Parent Tab Of All Children Tabs
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"border-color:green;")
        self.tabWidget.setObjectName("tabWidget")

# TAB ONE

        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("border-color:green;\n"
"border-width:3px;\n"
"border-style:solid;")
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.main_image = QtWidgets.QLabel(self.tab)
        self.main_image.setStyleSheet("border-color:black;\n"
"border-width:4px;")
        self.main_image.setPixmap(QtGui.QPixmap(":/Concrete_blocks/concrete_block.jpg"))
        self.main_image.setScaledContents(True)
        self.main_image.setObjectName("main_image")
        self.gridLayout_4.addWidget(self.main_image, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.main_title = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.main_title.setFont(font)
        self.main_title.setStyleSheet("border-color:white;")
        self.main_title.setAlignment(QtCore.Qt.AlignCenter)
        self.main_title.setObjectName("main_title")
        self.gridLayout_2.addWidget(self.main_title, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(30, 10, 10, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")

# BUTTON ON MAIN SCREEN FOR PRICE SEARCH

        self.main_price_button = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_price_button.sizePolicy().hasHeightForWidth())
        self.main_price_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.main_price_button.setFont(font)
        self.main_price_button.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(204, 204, 204);")
        self.main_price_button.setObjectName("main_price_button")
        self.main_price_button.clicked.connect(lambda:self.tab_change(1))
        self.gridLayout_5.addWidget(self.main_price_button, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_5.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_5.addItem(spacerItem1, 5, 0, 1, 1)

# BUTTON ON MAIN SCREEN FOR COMPARISON SEARCH

        self.main_comparison_button = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_comparison_button.sizePolicy().hasHeightForWidth())
        self.main_comparison_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.main_comparison_button.setFont(font)
        self.main_comparison_button.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(204, 204, 204);")
        self.main_comparison_button.setObjectName("main_comparison_button")
        self.main_comparison_button.clicked.connect(lambda:self.tab_change(2))
        self.gridLayout_5.addWidget(self.main_comparison_button, 2, 0, 1, 1)
        self.main_tool_button = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

# BUTTON ON MAIN SCREEN FOR TOOL LOANING

        sizePolicy.setHeightForWidth(self.main_tool_button.sizePolicy().hasHeightForWidth())
        self.main_tool_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.main_tool_button.setFont(font)
        self.main_tool_button.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(204, 204, 204);")
        self.main_tool_button.setObjectName("main_tool_button")
        self.main_tool_button.clicked.connect(lambda:self.tab_change(3))
        self.gridLayout_5.addWidget(self.main_tool_button, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_5.addItem(spacerItem2, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 1, 2, 1, 1)

# TAB TWO

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem3, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem4, 1, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem5 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem5, 1, 0, 1, 1)
        self.price_image = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price_image.sizePolicy().hasHeightForWidth())
        self.price_image.setSizePolicy(sizePolicy)
        self.price_image.setMaximumSize(QtCore.QSize(16777215, 300))
        self.price_image.setStyleSheet("")
        self.price_image.setText("")
        self.price_image.setPixmap(QtGui.QPixmap(":/Concrete_blocks/search.png"))
        self.price_image.setStyleSheet("border-width:0px;")
        self.price_image.setScaledContents(True)
        self.price_image.setObjectName("price_image")
        self.gridLayout_11.addWidget(self.price_image, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem6, 1, 2, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_11, 4, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem7, 0, 0, 1, 1)
        self.price_search_button = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price_search_button.sizePolicy().hasHeightForWidth())
        self.price_search_button.setSizePolicy(sizePolicy)
        self.price_search_button.setMinimumSize(QtCore.QSize(150, 0))
        self.price_search_button.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.price_search_button.setFont(font)
        self.price_search_button.setStyleSheet("border-width:2px;\n"
"background-color: rgb(203, 203, 203);\n"
"padding:10px;\n"
"border-radius:5px;")
        self.price_search_button.setCheckable(True)
        self.price_search_button.setObjectName("price_search_button")
        self.price_search_button.clicked.connect(self.price_query_display)
        self.gridLayout_8.addWidget(self.price_search_button, 0, 5, 1, 1)

        self.stock_modal_button = QtWidgets.QPushButton(self.tab_2)
        sizePolicy.setHeightForWidth(self.stock_modal_button.sizePolicy().hasHeightForWidth())
        self.stock_modal_button.setSizePolicy(sizePolicy)
        self.stock_modal_button.setMinimumSize(QtCore.QSize(150, 0))
        self.stock_modal_button.setMaximumSize(QtCore.QSize(16777215, 100))
        self.stock_modal_button.setFont(font)
        self.stock_modal_button.setText("Add new stock")
        self.stock_modal_button.setStyleSheet("border-width:2px;\n"
"background-color: rgb(203, 203, 203);\n"
"padding:10px;\n"
"border-radius:5px;")
        self.stock_modal_button.clicked.connect(self.stock_modal_input)
        self.gridLayout_8.addWidget(self.stock_modal_button, 2, 5, 1, 1)


        self.price_dropdown = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price_dropdown.sizePolicy().hasHeightForWidth())
        self.price_dropdown.setSizePolicy(sizePolicy)
        self.price_dropdown.setMinimumSize(QtCore.QSize(100, 0))
        self.price_dropdown.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.price_dropdown.setFont(font)
        self.price_dropdown.setStyleSheet("border-width:3px;\n"
"border-color:green;\n"
"padding:10px;")
        self.price_dropdown.setEditable(False)
        self.price_dropdown.setMaxVisibleItems(6)
        self.price_dropdown.setObjectName("price_dropdown")
        self.price_dropdown.addItem("")
        self.price_dropdown.addItem("")
        self.price_dropdown.addItem("")
        self.gridLayout_8.addWidget(self.price_dropdown, 0, 3, 1, 1)
        self.price_input = QtWidgets.QLineEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price_input.sizePolicy().hasHeightForWidth())
        self.price_input.setSizePolicy(sizePolicy)
        self.price_input.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.price_input.setFont(font)
        self.price_input.setObjectName("price_input")
        self.gridLayout_8.addWidget(self.price_input, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem8, 0, 4, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem9, 0, 6, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem10, 0, 2, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_8, 2, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.price_title = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price_title.sizePolicy().hasHeightForWidth())
        self.price_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.price_title.setFont(font)
        self.price_title.setStyleSheet("border-width:0px")
        self.price_title.setObjectName("price_title")
        self.gridLayout_7.addWidget(self.price_title, 1, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_7.addItem(spacerItem11, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_7, 0, 0, 1, 1)

# TAB THREE

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")

        self.comparison_price_input = QtWidgets.QLineEdit(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comparison_price_input.sizePolicy().hasHeightForWidth())
        self.comparison_price_input.setSizePolicy(sizePolicy)
        self.comparison_price_input.setMaximumSize(QtCore.QSize(16777215, 100))
        self.comparison_price_input.setStyleSheet("padding:7px;")
        self.comparison_price_input.setObjectName("comparison_price_input")
        self.gridLayout_12.addWidget(self.comparison_price_input, 0, 3, 1, 1)

        self.comparison_input = QtWidgets.QLineEdit(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comparison_input.sizePolicy().hasHeightForWidth())
        self.comparison_input.setSizePolicy(sizePolicy)
        self.comparison_input.setMaximumSize(QtCore.QSize(16777215, 100))
        self.comparison_input.setObjectName("comparison_input")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comparison_input.setFont(font)
        self.comparison_input.setText("Enter Tool Name")
        self.comparison_price_input.setFont(font)
        self.comparison_price_input.setText("Enter Your Price")

        self.gridLayout_12.addWidget(self.comparison_input, 0, 1, 1, 1)

        self.comparison_input_2 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comparison_input_2.sizePolicy().hasHeightForWidth())
        self.comparison_input_2.setSizePolicy(sizePolicy)
        self.comparison_input_2.setMinimumSize(QtCore.QSize(150, 0))
        self.comparison_input_2.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comparison_input_2.setFont(font)
        self.comparison_input_2.setStyleSheet("border-width:2px;\n"
"background-color: rgb(203, 203, 203);\n"
"padding:10px;\n"
"border-radius:5px;")
        self.comparison_input_2.setObjectName("comparison_input_2")
        self.comparison_input_2.clicked.connect(self.tool_comparison_query)

        self.gridLayout_12.addWidget(self.comparison_input_2, 0, 5, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem12, 0, 4, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem13, 0, 2, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem14, 0, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem15, 0, 6, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_12, 2, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.comparison_title = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comparison_title.sizePolicy().hasHeightForWidth())
        self.comparison_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.comparison_title.setFont(font)
        self.comparison_title.setStyleSheet("border-width:0px")
        self.comparison_title.setObjectName("comparison_title")
        self.gridLayout_9.addWidget(self.comparison_title, 1, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_9.addItem(spacerItem16, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.comparison_search = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comparison_search.sizePolicy().hasHeightForWidth())
        self.comparison_search.setSizePolicy(sizePolicy)
        self.comparison_search.setMaximumSize(QtCore.QSize(16777215, 300))
        self.comparison_search.setText("")
        self.comparison_search.setPixmap(QtGui.QPixmap(":/Concrete_blocks/concrete_block.jpg"))
        self.comparison_search.setScaledContents(True)
        self.comparison_search.setObjectName("comparison_search")
        self.gridLayout_13.addWidget(self.comparison_search, 0, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem17, 0, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem18, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_13, 4, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem19, 1, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem20, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")

# TAB FOUR


        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "Tool Loaning")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.gridLayout = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.add_customers = QtWidgets.QPushButton(self.tab_4)
        self.add_customers.setText("Add Customers")
        self.add_customers.setStyleSheet("font-size:35px;padding:5px;")
        self.add_customers.clicked.connect(self.input_modal)

        self.show_customers = QtWidgets.QPushButton(self.tab_4)
        self.show_customers.setText("Show Customers")
        self.show_customers.setStyleSheet("font-size:35px;padding:5px;")
        self.show_customers.clicked.connect(self.show_loaning_page)

        self.delete_customers = QtWidgets.QPushButton(self.tab_4)
        self.delete_customers.setText("Delete Customers")
        self.delete_customers.setStyleSheet("font-size:35px;padding:5px;")
        self.delete_customers.clicked.connect(self.delete_modal)



        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.add_customers.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.delete_customers.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.show_customers.sizePolicy().hasHeightForWidth())

        self.add_customers.setSizePolicy(sizePolicy)
        self.add_customers.setObjectName("AddpushButton")
        self.delete_customers.setSizePolicy(sizePolicy)
        self.show_customers.setSizePolicy(sizePolicy)
        self.show_customers.setObjectName("ShowpushButton")


        self.gridLayout_2.addWidget(self.add_customers, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.show_customers, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.delete_customers, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setText("")
        self.image_label.setPixmap(QtGui.QPixmap(":/Concrete_blocks/database.png"))
        self.image_label.setStyleSheet("border-width:0px;")
        self.image_label.setScaledContents(False)
        self.image_label.setObjectName("label")
        self.gridLayout_3.addWidget(self.image_label, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)

    def stock_modal_input(self):
        self.dialog = QtWidgets.QDialog()
        self.modal_stock_button = QtWidgets.QPushButton("Save In Database",self.dialog)
        self.modal_stock_button.move(45,120)
        self.modal_stock_input = QtWidgets.QLineEdit("Stock X...",self.dialog)
        self.modal_stock_input.move(30,50)
        self.modal_stock_input2 = QtWidgets.QLineEdit("0.00",self.dialog)
        self.modal_stock_input2.move(30,80)
        self.modal_stock_button.clicked.connect(lambda:self.add_stock_names(self.modal_stock_input.text(),self.modal_stock_input2.text()  ))
        self.dialog.setWindowTitle("Input Stock")
        self.dialog.exec_()

    def add_stock_names(self,name,price):

        try:
            price = float(price)
            c.execute("INSERT INTO stock_prices VALUES(?,?)",(name,price,))
            connect.commit()
        except ValueError:
            self.error_modal("Incorrect input data")

    def add_loaning_customers(self,input):
        c.execute("INSERT INTO customers VALUES(?,?)",(input,"No Tools",))
        connect.commit()
    def delete_loaning_customers(self,input):
        c.execute("DELETE FROM customers WHERE customer_name = ? ",(input,))
        connect.commit()

    def error_modal(self,text):
        self.error_modal = QtWidgets.QDialog()
        self.text_output = QtWidgets.QLabel(text,self.error_modal)
        self.text_output.move(20,20)
        self.error_modal.setWindowTitle("Error")
        self.error_modal.exec_()

    def input_modal(self):
        self.dialog = QtWidgets.QDialog()
        self.modal_save_button = QtWidgets.QPushButton("Save",self.dialog)
        self.modal_save_button.move(50,100)
        self.modal_save_input = QtWidgets.QLineEdit("Customer X...",self.dialog)
        self.modal_save_input.move(30,50)
        self.modal_save_button.clicked.connect(lambda:self.add_loaning_customers(self.modal_save_input.text()))
        self.dialog.setWindowTitle("Input")
        self.dialog.exec_()

    def delete_modal(self):
        self.dialog = QtWidgets.QDialog()
        self.modal_delete_button = QtWidgets.QPushButton("Delete",self.dialog)
        self.modal_delete_button.move(50,100)
        self.modal_delete_input = QtWidgets.QLineEdit("Customer Name",self.dialog)
        self.modal_delete_input.move(30,50)
        self.modal_delete_button.clicked.connect(lambda:self.delete_loaning_customers(self.modal_delete_input.text()))
        self.dialog.setWindowTitle("Delete")
        self.dialog.exec_()






    def show_loaning_page(self):


        self.tab_loaned_customers = QtWidgets.QWidget()
        self.tab_loaned_customers.setObjectName("tab_loaned_customers")
        self.tabWidget.addTab(self.tab_loaned_customers, "loaned_customers")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        layout = QtWidgets.QVBoxLayout(self.tab_loaned_customers)
        self.scrollArea = QtWidgets.QScrollArea(self.tab_loaned_customers)
        layout.addWidget(self.scrollArea)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 2000, 2000))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        layout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)

        c.execute("select * from customers")
        results = c.fetchall()
        resizing = 100
        tool_outputs = []

        for i in range(len(results)):

            self.result = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.result.setText(results[i][0])
            self.result.move(400,resizing)
            self.result.setStyleSheet("font-size:50px;padding:10px;")
            self.result.setFixedHeight(150)
            self.result.setFixedWidth(500)

            tool_outputs.append(QtWidgets.QTextEdit(self.scrollAreaWidgetContents))
            tool_outputs[i].setText(results[i][1])
            tool_outputs[i].move(950,resizing)
            tool_outputs[i].setObjectName(results[i][0])
            tool_outputs[i].setStyleSheet("font-size:30px;padding:2px;")
            tool_outputs[i].setFixedHeight(150)
            tool_outputs[i].setFixedWidth(350)

            resizing = resizing + 250

        self.save_button = QtWidgets.QPushButton("Save Changes?",self.scrollAreaWidgetContents)
        self.save_button.move(675,resizing)
        self.save_button.setStyleSheet("font-size:30px;padding:10px;border-radius:5px;background-color:grey")
        self.save_button.setFixedHeight(100)
        self.save_button.setFixedWidth(350)
        self.save_button.clicked.connect(lambda:self.save_loan_text(tool_outputs,results))

        self.tabWidget.setCurrentIndex(int(self.tabWidget.count()) - 1)

    def save_loan_text(self,tool_outputs,results):
        tool_outputs[0].toPlainText()
        for x in range (len(tool_outputs)):
            c.execute("UPDATE customers SET tool_name = ? WHERE customer_name = ?",(   tool_outputs[x].toPlainText(), results[x][0],)  )
            connect.commit()
        self.tabWidget.removeTab(self.tabWidget.count() - 1)
        self.show_loaning_page()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_title.setText(_translate("MainWindow", "Builder & Plumber Merchants"))
        self.main_price_button.setText(_translate("MainWindow", "Stock price search"))
        self.main_comparison_button.setText(_translate("MainWindow", "Tool price comparison"))
        self.main_tool_button.setText(_translate("MainWindow", "Tool loaning"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main Page"))
        self.price_search_button.setText(_translate("MainWindow", "Search"))
        self.price_dropdown.setCurrentText(_translate("MainWindow", "Alphabetical"))
        self.price_dropdown.setItemText(0, _translate("MainWindow", "Alphabetical"))
        self.price_dropdown.setItemText(1, _translate("MainWindow", "Price(high-low)"))
        self.price_dropdown.setItemText(2, _translate("MainWindow", "Price (low-high)"))
        self.price_title.setText(_translate("MainWindow", "Stock Price Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Price Search"))
        self.comparison_input_2.setText(_translate("MainWindow", "Search"))
        self.comparison_title.setText(_translate("MainWindow", "Tool Price Comparison"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tool comparison"))


    def tab_change(self,x):
        self.tabWidget.setCurrentIndex(x)

    def price_query_display(self):
        query_selector = "%"+self.price_input.text()+"%"
        data_verification_variable = self.price_input.text()
        if data_verification_variable != "":

            self.price_tab = QtWidgets.QWidget()
            self.price_tab.setObjectName("price_tab")
            self.tabWidget.addTab(self.price_tab, "Price Query Results")
            self.tableWidget = QtWidgets.QTableWidget(self.price_tab)

            self.tableWidget.setObjectName("tableWidget")
            self.gridLayout = QtWidgets.QGridLayout(self.price_tab)
            self.gridLayout.setObjectName("table_gridLayout")
            self.gridLayout.addWidget(self.tableWidget,50,50)

            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, "stock_prices.db")
            connect = sqlite3.connect(db_path)
            c = connect.cursor()

            dropdown_index = self.price_dropdown.currentIndex()

            if dropdown_index == 0:
                c.execute("SELECT stock_name,price FROM stock_prices WHERE stock_name LIKE ? ORDER BY stock_name ASC",(query_selector,))
            elif dropdown_index == 1:
                c.execute("SELECT stock_name,price FROM stock_prices WHERE stock_name LIKE ? ORDER BY price DESC",(query_selector,))
            elif dropdown_index == 2:
                c.execute("SELECT stock_name,price FROM stock_prices WHERE stock_name LIKE ? ORDER BY price ASC",(query_selector,))

            results = c.fetchall()
            c.execute("SELECT COUNT(stock_name)FROM stock_prices WHERE stock_name LIKE ? ",(query_selector,) )
            count_results = c.fetchall()

            count_results = count_results[0][0]
            column_values = ["Stock Name","Stock Price"]
            row_values = []
            for x in range(count_results):
                i = str(x)
                row_values.append(i)
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(column_values)
            self.tableWidget.setRowCount(count_results)
            self.tableWidget.setVerticalHeaderLabels(row_values)
            self.tableWidget.setStyleSheet("font-size:15px;padding:5px;margin:20px;")

            for x in range(count_results):
                self.tableWidget.setItem(x,0, QtWidgets.QTableWidgetItem(str(results[x][0])))
                self.tableWidget.setItem(x,1, QtWidgets.QTableWidgetItem(str(results[x][1])))

            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

            self.tabWidget.setCurrentIndex(int(self.tabWidget.count()) - 1)

    def tool_comparison_query(self):
        if self.comparison_input.text() != "" and self.comparison_price_input.text() != "":
            def standard_deviation_check(prices_list):
                try:
                    price_input = float(self.comparison_price_input.text())
                    deviation_magnitude = price_input / 3
                    list_length = len(prices_list)
                    total = 0
                    for x in prices_list:
                        try:
                            if float(x) > (price_input + deviation_magnitude) or float(x) < (price_input - deviation_magnitude):
                                list_length = list_length - 1
                            else:
                                total = total + float(x)
                        except ValueError:
                            list_length = list_length - 1
                            pass

                    try:
                        mean = total / list_length
                        return(round(mean,2))
                    except ZeroDivisionError:
                        return(0)
                except ValueError:
                    self.error_modal("Incorrect price input")







            qcount = 0
            products=[] #List to store name of the product
            prices=[] #List to store price of the product
            ratings=[] #List to store ratings of the product
            no_pages = 2

            def get_data(pageNo,q,first):
                headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

                r = requests.get("https://www.amazon.co.uk/s?k="+self.comparison_input.text()+"&page="+str(pageNo), headers=headers)
                content = r.content
                soup = BeautifulSoup(content, "lxml")

                if first == "first":
                    for d in soup.findAll('div', attrs={'class':'sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28'}):
                        price = d.find('span', attrs={'class':'a-offscreen'})
                        all=[]

                        if price is not None:
                            all.append(price.text)
                        else:
                            all.append('$0')
                        q.put(all)
                elif first == "second":
                    for d in soup.findAll('div', attrs={'class':'sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32'}):
                        price = d.find('span', attrs={'class':'a-offscreen'})
                        all=[]

                        if price is not None:
                            all.append(price.text)
                        else:
                            all.append('$0')
                        q.put(all)



            results = []
            if __name__ == "__main__":
                m = Manager()
                q = m.Queue()
                p = {}
                for i in range(1,no_pages):
                    p[i] = threading.Thread(target=get_data, args=(i,q,"first"))
                    p[i].start()
                for i in range(1,no_pages):
                    p[i].join()

                while q.empty() is not True:
                    qcount = qcount+1
                    queue_top = q.get()
                    prices.append(queue_top[0])
                if prices != []:
                    for x in range(len(prices) - 1):
                        prices[x] = prices[x].replace("£","")
                else:
                    m = Manager()
                    q = m.Queue()
                    p = {}
                    for i in range(1,no_pages):
                        p[i] = threading.Thread(target=get_data, args=(i,q,"second"))
                        p[i].start()
                    for i in range(1,no_pages):
                        p[i].join()

                    while q.empty() is not True:
                        qcount = qcount+1
                        queue_top = q.get()
                        prices.append(queue_top[0])
                    if prices != []:
                        for x in range(len(prices) - 1):
                            prices[x] = prices[x].replace("£","")

            self.tool_tab = QtWidgets.QWidget()
            self.tool_tab.setObjectName("tool_tab")
            self.tabWidget.addTab(self.tool_tab, "Tool Query Results")
            self.tool_query_results = QtWidgets.QLabel(self.tool_tab)
            self.tool_query_results.setText("Mean Price Of "+ str(self.comparison_input.text()) + " Is £" + str(standard_deviation_check(prices)))
            self.tool_query_results.setStyleSheet("border-color:black;\n""border-width:4px;font-size:40px;padding:10px;margin:40px;")














if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
