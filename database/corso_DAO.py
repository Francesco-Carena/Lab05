# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso

class corso_DAO():

    @staticmethod
    def getAllCorsi():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                   from corso"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(
                codins=row["codins"],
                nome=row["nome"],
                crediti=row["crediti"],
                pd=row["pd"],
            ))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiStudente(matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select c.*
                from corso c, iscrizione i
                where i.matricola = %s and c.codins = i.codins """
        cursor.execute(query, (matricola,))

        res = []
        for row in cursor:
            res.append(Corso(
                codins=row["codins"],
                nome=row["nome"],
                crediti=row["crediti"],
                pd=row["pd"],
            ))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorso(codcorso):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select c.*
                   from corso c
                   where c.codins = %s """
        cursor.execute(query, (codcorso,))

        row = cursor.fetchone()

        if row is None:
            cursor.close()
            cnx.close()
            return None

        res= Corso(
            codins=row["codins"],
            nome=row["nome"],
            crediti=row["crediti"],
            pd=row["pd"],
        )
        cursor.close()
        cnx.close()
        return res
