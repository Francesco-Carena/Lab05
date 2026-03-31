from database.studente_DAO import studente_DAO
from database.corso_DAO import corso_DAO
from database.iscrizione_DAO import iscrizione_DAO

class Model:
    def __init__(self):
        pass

    def getAllCorsi(self):
        return corso_DAO.getAllCorsi()

    def getStudentiIscritti(self,codcorso):
        return studente_DAO.getStudentiIscritti(codcorso)

    def getStudente(self, matricola):
        return studente_DAO.getStudente(matricola)

    def getCorsiStudente(self,matricola):
        return corso_DAO.getCorsiStudente(matricola)

    def getCorso(self,codcorso):
        return corso_DAO.getCorso(codcorso)

    def checkIscrizione(self,matricola,codcorso):
        return iscrizione_DAO.checkIscrizione(matricola,codcorso)

    def newIscrizione(self, matricola, codcorso):
        iscrizione_DAO.newIscrizione(matricola, codcorso)
        return