from tkinter import*
from tkinter import font

import re


Croot  =  Tk()
Croot.configure(background  =  'white')
Croot.bind('<Escape>',lambda e: Croot.destroy())
Croot.title('Calculator')

BFont = font.Font(size=16)
GFont = font.Font(size=12)
SFont = font.Font(size=10)
S2Font = font.Font(size=1)
FTotal = Frame(Croot, background = 'grey25', borderwidth = 2, relief = 'flat')

Equation = StringVar()
Solution = StringVar()
obj = '0'
Equation.set('0')
class Func:
    def Append(n):
        global obj
        if obj == '0':
            obj = str(n)
        else:
            obj = obj + str(n)
        Equation.set(obj)
  #      print(eval(obj))
        if list(obj)[-1] != '+' and list(obj)[-1] != '-' and list(obj)[-1] != '×' and list(obj)[-1] != '÷':

            Solution.set(str(eval(obj)))
        else:
            Solution.set(obj)
        
'''

+-----------------+-----+--+           
|                 |  ←  |  |           
+-----+-----+-----+-----+  +           
|  9  |  8  |  7  |  +  |  |           
+-----+-----+-----+-----+  +           
|  6  |  5  |  4  |  -  |> |           
+-----+-----+-----+-----+  +           
|  3  |  2  |  1  |  ×  |  |           
+-----+-----+-----+-----+  +           
|  .  |  0  |  CE |  ÷  |  |           
+-----+-----+-----+-----+  +           

'''
FrameL = Frame(FTotal,
                background = 'grey25',
                borderwidth = 0.5,
                relief = 'flat')
label1 = Label(FrameL,
                textvariable = Equation,
                anchor = 'e',
                padx = 1,
                pady = 4,
                font = BFont,
                bd = 7,
                width = 23,
                height = 0,
                bg = 'grey10',
                fg = 'white',
                relief = 'flat',
                ).grid(row = 0,column = 0, columnspan = 3, rowspan = 4)
Holder = Label(FrameL,
                anchor = 'e',
                padx = 1,
                pady = 4,
                font = S2Font,
                bd = 7,
                width = 23,
                height = 0,
                bg = 'grey10',
                fg = 'white',
                relief = 'flat',
                ).grid(row = 2,column = 0, columnspan = 3, rowspan = 1)

label2 = Label(FrameL,
                textvariable = Solution,
                anchor = 'sw',
                padx = 1,
                pady = 3,
                font = SFont,
                bd = 0,
                width = 23,
                height = 0,
                bg = 'grey10',
                fg = 'white',
                relief = 'flat',
                ).grid(row = 3,column = 0, columnspan = 2)
