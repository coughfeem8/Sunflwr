from tkinter import ttk
import tkinter as tk
'''
this module will include all the setup for the style of the application in the
system.These are the palletsfor the gui
Group 1
#624734,  #d58637, #7c9f69,  #c04116, #e3ab3c
Group 2 text
 #392929,  #8f6d2e,  #f2c649, #f5e5b4,  #fadc84
highlight colors
#c42366, #ff4f01, #a92477, #f32645, #ffbf17

reference functions

s.lookup('TButton', 'font')
s.configure('TButton', font='helvetica 24')

s.configure('Emergency.TButton', font='helvetica 24',
foreground='red', padding=10)

s.map('TButton',
    background=[('disabled','#d9d9d9), ('active','#ececec)],
    foreground=[('disabled','#a3a3a3')],
    relief=[('pressed', '!disabled', 'sunken')])

'''


class SunStyle(ttk.Style):
    """docstring for SunStyle."""

    def __init__(self):
        super(SunStyle, self).__init__()


if __name__ == '__main__':
    app = tk.Tk()
    style = ttk.Style()
    style.theme_use('winnative')
    button = ttk.Button(app, text='text').pack()
    label = ttk.Label(app, text='text').pack()
    entry = ttk.Entry(app, width=10).pack()
    frame = ttk.Frame(master=app).pack(padx=10, pady=10)
    checkbox = ttk.Checkbutton(frame, text='selected').pack()
    scrollbar = ttk.Scrollbar(
        master=frame, orient='vertical').pack()
    separator = ttk.Separator(app, orient='horizontal').pack(side='top')

    # menu
    menu = tk.Menu(app)
    menu_file = tk.Menu(menu)
    menu.add_cascade(menu=menu_file, label="File")
    menu_file.add_command(label='Nueva',
                          command=lambda: print('Nueva Evaluacion'))
    menu_file.add_command(label='Nueva',
                          command=lambda: print('Nueva Evaluacion'))
    app.config(menu=menu)
    menu_file.add_command(label='Nueva',
                          command=lambda: print('Nueva Evaluacion'))
    app.config(menu=menu)
    menu_file.add_command(label='Nueva',
                          command=lambda: print('Nueva Evaluacion'))
    app.config(menu=menu)

    app.mainloop()
