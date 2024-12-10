from entities.task_entity import TaskEntity

class TaskManager:
    def __init__(self, repository):
        """
        Initialise le gestionnaire avec une instance de TaskRepository.
        """
        self.repository = repository

    def add_task(self, task_entity: TaskEntity) -> TaskEntity:
        """
        Ajoute une tâche via le repository et retourne la tâche avec son ID.
        :return: TaskEntity.
        """
        if task_entity.title:
            task_entity.id = self.repository.create(task_entity)
        return task_entity

    def get_all_tasks(self):
        """
        Récupère toutes les tâches.
        :return: Liste d'objets TaskEntity.
        """
        return self.repository.read_all()

    def get_task_by_id(self, task_id):
        """
        Récupère une tâche par son ID.
        :return: Instance de TaskEntity ou None.
        """
        return self.repository.read_by_id(task_id)

    def delete_task(self, task_id):
        """
        Supprime une tâche.
        :return: Booléen indiquant si la suppression a réussi.
        """
        return self.repository.delete(task_id)

    def mark_as_done(self, task_id, mark_as_done):
        """
        Met à jour l'état de mark_as_done pour une tâche.
        :param task_id: ID de la tâche.
        :param mark_as_done: Nouvel état de mark_as_done.
        :return: Booléen indiquant si la mise à jour a réussi.
        """
        return self.repository.update_mark_as_done(task_id, mark_as_done)

    def update_task(self, task_entity: TaskEntity):
        """
        Met à jour une tâche dans la base de données.
        :param task_entity: Instance de TaskEntity à mettre à jour.
        :return: Booléen indiquant si la mise à jour a réussi.
        """
        return self.repository.update(task_entity)
