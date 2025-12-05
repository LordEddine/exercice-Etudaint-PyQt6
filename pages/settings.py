from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class PageSettings(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Paramètres de l'application"))
        layout.addStretch()
        self.setLayout(layout)