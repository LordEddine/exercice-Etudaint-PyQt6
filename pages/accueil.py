from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class PageAccueil(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        # Titre centré
        titre = QLabel("<h1><b style='color:red;'>Bienvenue Eddine</b></h1>")
        titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Image centrée (utiliser un emoji ou caractère Unicode)
        image_label = QLabel("Bienvenu dans mon application")  # Emoji pirate pour remplacer Luffy
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label.setStyleSheet("font-size: 60px; margin: 20px;")
        
        
        layout.addStretch()  # Espace en haut
        layout.addWidget(titre)
        layout.addWidget(image_label)
        layout.addStretch()  # Espace en bas
        
        self.setLayout(layout)