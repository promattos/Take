import pyautgui
import tkinter as tk

root= tk.TK()

canvas1 = tk.canvas(root,widt = 300, height = 300)
canvas1.pack()

def tkeScreenshot ():

    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('screenshot2.png')
    print("SCREENSHOT HAS BEEN SAVED TO YOUR CURRENT DIRECTORY")
    
    myButton = tk.Button(text= 'Take Screenshot', command=takeScreenshot,
    bg='green', fg='white', font =10)
    canvas1.create_window(150, 150, window=myButton)


    root.mainloop()