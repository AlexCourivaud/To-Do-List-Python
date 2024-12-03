#import pyqt6
from PyQt6.QtWidgets import ( QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox)

from entities.list_entity import ListEntity

class ListView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TO DO LIST")
        self.setGeometry(100, 100, 600, 400)

        # Mise en page principale
        self.layout = QVBoxLayout()

        # Formulaire pour ajouter ou mettre à jour une liste
        self.form_layout = QVBoxLayout()
        self.title_input = self.create_input_field("Titre")
        self.book_id_input = self.create_input_field("ID (pour mise à jour ou suppression)")
