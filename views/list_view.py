from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox
)

from entities.list_entity import ListEntity

class ListView(QWidget):
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
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Titre", "Statut", "Action"])

        # Ajuster la taille du tableau
        self.table.setFixedSize(800, 500)  # Définir une taille fixe pour le tableau

        # Ajuster la largeur des colonnes
        self.table.setColumnWidth(0, 300)  # Titre
        self.table.setColumnWidth(1, 100)  # Marqué comme terminé
        self.table.setColumnWidth(2, 150)  # Action

        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    def create_input_field(self, label_text):
        layout = QHBoxLayout()
        label = QLabel(label_text)
        input_field = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(input_field)
        return layout, input_field

    def connect_signals(self, controller):
        self.add_button.clicked.connect(controller.add_list)

    def get_list_input(self):
        """
        Récupère les données du formulaire pour ajouter ou mettre à jour une tâche.
        :return: Instance de ListEntity.
        """
        return ListEntity(
            title=self.title_input.text(),
        )



    def display_lists(self, lists: list[ListEntity]):
        """
        Affiche une liste de tâches dans le tableau.
        :param lists: Liste d'objets ListEntity.
        """
        self.table.setRowCount(len(lists))
        for row, list in enumerate(lists):
            self.table.setItem(row, 0, QTableWidgetItem(list.title))
            self.table.setItem(row, 1, QTableWidgetItem("Complètée" if list.mark_as_done else "Incomplète"))

            # Ajouter un bouton "Marquer comme terminé"
            mark_as_done_button = QPushButton("Marquer comme terminé")
            mark_as_done_button.clicked.connect(lambda _, list_id=list.id: self.mark_as_done_clicked(list_id))
            self.table.setCellWidget(row, 2, mark_as_done_button)

            # Ajouter un bouton "Supprimer"
            delete_button = QPushButton("Supprimer")
            delete_button.clicked.connect(lambda _, list_id=list.id: self.delete_clicked(list_id))
            self.table.setCellWidget(row, 3, delete_button)

    def display_list(self, list: ListEntity):
        """
        Affiche les détails d'une seule tâche dans le formulaire.
        :param list: Instance de ListEntity.
        """
        self.list_id_input.setText(str(list.id))
        self.title_input.setText(list.title)

    def show_message(self, message):
        """
        Affiche un message à l'utilisateur via une boîte de dialogue.
        :param message: Message à afficher.
        """
        QMessageBox.information(self, "Information", message)

    def mark_as_done_clicked(self, list_id):
        """
        Méthode appelée lorsque le bouton "Marquer comme terminé" est cliqué.
        :param list_id: ID de la tâche à marquer comme terminée.
        """
        self.controller.mark_as_done(list_id)

    def delete_clicked(self, list_id):
        """
        Méthode appelée lorsque le bouton "Supprimer" est cliqué.
        :param list_id: ID de la tâche à supprimer.
        """
        self.controller.delete_list(list_id)


    def set_controller(self, controller):
        """
        Définit le contrôleur pour la vue.
        :param controller: Instance de ListController.
        """
        self.controller = controller
