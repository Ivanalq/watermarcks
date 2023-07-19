from Refactor_img import refactor_img
from tkinter import filedialog
import tkinter as tk
import tkinter.filedialog as fd


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        btn_file = tk.Button(self, text='Выберите файл', command=self.choise_file)
        btn_dir = tk.Button(self, text='Выберите Папку', command=self.choise_directiry)
        btn_sub = tk.Button(self, text='Наложить водяные знаки', command=self.start_wm)
        btn_file.pack(padx=60, pady=10) 
        btn_dir.pack(padx=60, pady=10)
        btn_sub.pack(padx=60, pady=10)

    def choise_file(self): #Функция выбора фалов
        self.res = filedialog.askopenfilename(multiple=1)

    def choise_directiry(self): #Функция выбора папки
        self.directiry = fd.askdirectory(title='Открыть папку', initialdir='/') + '/'

    def start_wm(self): #Функция, которая начинает процесс наложения водяных знаков
        refactor_img(list_images=self.res, directory_exit=self.directiry)


if __name__ == "__main__":
    app = App()
    app.title('Добавление Водяных Знаков')
    app.resizable(width=False, height=False)
    app.mainloop()
