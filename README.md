# 🎓 Exercice Étudiants - PyQt6

Application de gestion d'étudiants développée avec PyQt6 et design moderne.

## 🚀 Fonctionnalités

- **Interface moderne** avec thème sombre
- **Gestion d'étudiants** : Ajouter, supprimer, visualiser
- **Navigation intuitive** avec sidebar
- **Tableau responsive** qui s'adapte à la taille de la fenêtre
- **Design élégant** avec CSS personnalisé

## 📁 Structure du projet

```
exercice-Etudaint/
├── main.py                 # Fenêtre principale et navigation
├── pages/
│   ├── accueil.py          # Page d'accueil avec image Luffy
│   ├── etudiants.py        # Gestion des étudiants
│   └── settings.py         # Page paramètres
├── windows/
│   └── add_student.py      # Fenêtre d'ajout d'étudiant
└── style/
    └── style.qss           # Styles CSS pour l'interface
```

## 🎨 Fonctionnalités techniques

- **Architecture MVC** avec séparation des pages
- **Signaux personnalisés** pour la communication entre fenêtres
- **Layouts responsifs** (QHBoxLayout, QVBoxLayout)
- **Tableaux adaptatifs** avec QHeaderView
- **Styles CSS avancés** avec alternating row colors
- **Navigation par boutons checkables**

## ⚙️ Installation et utilisation

1. **Prérequis** :
   ```bash
   pip install PyQt6
   ```

2. **Lancer l'application** :
   ```bash
   python main.py
   ```

## 🎯 Fonctionnalités de l'interface

### Page Accueil
- Message de bienvenue personnalisé
- Image Luffy centrée
- Design responsive

### Page Étudiants
- Tableau avec colonnes : Nom, Programme, Âge
- Boutons Ajouter/Supprimer
- Sélection de lignes entières
- Couleurs alternées personnalisables
- Redimensionnement automatique des colonnes

### Fenêtre d'ajout
- Formulaire avec validation
- Signal personnalisé pour communication
- Fermeture automatique après ajout

## 🎨 Personnalisation

Le fichier `style/style.qss` contient tous les styles :
- Thème sombre moderne
- Couleurs personnalisables
- Effets hover et selection
- Headers de tableau stylisés

## 📚 Technologies utilisées

- **PyQt6** : Interface graphique
- **Python 3.11+** : Langage de programmation
- **QSS (Qt Style Sheets)** : Stylisation CSS

## 👨‍💻 Auteur

**Eddine** - Cours CMaisonneuve - Développement d'applications de bureau

---
*Application développée dans le cadre du cours PyQt6 - CMaisonneuve* 🎓