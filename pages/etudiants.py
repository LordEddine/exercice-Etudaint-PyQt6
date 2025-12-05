from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView
from windows.add_student import AddStudentWindow

class PageEtudiants(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        btn_layout = QHBoxLayout()

        self.btn_add = QPushButton("Ajouter")
        self.btn_delete = QPushButton("Supprimer")
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_delete)

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Nom", "Programme", "Âge"])
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        
        # Configuration du redimensionnement automatique des colonnes
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.btn_add.clicked.connect(self.ouvrir_fenetre_ajout)
        self.btn_delete.clicked.connect(self.supprimer_selection)

        layout.addLayout(btn_layout)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def ouvrir_fenetre_ajout(self):
        self.fenetre = AddStudentWindow()
        self.fenetre.etudiantAjoute.connect(self.ajouter_etudiant)
        self.fenetre.show()

    def ajouter_etudiant(self, data):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(data["nom"]))
        self.table.setItem(row, 1, QTableWidgetItem(data["programme"]))
        self.table.setItem(row, 2, QTableWidgetItem(str(data["age"])))

    def supprimer_selection(self):
        row = self.table.currentRow()
        if row >= 0:
            self.table.removeRow(row)