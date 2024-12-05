from entities.list_entity import ListEntity

class ListController:
    def __init__(self, manager, view):
        """
        Initialise le contrôleur avec un gestionnaire et une vue.
        :param manager: Instance de ListManager.
        :param view: Instance de ListView.
        """
        self.manager = manager
        self.view = view

    def add_list(self):
        """
        Ajoute une Liste via les données saisies dans la vue.
        """
        list_entity: ListEntity = self.view.get_list_input()

        list_entity = self.manager.add_list(list_entity)

        if list_entity.id:
            self.view.display_list(list_entity)
            self.view.show_message(f"liste ajoutée avec succès avec l'ID : {list_entity.id}")
        else:
            self.view.show_message(f"Echec de l'ajout d'une liste")

    def update_list(self):
        """
        Met à jour une Liste via les données saisies dans la vue.
        """
        list_entity = self.view.get_list_input()
        updated_list = self.manager.update_list(list_entity)
        if updated_list:
            self.view.show_message(f"Liste mis à jour avec succès : {updated_list}")
        else:
            self.view.show_message("Mise à jour échouée : Liste non trouvé.")






    def delete_list(self):
        """
        Supprime une liste via son ID saisi dans la vue.
        """
        list_id = self.view.get_list_id()
        is_deleted = self.manager.delete_list(list_id)
        if is_deleted:
            self.view.show_message(f"Liste avec l'ID {list_id} supprimé avec succès.")
        else:
            self.view.show_message("Échec de la suppression : Liste non trouvé.")

      
