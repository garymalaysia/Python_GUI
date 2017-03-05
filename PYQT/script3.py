import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QAction

class App(QMainWindow):

	def __init__(self):
		super().__init__()
		self.title = 'Mark III'
		self.left = 100
		self.top = 100
		self.width = 500
		self.height = 300
		self.message = 'Tutorial 3'
		self.initUI()

	def getAge(self):
		age, okPressed = QInputDialog.getInt(self, 'Get Integer', 'Age?',
											 18, 16, 50, 1)
		return age
	
	def chooseColor(self):
		color = ('Red', 'Blue', 'Green')
		color, choice = QInputDialog.getItem(self, 'Choose color', 'Color: ',
											 color, 0, False)
		return color

	def open(self):
		print('Open')

	def save(self):
		print('Save')

	def help(self):
		print('Help')

	def about(self):
		print('About')

	def initUI(self):
		'''
		answer = QMessageBox.question(self, 'DC/Marvel', 'Which do you prefer?',
							 		  QMessageBox.Yes | QMessageBox.No )
		if answer == QMessageBox.Yes:
			self.setWindowTitle(self.title)
			self.setGeometry(self.left,self.top,self.width,self.height)
			self.statusBar().showMessage(self.message)
		else:
			self.setWindowTitle('Exiting Window')
			self.setGeometry(100,100,250,40)
			self.statusBar().showMessage('Goodbye!')
		'''

		self.setWindowTitle(self.title)
		self.setGeometry(self.left,self.top,self.width,self.height)
		self.statusBar().showMessage(self.message)

		#self.getAge()	
		#self.chooseColor()
		self.show()

		#Main menu
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('File')
		helpMenu = mainMenu.addMenu('Help')

		#Adding to File menu
		openButton = QAction('Open', self)
		openButton.triggered.connect(self.open)
		fileMenu.addAction(openButton)

		saveButton = QAction('Save', self)
		saveButton.triggered.connect(self.save)
		fileMenu.addAction(saveButton)

		#Adding to Help menu
		helpButton = QAction('Help', self)
		helpButton.triggered.connect(self.help)
		helpMenu.addAction(helpButton)

		aboutButton = QAction('About', self)
		aboutButton.triggered.connect(self.about)
		helpMenu.addAction(aboutButton)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())