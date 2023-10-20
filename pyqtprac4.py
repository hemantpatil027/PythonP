from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("CLICK", self)
        self.button.setGeometry(20, 15, 100, 40)
        self.button.clicked.connect(self.buttonClickedEvent)

        self.input_text = QLineEdit(self)
        self.input_text.setGeometry(20, 70, 200, 30)

    def buttonClickedEvent(self):
        self.user_input = self.input_text.text()

        if self.user_input.isalpha():
            print("is not alphanumeric")
            QMessageBox.information(self, "Alphanumeric Check", f"'{self.user_input}' is not alphanumeric.")
        else:
            print("is alphanumeric")
            QMessageBox.warning(self, "Alphanumeric Check", f"'{self.user_input}' is alphanumeric.")

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()
