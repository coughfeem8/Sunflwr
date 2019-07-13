from tkinter import ttk
import tkinter as tk


class CheckbuttonList(ttk.Frame):
    '''
    CheckbuttonList class will create a list of checkbuttons in a frame
    as part of abigger more complex ui.
    it will have acess to each of its internall variables an value of the list
    from a parent controller.
    variables:
    - names =  list of the names of every checkbutton.
    - values= list of boolean variables corresponding to each checkbutton
    - checkbuttons = list of chekbutton widgets.
    - master = frame of which LabeledCheckButtonList belongs to.
    - controller = controller the frame interacts with.
    '''

    def __init__(self, master, item_names, controller=None):
        super(CheckbuttonList, self).__init__(master)
        self.master = master
        self.controller = controller
        self.values = {}
        self.checkbuttons = {}

        for i, item in enumerate(item_names):
            # create variable
            self.values[str(item)] = tk.BooleanVar(value=0)
            # create widget
            self.checkbuttons[str(item)] = ttk.Checkbutton(self, text=str(item))
            # position widgets
            self.checkbuttons[str(item)].grid(column=0, row=i, sticky='w')


class LabeledEntryList(ttk.Frame):
    '''
    CheckboxList class will create alist of check boxes in a frame
    as part of a bigger more complex ui.
    variables:
    - names =  list of the names of every checkbutton.
    - values= list of boolean variables corresponding to each checkbutton
    - checkbuttons = list of chekbutton widgets.
    - width = size of the entry label: default size 10
    - master = frame of which LabeledCheckButtonList belongs to.
    - controller = controller the frame interacts with.
    '''

    def __init__(self, master, item_names,
                 width=10, controller=None):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.names = item_names
        self.values = {}
        self.labels = {}
        self.widgets = {}
        for i, name in enumerate(self.names):
            # create variable
            self.values[str(name)] = tk.StringVar(value='')
            # create widget
            self.labels[str(name)] = ttk.Label(self, text=str(name))
            self.widgets[str(name)] = ttk.Entry(self, text=str(name),
                                                textvariable=self.values
                                                [str(name)], width=width)

            self.widgets[str(name)].grid(column=1, row=i, sticky='w')
            self.labels[str(name)].grid(column=0, row=i, sticky='e')
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=2)


class MenuBar(tk.Menu):
    '''Menubar class is the menubar that will recide as the main bar for the
    system. It will include features such as:
    - file menu for opening and creating new evaluations
    - help menu for about and tutorial.
    '''

    def __init__(self, master, controller=None):
        super(MenuBar, self).__init__(master)
        self.master = master
        self.controller = controller
        menubar = tk.Menu(self.master)
        self.master['menu'] = menubar
        self.master.option_add('*tearoff', False)
        menu_file = tk.Menu(menubar)
        menu_help = tk.Menu(menubar)

        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_help, label='Help')

        menu_file.add_command(label='Nueva Evaluacion',
                              command=lambda: print('Nueva Evaluacion'))
        menu_file.add_command(label='Abrir Evaluacion',
                              command=lambda: print('Abrir Evaluacion'))

        menu_help.add_command(label='Tutorial',
                              command=lambda: print('tutorial'))
        menu_help.add_command(label='Sobre...',
                              command=lambda: print('informacion del sistema'))


class StatusBar(ttk.Frame):
    """Statusbar class will have the setup for a bar that will display the
    version of the system, plus log information of the system"""

    def __init__(self, master, controller=None):
        super(StatusBar, self).__init__(master)
        self.controller = controller
        self.master = master
        # labels
        self.version = tk.StringVar(value='Version: 0.0.0.0.0.01')
        self.status = tk.StringVar(value='the Program is working')

        self.separator = ttk.Separator(self, orient='horizontal')
        self.version_label = ttk.Label(self, text=self.version.get())
        self.status_label = ttk.Label(self, text=self.status.get())

        self.separator.grid(row=0, sticky='we', columnspan=2)
        self.version_label.grid(row=1, column=1, sticky='e')
        self.status_label.grid(row=1, column=0, sticky='w')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)


if __name__ == '__main__':
    root = tk.Tk()
    items = [1, 1, 1, 'long word or somehthing', 'blah', 'blah blah']
    frame = LabeledEntryList(root, items)
    frame2 = CheckbuttonList(root, items)

    frame.pack(side='left')
    frame2.pack(side='left')

    root.mainloop()
