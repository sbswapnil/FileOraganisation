from tkinter import ttk
from tkinter import *


class Popup(Tk):
    bool1 = None

    def __init__(self):
        super(Popup, self).__init__()
        self.title("Popup")

        self.label()
        self.btn_Ok()
        self.btn_cancel()

    def label(self):
        label = ttk.Label(self, text="Are you sure you want to pply changes")
        label.grid(column=0, columnspan=2, row=0)

    def btn_Ok(self):
        button = ttk.Button(self, text="Ok", command=self.apply, width=11)
        button.grid(column=0, row=1)

    def btn_cancel(self):
        button = ttk.Button(self, text="Cancel", command=self.quit, width=11)
        button.grid(column=1, row=1)

    def quit(self):
        bool1 = False
        quit()

    def apply(self):
        bool1 = True
        quit()


if __name__ == "__main__":
    popup = Popup()
    popup.mainloop()
