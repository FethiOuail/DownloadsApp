import sys
from typing import re

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import urllib.request

import os
from os import path

# FORM_CLASS = loadUiType(path.join(path.dirname(__file__), "main.ui"))
from setuptools._vendor.six import print_

ui, _ = loadUiType('main.ui')


class MainApp(QMainWindow, ui):
	def __init__(self, parent=None):
		super(MainApp, self).__init__(parent)
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.Hundel_Ui()
		self.Hundel_Buttons()

	def Hundel_Buttons(self):
		self.btnDownload.clicked.connect(self.Download)

	def hundelBrowse(self):
		pass

	def Hundle_Progress(self, blocknum, blocksize, totalesize):

		read = blocknum * blocksize

		if totalesize > 0:
			percent = read * 100 / totalesize
			self.progressBar.setValue(int(percent))
			QApplication.processEvents()  # Fix Lag

	def Download(self):
		url_d = self.urlEdit.text()
		save_location = self.saveLocation.text()
		print(url_d)
		# F:/PycharmProjects/DownloadsApp/img3.jpg

		try:
			urllib.request.urlretrieve(url_d, save_location, self.Hundle_Progress)
		except Exception :
			QMessageBox.warning(self, "Downloads Error", " Error")
			return

		QMessageBox.information(self, "Download Completed", "The Download Finished")
		self.progressBar.setValue(0)
		self.urlEdit.setText('')
		self.saveLocation.setText('')

	def Hundel_Ui(self):
		self.setWindowTitle("Downloader")
		self.setFixedSize(600, 260)


def main():
	app = QApplication(sys.argv)
	window = MainApp()
	window.show()
	app.exec_()


if __name__ == '__main__':
	main()
