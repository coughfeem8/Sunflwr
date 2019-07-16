import tkinter as tk
from tkinter import ttk
from frameassets import LabeledEntryList
from navigationframes import NavigationMenu


class LandDescription(ttk.Frame):
    """docstring for LandDescription."""

    def __init__(self, master, controller=None):
        super(LandDescription, self).__init__(master)
        self.master = master
        self.controller = controller

        # frames
        labels = ['Uso Actual del Terreno:', 'Configuracion del Terreno:',
                  'Servidumbre y/o Restricciones', 'Topografia del Terreno',
                  'Caracteristicas panoramicas:']
        descriptions = LabeledEntryList(self, labels, width=30)
        description_label = ttk.Label(self, text='Descripcion de Terreno:')
        land_description = tk.Text(self, width=40, height=20)

        # layout
        descriptions.grid(row=0, column=0, columnspan=2, rowspan=5)
        description_label.grid(row=5, column=0, columnspan=1, rowspan=1)
        descriptions.grid(row=6, column=0, columnspan=2, rowspan=2)

        # spacing


class MeasumentsAndAdjencies(ttk.Frame):
    """docstring for MeasumentsAndAdjencies."""

    def __init__(self, master, controller=None):
        super(MeasumentsAndAdjencies, self).__init__(master)
        self.master = master
        self.controller = controller

        # frames
        # layout
        # spacing


class LandMeasurements(ttk.Frame):
    """docstring for LandMeasurements."""

    def __init__(self, master, controller=None):
        super(LandMeasurements, self).__init__(master)
        self.master = master
        self.controller = controller

        # frames

        # layout
        # spacing


class MeasumentsTable(ttk.Frame):
    """docstring for MeasumentsTable."""

    def __init__(self, master, controller=None):
        super(MeasumentsTable, self).__init__(master)
        self.master = master
        self.controller = controller

        # frames
        # layout
        # spacing


class SurfaceTable(ttk.Frame):
    """docstring for SurfaceTable."""

    def __init__(self, master, controller=None):
        super(SurfaceTable, self).__init__(master)
        self.master = master
        self.controller = controller

        # frames
        # layout
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

    frame = LandDescription(root)
    frame.pack(expand=True)

    root.mainloop()
'''Layout :
-------------------------------------------------------------------------------
|                                                                             |
|          Uso Actual                                                         |
|         del  Terreno:                  [_________]                          |
|         Configuracion del Terreno:     [_________]                          |
|         Topografia del Terreno:        [_________]                          |
|         Caracteristicas panoramicas:   [_________]                          |
|         Servidumbre y/o Restricciones: [_________]                          |
|                                                                             |
|        Descripcion del Terreno:                                             |
|        -----------------------                                              |
|        |                      |                                             |
|        |                      |                                             |
|        -----------------------                                              |
|                                        -------------------------------------|
|        ---medidas y conlindancias--    | Lado | Rumbo| Medida |Colindancia| |
|        |  lado:         [_____]   |    |----------------------------------|^|
|        |  Rumbo:        [_____]   |    | ~~~~   ~~~~~  ~~~~~~  ~~~~~~~~~~ | |
|        |  Medida:       [_____]   |    | ~~~~   ~~~~~  ~~~~~~  ~~~~~~~~~~ |#|
|        |  Colindancia:  [_____]   |    | ~~~~   ~~~~~  ~~~~~~  ~~~~~~~~~~ |#|
|        |           [add] [clear]  |    | ~~~~   ~~~~~  ~~~~~~  ~~~~~~~~~~ | |
|        ----------------------------    | ~~~~   ~~~~~  ~~~~~~  ~~~~~~~~~~ | |
|                                        |----------------------------------| |
|        ---superficie de La--------     |                                  |V|
|        |    Construccion          |    |   Nombre  medida    unidad       |^|
|        |  Nombre:        [_____]  |    | ~~~~~~~~~~  ~~~~~~  ~~~~~~~~~~   | |
|        |  Medida:        [_____]  |    | ~~~~   ~~~~~  ~~~~~~  ~~~~~~~~~~ |#|
|        |  Unidad:        [____V]  |    | ~~~~   ~~~~~  ~~~~~~  ~~~~~~~~~~ |#|
|        |                          |    | ~~~~   ~~~~~  ~~~~~~  ~~~~~~~~~~ | |
|        |           [add] [clear]  |    | ~~~~   ~~~~~  ~~~~~~  ~~~~~~~~~~ | |
|        ----------------------------    | ~~~~   ~~~~~  ~~~~~~  ~~~~~~~~~~ |V|
|                                        -------------------------------------|
|                                                                             |
|                                                 [save]    [back]  [forward] |
-------------------------------------------------------------------------------
'''
