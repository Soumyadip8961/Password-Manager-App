from tkinter import *
from tkinter import messagebox
from random import randint, choice,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genarate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
               'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list=[choice(letters) for _ in range(randint(8, 10))]
    symbol_list=[choice(symbols) for _ in range(randint(2, 4))]
    num_list=[choice(numbers) for _ in range(randint(2, 4))]

    password_list=letter_list + symbol_list + num_list
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={website:{
        "email": email,
        "password": password

    }
    }

    if website=="" or password=="":
        messagebox.showinfo(title=website, message="Please dont leave any fields empty!")
    else:
        message= messagebox.askokcancel(title=website,
                                         message=f"Details Entered:-\nEmail: {email}\nPassword: {password}"
                                                 f"\nis it okay to save above details?")
        if message:
            try:
                with open("data.json", mode="r") as file:
                    #Reading Old json Data
                    data=json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    #Wrtting json Data
                    json.dump(new_data, file)
            else:
                with open("data.json", mode="r") as file:
                    #Updating Old json Data
                    data = json.load(file)
                    data.update(new_data)
                with open("data.json", mode="w") as file:
                    #Saving New json Data in the json file
                    json.dump(data, file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
#-----------------------------Search Mechanism-------------------------#
def search():

    website=website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        for (key, value) in data.items():
            if key==website:
                messagebox.showinfo(title=website, message=f"Email: {value['email']}\nPassword: "
                                                       f"{value['password']}")
        if website not in data:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg="white")

canvas=Canvas(width=200, height=200, bg="white", highlightthickness=0)
img=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img,)
canvas.grid(row=0, column=1)

##Labels:-
website_label=Label(text="Website:", bg="white",pady=5)
website_label.grid(row=1, column=0)


email_label=Label(text="Email/Username:", bg="white", pady=5, padx=8)
email_label.grid(row=2,column=0)

passward_label=Label(text="Password", bg="white", pady=5)
passward_label.grid(row=3, column=0)


##Entries:-
website_entry=Entry(width=32, borderwidth=2 )
website_entry.focus()
website_entry.grid(row=1, column=1,)

email_entry=Entry(width=51, borderwidth=2)
email_entry.insert(0, "soumyadip@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry=Entry( width=32, borderwidth=2, )
password_entry.grid(row=3, column=1, columnspan=1, )


##Buttons:-
generate_btn=Button(text="Generate Password",  borderwidth=1, command=genarate_password)
generate_btn.grid(row=3, column=2, columnspan=1)

add_btn=Button(text="Add",  width=44, height=1,borderwidth=1, command=save_data)
add_btn.grid(row=4, column=1 ,columnspan=2)

search_btn=Button(text="Search",  borderwidth=1, width=14, bg="blue", fg="white", command=search )
search_btn.grid(column=2, row=1)



window.mainloop()