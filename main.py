import sys

from managers.task_manager import TaskManager
from repositories.task_repository import TaskRepository
from views.task_view import TaskView
from controllers.task_controller import TaskController
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)


    repo = TaskRepository(host="localhost", database="listmanager", user="root", password="")
    manager = TaskManager(repo)
    view = TaskView()
    controller = TaskController(manager, view)

    # Connecter les signaux et afficher la fenêtre
    view.connect_signals(controller)
    view.show()

    # Rafraîchir la liste des tâches au démarrage
    controller.refresh_tasks()

    sys.exit(app.exec())