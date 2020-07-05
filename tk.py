from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
from main import Organiser


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.PATH = "C:\\Users\\" + os.getlogin() + "\\Downloads\\"
        self.dir_opt = {}
        self.title("Python Tkinter Dialog Widget")
        self.minsize(640, 400)

        self.labelFrame = ttk.LabelFrame(self, text="Open File you want to Organise")
        self.labelFrame.grid(column=0, row=0, padx=20, pady=20)
        self.labelFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.text_Entry()
        self.btn_BrowseFile()
        self.btn_AplayWindow()

        self.btn_QuitWindow()

    def text_Entry(self):
        self.entry = ttk.Entry(self.labelFrame, width=40)
        self.entry.grid(column=0, columnspan=3, row=0)
        self.entry.insert(0, self.PATH)
        print(self.entry.get())

    def btn_BrowseFile(self):
        self.button = ttk.Button(self.labelFrame, text="Browse File", command=self.fileDialog, width=25)
        self.button.grid(column=3, columnspan=2, row=0)

    def btn_AplayWindow(self):
        self.button = ttk.Button(self.labelFrame, text="Apply", command=self.apply, width=11)
        self.button.grid(column=3, row=1)

    def btn_QuitWindow(self):
        self.button = ttk.Button(self.labelFrame, text="Cancel", command=self.quit, width=11)
        self.button.grid(column=4, row=1)

    def fileDialog(self):
        self.folderName = filedialog.askdirectory(title="select file")
        self.entry.delete(0, 'end')
        self.entry.insert(0, self.folderName)
        self.PATH = self.folderName

    def get_text_entry(self):
        return self.PATH

    def apply(self):
        self.PATH = self.entry.get()
        Organiser(self.get_text_entry())
        self.quit()
        # self.o = Organiser()
        # self.popupmsg(f"are you sure you want to organize {self.PATH}  this file !!")

    def quit(self):
        self.destroy()

    def popupmsg(self, msg):
        label = ttk.Label(self, text=msg)
        label.pack(side="top", pady=10)
        B1 = ttk.Button(self, text="Okay", command=self.destroy)
        B1.pack()
        self.mainloop()

    # def rename_file(self):
    #     rename = ttk.Entry(self, width=40)
    #     rename.grid(column=0, row=0)
    #
    #     button = ttk.Button(self, text="Ok", command=self.quit, width=11)
    #     button.grid(column=1, row=0)
    #     return rename.get()
    #


if __name__ == "__main__":
    root = Root()
    root.mainloop()
