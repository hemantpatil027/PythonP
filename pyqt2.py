import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('First Window')

        self.label = QLabel('Enter text:')
        self.text_input = QLineEdit()
        self.button = QPushButton('Open Second Window')

        self.button.clicked.connect(self.open_second_window)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def open_second_window(self):
        text = self.text_input.text()
        if not text:
            self.show_warning("Please enter text in the input field.")
        else:
            self.second_window = SecondWindow(self)
            self.second_window.set_text_from_first_window(text)
            self.second_window.show()

    def show_warning(self, message):
        warning = QLabel(message)
        warning.setStyleSheet("color: red;")
        layout = self.layout()
        layout.addWidget(warning)

    def set_text_from_second_window(self, text):
        #self.text_input.setText(text)  # Set the text in the QLineEdit
        self.label.setText(f'Entered text from Second Window: {text}')  # Update the label

class SecondWindow(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Second Window')

        self.label = QLabel('Entered text from First Window:')
        self.label_value = QLabel('')
        self.text_input = QLineEdit()
        self.button = QPushButton('Update First Window')

        self.button.clicked.connect(self.update_first_window)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label_value)
        layout.addWidget(self.text_input)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def set_text_from_first_window(self, text):
        self.label_value.setText(text)

    def update_first_window(self):
        text = self.text_input.text()
        if not text:
            self.parent.show_warning("Please enter text in the input field.")
        else:
            self.parent.set_text_from_second_window(text)
            self.close()

def main():
    app = QApplication(sys.argv)
    first_window = FirstWindow()
    first_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
