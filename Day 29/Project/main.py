import tkinter as tki
from tkinter import messagebox
import password_generator
import pyperclip

###################### Generate Pass #############################
def generate_and_write_pass():
    password = password_generator.generate()
    password_entry.delete(0, tki.END)
    password_entry.insert(tki.END, password)
    pyperclip.copy(password)

######################## Save Password ###########################

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty field", message="Please do not leave any field empty!")
        return
    is_ok = messagebox.askyesno(title=website, message=f"You entered:\nEmail: {email}\n \
                                                       Password: {password}\nIs this ok?")
    if not is_ok:
        return
    with open("data.txt", mode="a") as outfile:
        outfile.write(website + " | " + email + " | " + password + "\n")
    website_entry.delete(0, tki.END)
    password_entry.delete(0, tki.END)

########################### Widgets ##############################
window = tki.Tk()
window.title("Password Manager")
window.config(bg="white", padx=50, pady=50)

canvas = tki.Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = tki.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = tki.Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

website_entry = tki.Entry(width=42)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_label = tki.Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

email_entry = tki.Entry(width=42)
email_entry.insert(tki.END, "sureshyhap@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = tki.Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

password_entry = tki.Entry(width=23)
password_entry.grid(row=3, column=1)

generate_pass_button = tki.Button(text="Generate Password", bg="white", command=generate_and_write_pass)
generate_pass_button.grid(row=3, column=2)

add_button = tki.Button(text="Add", width=40, bg="white", command=save_password)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()