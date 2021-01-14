# -*- coding: utf-8 -*-

from Core.mainWindow import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

ui.searchButton.clicked.connect(lambda: ui.infoVideo())

ui.button1080p.clicked.connect(lambda: ui.videoSize('1080p'))
ui.button720p.clicked.connect(lambda: ui.videoSize('720p'))
ui.button480p.clicked.connect(lambda: ui.videoSize('480p'))
ui.button360p.clicked.connect(lambda: ui.videoSize('360p'))
ui.buttonMp3.clicked.connect(lambda: ui.videoSize('mp3'))

ui.downloadButton.clicked.connect(lambda: ui.videoDownload())

MainWindow.show()
sys.exit(app.exec_())