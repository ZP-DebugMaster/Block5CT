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

def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "B5 GUI Projects")
    LMain.grid(column = 2, row = 1)

    B1Main = Button(text = "Week 1", bg = "white", command = week1)
    B1Main.grid(column = 2, row = 2)
    
    B2Main = Button(text = "Week 2", bg = "white")
    B2Main.grid(column = 2, row = 3)

    B3Main = Button(text = "Week 3", bg = "white")
    B3Main.grid(column = 2, row = 4)

def week1():
    clearWindow()
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

    B3 = Button(text = "Export List", bg = "#ceb0af", command = exportList)
    B3.grid(column = 0, row = 4)

    """
    Bclear = Button(text = "Clear Window", bg = "white", command = clearWindow)
    Bclear.grid(column = 3, row = 1)
    """

if __name__== "__main__":
    mainMenu()
    top.mainloop()
