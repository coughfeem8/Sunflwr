from tkinter import ttk
from PIL import ImageTk, Image


class StartWindow(ttk.Frame):
    def __init__(self, parent, controller=None):
        ttk.Frame.__init__(self, parent)

        # Logo Image
        logo_frame = ttk.Frame(parent).grid(row=0, columnspan=3)
        logo_img = Image.open('SunFlwr/res/ok.png')
        logo_img.thumbnail([128, 128])
        logo_img = ImageTk.PhotoImage(logo_img)
        logo_label = ttk.Label(master=logo_frame, text='SunFlwr',
                               image=logo_img).grid()

        # menu buttons
        option_list = ttk.Frame(parent).grid(row=1, columnspan=3, column=0)
        new_button = ttk.Button(option_list, text='Create Evaluation',
                                command=lambda: print('Create Evaluation'))
        new_button.grid(column=0, row=0)
        open_button = ttk.Button(option_list, text='Open Evaluation')
        open_button.grid(column=1, row=0)
        cancel_button = ttk.Button(option_list, text='Cancel')
        cancel_button.grid(column=2, row=0)
