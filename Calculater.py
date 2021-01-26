#Calculator
#Start
from tkinter import*
Croot  =  Tk()
Croot.configure(background  =  'white')
Croot.bind('<Escape>',lambda e: Croot.destroy())

FTotal = Frame(Croot, background = 'grey90', borderwidth = 1, relief = 'flat')
#1
Frame1 = Frame(FTotal, background = 'grey90', borderwidth = 1, relief = 'flat')
button1 = Button(Frame1, text = 1,
                 width = 14, bg = 'white',
                 relief = 'flat',
                 activebackground = 'grey'
                 ).grid(row = 1,column = 1)
Frame1.grid(row = 7,column = 7)
#2
Frame2 = Frame(FTotal, background = 'grey90', borderwidth = 1, relief = 'flat')
button1 = Button(Frame2, text = 2, width = 14, height = 2, bg = 'white', relief = 'flat', activebackground = 'grey').grid(row = 1,column = 1)
Frame2.grid(row = 7,column = 6)
#3
Frame3 = Frame(FTotal, background = 'grey90', borderwidth = 1, relief = 'flat')
button1 = Button(Frame3, text = 3, width = 14, height = 2, bg = 'white', relief = 'flat', activebackground = 'grey').grid(row = 1,column = 1)
Frame3.grid(row = 7,column = 5)
#4
Frame4 = Frame(FTotal, background = 'grey90', borderwidth = 1, relief = 'flat')
button1 = Button(Frame4, text = 4, width = 14, height = 2, bg = 'white', relief = 'flat', activebackground = 'grey').grid(row = 1,column = 1)
Frame4.grid(row = 6,column = 7)
#5
Frame5 = Frame(FTotal, background = 'grey90', borderwidth = 1, relief = 'flat')
button1 = Button(Frame5, text = 5, width = 14, height = 2, bg = 'white', relief = 'flat', activebackground = 'grey').grid(row = 1,column = 1)
Frame5.grid(row = 6,column = 6)
#6
Frame6 = Frame(FTotal, background = 'grey90', borderwidth = 1, relief = 'flat')
button1 = Button(Frame6, text = 6, width = 14, height = 2, bg = 'white', relief = 'flat', activebackground = 'grey').grid(row = 1,column = 1)
Frame6.grid(row = 6,column = 5)
#7
Frame7 = Frame(FTotal, background = 'grey90', borderwidth = 1, relief = 'flat')
button1 = Button(Frame7, text = 7, width = 14, height = 2, bg = 'white', relief = 'flat', activebackground = 'grey').grid(row = 1,column = 1)
Frame7.grid(row = 5,column = 7)
#8
Frame8 = Frame(FTotal, background = 'grey90', borderwidth = 1, relief = 'flat')
button1 = Button(Frame8, text = 8, width = 14, height = 2, bg = 'white', relief = 'flat', activebackground = 'grey').grid(row = 1,column = 1)
Frame8.grid(row = 5,column = 6)
#9
Frame9 = Frame(FTotal, background = 'grey90', borderwidth = 1, relief = 'flat')
button1 = Button(Frame9, text = 9, width = 14, height = 2, bg = 'white', relief = 'flat', activebackground = 'grey').grid(row = 1,column = 1)
Frame9.grid(row = 5,column = 5)
#0
Frame0 = Frame(FTotal, background = 'grey90', borderwidth = 1, relief = 'flat')
button1 = Button(Frame0, text = 0, width = 14, height = 2, bg = 'white', relief = 'flat', activebackground = 'grey').grid(row = 1,column = 1)
Frame0.grid(row = 8,column = 6)

FTotal.grid(row = 1,column = 1)

#button0 = Button(Croot, text = 0, width = 14, height = 2, bg = 'white', relief = 'flat', activebackground = 'white').grid(row = 4,column = 2)
#button0 = Button(Croot, text = 0, width = 14, height = 2, bg = 'white', relief = 'flat', activebackground = 'white').grid(row = 4,column = 2)

