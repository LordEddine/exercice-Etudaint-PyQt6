from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedWidget
from pages.accueil import PageAccueil
from pages.etudiants import PageEtudiants
from pages.settings import PageSettings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Conteneur principal
        container = QWidget()
        self.setCentralWidget(container)
        layout = QHBoxLayout(container)

        # === Sidebar ===
        self.sidebar = QVBoxLayout()
        self.btn_home = QPushButton("Accueil")
        self.btn_students = QPushButton("Étudiants")
        self.btn_settings = QPushButton("Paramètres")

        for btn in [self.btn_home, self.btn_students, self.btn_settings]:
            btn.setCheckable(True)
            self.sidebar.addWidget(btn)
        self.sidebar.addStretch()

        # === Pages ===
        self.stack = QStackedWidget()
        self.page_home = PageAccueil()
        self.page_students = PageEtudiants()
        self.page_settings = PageSettings()

        self.stack.addWidget(self.page_home)
        self.stack.addWidget(self.page_students)
        self.stack.addWidget(self.page_settings)

        # Navigation
        self.btn_home.clicked.connect(lambda: self.switch_page(0, self.btn_home))
        self.btn_students.clicked.connect(lambda: self.switch_page(1, self.btn_students))
        self.btn_settings.clicked.connect(lambda: self.switch_page(2, self.btn_settings))

        layout.addLayout(self.sidebar, 1)
        layout.addWidget(self.stack, 4)

        self.switch_page(0, self.btn_home)
        self.setWindowTitle("Dashboard — Gestion Étudiants")
        self.resize(900, 600)

    def switch_page(self, index, active_btn):
        self.stack.setCurrentIndex(index)
        for btn in [self.btn_home, self.btn_students, self.btn_settings]:
            btn.setChecked(False)
        active_btn.setChecked(True)


if __name__ == "__main__":
    app = QApplication([])
    with open("style/style.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()
    app.exec()