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
      
