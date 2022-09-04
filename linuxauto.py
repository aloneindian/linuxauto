from tkinter import *
from tkinter.font import Font
from tkinter import simpledialog
import pyautogui as pgui
import time
import os
# counting while funciotn is starting
i = 0
j = 0

#globle variable and counter of initial counting while intializing
SEQUENCE = []
COUNT = 0
ADDSQNC = 0
MVX =[]
MVY = []

SCOUNT = -1
SCRL =[]


class Start:
    def Mv():
        global i
        pgui.moveTo(MVX[i],MVY[i] ,3)
        i += 1
    def Scr(t):
        global j
        pgui.hscroll(SCRL[j],interval=0.70)
        j +=1

    def Ck(ct):
        pgui.click()

    def Ml(mL):
        pgui.click(button="left", interval = 0.30)

    def Mr(mR):
        pgui.click(button="right", interval=0.23)

def MvOn():
    global COUNT
    mX = int(simpledialog.askstring("enter the position of the secreen where you want to go on", "eneter x axis"))
    mY= int(simpledialog.askstring("enter the position of the secreen where you want to go on", "eneter y axis"))
    MVX.append(mX)
    MVY.append(mY)
    SEQUENCE.append("M")
    COUNT +=1
    
def ScrOn():
    global SCOUNT
    scronVal = int(simpledialog.askstring("how much time you want to scroll", "enter time in sec"))
    SCRL.append(scronVal)
    SCOUNT += 1
    SEQUENCE.append("S")
    
def ClickOn():
    clickonVal= int(simpledialog.askstring("how much time you want to click here", "enter here"))
    SEQUENCE.append("C")
    
def GPosOn():
    
    SEQUENCE.append("GP")
    
def ResetOn():
    print("Reset all the value that user entered perviously")
    SEQUENCE.append("RS")
    
def MLFOn():
    print("")
    SEQUENCE.append("ML")
    
def MRFOn():
    print("mouse right click ")
    SEQUENCE.append("MR")

def EnterOn():
    print("fuction in noe starting")
    for i in SEQUENCE:
        time.sleep(3)
        if ( i == "M"):
            Start.Mv()
        elif(i == "S"):
            Start.Scr(5)
        elif(i == "C"):
            Start.Ck(3)
        elif(i == "GP"):
            print("This is the get position funcion")
        elif(i == "RS"):
            print("RESET")
        elif(i == "ML"):
            Start.Ml(22)
        else:
            Start.Mr(4)


root = Tk()
frame1 = Frame(root, width= 400, height=200,bg = 'pink')
tex = Text(frame1, width = 35, height = 10, padx = 10, pady= 10, bd = 5, selectbackground="black")
tex.pack()

frame1.pack()
frame2 = Frame(root, width = 400, height=100, bg ='green')
but1= Button(frame2, text ="MOVE", command = MvOn)
but2= Button(frame2, text ="scroll", command = ScrOn)
but3= Button(frame2, text ="click", command = ClickOn)
but4= Button(frame2, text ="Enter", command = EnterOn)
but5= Button(frame2, text ="G.Pos", command = GPosOn)
but6= Button(frame2, text ="Reset", command = ResetOn)
but7= Button(frame2, text ="MLF" , command = MLFOn)
but8= Button(frame2, text ="RLF" ,command = MRFOn)


but1.grid(row= 0, column = 0)
but2.grid(row = 0, column =1)
but3.grid(row = 0 ,column = 2)
but4.grid(row = 0 , column = 3)
but5.grid(row = 1, column=0)
but6.grid(row = 1, column = 1)
but7.grid(row =1, column = 2)
but8.grid(row  = 1, column = 3)


frame2.pack()
root.geometry('450x300+450+200')
root.configure(background = 'pink')
root.mainloop()




