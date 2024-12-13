import mysql.connector
from mysql.connector import Error
from entities.task_entity import TaskEntity

class TaskRepository:
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

    def create(self, task_entity) -> int:
        """
        Insère une tâche dans la base de données et retourne l'ID généré.
        :param task_entity: Instance de TaskEntity contenant les données.
        :return: ID de la tâche créée.
        """
        query = "INSERT INTO task (title, mark_as_done) VALUES (%s, %s)"
        values = (task_entity.title, task_entity.mark_as_done)
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
        Récupère toutes les tâches sous forme d'objets TaskEntity.
        :return: Liste d'instances de TaskEntity.
        """
        query = "SELECT * FROM task"
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            tasks = cursor.fetchall()
            return [TaskEntity(task["id"], task["title"], task["mark_as_done"]) for task in tasks]
        except Error as e:
            print(f"Erreur lors de la récupération des tâches : {e}")
            return []

    def read_by_id(self, task_id):
        """
        Récupère une tâche par son ID.
        :param task_id: ID de la tâche.
        :return: Instance de TaskEntity ou None si non trouvé.
        """
        query = "SELECT * FROM task WHERE id = %s"
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, (task_id,))
            task = cursor.fetchone()
            return TaskEntity(
                task["id"],
                task["title"],
                task["mark_as_done"]
            ) if task else None
        except Error as e:
            print(f"Erreur lors de la récupération de la tâche : {e}")
            return None

    def delete(self, task_id):
        """
        Supprime une tâche par son ID.
        :param task_id: ID de la tâche.
        :return: Booléen indiquant si la suppression a été effectuée.
        """
        query = "DELETE FROM task WHERE id = %s"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (task_id,))
            self.connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Erreur lors de la suppression de la tâche : {e}")
            return False

    def update_mark_as_done(self, task_id, mark_as_done):
        """
        Met à jour l'état de mark_as_done pour une tâche.
        :param task_id: ID de la tâche.
        :param mark_as_done: Nouvel état de mark_as_done.
        :return: Booléen indiquant si la mise à jour a réussi.
        """
        query = "UPDATE task SET mark_as_done = %s WHERE id = %s"
        values = (mark_as_done, task_id)
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
