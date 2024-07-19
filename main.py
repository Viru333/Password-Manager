from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def get_password():
    generated_password = PasswordGenerator().generate_password()
    window.clipboard_clear()
    window.clipboard_append(generated_password)
    password_entry.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_entry():
    website_name = website_entry.get()
    username = username_entry.get()
    password_input = password_entry.get()

    if website_name == "" or username == "" or password_input == "":
        messagebox.showerror(title="Blank Entries Not Allowed", message="Error!You left some entries blank.")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \nEmail: {username} \nPassword: {password_input} \nIs it ok to save?")
        if is_ok:
            with open("Manage Passwords.txt", 'a') as f:
                f.write(f"{website_name} | {username} | {password_input}\n")
                # Clearing text entered in entries
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20, bg="white")
# window.minsize(300, 300)
window.title("Password Manager")
lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
canvas.create_image(65, 100, image=lock_img)
canvas.grid(column=1, row=0, padx=5, pady=5)


# Labels
website = Label(window, text="Website:", bg="white")
website.grid(row=1, column=0, sticky=E, padx=5, pady=5)

user_name = Label(window, text="Email/Username:", bg="white")
user_name.grid(row=2, column=0, sticky=E, padx=5, pady=5)

password = Label(window, text="Password:", bg="white")
password.grid(row=3, column=0, sticky=E, padx=5, pady=5)


# Entries

website_entry = Entry(window, width=42, bg="white")
website_entry.grid(row=1, column=1, sticky=W, columnspan=2, padx=5, pady=5)
website_entry.focus()

username_entry = Entry(window, width=42, bg="white")
username_entry.insert(END, "aman902821@gmail.com")
username_entry.grid(row=2, column=1, sticky=W, columnspan=2, padx=5, pady=5)

password_entry = Entry(window, width=23, bg="white")
password_entry.grid(row=3, column=1, sticky=W, columnspan=2, padx=5, pady=5)


# Buttons
generate_pass = Button(window, text="Generate Password", bg="white", highlightthickness=0, bd=1, command=get_password)
generate_pass.grid(row=3, column=1, columnspan=2, sticky=E, padx=5, pady=5)

add = Button(window, text="Add", width=35, bg="white", highlightthickness=0, bd=1, command=save_entry)
add.grid(row=4, column=1, sticky=W, columnspan=2, padx=5, pady=5)


window.mainloop()