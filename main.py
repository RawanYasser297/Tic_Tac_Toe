import tkinter
from tkinter import *
m = tkinter.Tk()
is_enabled = False 
import tkinter as tk
import tkinter.font
import logic 




m.minsize(600, 400)
m.maxsize(800, 600)

m.title('Tic_Tac_Toe Almdrasa')
m.config(bg="light gray")



# user,computer buttons style
stylingX={
    "txt":"X",
    "color":"midnight blue",
    
}
# ..........add more button style .....................
stylingO={
    "txt":"O",
    "color":"light gray"
}



massageFrame = Frame(m,width=30)
msg=tk.Label(massageFrame)
cf = tkinter.font.Font(family="Arial", size=25, weight="bold")
msg.config( text = "choose X or O first ​",font=cf) 



def chooseO():
        global is_enabled
        logic.user["choice"]=stylingO
        logic.computer["choice"]=stylingX
        buttonX['state'] = tk.DISABLED
        buttonO['state'] = tk.DISABLED
        is_enabled = True
        setAllBoxesEnabled()
        msg.config( text = "start the game​")


def chooseX():
        global is_enabled
        logic.user["choice"]=stylingX
        logic.computer["choice"]=stylingO
        buttonX['state'] = tk.DISABLED
        buttonO['state'] = tk.DISABLED
        is_enabled = True
        setAllBoxesEnabled()
        msg.config( text = "start the game​")

chooseFrame = Frame(m,pady = 5,padx = 5,bg="light gray")
buttonX = tk.Button(chooseFrame, text='X',bg="midnight blue",font=cf,command=chooseX,pady = 1,padx = 1,cursor="")
buttonO = tk.Button(chooseFrame, text='O',bg="light gray",font=cf, command=chooseO,pady = 1,padx = 1)
# X or O buttons
buttonX.grid(row=0, column=0)
buttonO.grid(row=0, column=1)
chooseFrame.grid(row=0, column=5)

# restart again button 
def restartSetEnabled():
    global is_enabled
    if(is_enabled):
        restartButton['state'] = tk.NORMAL
    else:
        restartButton['state'] =  tk.DISABLED


def restartScore():
    # logic.computer["winningTimes"]=0
    # logic.user["winningTimes"]=0
    logic.restart()
    scoreUpdates()
    msg.config( text = "​",background="light gray")


restartButton = tk.Button(m,text='restart', width=10 ,height=2, command=restartScore )
restartButton.grid(row=0, column=4)

restartSetEnabled()



# refresh button  
def finishSetEnabled():
        global is_enabled
        if(is_enabled):
            finishButton['state'] =tk.NORMAL
        else:
            finishButton['state'] =tk.DISABLED






def finish():
    global is_enabled
    c=logic.computer["winningTimes"]
    u=logic.user["winningTimes"]
    
    if(u>c):
        msg.config(text = "🏆​ 🥳 you win​ 🥳​ 🏆​") 
    elif(u<c):
        msg.config( text = "🙂 you lose​ 🙃​") 
    else:
        msg.config(text = "🥱​ 😩 ​​​tie 😩 ​🥱​") 

    
    logic.computer["winningTimes"]=0
    logic.user["winningTimes"]=0
    logic.restart()
    scoreUpdates()
    logic.disableAllButtons()
    buttonX['state'] = tk.NORMAL
    buttonO['state'] = tk.NORMAL


msg.grid(row=0, column=1)

massageFrame.grid(row=3, column=0,columnspan=8)

    

    
    

finishButton = tk.Button(m,text='finish', width=10 ,height=2, command=finish)
finishButton.grid(row=0, column=3)



finishSetEnabled()


# user vs computer
scoreFrame = Frame(m)

def scoreUpdates():
    you = tk.Label(scoreFrame, text=logic.user["winningTimes"],font=cf)
    you.grid(row=1, column=0)
    pc = tk.Label(scoreFrame, text=logic.computer["winningTimes"],font=cf)
    pc.grid(row=1, column=1)
    label2 = tk.Label(scoreFrame, text="you")
    label3 = tk.Label(scoreFrame, text="computer")
    # Grid the labels in a 2x2 grid
    label2.grid(row=0, column=0)
    label3.grid(row=0, column=1)
    scoreFrame.grid(row=0, column=6,columnspan=2)




bxsFrame = Frame(m, width=700, height=700,)

class XObox:
    def __init__(self, row, column, boxNum):
        self.button = tk.Button(
            bxsFrame,
            command=self.button_clicked,
            bg="light gray",
            fg="white",
            font=cf,
            height=3,
            width=6,
            justify="center"
        )
        self.button.grid(row=row,column=column)
        self.boxNum = boxNum
    def button_clicked(self):
        global is_enabled
        logic.playRound(self.boxNum,msg=msg)
        restartSetEnabled()
        finishSetEnabled()
        scoreUpdates()
        


    def setEnabled(self):
        global is_enabled
        if(is_enabled):
            self.button['state'] = tk.NORMAL
        else:
            self.button['state'] =  tk.DISABLED



# Create buttons and map them
boxMap = {}
positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
for i, (r, c) in enumerate(positions):
    boxMap[i + 1] = XObox(r, c, i + 1)

# Provide boxMap to logic.py
logic.setBoxMap(boxMap)

def setAllBoxesEnabled():
    for box in boxMap.values():
        box.setEnabled()

setAllBoxesEnabled()


bxsFrame.grid(row=4, column=2,columnspan=5,rowspan=4,padx=5,pady=5)

m.mainloop()