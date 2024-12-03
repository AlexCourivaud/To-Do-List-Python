import sys

from views.list_view import ListView
from PyQt6.QtWidgets import QApplication
from repositories.list_repository import ListRepository
from managers.list_manager import ListManager
from controllers.list_controller import ListController

if __name__ == "__main__":

    app = QApplication(sys.argv)

    repo = ListRepository(host="localhost", database="library", user="myuser", password="mypassword")
    
    manager = ListManager(repo)

    view = ListView()
    
    controller = ListController(manager, view)

    # Connecter les signaux et afficher la fenêtre
    view.connect_signals(controller)
    view.show()

    sys.exit(app.exec_())