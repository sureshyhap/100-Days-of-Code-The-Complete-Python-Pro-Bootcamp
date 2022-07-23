import tkinter as tki


def convert_miles_to_km():
    miles = my_entry.get()
    km = float(miles) * 1.60934
    km = "{:.4}".format(km)
    num_km["text"] = km


window = tki.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)

my_label = tki.Label(text="is equal to")
my_label.grid(row=1, column=0)

my_entry = tki.Entry(width=10)
my_entry.grid(row=0, column=1)

num_km = tki.Label(text="0")
num_km.grid(row=1, column=1)
num_km.config(padx=5, pady=5)

my_button = tki.Button(text="Calculate", command=convert_miles_to_km)
my_button.grid(row=2, column=1)

miles_label = tki.Label(text="Miles")
miles_label.grid(row=0, column=2)
miles_label.config(padx=2)

km_label = tki.Label(text="Km")
km_label.grid(row=1, column=2)

window.config(padx=20, pady=20)

window.mainloop()
