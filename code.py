#Without GUI
import pyautogui

screenShot_1 = pyautogui.screenshot()
screenShot_1.save(r'A:\Project\Screenshot-Capture-Apps\example.png')


#With GUI
import pyautogui
import tkinter as tk

root= tk.Tk()
root.title('Sc taker')