# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import pyperclip

def generate_password():
#Password Generator Project
    from random import randint,choice,shuffle
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

   
    password_list = []

    password_list += [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]
    
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    print(len(website))

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title=website, message='Please fill out all the fields.')
    else: 
        is_ok = messagebox.askyesno(title=website, message=f'Do you want to add? \n email: {email} \n password: {password}')
        if is_ok:
            string = f"{website} | {email} | {password}\n"
            with open("day-29-start/password-manager-start/passwords.txt", mode='a') as password_list:
                password_list.write(string)

                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40)

canvas = Canvas(width=200,height=200)
png = PhotoImage(file='day-29-start/password-manager-start/logo.png')
canvas.create_image(100, 100, image=png)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)
# Entries
website_entry = Entry(bg='white', width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(bg='white', width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'mark@mdias.co.uk')
password_entry = Entry(bg='white', width=21)
password_entry.grid(column=1, row=3)
# Buttons
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
