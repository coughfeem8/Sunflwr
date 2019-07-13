from tkinter import ttk
import tkinter as tk
import navigationframes as nav


class NewEvaluation(ttk.Frame):

    def __init__(self, parent, controller=None):
        super(NewEvaluation, self).__init__(parent)

        # FRAMES
        house_info = ttk.Frame(parent)
        fachada_frame = ttk.Frame(parent)
        nav_menu_frame = ttk.Frame(parent)

        house_info.grid(row=0, column=0)
        fachada_frame.grid(row=1, column=0)
        nav_menu_frame.grid(row=2, column=0, columnspan=2)

        # house info frame
        solicitante_label = ttk.Label(master=house_info, text='Solicitate:')
        solicitante_entry = ttk.Entry(master=house_info)

        propietario_label = ttk.Label(master=house_info, text='Propietario:')
        propietario_entry = ttk.Entry(master=house_info)

        ubicacion_label = ttk.Label(master=house_info, text='Ubicacion:')
        ubicacion_entry = ttk.Entry(master=house_info)

        find_button = ttk.Button(master=house_info, text='Validar')

        solicitante_entry.grid(column=1, row=0)
        solicitante_label.grid(column=0, row=0)
        propietario_label.grid(column=0, row=1)
        propietario_entry.grid(column=1, row=1)
        ubicacion_label.grid(column=0, row=2)
        ubicacion_entry.grid(column=1, row=2)
        find_button.grid(column=2, row=2)

        # images Frame
        self.file_count = tk.StringVar(value='')
        no_of_files = ttk.Label(master=fachada_frame,
                                text=self.file_count.get())
        fachada_label = ttk.Label(master=fachada_frame,
                                  text='Fachada:')
        fachada_button = ttk.Button(master=fachada_frame,
                                    text='...')

        fotos_label = ttk.Label(
            master=fachada_frame, text='Otras Fotos:')
        fotos_button = ttk.Button(master=fachada_frame,
                                  text='...')

        fachada_label.grid(column=0, row=0)
        fachada_button.grid(column=1, row=0)
        fotos_label.grid(column=0, row=1)
        fotos_button.grid(column=1, row=1)
        no_of_files.grid(column=2, row=1)

        # nav frame
        nav_menu_frame = nav.NavigationMenu(nav_menu_frame)
        nav_menu_frame.grid()


'''
    def fachada_file_picker(self):
        selected_file = tk.filedialog.askopenfilename()

    def extraphotos_file_picker(self):
        selected_files = tk.filedialog.askopenfilenames(parent=self)
        self.file_count.set('{} files(s)'.format(len(selected_files)))
'''
