import flet as ft
from UI import controller


class View(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        # text field for the name
        self.ddCorso=ft.Dropdown(label="corso", width=800)
        self._controller.fillddCorsi()
        self.txtMatricola=ft.TextField(label="Matricola",width=270)
        self.txtNome = ft.TextField(label="Nome", width=270)
        self.txtCognome = ft.TextField(label="Cognome", width=270)

        # button for the "hello" reply
        self.btnCercaIscritti=ft.ElevatedButton(text="Cerca Iscritti",on_click=self._controller.handleCercaIscritti)
        self.btnCercaStudente = ft.ElevatedButton(text="Cerca Studente", on_click=self._controller.handleCercaStudente,width=230)
        self.btnCercaCorsi = ft.ElevatedButton(text="Cerca Corsi", on_click=self._controller.handleCercaCorsi,width=230)
        self.btnIscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handleIscrivi,width=230)


        # List View where the reply is printed
        self.lvOut = ft.ListView(expand=True, spacing=10, padding=20)
        #self.lvOut = ft.ListView(height=300, spacing=10, padding=20)

        self.row1=ft.Row([self.ddCorso,self.btnCercaIscritti], alignment = ft.MainAxisAlignment.CENTER)
        self.row2=ft.Row([self.txtMatricola,self.txtNome,self.txtCognome], alignment = ft.MainAxisAlignment.CENTER)
        self.row3=ft.Row([self.btnCercaStudente,self.btnCercaCorsi,self.btnIscrivi], alignment = ft.MainAxisAlignment.CENTER)
        self.row4=ft.Row([self.lvOut])

        self._page.add(self.row1,self.row2,self.row3,self.row4)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
