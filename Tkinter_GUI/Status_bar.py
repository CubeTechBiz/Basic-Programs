from tkinter import *

def doNothing():
    print("ok I got it")

root = Tk()

# **** main menu ****

menu = Menu(root)
root.config(menu = menu)

subMenu = Menu(menu)
menu.add_cascade(label = "File", menu = subMenu)
subMenu.add_command(label = "New Project", command = doNothing)
subMenu.add_command(label = "New", command = doNothing)
subMenu.add_separator()
subMenu.add_command(label = "Exit", command = doNothing)

editMenu = Menu(menu)
menu.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Redo", command = doNothing)

# **** toolbar ****

toolbar = Frame(root, bg = "blue")

inserButt = Button(toolbar, text = "Insert image", command = doNothing)
inserButt.pack(side = LEFT, padx = 2, pady = 2)
printButt = Button(toolbar, text = "Print", command = doNothing)
printButt.pack(side = LEFT, padx = 2, pady = 2)

toolbar.pack(side = TOP, fill = X)

# **** status bar ****

status = Label(root, text = "File saved", bd = 1, relief = SUNKEN, anchor = W) # you can use font = "bold" if you want
status.pack(side = BOTTOM, fill = X)

root.mainloop()
