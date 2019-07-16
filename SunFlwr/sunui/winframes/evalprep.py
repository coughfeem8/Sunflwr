import tkinter as tk
from tkinter import ttk
from frameassets import LabeledEntryList
from navigationframes import NavigationMenu


class EvaluationPreparation(ttk.Frame):
    '''Docstring'''

    def __init__(self, master, controller=None):
        super(EvaluationPreparation, self).__init__(master)
        self.master = master
        self.controller = controller
        self.type = tk.StringVar('')

        self['borderwidth'] = 5
        self['relief'] = 'sunken'

        # frames
        labels = ['Proposito de Avaluo:',
                  'Destino del Avaluo:', 'Clave Castastral:']
        types = ['Avaluo Standard', 'type one', 'type two']

        self.entry_list = LabeledEntryList(self, labels, width=20)
        self.eval_type_label = ttk.Label(self, text='Tipo de Avaluo:')
        self.eval_type = ttk.Combobox(self, textvariable=self.type,
                                      values=types, width=10)
        self.eval_type.current(0)
        self.nav_menu = NavigationMenu(self)

        # layout
        self.entry_list.grid(column=0, columnspan=2, rowspan=3, row=0)
        self.eval_type_label.grid(column=3, row=2)
        self.eval_type.grid(column=3, row=3)
        self.nav_menu.grid(columnspan=3, column=1, row=4)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure(2, weight=4)


if __name__ == "__main__":
    root = tk.Tk()
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    w = (ws/5)*3  # 60%
    h = (hs/5)*3  # 60%
    root.geometry('%dx%d+%d+%d' %
                  (w, h,  (ws/2) - (w/2),  (hs/2) - (h/2) - 100))
    root.resizable(False, False)

    frame = EvaluationPreparation(root)
    frame2 = ttk.Frame(root)

    frame.pack(expand=True)

    root.mainloop()
'''Layout :
----------------------------------------------------------
|                                                        |
|         label [______]                                 |
|                                                        |
|         label [______]                                 |
|                                                        |
|         label [______]                                 |
|                                            label       |
|                                          [____v]       |
|                                                        |
|                            [save]    [back]  [foward]  |
----------------------------------------------------------
'''
