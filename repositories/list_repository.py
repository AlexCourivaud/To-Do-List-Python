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
            else :
                print("Connexion à la base de données échouée")
        except mysql.connector.Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
            self.connection = None



    def create(self, list_entity) -> int:
        """
        Insère une liste dans la base de données et retourne l'ID généré.
        :param list_entity: Instance de ListEntity contenant les données.
        :return: ID de la liste créé.
        """
        query = """
        INSERT INTO list title
        """
        values = (list_entity.title)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Erreur lors de l'ajout de la liste : {e}")
            return None
