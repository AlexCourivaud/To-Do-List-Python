from entities.list_entity import ListEntity

class ListManager:
    def __init(self, repository):
        """
        Initialise le gestionnaire avec une instance de ListRepository.
        """
        self.repository = repository

    def add_list(self, list_entity: ListEntity) -> ListEntity:
        """
        Ajoute un livre via le repository et retourne le livre avec son ID.
        :return: ListEntity.
        """

        if (not list_entity.title == "" ):

            list_entity.id = self.repository.create(list_entity)
        
        return list_entity
    
