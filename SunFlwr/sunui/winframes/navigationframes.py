from tkinter import ttk


class NavigationMenu(ttk.Frame):

    def __init__(self, parent, controller=None):
        ttk.Frame.__init__(self, parent)

        # buttons
        next_button = ttk.Button(master=parent, text='Continuar',
                                 command=lambda: print("Continuar Button"))
        back_button = ttk.Button(master=parent, text='Regresar',
                                 command=lambda: print("Continuar Button"))

        next_button.grid(column=0, row=0)
        back_button.grid(column=1, row=0)
