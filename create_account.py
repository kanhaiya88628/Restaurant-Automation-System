import tkinter as tk
from tkinter import ttk, messagebox
import pymongo


class WaiterCreateAccount:
    def __init__(self, root):
        self.root = root
        self.root.title("Create New Waiter Account")
        self.root.geometry("400x300")

        # MongoDB connection
        self.client = pymongo.MongoClient(
            "mongodb+srv://agrawalkanhaiya552:Agrawal88628@cluster0.jcaswif.mongodb.net/"
        )
        self.db = self.client["RAS"]
        self.waiters_collection = self.db["waiters"]

        tk.Label(self.root, text="Waiter Name:").pack()
        self.waiter_name_entry = tk.Entry(self.root)
        self.waiter_name_entry.pack()

        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Label(self.root, text="Confirm Password:").pack()
        self.confirm_password_entry = tk.Entry(self.root, show="*")
        self.confirm_password_entry.pack()

        tk.Button(
            self.root, text="Create Account", command=self.create_waiter_account
        ).pack(pady=10)

    def create_waiter_account(self):

        waiter_name = self.waiter_name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        if self.waiters_collection.find_one({"username": username}):
            messagebox.showerror("Error", "Username already exists")
            return

        waiter_data = {
            "waiter_name": waiter_name,
            "username": username,
            "password": password,
        }
        self.waiters_collection.insert_one(waiter_data)

        messagebox.showinfo("Success", "Waiter account created successfully")

        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = WaiterCreateAccount(root)
    root.mainloop()
