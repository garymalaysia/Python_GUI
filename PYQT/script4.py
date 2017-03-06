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
		self.width = 550
		self.height = 400
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
		self.tableWidget.setRowCount(7)
		self.tableWidget.setColumnCount(6)
		self.tableWidget.setItem(0,0, QTableWidgetItem('   '))
		self.tableWidget.setItem(0,1, QTableWidgetItem('Monday'))
		self.tableWidget.setItem(0,2, QTableWidgetItem('Tuesday'))
		self.tableWidget.setItem(0,3, QTableWidgetItem('Wednesday'))
		self.tableWidget.setItem(0,4, QTableWidgetItem('Thursday'))
		self.tableWidget.setItem(0,5, QTableWidgetItem('Friday'))
		self.tableWidget.setItem(1,0, QTableWidgetItem('9-10'))
		self.tableWidget.setItem(2,0, QTableWidgetItem('10-11'))
		self.tableWidget.setItem(3,0, QTableWidgetItem('11-12'))
		self.tableWidget.setItem(4,0, QTableWidgetItem('12-1'))
		self.tableWidget.setItem(5,0, QTableWidgetItem('1-2'))
		self.tableWidget.setItem(6,0, QTableWidgetItem('2-3'))
		self.tableWidget.setItem(1,1, QTableWidgetItem('Sarah'))
		self.tableWidget.setItem(2,1, QTableWidgetItem('Sarah'))
		self.tableWidget.setItem(3,1, QTableWidgetItem('Sarah'))
		self.tableWidget.setItem(4,1, QTableWidgetItem('John'))
		self.tableWidget.setItem(5,1, QTableWidgetItem('John'))
		self.tableWidget.setItem(6,1, QTableWidgetItem('John'))
		self.tableWidget.setItem(1,2, QTableWidgetItem('Jennifer'))
		self.tableWidget.setItem(2,2, QTableWidgetItem('Jennifer'))
		self.tableWidget.setItem(3,2, QTableWidgetItem('Jennifer'))
		self.tableWidget.setItem(4,2, QTableWidgetItem('Freddy'))
		self.tableWidget.setItem(5,2, QTableWidgetItem('Freddy'))
		self.tableWidget.setItem(6,2, QTableWidgetItem('Freddy'))

		self.tableWidget.doubleClicked.connect(self.on_click)

	@pyqtSlot()
	def on_click(self):
		print('\n')
		for currentQTableWidgetItem in self.tableWidget.selectedItems():
			print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

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