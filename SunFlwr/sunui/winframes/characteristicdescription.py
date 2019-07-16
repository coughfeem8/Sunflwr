import tkinter as tk
from tkinter import ttk
from frameassets import LabeledEntryList
from navigationframes import NavigationMenu


class CharacteristicDescription(ttk.Frame):
    """docstring for CharacteristicDescription."""

    def __init__(self, master, controller=None):
        super(CharacteristicDescription, self).__init__(master)
        self.master = master
        self.controller = controller

        characteristics = [
            'Clasificación de la zona:',
            'Tipo de Construcción Dominante:',
            'Índice de Saturación:'
            'Población:',
            'Contaminación Ambiental:',
            'Uso de Suelo:',
            'Vías de Acceso Importantes:',
        ]
        descriptions = ['Uso actual:', 'Tipos Apreciados:', 'Unidades rentables:',
                        'Edad Aproximada de Construcción:', 'Vida Probable:',
                        'Calidad de Projecto:', 'Numero de Niveles:',
                        'Estado de Concervación:']

        # frames
        left_frame = ttk.Frame(self)
        right_frame = ttk.Frame(self)

        descriptions_label = ttk.Label(left_frame,
                                       text="Descripcion General del Inmueble")
        descriptions_entries = LabeledEntryList(left_frame, descriptions,
                                                controller=self.controller)
        characteristics_label = ttk.Label(right_frame,
                                          text="Caracteristicas Urbanas")
        characteristics_entries = LabeledEntryList(right_frame, characteristics,
                                                   controller=self.controller)

        nav_menu = NavigationMenu(self, controller=self.controller)

        # Layout
        left_frame.grid(row=0, column=0, columnspan=1, rowspan=1, padx=10)
        descriptions_label.grid(row=0, column=0, columnspan=1, rowspan=1)
        descriptions_entries.grid(row=1, column=0, columnspan=1, rowspan=1)

        right_frame.grid(row=0, column=1, columnspan=1,
                         rowspan=1, sticky='n', padx=10)
        characteristics_label.grid(row=0, column=0, columnspan=1, rowspan=1)
        characteristics_entries.grid(row=1, column=0, columnspan=1, rowspan=1)

        characteristics_entries.grid(row=2, column=0, columnspan=1, rowspan=1)
        nav_menu.grid(row=2, column=2, columnspan=1, rowspan=1, sticky='s')
        # spacing
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    w = (ws/5)*3  # 60%
    h = (hs/5)*3  # 60%
    root.geometry('%dx%d+%d+%d' %
                  (w, h,  (ws/2) - (w/2),  (hs/2) - (h/2) - 100))
    root.resizable(False, False)

    frame = CharacteristicDescription(root)
    frame.pack(expand=True)

    root.mainloop()
'''Layout :
----------------------------------------------------------
|                                                        |
|     Descripcion General      Caracteristicas Urbanas   |
|        del Inmueble                                    |
|                                                        |
|     label  [________]        label  [________]         |
|     label  [________]        label  [________]         |
|     label  [________]        label  [________]         |
|     label  [________]        label  [________]         |
|     label  [________]        label  [________]         |
|     label  [________]        label  [________]         |
|                                                        |
|                            [save]    [back]  [foward]  |
----------------------------------------------------------
'''
