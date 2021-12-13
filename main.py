#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, HORIZONTAL, Canvas, LEFT, Frame, Entry, S, END
# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "ColorMishMash"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

<<<<<<< HEAD
        self.bind("<Escape>", self.quit)  # klavesa esc spustí quit

        self.frameR = Frame(self)
        self.frameR.pack()
        self.frameG = Frame(self)
        self.frameG.pack()
        self.frameB = Frame(self)
        self.frameB.pack()
#r
        self.lblR = tk.Label(self.frameR, text="R:")
        self.lblR.pack(side = LEFT, anchor = S)
        self.scaleR = Scale(self.frameR, from_=0, to=255,
                            orient=HORIZONTAL, length=200, command=self.change)
        self.scaleR.pack(side=LEFT)
        self.entryR = Entry(self.frameR)
        self.entryR.pack(side=LEFT)
#g

        self.lblG = tk.Label(self.frameG, text="G:")
        self.lblG.pack(side = LEFT, anchor = S)
        self.scaleG = Scale(self, from_=0, to=255,
                            orient=HORIZONTAL, length=200, command=self.change)
        self.scaleG.pack(side=LEFT)
        self.entryG = Entry(self.frameG)
        self.entryG.pack(side=LEFT)
#b
        self.lblB = tk.Label(self.frameB, text="B:")
        self.lblB.pack(side = LEFT, anchor = S)
        self.scaleB = Scale(self, from_=0, to=255, orient=HORIZONTAL, length=200, command=self.change
                            )
        self.scaleB.pack(side=LEFT)
        self.entryB = Entry(self.frameR)
        self.entryB.pack(side=LEFT)

        self.canvasMain = Canvas(
            self, width=200, height=100, background="#000000")
=======
        self.bind("<Escape>", self.quit) #klavesa esc spustí quit






        self.lblR = tk.Label(self, text="R")
        self.lblR.pack()
        self.scaleR = Scale(self, from_=0, to=255, orient = HORIZONTAL, length= 200, command=self.change)
        self.scaleR.pack()

        self.lblG = tk.Label(self, text="G")
        self.lblG.pack()
        self.scaleG = Scale(self, from_=0, to=255, orient = HORIZONTAL, length= 200, command=self.change)
        self.scaleG.pack()

        self.lblB = tk.Label(self, text="B")
        self.lblB.pack()
        self.scaleB = Scale(self, from_=0, to=255, orient = HORIZONTAL, length= 200, command=self.change)
        self.scaleB.pack()





        self.canvasMain = Canvas(self, width=200, height=100, background= "#000000")
>>>>>>> 59fdc585a0e9a0c0377f14e421d652b8dccde9fc
        self.canvasMain.pack()
        self.entryMain = Entry(self,)
        self.entryMain.pack(side=LEFT)

        self.btnQuit = tk.Button(self, text="Quit", command=self.quit)
        self.btnQuit.pack()

        self.btn2 = tk.Button(self, text="Change", command=self.change)
        self.btn2.pack()

    def change(self, event):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        colorcode =f"#{r:02x}{g:02x}{b:02x}"
        self.canvasMain.config(background=colorcode)
        self.entryMain.delete(0, END)
        self.entryMain.insert(0, colorcode)


        self.varR.set(r)
        self.varG.set(g)
        self.varB.set(b)

        self.entryR.delete(0, END)
        self.entryR.insert(0, str(r))
        self.entryG.delete(0, END)
        self.entryG.insert(0, str(g))
        self.entryB.delete(0, END)
        self.entryB.insert(0, str(b))

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
