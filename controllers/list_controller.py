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
        self.view.set_controller(self)

    def add_list(self):
        """
        Ajoute une TACHE via les données saisies dans la vue.
        """
        list_entity: ListEntity = self.view.get_list_input()

        list_entity = self.manager.add_list(list_entity)

        if list_entity.id:
            self.view.show_message(f"Tâche '{list_entity.title}' ajoutée avec succès.")
            self.refresh_lists()
        else:
            self.view.show_message(f"Échec de l'ajout d'une tâche")

    def delete_list(self, list_id):
        """
        Supprime une tâche via son ID saisi dans la vue.
        """
        list_entity = self.manager.get_list_by_id(list_id)
        if list_entity:
            is_deleted = self.manager.delete_list(list_id)
            if is_deleted:
                self.view.show_message(f"Tâche '{list_entity.title}' supprimée avec succès.")
                self.refresh_lists()
            else:
                self.view.show_message("Échec de la suppression : Tâche non trouvée.")
        else:
            self.view.show_message("Échec de la suppression : Tâche non trouvée.")

    def mark_as_done(self, list_id):
        """
        Marque une tâche comme terminée.
        :param list_id: ID de la tâche à marquer comme terminée.
        """
        list_entity = self.manager.get_list_by_id(list_id)
        if list_entity:
            new_mark_as_done = not list_entity.mark_as_done
            is_updated = self.manager.mark_as_done(list_id, new_mark_as_done)
            if is_updated:
                self.view.show_message(f"Tâche '{list_entity.title}' marquée comme {'terminée' if new_mark_as_done else 'non terminée'}.")
                self.refresh_lists()
            else:
                self.view.show_message("Échec de la mise à jour de la tâche.")
        else:
            self.view.show_message("Échec de la mise à jour : Tâche non trouvée.")

    def refresh_lists(self):
        """
        Rafraîchit la liste des tâches affichées dans la vue.
        """
        lists = self.manager.get_all_lists()
        self.view.display_lists(lists)