FrameL.grid(row = 4,column = 5, columnspan = 3)
#                                       1
Frame1 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
button1 = Button(Frame1,
                text = 1,
                command = lambda: Func.Append('1'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'grey10',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'grey5',
                activeforeground = 'white',
                ).grid(row = 7,column = 7)
Frame1.grid(row = 7,column = 7)

#                                       2
Frame2 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
button2 = Button(Frame2,
                text = 2,
                command = lambda: Func.Append('2'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'grey10',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'grey5',
                activeforeground = 'white',
                ).grid(row = 7,column = 6)
Frame2.grid(row = 7,column = 6)

#                                       3
Frame3 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
button3 = Button(Frame3,
                text = 3,
                command = lambda: Func.Append('3'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'grey10',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'grey5',
                activeforeground = 'white',
                ).grid(row = 7,column = 5)
Frame3.grid(row = 7,column = 5)

#                                        4
Frame4 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
button4 = Button(Frame4,
                text = 4,
                command = lambda: Func.Append('4'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'grey10',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'grey5',
                activeforeground = 'white',
                ).grid(row = 6,column = 7)
Frame4.grid(row = 6,column = 7)

#                                        5
Frame5 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
button5 = Button(Frame5,
                text = 5,
                command = lambda: Func.Append('5'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'grey10',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'grey5',
                activeforeground = 'white',
                ).grid(row = 6,column = 6)
Frame5.grid(row = 6,column = 6)

#                                        6
Frame6 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
button6 = Button(Frame6,
                text = 6,
                command = lambda: Func.Append('6'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'grey10',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'grey5',
                activeforeground = 'white',
                ).grid(row = 6,column = 5)
Frame6.grid(row = 6,column = 5)

#                                        7
Frame7 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
button7 = Button(Frame7,
                text = 7,
                command = lambda: Func.Append('7'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'grey10',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'grey5',
                activeforeground = 'white',
                ).grid(row = 5,column = 7)
Frame7.grid(row = 5,column = 7)

#                                        8
Frame8 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
button8 = Button(Frame8,
                text = 8,
                command = lambda: Func.Append('8'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'grey10',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'grey5',
                activeforeground = 'white',
                ).grid(row = 5,column = 6)
Frame8.grid(row = 5,column = 6)

#                                        9
Frame9 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
button9 = Button(Frame9,
                text = 9,
                command = lambda: Func.Append('9'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'grey10',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'grey5',
                activeforeground = 'white',
                ).grid(row = 5,column = 5)
Frame9.grid(row = 5,column = 5)

#                                        0
Frame0 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
button0 = Button(Frame0,
                text = 0,
                command = lambda: Func.Append('0'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'grey10',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'grey5',
                activeforeground = 'white',
                ).grid(row = 8,column = 6)
Frame0.grid(row = 8,column = 6)

#                                        .
Framep = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
buttonp = Button(Framep,
                text = '.',
                command = lambda: Func.Append('.'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'grey10',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'grey5',
                activeforeground = 'white',
                ).grid(row = 8,column = 5)
Framep.grid(row = 8,column = 5)

#                                       CE
FrameCE = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
buttonCE = Button(FrameCE,
                text = 'CE',
#                command = lambda: Func.Append(''),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'grey10',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'grey5',
                activeforeground = 'white',
                ).grid(row = 8,column = 7)
FrameCE.grid(row = 8,column = 7)
#                                        #
#                                        #
#                                        #
#                                        +
Frameop1 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
buttonop1 = Button(Frameop1,
                text = '+',
                command = lambda: Func.Append('+'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'royal blue1',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'royal blue2',
                activeforeground = 'white',
                ).grid(row = 5,column = 8)
Frameop1.grid(row = 5,column = 8)

#                                        -
Frameop2 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
buttonop2 = Button(Frameop2,
                text = '-',
                command = lambda: Func.Append('-'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'royal blue1',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'royal blue2',
                activeforeground = 'white',
                ).grid(row = 5,column = 8)
Frameop2.grid(row = 6,column = 8)

#                                        x
Frameop3 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
buttonop3 = Button(Frameop3,
                text = '×',
                command = lambda: Func.Append('×'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'royal blue1',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'royal blue2',
                activeforeground = 'white',
                ).grid(row = 7,column = 8)
Frameop3.grid(row = 7,column = 8)

#                                        /
Frameop4 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
buttonop4 = Button(Frameop4,
                text = '÷',
                command = lambda: Func.Append('÷'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'royal blue1',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'royal blue2',
                activeforeground = 'white',
                ).grid(row = 8,column = 8)
Frameop4.grid(row = 8,column = 8)
Frameop4 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
buttonop4 = Button(Frameop4,
                text = '÷',
                command = lambda: Func.Append('÷'),
                font = GFont,
                width = 10,
                height = 2,
                bg = 'royal blue1',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'royal blue2',
                activeforeground = 'white',
                ).grid(row = 4,column = 8)
Frameop4.grid(row = 4,column = 8)
'''
FrameO1 = Frame(FTotal,
                background = 'grey25',
                borderwidth = 1,
                relief = 'flat')
FrameO = Frame(FrameO1,
                background = 'royalblue2',
                borderwidth = 3,
                relief = 'flat')
buttonO = Button(FrameO,
                text = '>',
                font = GFont,
                width = 1,
                height = 12,
                bg = 'royal blue2',
                bd = 0,
                fg = 'white',
                relief = 'flat',
                activebackground = 'royal blue2',
                activeforeground = 'white',
                ).grid(row = 0,column = 0)
FrameO.grid(row = 4,column =9, rowspan = 5)
FrameO1.grid(row = 4,column =9, rowspan = 5)
'''
FTotal.grid(row = 1,column = 1)
Croot.mainloop()