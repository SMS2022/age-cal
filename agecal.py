import tkinter as tk

root=tk.Tk()
root.geometry("200x200")
root.title("Age Calculator")

name=tk.Label(text="Name")
name.grid(row=1,column=0)

nameEntry=tk.Entry()
nameEntry.grid(row=1,column=1)

year=tk.Label(text="Year")
year.grid(row=2,column=0)

yearEntry=tk.Entry()
yearEntry.grid(row=2,column=1)

month=tk.Label(text="Month")
month.grid(row=3,column=0)

monthEntry=tk.Label()
monthEntry.grid(row=3,column=1)

date=tk.Label(text="Day")
date.grid(row=4,column=0)

dateEntry=tk.Entry()
dateEntry.grid(row=4,column=1)


root.mainloop()