#Without GUI
import pyautogui

screenShot_1 = pyautogui.screenshot()
screenShot_1.save(r'A:\Project\Screenshot-Capture-Apps\example.png')


#With GUI
import pyautogui
import tkinter as tk

root= tk.Tk()
root.title('Sc taker')

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def myScreenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'A:\Project\Screenshot-Capture-Apps\example1.png')

myButton = tk.Button(text='Take Screenshot', command=myScreenshot, bg='green',fg='white',font= 15)

