import random
from tkinter import *
from tkinter import messagebox
import tkinter as tk



enable=True
lucyArrays = [[1,2,3],[1,4,7],[4,5,6],[7,8,9],[2,5,8],[3,5,7],[1,5,9],[3,6,9]]
numbersArray=[1,2,3,4,5,6,7,8,9]
#user array
userArray=[]
user={
    "choice":"",
    "winningTimes":0
    }
#computer array
computerArray=[]

computer={
    "choice":"",
    "winningTimes":0
}

boxMap = {}

def setBoxMap(bmap):
    global boxMap
    boxMap = bmap





# onClickFun
def onUserClick(boxNum,msg):
    global enable
    userArray.append(boxNum)
    numbersArray.remove(boxNum)

    if len(boxMap) > 0 and len(userArray) > 0:
        enable = False
        boxMap[boxNum].button.config(
            text=user["choice"]["txt"],
            background=user["choice"]["color"],
            foreground="white",
            state="disabled"
        )

    for l in lucyArrays:
        r = [item for item in userArray if item in l]
        if len(r) == 3:
            msg.config(text = "you win​​") 
            user["winningTimes"] += 1
            disableAllButtons()
            return True  # Stop game
    if len(numbersArray) == 0:
        for key in boxMap:
            boxMap[key].button.config(
            text=user["choice"]["txt"],
            background="red",
            foreground="white",
            state="disabled"
        )
        boxMap[key].button['state'] = tk.DISABLE
        msg.config(text = "Tie ​🥱​,No Winner") 
        
        disableAllButtons()
        return True 
    return False  


def computerChoice(msg):
    global enable
    if not numbersArray:
        return False  # No moves left

    s = random.choice(numbersArray)
    computerArray.append(s)
    numbersArray.remove(s)

    if len(computerArray) > 0:
        boxMap[s].button.config(
            text=computer["choice"]["txt"],
            background=computer["choice"]["color"],
            foreground="white",
            state="disabled"
        )

    for l in lucyArrays:
        r = [item for item in computerArray if item in l]
        if len(r) == 3:
            enable = False
            msg.config(text = "You lose ​​😫") 
            computer["winningTimes"] += 1
            disableAllButtons()
            return True  # Stop game
        
    if len(numbersArray) == 0:
        for i in range(1, 10):
            boxMap[i].button.config(
            text=user["choice"]["txt"],
            background="red",
            foreground="white",
            state="disabled"
        )
        msg.config(text = "Tie ​🥱​,No Winner") 
        return True 
    return False  # Continue game      
        
    

        

def restart():
    userArray.clear()
    computerArray.clear()
    numbersArray[:]=[1,2,3,4,5,6,7,8,9]
    for b in boxMap.values():
        b.button.config(text="",  # Remove the label
        background="SystemButtonFace",  # Default background 
        foreground="black",   # Default text color
        state="normal" )
    
    
def playRound(boxNum,msg):
    if onUserClick(boxNum,msg):
        return  # user won or tie, stop here
    if computerChoice(msg):
        return  # computer won, stop here
    


def disableAllButtons():
    for box in boxMap.values():
        box.button.config(state="disabled")



