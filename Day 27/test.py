import tkinter
import time

def button_clicked_handler():
    global my_label
    my_label["text"] = input.get()


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=200)

# Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="Newer Text")
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

button = tkinter.Button(text="Click me", command=button_clicked_handler)
# button.pack()
button.grid(column=1, row=1)

button2 = tkinter.Button(text="New Button")
button2.grid(column=2, row=0)

input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


"""
while True:
    string_input = input.get()
    print(string_input)
    time.sleep(1)
"""
"""
def add(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum


print(add(1, 2, 3, 4))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(2, add=3, multiply=5))
"""

window.mainloop()