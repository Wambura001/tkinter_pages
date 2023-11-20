import tkinter as tk

class EmailForm(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create labels
        label_email = tk.Label(self, text="Email:")
        label_password = tk.Label(self, text="Password:")

        # Create entry fields
        entry_email = tk.Entry(self)
        entry_password = tk.Entry(self, show="*")

        # Create buttons
        button_login = tk.Button(self, text="Login", command=self.login)
        button_register = tk.Button(self, text="Register", command=self.register)

        # Grid layout
        label_email.grid(row=0, column=0)
        entry_email.grid(row=0, column=1)
        label_password.grid(row=1, column=0)
        entry_password.grid(row=1, column=1)
        button_login.grid(row=2, column=0)
        button_register.grid(row=2, column=1)

    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()

        # Validate email and password

        # Login to email account

    def register(self):
        # Open registration form

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Email System")

    email_form = EmailForm(root)
    email_form.pack()

    root.mainloop()