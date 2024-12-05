from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel
)

from entities.list_entity import ListEntity

class ListView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TO DO LIST")
        self.setGeometry(100, 100, 400, 400)

        # Mise en page principale
        self.layout = QVBoxLayout()

        # Formulaire pour ajouter ou mettre à jour une liste
        self.form_layout = QVBoxLayout()
        self.title_input = self.create_input_field("Nom")
        self.list_id_input = self.create_input_field("ID")

        self.button_layout = QHBoxLayout()
        self.add_button = QPushButton("Creer")
        self.update_button = QPushButton("Mettre à jour")
        self.delete_button = QPushButton("Supprimer")

        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.update_button)
        self.button_layout.addWidget(self.delete_button)

        self.form_layout.addLayout(self.title_input)
        self.form_layout.addLayout(self.list_id_input)
        self.form_layout.addLayout(self.button_layout)

        self.layout.addLayout(self.form_layout)
        self.setLayout(self.layout)

    def create_input_field(self, label_text):
        layout = QHBoxLayout()
        label = QLabel(label_text)
        input_field = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(input_field)
        return layout

    def connect_signals(self, controller):
        self.add_button.clicked.connect(controller.add_list)
        self.update_button.clicked.connect(controller.update_list)
        self.delete_button.clicked.connect(controller.delete_list)
