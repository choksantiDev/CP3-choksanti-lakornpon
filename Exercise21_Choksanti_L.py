from tkinter import *
import math

def convertBMI(bmi_input):
    if bmi_input < 18.5:
        return "ผอมเกินไป"
    elif 18.5 <= bmi_input < 22.9:
        return "น้ำหนักปกติ เหมาะสม"
    elif 23 <= bmi_input < 25:
        return "น้ำหนักเกิน"
    elif 25 <= bmi_input < 30:
        return "อ้วน"
    else:
        return "อ้วนมาก"
    
def leftClickButton(event):
    bmi = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    labelResult.configure(text=convertBMI(bmi))

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)


MainWindow.mainloop()