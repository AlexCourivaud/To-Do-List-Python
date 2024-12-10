from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QCheckBox,
    QHeaderView
)
from PyQt6.QtCore import Qt

from entities.task_entity import TaskEntity

class TaskView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TO DO LIST")
        self.setGeometry(100, 100, 700, 500)

        # Mise en page principale
        self.layout = QVBoxLayout()

        # Texte de présentation :
        self.explanation_label = QLabel("Bienvenue sur la To Do List ! Veuillez ajouter votre tâche svp:")
        self.layout.addWidget(self.explanation_label)

        # Formulaire pour ajouter ou mettre à jour une tâche
        self.form_layout = QVBoxLayout()
        self.title_input_layout, self.title_input = self.create_input_field("Nom")

        self.button_layout = QHBoxLayout()
        self.add_button = QPushButton("Creer")

        self.button_layout.addWidget(self.add_button)

        self.form_layout.addLayout(self.title_input_layout)
        self.form_layout.addLayout(self.button_layout)

        # Tableau pour afficher les tâches
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", " ", "Titre", "Statut"])

        # Ajuster la taille du tableau
        self.table.setFixedSize(800, 440)  # Définir une taille fixe pour le tableau

        # Ajuster la largeur des colonnes
        self.table.setColumnWidth(0, 0)  # ID (caché)
        self.table.setColumnWidth(1, 30)  # Sélectionner
        self.table.setColumnWidth(2, 300)  # Titre
        self.table.setColumnWidth(3, 100)  # Marqué comme terminé

        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.table)

        # Boutons pour agir sur les tâches sélectionnées
        self.action_layout = QHBoxLayout()
        self.mark_as_done_button = QPushButton("Marquer comme terminé")
        self.delete_button = QPushButton("Supprimer")

        self.action_layout.addWidget(self.mark_as_done_button)
        self.action_layout.addWidget(self.delete_button)

        self.layout.addLayout(self.action_layout)
        self.setLayout(self.layout)

    def create_input_field(self, label_text):
        layout = QHBoxLayout()
        label = QLabel(label_text)
        input_field = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(input_field)
        return layout, input_field

    def connect_signals(self, controller):
        self.add_button.clicked.connect(controller.add_task)
        self.mark_as_done_button.clicked.connect(controller.mark_selected_as_done)
        self.delete_button.clicked.connect(controller.delete_selected)

    def get_task_input(self):
        """
        Récupère les données du formulaire pour ajouter ou mettre à jour une tâche.
        :return: Instance de TaskEntity.
        """
        return TaskEntity(
            title=self.title_input.text(),
        )

    def display_tasks(self, tasks: list[TaskEntity]):
        """
        Affiche une liste de tâches dans le tableau.
        :param tasks: Liste d'objets TaskEntity.
        """
        self.table.setRowCount(len(tasks))
        for row, task_item in enumerate(tasks):
            # Ajouter l'ID de la tâche dans une colonne cachée
            self.table.setItem(row, 0, QTableWidgetItem(str(task_item.id)))

            # Ajouter une case à cocher pour la sélection
            checkbox = QCheckBox()
            checkbox_widget = QWidget()
            checkbox_layout = QHBoxLayout(checkbox_widget)
            checkbox_layout.addWidget(checkbox)
            checkbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            checkbox_layout.setContentsMargins(0, 0, 0, 0)
            self.table.setCellWidget(row, 1, checkbox_widget)

            self.table.setItem(row, 2, QTableWidgetItem(task_item.title))
            self.table.setItem(row, 3, QTableWidgetItem("Complétée" if task_item.mark_as_done else "Incomplète"))

    def show_message(self, message):
        """
        Affiche un message à l'utilisateur via une boîte de dialogue.
        :param message: Message à afficher.
        """
        QMessageBox.information(self, "Information", message)

    def get_selected_ids(self):
        """
        Récupère les IDs des tâches sélectionnées.
        :return: Liste des IDs des tâches sélectionnées.
        """
        selected_ids = []
        for row in range(self.table.rowCount()):
            checkbox_widget = self.table.cellWidget(row, 1)
            checkbox = checkbox_widget.findChild(QCheckBox)
            if checkbox.isChecked():
                task_id = int(self.table.item(row, 0).text())
                selected_ids.append(task_id)
        return selected_ids

    def set_controller(self, controller):
        """
        Définit le contrôleur pour la vue.
        :param controller: Instance de TaskController.
        """
        self.controller = controller
