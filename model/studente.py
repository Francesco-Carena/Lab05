from dataclasses import dataclass

@dataclass
class Studente:
    matricola:str
    nome:str
    cognome:str
    CDS:str

    def __str__(self):
        return f"{self.matricola} - {self.nome} {self.cognome}"

    def __eq__(self, other):
        return self.matricola==other.matricola

    def __hash__(self):
        return hash(self.matricola)