# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_7 = QtWidgets.QWidget(self.centralwidget)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.widget_4 = QtWidgets.QWidget(self.widget_7)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_logoIUH = QtWidgets.QLabel(self.widget_4)
        self.label_logoIUH.setMaximumSize(QtCore.QSize(150, 110))
        self.label_logoIUH.setText("")
        self.label_logoIUH.setPixmap(QtGui.QPixmap(":/logo/iuh_logo.png"))
        self.label_logoIUH.setScaledContents(True)
        self.label_logoIUH.setObjectName("label_logoIUH")
        self.horizontalLayout.addWidget(self.label_logoIUH)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_Title = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Title.setObjectName("label_Title")
        self.horizontalLayout.addWidget(self.label_Title)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_StatusConnection = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(15)
        self.label_StatusConnection.setFont(font)
        self.label_StatusConnection.setStyleSheet("color:rgb(204, 43, 82);")
        self.label_StatusConnection.setAlignment(QtCore.Qt.AlignCenter)
        self.label_StatusConnection.setObjectName("label_StatusConnection")
        self.horizontalLayout.addWidget(self.label_StatusConnection)
        self.horizontalLayout_16.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem3)
        self.verticalLayout_11.addWidget(self.widget_4)
        self.widget_6 = QtWidgets.QWidget(self.widget_7)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem4)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem5 = QtWidgets.QSpacerItem(372, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem6)
        self.widget_3 = QtWidgets.QWidget(self.widget_6)
        self.widget_3.setObjectName("widget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.widget_3)
        self.formLayout_3.setObjectName("formLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.label_Connection = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(15)
        self.label_Connection.setFont(font)
        self.label_Connection.setStyleSheet("color:rgb(87, 143, 202);")
        self.label_Connection.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Connection.setObjectName("label_Connection")
        self.horizontalLayout_2.addWidget(self.label_Connection)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_IPAddress = QtWidgets.QLineEdit(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.lineEdit_IPAddress.setFont(font)
        self.lineEdit_IPAddress.setObjectName("lineEdit_IPAddress")
        self.horizontalLayout_3.addWidget(self.lineEdit_IPAddress)
        self.ConnectButton = QtWidgets.QPushButton(self.widget_3)
        self.ConnectButton.setMinimumSize(QtCore.QSize(88, 30))
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.ConnectButton.setFont(font)
        self.ConnectButton.setObjectName("ConnectButton")
        self.horizontalLayout_3.addWidget(self.ConnectButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_Port = QtWidgets.QLineEdit(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.lineEdit_Port.setFont(font)
        self.lineEdit_Port.setObjectName("lineEdit_Port")
        self.horizontalLayout_4.addWidget(self.lineEdit_Port)
        self.DisconnectButton = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.DisconnectButton.setFont(font)
        self.DisconnectButton.setObjectName("DisconnectButton")
        self.horizontalLayout_4.addWidget(self.DisconnectButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.horizontalLayout_15.addWidget(self.widget_3)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem10)
        self.verticalLayout_10.addLayout(self.horizontalLayout_15)
        spacerItem11 = QtWidgets.QSpacerItem(372, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem11)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem12)
        self.widget = QtWidgets.QWidget(self.widget_6)
        self.widget.setObjectName("widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.label_VoiceController = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(15)
        self.label_VoiceController.setFont(font)
        self.label_VoiceController.setStyleSheet("color:rgb(87, 143, 202);")
        self.label_VoiceController.setAlignment(QtCore.Qt.AlignCenter)
        self.label_VoiceController.setObjectName("label_VoiceController")
        self.horizontalLayout_9.addWidget(self.label_VoiceController)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem14)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem15)
        self.label_SpeechToText = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_SpeechToText.setFont(font)
        self.label_SpeechToText.setStyleSheet("color:rgb(167, 180, 158);")
        self.label_SpeechToText.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SpeechToText.setObjectName("label_SpeechToText")
        self.verticalLayout_4.addWidget(self.label_SpeechToText)
        spacerItem16 = QtWidgets.QSpacerItem(270, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem16)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_4.addWidget(self.comboBox)
        self.HoldSpeakButton = QtWidgets.QPushButton(self.widget)
        self.HoldSpeakButton.setMinimumSize(QtCore.QSize(88, 30))
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.HoldSpeakButton.setFont(font)
        self.HoldSpeakButton.setObjectName("HoldSpeakButton")
        self.verticalLayout_4.addWidget(self.HoldSpeakButton)
        self.verticalLayout_9.addLayout(self.verticalLayout_4)
        self.horizontalLayout_17.addWidget(self.widget)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem17)
        self.verticalLayout_10.addLayout(self.horizontalLayout_17)
        spacerItem18 = QtWidgets.QSpacerItem(372, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem18)
        self.horizontalLayout_20.addLayout(self.verticalLayout_10)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem19)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem20)
        self.widget_2 = QtWidgets.QWidget(self.widget_6)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem21)
        self.label_Control = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(15)
        self.label_Control.setFont(font)
        self.label_Control.setStyleSheet("color:rgb(87, 143, 202);")
        self.label_Control.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Control.setObjectName("label_Control")
        self.horizontalLayout_6.addWidget(self.label_Control)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem22)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_Device1_1 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.label_Device1_1.setFont(font)
        self.label_Device1_1.setStyleSheet("color:rgb(0, 0, 0);")
        self.label_Device1_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Device1_1.setObjectName("label_Device1_1")
        self.horizontalLayout_5.addWidget(self.label_Device1_1)
        spacerItem23 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem23)
        self.OnDevice1Button = QtWidgets.QPushButton(self.widget_2)
        self.OnDevice1Button.setMinimumSize(QtCore.QSize(88, 30))
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.OnDevice1Button.setFont(font)
        self.OnDevice1Button.setObjectName("OnDevice1Button")
        self.horizontalLayout_5.addWidget(self.OnDevice1Button)
        self.OffDevice1Button = QtWidgets.QPushButton(self.widget_2)
        self.OffDevice1Button.setMinimumSize(QtCore.QSize(88, 30))
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.OffDevice1Button.setFont(font)
        self.OffDevice1Button.setObjectName("OffDevice1Button")
        self.horizontalLayout_5.addWidget(self.OffDevice1Button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_Device2_1 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.label_Device2_1.setFont(font)
        self.label_Device2_1.setStyleSheet("color:rgb(0, 0, 0);")
        self.label_Device2_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Device2_1.setObjectName("label_Device2_1")
        self.horizontalLayout_7.addWidget(self.label_Device2_1)
        spacerItem24 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem24)
        self.OnDevice2Button = QtWidgets.QPushButton(self.widget_2)
        self.OnDevice2Button.setMinimumSize(QtCore.QSize(88, 30))
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.OnDevice2Button.setFont(font)
        self.OnDevice2Button.setObjectName("OnDevice2Button")
        self.horizontalLayout_7.addWidget(self.OnDevice2Button)
        self.OffDevice2Button = QtWidgets.QPushButton(self.widget_2)
        self.OffDevice2Button.setMinimumSize(QtCore.QSize(88, 30))
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.OffDevice2Button.setFont(font)
        self.OffDevice2Button.setObjectName("OffDevice2Button")
        self.horizontalLayout_7.addWidget(self.OffDevice2Button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_Device3_1 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.label_Device3_1.setFont(font)
        self.label_Device3_1.setStyleSheet("color:rgb(0, 0, 0);")
        self.label_Device3_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Device3_1.setObjectName("label_Device3_1")
        self.horizontalLayout_8.addWidget(self.label_Device3_1)
        spacerItem25 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem25)
        self.OnDevice3Button = QtWidgets.QPushButton(self.widget_2)
        self.OnDevice3Button.setMinimumSize(QtCore.QSize(88, 30))
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.OnDevice3Button.setFont(font)
        self.OnDevice3Button.setObjectName("OnDevice3Button")
        self.horizontalLayout_8.addWidget(self.OnDevice3Button)
        self.OffDevice3Button = QtWidgets.QPushButton(self.widget_2)
        self.OffDevice3Button.setMinimumSize(QtCore.QSize(88, 30))
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.OffDevice3Button.setFont(font)
        self.OffDevice3Button.setObjectName("OffDevice3Button")
        self.horizontalLayout_8.addWidget(self.OffDevice3Button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_18.addWidget(self.widget_2)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem26)
        self.verticalLayout_8.addLayout(self.horizontalLayout_18)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem27)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem28)
        self.widget_5 = QtWidgets.QWidget(self.widget_6)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem29)
        self.label_11 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgb(87, 143, 202);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem30)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem31 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem31)
        self.IconDevice1 = QtWidgets.QLabel(self.widget_5)
        self.IconDevice1.setMinimumSize(QtCore.QSize(40, 40))
        self.IconDevice1.setMaximumSize(QtCore.QSize(70, 70))
        self.IconDevice1.setText("")
        self.IconDevice1.setPixmap(QtGui.QPixmap(":/icon/close.png"))
        self.IconDevice1.setScaledContents(True)
        self.IconDevice1.setObjectName("IconDevice1")
        self.horizontalLayout_11.addWidget(self.IconDevice1)
        spacerItem32 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem32)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.label_Device1_2 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.label_Device1_2.setFont(font)
        self.label_Device1_2.setStyleSheet("color:rgb(0, 0, 0);")
        self.label_Device1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Device1_2.setObjectName("label_Device1_2")
        self.verticalLayout_3.addWidget(self.label_Device1_2)
        self.horizontalLayout_14.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem33 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem33)
        self.IconDevice2 = QtWidgets.QLabel(self.widget_5)
        self.IconDevice2.setMinimumSize(QtCore.QSize(40, 40))
        self.IconDevice2.setMaximumSize(QtCore.QSize(70, 70))
        self.IconDevice2.setText("")
        self.IconDevice2.setPixmap(QtGui.QPixmap(":/icon/OFF.png"))
        self.IconDevice2.setScaledContents(True)
        self.IconDevice2.setObjectName("IconDevice2")
        self.horizontalLayout_12.addWidget(self.IconDevice2)
        spacerItem34 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem34)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.label_Device2_2 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.label_Device2_2.setFont(font)
        self.label_Device2_2.setStyleSheet("color:rgb(0, 0, 0);")
        self.label_Device2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Device2_2.setObjectName("label_Device2_2")
        self.verticalLayout_5.addWidget(self.label_Device2_2)
        self.horizontalLayout_14.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem35 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem35)
        self.IconDevice3 = QtWidgets.QLabel(self.widget_5)
        self.IconDevice3.setMinimumSize(QtCore.QSize(40, 40))
        self.IconDevice3.setMaximumSize(QtCore.QSize(70, 70))
        self.IconDevice3.setText("")
        self.IconDevice3.setPixmap(QtGui.QPixmap(":/icon/fan off.png"))
        self.IconDevice3.setScaledContents(True)
        self.IconDevice3.setObjectName("IconDevice3")
        self.horizontalLayout_13.addWidget(self.IconDevice3)
        spacerItem36 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem36)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.label_Device3_2 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(12)
        self.label_Device3_2.setFont(font)
        self.label_Device3_2.setStyleSheet("color:rgb(0, 0, 0);")
        self.label_Device3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Device3_2.setObjectName("label_Device3_2")
        self.verticalLayout_6.addWidget(self.label_Device3_2)
        self.horizontalLayout_14.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_19.addWidget(self.widget_5)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem37)
        self.verticalLayout_8.addLayout(self.horizontalLayout_19)
        spacerItem38 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem38)
        self.horizontalLayout_20.addLayout(self.verticalLayout_8)
        spacerItem39 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem39)
        self.verticalLayout_11.addWidget(self.widget_6)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem40)
        self.label_Connection_2 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Vinhan")
        font.setPointSize(11)
        font.setItalic(True)
        self.label_Connection_2.setFont(font)
        self.label_Connection_2.setStyleSheet("color:rgb(0, 0, 0);")
        self.label_Connection_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Connection_2.setObjectName("label_Connection_2")
        self.horizontalLayout_21.addWidget(self.label_Connection_2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_21)
        self.gridLayout_2.addWidget(self.widget_7, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Title.setText(_translate("MainWindow", "VOICE RECOGNITION SOFTWARE"))
        self.label_StatusConnection.setText(_translate("MainWindow", "Disconnected"))
        self.label_Connection.setText(_translate("MainWindow", "CONNECTION"))
        self.lineEdit_IPAddress.setPlaceholderText(_translate("MainWindow", "Type IP Address"))
        self.ConnectButton.setText(_translate("MainWindow", "Connect"))
        self.lineEdit_Port.setPlaceholderText(_translate("MainWindow", "Type Port"))
        self.DisconnectButton.setText(_translate("MainWindow", "Disconnect"))
        self.label_VoiceController.setText(_translate("MainWindow", "VOICE CONTROLLER"))
        self.label_SpeechToText.setText(_translate("MainWindow", "Speak to microphone"))
        self.HoldSpeakButton.setText(_translate("MainWindow", "Hold and speak"))
        self.label_Control.setText(_translate("MainWindow", "CONTROL"))
        self.label_Device1_1.setText(_translate("MainWindow", "DEVICE 1"))
        self.OnDevice1Button.setText(_translate("MainWindow", "ON"))
        self.OffDevice1Button.setText(_translate("MainWindow", "OFF"))
        self.label_Device2_1.setText(_translate("MainWindow", "DEVICE 2"))
        self.OnDevice2Button.setText(_translate("MainWindow", "ON"))
        self.OffDevice2Button.setText(_translate("MainWindow", "OFF"))
        self.label_Device3_1.setText(_translate("MainWindow", "DEVICE 3"))
        self.OnDevice3Button.setText(_translate("MainWindow", "ON"))
        self.OffDevice3Button.setText(_translate("MainWindow", "OFF"))
        self.label_11.setText(_translate("MainWindow", "DEVICE STATUS"))
        self.label_Device1_2.setText(_translate("MainWindow", "DEVICE 1"))
        self.label_Device2_2.setText(_translate("MainWindow", "DEVICE 2"))
        self.label_Device3_2.setText(_translate("MainWindow", "DEVICE 3"))
        self.label_Connection_2.setText(_translate("MainWindow", "UI Designed by Hoang Long"))
import res


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
