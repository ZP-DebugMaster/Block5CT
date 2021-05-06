from tkinter import *


top = Tk()
playlistList = []

def results():
    print(playlistList)

def addToList():
    newItem = E1.get()
    playlistList.append(newItem)
    E1.delete(0, END)

def exportList():
    with open('test.txt', 'w') as f:
        for item in playlistList:
            f.write("%s/n" % item)



#This is a label widget
L1 = Label(top, text = "Playlist Maker")
L1.grid(column = 0, row = 1)

#This is an entry widget
E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)

#This is a button widget
B1 = Button(text = "  Print Playlist    ", bg = "#c6edee", command = results )
B1.grid(column = 0, row = 3)

B2 = Button(text = " + ", bg = "#f7cac9", command = addToList)
B2.grid(column = 1, row = 2)

B3 = Button(text = "Export List", bg = "#ceb0af", command = export)
B3.grid(column = 0, row = 4)

top.mainloop()
