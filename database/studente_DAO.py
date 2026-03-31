# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente

class studente_DAO():
    @staticmethod
    def getAllStudenti():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                   from studente"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Studente(
                matricola=row["matricola"],
                nome=row["nome"],
                cognome=row["cognome"],
                CDS=row["CDS"],
            ))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStudentiIscritti(codcorso):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                from studente s, iscrizione i
                where s.matricola = i.matricola and i.codins = %s
                   """
        cursor.execute(query,(codcorso,))

        res = []
        for row in cursor:
            res.append(Studente(
                matricola=row["matricola"],
                nome=row["nome"],
                cognome=row["cognome"],
                CDS=row["CDS"],
            ))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStudente(matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                   from studente s 
                   where s.matricola = %s
                """
        cursor.execute(query, (matricola,))

        row = cursor.fetchone()

        if row is None:
            cursor.close()
            cnx.close()
            return None  # Restituisce None se lo studente non esiste

        # Creiamo un SINGOLO oggetto Studente, non una lista
        res = Studente(
            matricola=row["matricola"],
            nome=row["nome"],
            cognome=row["cognome"],
            CDS=row["CDS"],
        )

        cursor.close()
        cnx.close()
        return res