from tkinter import ttk
import tkinter as tk


class ToolTip(object):
    '''Small pop up window that show text next to a generic widget.'''

    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None
        self.id = None
        self.x = 0
        self.y = 0

    def showtip(self, text):
        'display text in tooltip window'
        self.text = text
        if self.tip_window or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox('insert')
        x = x + self.widget.winfo_rootx() + 27
        y = y + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        # self.fade_in(tw)
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief='sunken', borderwidth=1,
                         font=('tahoma', '8', 'normal'))
        label.pack(padx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            # self.fade_away(tw)
            tw.destroy()

    def fade_in(self, window):
        alpha = window.attributes("-alpha")
        alpha = min(alpha + .1, 1.0)
        window.attributes("-alpha", alpha)
        if alpha < 1.0:
            window.after(10, self.fade_in)

    def fade_away(self, window):
        alpha = window.attributes("-alpha")
        if alpha > 0:
            alpha -= .1
            window.attributes("-alpha", alpha)
            window.after(10, self.fade_away)


def create_tooltip(widget, text):
    tooltip = ToolTip(widget)

    def enter(event):
        tooltip.showtip(text)

    def leave(event):
        tooltip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


class CheckbuttonList(ttk.Frame):
    '''
    CheckbuttonList class will create a list of checkbuttons in a frame
    as part of abigger more complex ui.
    it will have acess to each of its internall variables an value of the list
    from a parent controller.
    variables:
    - names      = list of the names of every checkbutton.
    - values     = list of boolean variables corresponding to each checkbutton.
    - widgets    = list of chekbutton widgets.
    - master     = frame of which LabeledCheckButtonList belongs to.
    - controller = controller the frame interacts with.
    '''

    def __init__(self, master, item_names, controller=None):
        super(CheckbuttonList, self).__init__(master)
        self.master = master
        self.controller = controller
        self.names = item_names
        self.values = {}
        self.widgets = {}

        for i, item in enumerate(item_names):
            # create variable
            self.values[str(item)] = tk.BooleanVar(0)
            # create widget
            self.widgets[str(item)] = ttk.Checkbutton(
                self, text=str(item), variable=self.values[str(item)])
            # position widgets
            self.widgets[str(item)].grid(column=0, row=i, sticky='w')


class LabeledEntryList(ttk.Frame):
    '''
    LabeledEntryList class will create a list of entries within a frame
    as part of a bigger more complex ui.
    variables:
    - names        = dict of the names of every entry.
    -labels        = dict of all the labes of the frame.
    - values       = dict of String variables corresponding to each entry.
    - widgets      = dict of chekbutton widgets.
    - width        = size of the entry label: default size 10.
    - master       = frame of which LabeledCheckButtonList belongs to.
    - controller   = controller the frame interacts with.
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
    items = [1, 1, 1, 'long word or something', 'blah', 'blah blah']
    frame = LabeledEntryList(root, items)
    frame2 = CheckbuttonList(root, items)
    frame.values['blah'].set(1)
    frame2.values['blah'].set(1)

    frame.pack(side='left')
    frame2.pack(side='left')

    root.mainloop()
