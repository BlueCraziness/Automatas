
from tkinter import *

import os


#Interfaz gŕafica
#root widget
root = Tk()
root.title("Titulo de la historia")
root.resizable(False,False)
root.configure(bg="black")

#FirstFrame Creation
myFrame = Frame(root,width=500, height=400)
myFrame.pack()
myFrame.config(width="650", height="350")
myFrame.config(bd= 8,bg = "black")
myFrame.config(relief = "groove")
#LabelFirstText
textLabel = Label(myFrame, text="Hubo una época donde energía era sinónimo de suciedad," +
    " encender las luces una importante elección, \nlas ciudades tenían apagones"+
    " y los autos quemaban combustible para funcionar..."
    , bg = "black", fg = "white", font=("Arial Unicode MS",15))
textLabel.grid(row= 0,column=1, padx=10, pady = 10)
#Image 
img = PhotoImage(file='files/fondo.gif')#Reemplazar por función que pondra la imagen dependiendo del estado
imageLabel = Label(myFrame, image = img)
imageLabel.grid(row= 1,column=1, padx=10, pady = 10)
#Action Buttons
def actionYesButton():
     print("Holaaaaa")

def actionNoButton():
    print("AntiHola")


#Buttons
buttonNo = Button(myFrame, text="NO", bg = "black", fg = "green", font = (20),
            width = 7, height =5, command = actionNoButton)
buttonNo.grid(row = 2,column = 0, padx = 10, pady = 10)

buttonYes = Button(myFrame, text="YES", bg = "black", fg = "green", font = (20),width = 7,
             height =5, command = actionYesButton)
buttonYes.grid(row = 2, column = 3, padx = 10, pady = 10)



root.mainloop()








































































