import tkinter as tk
import re

root = tk.Tk()
root.geometry("270x200")
root.title("Email Verify")

email = tk.StringVar()

def checkEmail():
    pattern = "[a-zA-Z0-9]+@[a-z]+\.(com|net)"
    mail = email.get()
    if re.search(pattern, mail):
        verify.config(text="Entered Email is Correct")
    else:
        verify.config(text="Entered Email is Incorrect")
        

welcome = tk.Label(root, text = "Verify Email", font=("Helvetica", 24))
welcome.place(x = 40,y=10)

email_label = tk.Label(root, text= "Enter Email", font=("Helvetica", 12))
email_label.place(x=40, y =70)

email_entry = tk.Entry(root, textvariable = email,font=("Helvetica", 12), width=20)
email_entry.place(x=40, y =90)

submit = tk.Button(root, text = "Submit", width = 10, command = checkEmail,font=("Helvetica", 12))
submit.place(x=80, y =130)

verify = tk.Label(root, text="", font=("Helvetica", 12))
verify.place(x=30, y =170)

root.mainloop()