import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import os
from os import path

# FORM_CLASS = loadUiType(path.join(path.dirname(__file__), "main.ui"))
ui, _ = loadUiType('main.ui')


class MainApp(QMainWindow, ui):
	def __init__(self, parent=None):
		super(MainApp, self).__init__(parent)
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.Hundel_Ui()

	def Hundel_Buttons(self):
		pass

	def hundelBrowse(self):
		pass

	def Hundle_Progress(self):
		pass

	def Download(self):
		pass

	def Hundel_Ui(self):
		self.setWindowTitle("Downloader")


def main():
	app = QApplication(sys.argv)
	window = MainApp()
	window.show()
	app.exec_()


if __name__ == '__main__':
	main()
