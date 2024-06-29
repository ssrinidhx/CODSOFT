from tkinter import *
import string
import random

def generate_password():
    small_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = small_letters + capital_letters + digits + special_characters
    password_length = int(length_spinbox.get())

    if choice.get() == 1:
        password = ''.join(random.sample(small_letters + capital_letters, password_length))
    elif choice.get() == 2:
        password = ''.join(random.sample(small_letters + capital_letters + numbers, password_length))
    elif choice.get() == 3:
        password = ''.join(random.sample(all_characters, password_length))

    password_entry.delete(0, END)
    password_entry.insert(0, password)

root = Tk()
root.title("Password Generator")
root.geometry("370x320")
root.config(bg='#f0f0f0')

font_title = ('Calibri', 24, 'bold')
font_label = ('Calibri', 14)
font_button = ('Calibri', 12)
font_entry = ('Calibri', 14)

title_label = Label(root, text='Password Generator', font=font_title, bg='#f0f0f0', fg='#333')
title_label.pack(pady=20)

choice = IntVar()
weak_radio = Radiobutton(root, text='Weak', value=1, variable=choice, font=font_label, bg='#f0f0f0')
medium_radio = Radiobutton(root, text='Medium', value=2, variable=choice, font=font_label, bg='#f0f0f0')
strong_radio = Radiobutton(root, text='Strong', value=3, variable=choice, font=font_label, bg='#f0f0f0')

weak_radio.pack()
medium_radio.pack()
strong_radio.pack()

weak_radio.place(x=50, y=130)
medium_radio.place(x=50, y=160)
strong_radio.place(x=50, y=190)

length_label = Label(root, text='Password Length', font=font_label, bg='#f0f0f0', fg='#333')
length_label.pack(pady=10)
length_spinbox = Spinbox(root, from_=5, to_=18, width=5, font=font_entry)
length_spinbox.pack()

generate_button = Button(root, text='Generate', font=font_button, command=generate_password)
generate_button.pack(pady=20)

password_entry = Entry(root, width=25, font=font_entry, bd=2)
password_entry.pack()

root.mainloop()
