from tkinter import ttk
import tkinter as tk


class ServiviosPublicos(ttk.Frame):
    def __init__(self, master, controller=None):
        super().__init__(master)

        self.items1 = ['one', 'two', 'three', 'pi']
        self.items2 = ['four', 'five', 'six']
        self.items3 = ['seven', 'eight', 'nine', 'theta']

        self.option_list = ['basic', 'custom1', 'custom2']
        self.preset = tk.StringVar()

        # frames
        preset_frame = ttk.Frame(master)
        checkbox_frame = ttk.Frame(master)
        checkbox_frame['relief'] = 'sunken'
        checkbox_frame['borderwidth'] = 3
        checkbox_frame['padding'] = (10, 20)

        preset_frame.grid(column=0, row=0, sticky='n')
        checkbox_frame.grid(column=0, row=1, columnspan=3,
                            pady=20, padx=10, sticky='s')

        # preset info
        preset_menu = ttk.Combobox(preset_frame,
                                   width=10, textvariable=self.preset)

        preset_menu['values'] = self.option_list
        load_button = ttk.Button(master=preset_frame, text="Load",
                                 command=lambda: print('Load Button.'))
        create_button = ttk.Button(master=preset_frame, text='Create',
                                   command=lambda: print('Create Button.'))

        preset_menu.grid(column=0, row=0)
        load_button.grid(column=1, row=0)
        create_button.grid(column=2, row=0)

        # checkboxes
        list_left = CheckboxList(checkbox_frame, self.items1)
        list_mid = CheckboxList(checkbox_frame, self.items2)
        list_right = CheckboxList(checkbox_frame, self.items3)

        list_left.grid(column=0, row=2)
        list_mid.grid(column=1, row=2)
        list_right.grid(column=2, row=2)
