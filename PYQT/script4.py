import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QAction, QLabel
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QFileDialog
from PyQt5.QtWidgets import QVBoxLayout

#class App(QMainWindow):
class App(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'Mark IV'
		self.left = 100
		self.top = 100
		self.width = 500
		self.height = 300
		self.message = 'Python GUI Tutorial'
		self.initUI()

	#function to open files
	def openFileNameDialog(self):
		options = QFileDialog.Options()
		fileName, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '', 'All Files (*);;Python Files (*.py)', options=options)
		if fileName:
			return fileName

	#function to save files
	def saveFileDialog(self):
		options = QFileDialog.Options()
		options = QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getSaveFileName(self, 'QFileDialog.getSaveFileName()', '', 'All Files (*);;Text Files (*.txt)', options=options) 
		if fileName:
			return fileName

	#function to call 'openFileNameDialog' method 
	def open(self):
		print('Opening')
		self.openFileNameDialog()

	#function to call 'saveFileDialog' method
	def save(self):
		print('Saving')
		self.saveFileDialog()

	def help(self):
		print('Help')

	def about(self):
		QMessageBox.question(self, 'About', 'About us')

	def createTable(self):
		#Table
		self.tableWidget = QTableWidget()
		self.tableWidget.setRowCount(4)
		self.tableWidget.setColumnCount(2)

	def initUI(self):

		self.setWindowTitle(self.title)
		self.setGeometry(self.left,self.top,self.width,self.height)
		#self.statusBar().showMessage(self.message)

		self.createTable()
		
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.tableWidget)
		self.setLayout(self.layout)

		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())