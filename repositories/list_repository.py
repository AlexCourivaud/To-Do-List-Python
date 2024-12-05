import mysql.connector
from mysql.connector import Error
from entities.list_entity import ListEntity

class ListRepository:
    def __init__(self, host, database, user, password):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                port=3306,
                database=database,
                user=user,
                password=password
            )
            if self.connection.is_connected():
                print("Connexion à la base de données réussie")
            else:
                print("Connexion à la base de données échouée")
        except mysql.connector.Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
            self.connection = None

    def create(self, list_entity) -> int:
        """
        Insère une tâche dans la base de données et retourne l'ID généré.
        :param list_entity: Instance de ListEntity contenant les données.
        :return: ID de la tâche créée.
        """
        query = "INSERT INTO list (title, mark_as_done) VALUES (%s, %s)"
        values = (list_entity.title, list_entity.mark_as_done)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Erreur lors de l'ajout de la tâche : {e}")
            return None

    def read_all(self):
        """
        Récupère toutes les tâches sous forme d'objets ListEntity.
        :return: Liste d'instances de ListEntity.
        """
        query = "SELECT * FROM list"
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            lists = cursor.fetchall()
            return [ListEntity(list["id"], list["title"], list["mark_as_done"]) for list in lists]
        except Error as e:
            print(f"Erreur lors de la récupération des tâches : {e}")
            return []

    def read_by_id(self, list_id):
        """
        Récupère une tâche par son ID.
        :param list_id: ID de la tâche.
        :return: Instance de ListEntity ou None si non trouvé.
        """
        query = "SELECT * FROM list WHERE id = %s"
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, (list_id,))
            list = cursor.fetchone()
            return ListEntity(
                list["id"],
                list["title"],
                list["mark_as_done"]
            ) if list else None
        except Error as e:
            print(f"Erreur lors de la récupération de la tâche : {e}")
            return None

    def delete(self, list_id):
        """
        Supprime une tâche par son ID.
        :param list_id: ID de la tâche.
        :return: Booléen indiquant si la suppression a été effectuée.
        """
        query = "DELETE FROM list WHERE id = %s"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (list_id,))
            self.connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Erreur lors de la suppression de la tâche : {e}")
            return False

    def update_mark_as_done(self, list_id, mark_as_done):
        """
        Met à jour l'état de mark_as_done pour une tâche.
        :param list_id: ID de la tâche.
        :param mark_as_done: Nouvel état de mark_as_done.
        :return: Booléen indiquant si la mise à jour a réussi.
        """
        query = "UPDATE list SET mark_as_done = %s WHERE id = %s"
        values = (mark_as_done, list_id)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Erreur lors de la mise à jour de la tâche : {e}")
            return False

    def __del__(self):
        """
        Ferme la connexion à la base de données.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Connexion à la base de données fermée")
