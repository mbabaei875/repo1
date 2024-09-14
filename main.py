from tkinter import *
from pl.form import RegisterPrs
#from be.Personel import Personel


if __name__=="__main__":
    screen = Tk()
    screen.geometry("%dx%d+%d+%d" % (750, 500, 600, 150))
    screen.title("مدیریت انبار")
    #screen.iconbitmap("file/icon.ico")
    PageMe=RegisterPrs.App(screen)
    screen.mainloop()


