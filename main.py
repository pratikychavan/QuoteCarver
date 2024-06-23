import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QLabel, QPushButton, QLineEdit, QTextEdit, QFormLayout, QFileDialog, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QPainter, QFont, QColor

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quote Carver")

        self.heading = QLabel("Quote Carver", alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.load_image_button = QPushButton("Load Image")
        self.generate_image_button = QPushButton("Generate Image")

        self.layout = QFormLayout(self)
        self.image_location = QLineEdit()
        self.image_location.setReadOnly(True)
        self.quote = QTextEdit()
        self.author = QLineEdit()
        self.preview_label = QLabel(self)  # Label to display the preview
        self.preview_label.setFixedSize(400, 400)  # Set the size of the preview label

        self.layout.addWidget(self.heading)
        self.layout.addRow(QLabel("Image location"), self.image_location)
        self.layout.addRow(self.load_image_button)
        self.layout.addRow(QLabel("Quote"), self.quote)
        self.layout.addRow(QLabel("Author"), self.author)
        self.layout.addWidget(self.generate_image_button)
        self.layout.addWidget(self.preview_label)

        self.load_image_button.clicked.connect(self.load_image)
        self.generate_image_button.clicked.connect(self.magic)

    @QtCore.Slot()
    def load_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)", options=options)
        if file_name:
            self.image_location.setText(file_name)

    @QtCore.Slot()
    def magic(self):
        image_path = self.image_location.text()
        quote_text = self.quote.toPlainText()
        author_text = self.author.text()

        if image_path and quote_text:
            combined_image_path = self.create_quote_image(image_path, quote_text, author_text)
            if combined_image_path:
                pixmap = QPixmap(combined_image_path)
                self.preview_label.setPixmap(pixmap.scaled(self.preview_label.size(), QtCore.Qt.KeepAspectRatio))

    def create_quote_image(self, image_path, quote, author):
        try:
            base_image = QPixmap(image_path)
            if base_image.isNull():
                raise ValueError("Cannot load image")

            painter = QPainter(base_image)
            initial_font_size = 30
            font = QFont('Arial', initial_font_size)
            painter.setFont(font)
            painter.setPen(QColor('white'))

            line_count = len(quote.splitlines())
            text = f'"{quote}"\n- {author}'
            im_height = base_image.height()
            im_width = base_image.width()
            text_rect = QtCore.QRect(50, im_height/2 + 50*(line_count/2) , base_image.width() - 100, im_height/2 - 50*(line_count/2))
            
            while True:
                bounding_rect = painter.boundingRect(text_rect, QtCore.Qt.AlignCenter, text)
                if bounding_rect.height() <= text_rect.height() and bounding_rect.width() <= text_rect.width():
                    break
                initial_font_size -= 1
                if initial_font_size <= 0:
                    raise ValueError("Text is too long to fit within the image")
                font.setPointSize(initial_font_size)
                painter.setFont(font)

            painter.drawText(text_rect, QtCore.Qt.AlignCenter, text)
            painter.end()

            combined_image_path = "combined_image.png"
            base_image.save(combined_image_path)

            return combined_image_path
        except Exception as e:
            print(f"Error: {e}")
            return None

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())


