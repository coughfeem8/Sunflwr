from tkinter import ttk
import tkinter as tk
from navigationframes import NavigationMenu
from frameassets import LabeledEntryList


class NewEvaluation(ttk.Frame):

    def __init__(self, master, controller=None):
        super(NewEvaluation, self).__init__(master)

        self.master = master
        self.controller = controller

        house_info = ['Solicitate Del Avalúo: ', 'Propetario del Inmueble: ',
                      'Ubicación:']
        photos_labels = ['Fachada:', 'Fotos:']

        # FRAMES
        house = LabeledEntryList(self, house_info, width=15)
        validate_button = ttk.Button(self, text="Validar",
                                     command=lambda: print('validando direccion'))
        photos = LabeledEntryList(self, photos_labels, width=15)
        facade_button = ttk.Button(self, text='...', width=3,
                                   command=lambda: print('choose facade'))
        photos_button = ttk.Button(self, text='...', width=3,
                                   command=lambda: print('select pictures'))
        nav_menu = NavigationMenu(self, controller)

        # Layout
        house.grid(row=0, column=1, columnspan=2, rowspan=3)
        photos.grid(row=3, column=1, columnspan=2, rowspan=2, sticky='e')

        validate_button.grid(row=2, column=3, columnspan=1, rowspan=1)
        facade_button.grid(row=3, column=3, columnspan=1, rowspan=1)
        photos_button.grid(row=4, column=3, columnspan=1, rowspan=1)
        nav_menu.grid(row=5, column=2, columnspan=3, rowspan=1)

        # spacing
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    w = (ws/5)*3  # 60%
    h = (hs/5)*3  # 60%
    root.geometry('%dx%d+%d+%d' %
                  (w, h,  (ws/2) - (w/2),  (hs/2) - (h/2) - 100))
    root.resizable(False, False)

    frame = NewEvaluation(root)
    frame2 = ttk.Frame(root)

    frame.pack(expand=True)
    root.mainloop()

'''Layout :
----------------------------------------------------------
|                                                        |
|        Solicitante: [__persona___]                     |
|                                                        |
|        Propietario: [__persona___]                     |
|                                                        |
|        Ubication:   [_321 Street.Dr_]  [validar]       |
|                                                        |
|                                                        |
|        Fachada [fachada.jpeg]         [...]            |
|                                                        |
|        Fotos: [foto.jpeg,foto2.jpeg]  [...]            |
|                                                        |
|                            [save]    [back]  [foward]  |
----------------------------------------------------------
'''
