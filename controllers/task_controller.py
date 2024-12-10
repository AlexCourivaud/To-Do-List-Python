from entities.task_entity import TaskEntity

class TaskController:
    def __init__(self, manager, view):
        """
        Initialise le contrôleur avec un gestionnaire et une vue.
        :param manager: Instance de TaskManager.
        :param view: Instance de TaskView.
        """
        self.manager = manager
        self.view = view
        self.view.set_controller(self)

    def add_task(self):
        """
        Ajoute une TACHE via les données saisies dans la vue.
        """
        task_entity: TaskEntity = self.view.get_task_input()

        task_entity = self.manager.add_task(task_entity)

        if task_entity.id:
            self.view.show_message(f"Tâche '{task_entity.title}' ajoutée avec succès.")
            self.refresh_tasks()
        else:
            self.view.show_message(f"Échec de l'ajout d'une tâche")

    def delete_selected(self):
        """
        Supprime les tâches sélectionnées.
        """
        selected_ids = self.view.get_selected_ids()
        if selected_ids:
            for task_id in selected_ids:
                task_entity = self.manager.get_task_by_id(task_id)
                if task_entity:
                    is_deleted = self.manager.delete_task(task_id)
                    if is_deleted:
                        self.view.show_message(f"Tâche '{task_entity.title}' supprimée avec succès.")
                    else:
                        self.view.show_message("Échec de la suppression : Tâche non trouvée.")
            self.refresh_tasks()
        else:
            self.view.show_message("Veuillez sélectionner au moins une tâche à supprimer.")

    def mark_selected_as_done(self):
        """
        Marque les tâches sélectionnées comme terminées.
        """
        selected_ids = self.view.get_selected_ids()
        if selected_ids:
            for task_id in selected_ids:
                task_entity = self.manager.get_task_by_id(task_id)
                if task_entity:
                    new_mark_as_done = not task_entity.mark_as_done
                    is_updated = self.manager.mark_as_done(task_id, new_mark_as_done)
                    if is_updated:
                        self.view.show_message(f"Tâche '{task_entity.title}' marquée comme {'terminée' if new_mark_as_done else 'non terminée'}.")
                    else:
                        self.view.show_message("Échec de la mise à jour de la tâche.")
            self.refresh_tasks()
        else:
            self.view.show_message("Veuillez sélectionner au moins une tâche à marquer comme terminée.")

    def refresh_tasks(self):
        """
        Rafraîchit la liste des tâches affichées dans la vue.
        """
        tasks = self.manager.get_all_tasks()
        self.view.display_tasks(tasks)
