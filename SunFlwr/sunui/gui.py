from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image

from winframes import frameassets as fa
from winframes import startwindow as sw
from winframes import navigationframes as navf


class SunFlwrGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(SunFlwrGUI, self).__init__(*args, **kwargs)
        self.title("SunFlwr")

        # get screen width and height
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()  # height of the screen
        w = (ws/5)*3  # 60%
        h = (hs/5)*3  # 60%
        self.geometry('%dx%d+%d+%d' %
                      (w, h,  (ws/2) - (w/2),  (hs/2) - (h/2) - 100))
        self.resizable(False, False)
        self.frames = {}
        # keys is for internal use values are in spanish by client's request.
        self.sections = {'Splash Screen': 'Splash Screen',
                         'Start Window': 'Incio.',
                         'New Project': 'Nuevo Avaluo.',
                         'Evaluation Preparation': 'Preparacion del Avaluo.',
                         'Public Services And Urban Equipments':
                         'Servicios Publicos y Equipamientos Urbanos.',
                         'Land': 'Terreno',
                         'Urban Characteristics And Building Description':
                         'Caracteristicas Urbanas y Descripcion del Inmueble',
                         'Construction Elements': 'Elementos de Construcion',
                         'Elements And Accesories': 'Elementos y Accesorios',
                         'Preview': '',
                         'Evaluation Created': 'Avaluo Creado'}

        self.img_path = 'SunFlwr/res/logo.png'
        self.img = ImageTk.PhotoImage(Image.open(str(self.img_path)))
        self.logo_label = ttk.Label(self, image=self.img)
        for F in self.sections.keys():
            pass
            # for each of the sections
            # add a new type of frame depending on the name of the sections
            # the name of the frame is added to the frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.

        self.frames['StartWindow'] = sw.StartWindow(self, self)
        # FRAMES
        self.menu_bar = fa.MenuBar(self)
        self.status_bar = fa.StatusBar(self, self)
        self.navigation_frame = navf.StartWindowMenu(self, self)

        # layout
        self.contents = self.logo_label
        self.status_bar.pack(fill='x', side='bottom')
        self.navigation_frame.pack(fill='x', side='bottom')

        # image logo
        self.contents.pack(fill='y')

        # frames

        # layout

        def show_frame(self, page_name):
            '''Show a frame for the given page name'''
            frame = self.frames[page_name]
            self.show_frame("StartPage")


if __name__ == "__main__":
    app = SunFlwrGUI()
    app.mainloop()
