# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Core.controller import *
from Core.logo1_rc import *
import re
import sys


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(702, 521)
                MainWindow.setStyleSheet("background-color: rgb(29, 43, 66);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(240, 40, 81, 31))
                self.label_5.setObjectName("label_5")
        
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(320, 10, 101, 91))
                self.label_2.setStyleSheet("border-image: url(:/cct/logo.png);")
                self.label_2.setText("")
                self.label_2.setObjectName("label_2")
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(420, 40, 61, 31))
                self.label_6.setObjectName("label_6")
                self.labelTitle = QtWidgets.QLabel(self.centralwidget)
                self.labelTitle.setGeometry(QtCore.QRect(60, 210, 71, 27))
                self.labelTitle.setObjectName("labelTitle")
                self.LabelDuration = QtWidgets.QLabel(self.centralwidget)
                self.LabelDuration.setGeometry(QtCore.QRect(60, 240, 101, 41))
                self.LabelDuration.setObjectName("LabelDuration")
                self.LabelTitleName = QtWidgets.QLabel(self.centralwidget)
                self.LabelTitleName.setGeometry(QtCore.QRect(140, 210, 471, 27))
                self.LabelTitleName.setObjectName("LabelTitleName")
                self.labelTime = QtWidgets.QLabel(self.centralwidget)
                self.labelTime.setGeometry(QtCore.QRect(170, 250, 81, 27))
                self.labelTime.setObjectName("labelTime")
                self.widget = QtWidgets.QWidget(self.centralwidget)
                self.widget.setGeometry(QtCore.QRect(50, 140, 601, 38))
                self.widget.setObjectName("widget")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.lineEdit = QtWidgets.QLineEdit(self.widget)
                self.lineEdit.setObjectName("lineEdit")
                self.horizontalLayout_2.addWidget(self.lineEdit)
                self.searchButton = QtWidgets.QPushButton(self.widget)
                self.searchButton.setEnabled(True)
                self.searchButton.setStyleSheet("background-color: rgb(38, 73, 138);\n"
        "font: 75 italic 14pt \"Nimbus Roman\";\n"
        "color: rgb(245, 245, 245);")
                self.searchButton.setObjectName("searchButton")
                self.horizontalLayout_2.addWidget(self.searchButton)
                self.widget1 = QtWidgets.QWidget(self.centralwidget)
                self.widget1.setGeometry(QtCore.QRect(60, 310, 365, 59))
                self.widget1.setObjectName("widget1")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setObjectName("verticalLayout")
                self.label = QtWidgets.QLabel(self.widget1)
                self.label.setObjectName("label")
                self.verticalLayout.addWidget(self.label)
                self.horizontalLayout = QtWidgets.QHBoxLayout()
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.button1080p = QtWidgets.QRadioButton(self.widget1)
                self.button1080p.setStyleSheet("font: 87 12pt \"Noto Sans\";")
                self.button1080p.setObjectName("button1080p")
                self.horizontalLayout.addWidget(self.button1080p)
                self.button720p = QtWidgets.QRadioButton(self.widget1)
                self.button720p.setStyleSheet("font: 87 12pt \"Noto Sans\";")
                self.button720p.setObjectName("button720p")
                self.horizontalLayout.addWidget(self.button720p)
                self.button480p = QtWidgets.QRadioButton(self.widget1)
                self.button480p.setStyleSheet("font: 87 12pt \"Noto Sans\";")
                self.button480p.setObjectName("button480p")
                self.horizontalLayout.addWidget(self.button480p)
                self.button360p = QtWidgets.QRadioButton(self.widget1)
                self.button360p.setStyleSheet("font: 87 12pt \"Noto Sans\";")
                self.button360p.setObjectName("button360p")
                self.horizontalLayout.addWidget(self.button360p)
                self.buttonMp3 = QtWidgets.QRadioButton(self.widget1)
                self.buttonMp3.setStyleSheet("font: 87 12pt \"Noto Sans\";")
                self.buttonMp3.setObjectName("buttonMp3")

                self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
                self.downloadButton.setGeometry(QtCore.QRect(300, 430, 151, 41))
                self.downloadButton.setStyleSheet("background-color: rgb(6, 147, 53);\n"
        "font: 75 italic 14pt \"Nimbus Roman\";\n"
        "color: rgb(245, 245, 245);")
                self.downloadButton.setObjectName("downloadButton")


                self.horizontalLayout.addWidget(self.buttonMp3)
                self.verticalLayout.addLayout(self.horizontalLayout)
                self.widget2 = QtWidgets.QWidget(self.centralwidget)
                self.widget2.setGeometry(QtCore.QRect(490, 330, 168, 34))
                self.widget2.setObjectName("widget2")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
                self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.SizeTitle = QtWidgets.QLabel(self.widget2)
                self.SizeTitle.setStyleSheet("font: 75 14pt \"Ligconsolata\";")
                self.SizeTitle.setObjectName("SizeTitle")
                self.horizontalLayout_3.addWidget(self.SizeTitle)
                self.Size = QtWidgets.QLabel(self.widget2)
                self.Size.setStyleSheet("font: 29 14pt \"Noto Sans CJK KR\";")
                self.Size.setObjectName("Size")
                self.horizontalLayout_3.addWidget(self.Size)
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">DOWN</span></p></body></html>"))
                self.downloadButton.setText(_translate("MainWindow", "Descargar"))
                self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">LOAD</span></p></body></html>"))
                self.lineEdit.setPlaceholderText(_translate("MainWindow", "https://www.youtube.com/watch?v=vHHKMQ0kD2M"))
                self.searchButton.setText(_translate("MainWindow", "Buscar"))
                self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Seleccione la resolución o el formato</span></p></body></html>"))
                self.button1080p.setText(_translate("MainWindow", "1080p"))
                self.button720p.setText(_translate("MainWindow", "  720p"))
                self.button480p.setText(_translate("MainWindow", "480p"))
                self.button360p.setText(_translate("MainWindow", "360p"))
                self.buttonMp3.setText(_translate("MainWindow", "MP3"))


        def infoVideo(self):
                _translate = QtCore.QCoreApplication.translate
                if(re.match(r'^https:\/\/www.youtube.com\/watch\?v=[\d\w\-\=\&\_]*$',self.lineEdit.text())):
                        self.controller = Controller(self.lineEdit.text())
                        self.labelTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Título : </span></p></body></html>"))
                        self.LabelTitleName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">%s</span></p></body></html>" %self.controller.getNameVideo()))
                        self.LabelDuration.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Duracion :</span></p></body></html>"))
                        self.labelTime.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">%s</span></p></body></html>" %self.controller.getDuration()))
                else:
                        self.LabelTitleName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\"> ERROR: Dirección Invalida, Por Favor Vuelva a Intentarlo  </span></p></body></html>"))
                        self.LabelDuration.setText('')
                        self.labelTime.setText('')
                        self.labelTitle.setText('')

        def videoSize(self,resolution):
                _translate = QtCore.QCoreApplication.translate
                if(resolution in self.controller.formats()):
                        self.controller.setResolution(resolution)
                        self.SizeTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Tamaño:</span></p></body></html>"))
                        self.Size.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:400; font-style:italic;\">%s MB</span></p></body></html>" %self.controller.getSize()))

                else:
                        self.Size.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:400; font-style:italic;\">N/D</span></p></body></html>" ))
                        
        def videoDownload(self):
                self.controller.video()