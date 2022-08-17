from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

# Label
is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0, row=1)

result_label = Label(text=0)
result_label.grid(column=1, row=1)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

def miles_to_km():
    miles = float(miles_input.get())
    km = 1.60934
    conversion = miles * km
    result_label.config(text=conversion)


calc_button = Button(text='Calculate', command=miles_to_km)
calc_button.grid(column=1, row=2)


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)




window.mainloop()
    