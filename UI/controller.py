import flet as ft

from database.corso_DAO import corso_DAO
from model.model import Model
from model.studente import Studente
from model.corso import Corso

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCercaIscritti(self,e):
        self._view.lvOut.controls.clear()
        codCorso=self._view.ddCorso.value
        if codCorso is None:
            self._view.create_alert("Selezionare un corso!")
            return

        listaStudenti=self._model.getStudentiIscritti(codCorso)
        self._view.lvOut.controls.append(ft.Text(f"Ci sono {len(listaStudenti)} iscritti al corso"))
        for s in listaStudenti:
            self._view.lvOut.controls.append(ft.Text(s.__str__()))
        self._view.update_page()
        return

    def handleCercaStudente(self,e):
        self._view.txtNome.value=""
        self._view.txtCognome.value=""
        matricola=self._view.txtMatricola.value
        if not matricola:
            self._view.create_alert("Inserisci una matricola!")
            return

        studente=self._model.getStudente(matricola)

        if studente is None:
            self._view.create_alert("Matricola non trovata nel database!")
            self._view.txtNome.value = ""
            self._view.txtCognome.value = ""
            return
        self._view.txtNome.value=studente.nome
        self._view.txtCognome.value=studente.cognome
        self._view.update_page()
        return

    def handleCercaCorsi(self,e):
        self._view.txtNome.value = ""
        self._view.txtCognome.value = ""
        self._view.lvOut.controls.clear()

        matricola = self._view.txtMatricola.value
        if not matricola:
            self._view.create_alert("Inserisci una matricola!")
            return

        studente = self._model.getStudente(matricola)

        if studente is None:
            self._view.create_alert("Matricola non trovata nel database!")
            self._view.txtNome.value = ""
            self._view.txtCognome.value = ""
            return

        listaCorsi = self._model.getCorsiStudente(matricola)
        self._view.lvOut.controls.append(ft.Text(f"Ci sono {len(listaCorsi)} corsi a cui è iscritto"))
        for c in listaCorsi:
            self._view.lvOut.controls.append(ft.Text(c.__str__()))
        self._view.update_page()
        return



    def handleIscrivi(self,e):
        #self._view.txtNome.value = ""
        #self._view.txtCognome.value = ""
        self._view.lvOut.controls.clear()

        matricola = self._view.txtMatricola.value
        if not matricola or not matricola.isdigit():
            self._view.create_alert("Inserisci una matricola!")
            return

        studente = self._model.getStudente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non trovata nel database!")
            self._view.txtNome.value = ""
            self._view.txtCognome.value = ""
            self._view.update_page()
            return
        self._view.txtNome.value = studente.nome
        self._view.txtCognome.value = studente.cognome
        self._view.update_page()

        codCorso = self._view.ddCorso.value
        if codCorso is None:
            self._view.create_alert("Selezionare un corso!")
            return

        if self._model.checkIscrizione(matricola,codCorso):
            self._view.create_alert(f"Studente {studente.nome} {studente.cognome} già iscritto al corso")
            self._view.txtNome.value = ""
            self._view.txtCognome.value = ""
            return

        try:
            self._model.newIscrizione(matricola, codCorso)
            self._view.lvOut.controls.append(
                ft.Text(f"Iscrizione di {studente.nome} {studente.cognome} avvenuta con successo!",
                        color="green")
            )
        except Exception as ex:
            self._view.create_alert(f"Errore tecnico durante l'iscrizione: {ex}")
        self._view.update_page()
        return




    def fillddCorsi(self):
        for c in self._model.getAllCorsi():
            self._view.ddCorso.options.append(ft.dropdown.Option(
                key=c.codins,
                text=c.__str__(),
                data=c,
                on_click=self._choiceDDCodins
            ))
        self._view.update_page()
        return

    def _choiceDDCodins(self,e):
        self._ddCodInsValue=e.control.data
        print(self._ddCodInsValue)
