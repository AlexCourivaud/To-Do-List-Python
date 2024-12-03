import sys



from views.list_view import ListView
from PyQt6.QtWidgets import QApplication


if __name__ == "__main__":

    app = QApplication(sys.argv)

    repo = ListRepository(host="localhost", database="library", user="myuser", password="mypassword")
    
    manager = BookManager(repo)

    view = BookView()
    
    controller = BookController(manager, view)

    # Connecter les signaux et afficher la fenêtre
    view.connect_signals(controller)
    view.show()

    sys.exit(app.exec_())