from tkinter import *
import cv2
from PIL import Image
root = Tk()
root.title("Ventana")
root.config(bg="skyblue")

left_frame = Frame(root, width=200, height=400)
left_frame.grid(row = 0, column = 0, padx = 10, pady = 5)
right_frame = Frame(root, width=650, height=400, bg='grey')
right_frame.grid(row = 0, column = 1, padx = 10, pady =5)

tool_bar = Frame(left_frame, width=180, height=185, bg="purple")
tool_bar.grid(row = 2, column = 0, padx = 5 , pady = 5)

Label(left_frame, text = "Example Test").grid(row=1,column = 0, padx = 5, pady = 5)
image = PhotoImage(file="sunset.gif")
original_image = image.subsample(3,3)
Label(left_frame, image=original_image).grid(row=0, column=0, padx=5,pady=5)

Label(right_frame, image=image).grid(row=1, column=0, padx=5, pady=5)

Label(tool_bar, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)
Label(tool_bar, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=3)
Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=3)
Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=3)
Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=3)
Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=3)



root.mainloop()