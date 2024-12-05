from entities.list_entity import ListEntity

class ListManager:
    def __init__(self, repository):
        """
        Initialise le gestionnaire avec une instance de ListRepository.
        """
        self.repository = repository

    def add_list(self, list_entity: ListEntity) -> ListEntity:
        """
        Ajoute une tâche via le repository et retourne la tâche avec son ID.
        :return: ListEntity.
        """
        if list_entity.title:
            list_entity.id = self.repository.create(list_entity)
        return list_entity

    def get_all_lists(self):
        """
        Récupère toutes les tâches.
        :return: Liste d'objets ListEntity.
        """
        return self.repository.read_all()

    def get_list_by_id(self, list_id):
        """
        Récupère une tâche par son ID.
        :return: Instance de ListEntity ou None.
        """
        return self.repository.read_by_id(list_id)

    def delete_list(self, list_id):
        """
        Supprime une tâche.
        :return: Booléen indiquant si la suppression a réussi.
        """
        return self.repository.delete(list_id)

    def mark_as_done(self, list_id, mark_as_done):
        """
        Met à jour l'état de mark_as_done pour une tâche.
        :param list_id: ID de la tâche.
        :param mark_as_done: Nouvel état de mark_as_done.
        :return: Booléen indiquant si la mise à jour a réussi.
        """
        return self.repository.update_mark_as_done(list_id, mark_as_done)
