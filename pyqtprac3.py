from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("CLICK", self)
        self.button.setGeometry(20, 15, 100, 40)
        self.button.clicked.connect(self.buttonClickedEvent)

        self.input_text = QLineEdit(self)
        self.input_text.setGeometry(20, 70, 200, 30)  # Adjust the position and size as needed

    def buttonClickedEvent(self):
        user_input = self.input_text.text()
        print("User Input:", user_input)

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()
