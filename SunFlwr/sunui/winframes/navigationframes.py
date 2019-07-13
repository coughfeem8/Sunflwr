from tkinter import ttk
import tkinter as tk


class NavigationMenu(ttk.Frame):

    def __init__(self, master, controller=None):
        super(NavigationMenu, self).__init__(master)
        self.controller = controller
        self.master = master
        # buttons
        next_button = ttk.Button(master=self, text='Continuar',
                                 command=lambda: print("Siguiente Seccion"))
        back_button = ttk.Button(master=self, text='Regresar',
                                 command=lambda: print("Seccion Anterior"))
        save_button = ttk.Button(master=self, text='Guardar',
                                 command=lambda: print("Avaluo Guardado"))

        next_button.grid(column=0, row=0)
        save_button.grid(column=1, row=0)
        back_button.grid(column=2, row=0)


class StartWindowMenu(ttk.Frame):
    """docstring for StartWindowMenu."""

    def __init__(self, master, controller=None):
        super(StartWindowMenu, self).__init__(master)
        self.controller = controller
        self.master = master
        # menu buttons
        new_button = ttk.Button(self, text='Crear Avaluo',
                                command=lambda: print('Crear Avaluo'))
        open_button = ttk.Button(self, text='Abrir Avaluo',
                                 command=lambda: print('Abrir Avaluo'))
        cancel_button = ttk.Button(self, text='Cancelar',
                                   command=lambda: print("Cancelar"))

        new_button.grid(column=1, row=0, sticky='we')
        open_button.grid(column=2, row=0, sticky='we')
        cancel_button.grid(column=3, row=1, sticky='we', padx=10, pady=10)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
