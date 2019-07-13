
import tkinter as tk
import unittest


import context
import SunFlwr
from SunFlwr.sunui.winframes import navigationframes, neweval, frameassets


class GuiTestSuite(unittest.TestCase):
    """docstring for GuiTestSuite."""

    @classmethod
    def setUpClass(self):
        '''before the first test'''
        pass

    @classmethod
    def tearDownClass(self):
        '''after last test'''
        pass

    def setUp(self):
        '''before each test'''
        self.root = tk.Tk()
        self.root.bind('<Key>', lambda e: print(self.root, e.keysym))
        self.root.bind('<Button>', lambda e: print(self.root, e.keysym))
        # get screen width and height
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen
        w = (ws/5)*3
        h = (hs/5)*3
        self.root.geometry('%dx%d+%d+%d' %
                           (w, h,  (ws/2) - (w/2),  (hs/2) - (h/2)-100))

    def teardown():
        '''after each test'''
        if self.root:
            self.root.destroy()
        pass

# - parts of the frames
    # @unittest.skip('used in other bigger frames')

    def test_start_window_navigation_menu(self):
        self.root.title('start_window_navigation_menu')
        self.f = navigationframes.StartWindowMenu(self.root)
        self.f.grid()
        self.root.mainloop()

    # @unittest.skip('used in other bigger frames')
    def test_navigation_menu(self):
        self.root.title('test_navigation_menu')
        self.f = navigationframes.StartWindowMenu(self.root)
        self.f.grid()
        self.root.mainloop()

    def test_status_bar(self):
        self.root.title('test_status_bar')
        self.f = frameassets.StatusBar(self.root)
        self.f.pack(expand=True)
        self.root.mainloop()

    def test_menu_bar(self):
        self.root.title('test_menu_bar')
        self.f = frameassets.MenuBar(self.root)
        self.root['menu'] = self.f
        self.root.mainloop()

    def test_checkbutton_list(self):
        self.root.title('test_checkbutton_list')
        items = [1, 2, 3]
        self.f = frameassets.CheckbuttonList(self.root, items)
        self.root.mainloop()


'''
    def test_main_window(self):
        pass
        self.root.title('test_main_window')
        self.f = startwindow.StartWindow(self.root)
        self.f.grid()
        self.root.mainloop()
'''
# - main windows


def test_new_evaluation_window(self):
    self.root.title('test_new_evaluation_window')
    self.f = neweval.NewEvaluation(self.root)
    self.f.grid()
    self.root.mainloop()


if __name__ == '__main__':
    unittest.main()

'''def test_enter(self):
    v = MyGUI(self.root)
    v.pack()
    self.root.update_idletasks()

    # info
    v.after(100, lambda: self.root.event_generate('<Return>'))
    v.info_button.invoke()

    # quit
    def cancel():
        self.root.event_generate('<Tab>')
        self.root.event_generate('<Return>')

    v.after(100, cancel)
    v.quit_button.invoke()
    self.assertTrue(v.winfo_ismapped())
    v.after(100, lambda: self.root.event_generate('<Return>'))
    v.quit_button.invoke()
    with self.assertRaises(tkinter.TclError):
        v.winfo_ismapped()'''
