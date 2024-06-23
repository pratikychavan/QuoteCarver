import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.heading = QtWidgets.QLabel("Quote Carver", alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.button = QtWidgets.QPushButton("Generate Image")
        self.image_location_label = QtWidgets.QLabel("Image location", alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        self.image_location_input = QtWidgets.QLineEdit()
        self.quote_label = QtWidgets.QLabel("Quote", alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        self.quote_input = QtWidgets.QTextEdit()
        self.author_label = QtWidgets.QLabel("Author", alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        
        self.author_input = QtWidgets.QLineEdit()
        self.layout = QtWidgets.QFormLayout(self)
        self.layout.addWidget(self.heading)
        self.layout.addWidget(self.image_location_label)
        self.layout.addWidget(self.image_location_input)
        self.layout.addWidget(self.quote_label)
        self.layout.addWidget(self.quote_input)
        self.layout.addWidget(self.author_label)
        self.layout.addWidget(self.author_input)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())