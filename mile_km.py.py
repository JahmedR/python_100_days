from tkinter import *

def calculate_km():
    mile = int(input.get())
    km = round(1.609 * mile, 2)
    result = Label(text=str(km))
    result.grid(column= 1, row = 2)
    # return km


window = Tk()
window.title("Mile to kilometer calculator")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)



miles = Label(text = 'Miles')
miles.grid(column = 2, row=0)

my_label = Label(text = 'is equal to')
my_label.grid(column=0, row= 2)

input = Entry(width=7)
print(input.get())
input.grid(column=1, row=0)

km = Label(text='km')
km.grid(column=2, row=2)

calculate = Button(text="Calculate" ,command = calculate_km)
calculate.grid(column=1, row=3)
#Entry




window.mainloop()