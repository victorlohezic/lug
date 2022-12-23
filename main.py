# Import necessary modules
import sys
from pathlib import Path
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
    QPushButton, QDateEdit, QLineEdit, QTextEdit, QComboBox,
    QFormLayout, QHBoxLayout, QGridLayout, QFileDialog)
from PyQt6.QtCore import Qt, QRegularExpression, QDate
from PyQt6.QtGui import QFont, QRegularExpressionValidator, QPixmap
from script_email import send_email_smtp

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(500, 400)
        self.setWindowTitle("Lug")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        header_label = QLabel("Lug")
        header_label.setFont(QFont("Arial", 18))
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        logo = QLabel(self)
        pixmap = QPixmap('logo.png')
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create additional widgets to be added in the window
        self.receiver = QComboBox()
        self.receiver.addItems(["Customer", "Educational manager"])

        submit_button = QPushButton("Send email")
        submit_button.setMaximumWidth(140)
        submit_button.clicked.connect(self.send_email)

        #Create 
        file_layout = QHBoxLayout()

        # file selection
        file_browse = QPushButton('Browse')
        file_browse.clicked.connect(self.open_file_dialog)
        self.filename_edit = QLineEdit()

        file_layout.addWidget(self.filename_edit)
        file_layout.addWidget(file_browse)

        # Create horizontal layout for last row of widgets
        submit_h_box = QHBoxLayout()
        submit_h_box.addWidget(submit_button)      

        # Organize widgets and layouts in QFormLayout
        main_form = QFormLayout()
        main_form.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        main_form.setFormAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        main_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)

        main_form.addRow(header_label)
        main_form.addRow(logo)
        main_form.addRow("Receiver", self.receiver)
        main_form.addRow("File", file_layout)
        main_form.addRow(submit_h_box)

        # Set the layout for the main window
        self.setLayout(main_form)

    def send_email(self):
        """Send email"""
        send_email_smtp(self.receiver.currentText(), self.filename_edit.displayText())

    def open_file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File", 
            "~/Documents/Cours/2a/pfa/pfa-zds", 
            "*.pdf"
        )
        if filename:
            path = Path(filename)
            self.filename_edit.setText(str(path))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())