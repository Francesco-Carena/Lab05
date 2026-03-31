from database.DB_connect import get_connection
from model.studente import Studente

class iscrizione_DAO():

    @staticmethod
    def checkIscrizione(matricola, codcorso):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                   from iscrizione i
                   where i.matricola = %s and i.codins = %s """
        cursor.execute(query, (matricola, codcorso))
        row = cursor.fetchone()

        if row is None:
            cursor.close()
            cnx.close()
            return False

        cursor.close()
        cnx.close()
        return True

    @staticmethod
    def newIscrizione(matricola, codcorso):
        cnx = get_connection()

        cursor = cnx.cursor()
        query = """insert into iscrizione (matricola, codins) \
                   values (%s, %s)"""
        cursor.execute(query, (matricola, codcorso))

        cnx.commit()
        cursor.close()
        cnx.close()
        return
