import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon

class App(QMainWindow):

	def __init__(self):
		super().__init__()
		self.title = 'HIC Card Reader'
		self.left = 60 		
		self.top = 100       
		self.width = 600    
		self.height = 400
		#complete left side: 1
		#complete top side: 32
		#full screen width: 1363
		#full screen height: 693.5 
		self.message = "John Jay's Veterans Association"
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.statusBar().showMessage(self.message)
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())