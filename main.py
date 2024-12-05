import sys

from managers.list_manager import ListManager
from repositories.list_repository import ListRepository
from views.list_view import ListView
from controllers.list_controller import ListController
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    repo = ListRepository(host="localhost", database="listmanager", user="root", password="")
    manager = ListManager(repo)
    view = ListView()
    controller = ListController(manager, view)

    # Connecter les signaux et afficher la fenêtre
    view.connect_signals(controller)
    view.show()
    controller.refresh_lists()

    sys.exit(app.exec())
