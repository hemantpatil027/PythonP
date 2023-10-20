from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget


 

 

# Subclass QMainWindow to customize your application's main window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create a QLineEdit widget for user input
        self.input_text = QLineEdit(self)
        layout.addWidget(self.input_text)

        # Create a QPushButton to trigger an action
        self.button = QPushButton("CLICK", self)
        layout.addWidget(self.button)

        # Connect the button's click event to a function
        self.button.clicked.connect(self.display_user_input)

    def display_user_input(self):
        # Retrieve the text from the QLineEdit widget and display it
        user_input = self.input_text.text()
        print("User Input:", user_input)


if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()
