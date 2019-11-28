import tkinter


mainWindow = tkinter.Tk()

mainWindow.title("Main Window")
mainWindow.geometry('640x480+8+400')


label = tkinter.Label(mainWindow, text = 'Hello')
label.pack(side="top")

canvas = tkinter.Canvas(mainWindow, relief = 'raised', borderwidth = 1)
canvas.pack(side = 'top')

button1 = tkinter.Button(mainWindow, text = "Button 1")
button2 = tkinter.Button(mainWindow, text="Button 2")
button3 = tkinter.Button(mainWindow, text="Button 3")

button1.pack(side = 'top', anchor = 'n')
button1.pack(side = 'top', anchor = 's')
button1.pack(side = 'top', anchor='e')


mainWindow.mainloop()
