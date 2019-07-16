import tkinter as tk
from tkinter import ttk
from navigationframes import NavigationMenu
from frameassets import CheckbuttonList


class ServicesEquipment(ttk.Frame):
    """docstring for ServicesEquipment.
    this frame will contain series of check boxes that will """

    def __init__(self, master, controller=None):
        super(ServicesEquipment, self).__init__(master)
        self.master = master
        self. controller = controller

        row_1_values = ['Energía Eléctrica', 'Alumbrado Publico',
                        'Agua Potable', 'Hidrantes',
                        'Drenaje Sanitario', 'Banquetas', 'Camellones',
                        'Guarniciones', 'Pavimento Asfáltico',
                        'Pavimento Hidráulico', 'Trasporte Publico']

        row_2_values = ['Áreas Ajardinadas', 'Arbotantes Metálicos',
                        'Postes de Madera y/o Concreto', 'Nomenclaturas',
                        'Señalamientos Viales', 'Semaforización',
                        'Televisión por Cable', 'Líneas Telefónicas',
                        'Gas Natural', 'Recolección de Basura', 'Otros']

        row_3_values = ['Vigilancia', 'Comercio de Barrio', 'Hospitales',
                        'Escuelas Básica', 'Escuelas Media', 'Iglesias',
                        'Industria', 'Centros Comerciales', 'Bancos',
                        'Oficinas de Gobierno']

        # FRAMES
        self.presets = Presets(self, controller=self.controller)
        self.row_one = CheckbuttonList(self, row_1_values, self.controller)
        self.row_two = CheckbuttonList(self, row_2_values, self.controller)
        self.row_three = CheckbuttonList(self, row_3_values, self.controller)
        self.nav_menu = NavigationMenu(self, controller=self.controller)

        # layout
        self.presets.grid(column=2, columnspan=4, row=0, sticky='we')
        self.row_one.grid(column=0, columnspan=2, row=1, rowspan=1)
        self.row_two.grid(column=3, columnspan=2, row=1, rowspan=1)
        self.row_three.grid(column=5, columnspan=2, row=1, rowspan=1)
        self.nav_menu.grid(column=4, columnspan=3, row=2, rowspan=1)

        # spacing

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)


class Presets(ttk.LabelFrame):
    """docstring for Presets."""

    def __init__(self, master, name='Presets', controller=None):
        super(Presets, self).__init__(master, text=name)
        self.master = master
        self.name = name
        self.controlelr = controller
        self.preset_option = tk.StringVar(value='')
        options = ['option 1', 'option 2']

        # frames
        options = ttk.Combobox(self, values=options,
                               textvariable=self.preset_option, width=10)
        options.current(0)
        save_button = ttk.Button(self, text='Guardar',
                                 command=lambda: print('Guardar Predeterminado'))
        load_button = ttk.Button(self, text='Cargar',
                                 command=lambda: print('Cargando Predeterminado'))
        delete_button = ttk.Button(self, text="Borrar",
                                   command=lambda: print('Borrando Predeterminado'))

        # Layout
        options.grid(column=0, row=0)
        save_button.grid(column=1, row=0)
        load_button.grid(column=2, row=0)
        delete_button.grid(column=3, row=0)

        # spacing


if __name__ == "__main__":
    root = tk.Tk()
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    w = (ws/5)*3  # 60%
    h = (hs/5)*3  # 60%
    root.geometry('%dx%d+%d+%d' %
                  (w, h,  (ws/2) - (w/2),  (hs/2) - (h/2) - 100))
    root.resizable(False, False)

    frame = ServicesEquipment(root)
    frame2 = ttk.Frame(root)

    frame.pack(expand=True)

    root.mainloop()

'''Layout :
----------------------------------------------------------
|                                                        |
|           ------------- presets -------------          |
|           |[[_____ V_] [add] [save] [remove]]|         |
|           -----------------------------------          |
|                                                        |
|     [] thing           [] thing           [] thing     |
|     [] thing           [] thing           [] thing     |
|     [] thing           [] thing           [] thing     |
|     [] thing           [] thing           [] thing     |
|     [] thing           [] thing           [] thing     |
|     [] thing           [] thing           [] thing     |
|     [] thing           [] thing           [] thing     |
|     [] thing                                           |
|                                                        |
|                            [save]    [back]  [foward]  |
----------------------------------------------------------
expanded :
----------------------------------------------------------------------------
|                                                        |                |^|
|           ------------- presets -------------          |    --------    | |
|           |[[_____ V_] [add] [save] [remove]]|         |    | img  |    | |
|           -----------------------------------          |    |      |    | |
|                                                        |    --------    | |
|     [] thing           [] thing           [] thing     |                |#|
|     [] thing           [] thing           [] thing     |                |#|
|     [] thing           [] thing           [] thing     |                |#|
|     [] thing           [] thing           [] thing     |                |#|
|     [] thing           [] thing           [] thing     |                | |
|     [] thing           [] thing           [] thing     |                | |
|     [] thing           [] thing           [] thing     |                | |
|     [] thing                                           |                | |
|                                                        |                | |
|                            [save]    [back]  [foward]  |                |v|
----------------------------------------------------------------------------

'''
