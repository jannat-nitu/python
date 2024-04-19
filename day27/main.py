from tkinter import *
window = Tk()
window.title("miles to km converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)
my_label = Label(text="miles")
my_label.grid(column=3, row=1)
my_label2 = Label(text="km")
my_label2.grid(column=3, row=2)
my_label3 = Label(text="is equal to")
my_label3.grid(column=0, row=2)
new_label4 = Label(text="0")
new_label4.grid(column=2, row=2)

def miles_to_km():
    miles = float(my_entry.get())
    kilo = miles * 1.609
    new_label4.config(text=f"{kilo}")


button1 = Button(text="calculate", command=miles_to_km)
button1.grid(column=2, row=3)

my_entry = Entry(width=10)
my_entry.grid(column=2, row=1)
my_entry.get()

window.mainloop()
