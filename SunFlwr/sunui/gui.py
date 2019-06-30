from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image


class SunFlwrGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, *kwargs)
        self.title("SunFlwr")

        root = ttk.Frame(self).grid(column=0, row=0, sticky='nswe')

        sections = ['Boot-Up Page', 'Start Window', 'New Project',
                    'Evaluation Preparation',
                    'Public Services And Urban Equipments', 'Land',
                    'Urban Characteristics And Building Description',
                    'Construction Elements', 'Elements And Accesories',
                    'Preview', 'Evaluation Created']


if __name__ == "__main__":
    app = SunFlwrGUI()
    app.mainloop()
