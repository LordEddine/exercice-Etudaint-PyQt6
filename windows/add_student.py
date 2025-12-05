from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QComboBox, QSpinBox, QPushButton, QLabel
from PyQt6.QtCore import pyqtSignal

class AddStudentWindow(QWidget):

    etudiantAjoute = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.nom = QLineEdit()
        self.nom.setPlaceholderText("Nom")

        self.programme = QComboBox()
        self.programme.addItems(["Informatique", "Réseaux", "IA"])

        self.age = QSpinBox()
        self.age.setRange(1, 99)

        self.btn_add = QPushButton("Ajouter")
        self.btn_add.clicked.connect(self.valider)

        layout.addWidget(QLabel("Nom :"))
        layout.addWidget(self.nom)
        layout.addWidget(QLabel("Programme :"))
        layout.addWidget(self.programme)
        layout.addWidget(QLabel("Âge :"))
        layout.addWidget(self.age)
        layout.addWidget(self.btn_add)

        self.setLayout(layout)
        self.setWindowTitle("Ajouter un étudiant")

    def valider(self):
        data = {
            "nom": self.nom.text(),
            "programme": self.programme.currentText(),
            "age": self.age.value()
        }
        self.etudiantAjoute.emit(data)
        self.close()