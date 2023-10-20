from PyQt5.QtCore import QSize, Qt

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

 

 

# Subclass QMainWindow to customize your application's main window

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

       

        self.setWindowTitle("My App")

        self.button = QPushButton("CLICK",self)

        self.button.setGeometry(20, 15, 100, 40)

        self.button.clicked.connect(self.buttonClickedEvent)        

 

    def buttonClickedEvent(self):

        print("Button clicked")

        # self.close()

 

if __name__ == "__main__":

    app = QApplication([])

 

    window = MainWindow()

    window.show()

 

    app.exec()

    print("app is closed")