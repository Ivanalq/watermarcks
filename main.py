from Refactor_img import refactor_img
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

import tkinter as tk

import tkinter.filedialog as fd


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.directiry = ()
        self.res = ()
        btn_file = tk.Button(self, text='Выберите файл', command=self.choise_file)
        btn_dir = tk.Button(self, text='Выберите Папку', command=self.choise_directiry)
        btn_sub = tk.Button(self, text='Наложить водяные знаки', command=self.start_wm)
        btn_file.pack(padx=60, pady=10)
        btn_dir.pack(padx=60, pady=10)
        btn_sub.pack(padx=60, pady=10)


    def choise_file(self):
        self.res = filedialog.askopenfilename(multiple=1)
        return self.res


    def choise_directiry(self):
        self.directiry = fd.askdirectory(title='Открыть папку', initialdir='/') + '/'

    def start_wm(self):
        refactor_img(list_images=self.res, directory_exit=self.directiry)




if __name__ == "__main__":
    app = App()
    app.geometry('1000x1000')
    app.mainloop()
