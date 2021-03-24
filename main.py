from tkinter import *


root = Tk()
root.title("Mile Converter By GeekyAsif")
root.geometry("350x150")

def calculate():
    mile = mile_var.get()
    try:
        result = mile * 1.60934
        km_label = Label(root, text=f"is equal to {result} Km", font=15)
        km_label.grid(row=1, column=4)
    except Exception as e:
        print(e)

mile_var = IntVar()
mile_Entry = Entry(root, textvariable = mile_var, font=15)
mile_Entry.grid(row=0,column=4, pady=10,padx=10)

mile = Label(root, text="Miles", font=10)
mile.grid(row=0,column=5)


km_label = Label(root, text=f"is equal to 0 Km",font=15)
km_label.grid(row=1, column=4, pady=10)

cal = Button(root, text="Calculate" ,command=calculate, background="red", fg="white")
cal.grid(row=2,column=4, pady=10)


root.mainloop()
