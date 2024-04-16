from tkinter import *
from tkinter import ttk, messagebox
import pymongo
from bson import ObjectId


class EditWaiterWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Edit Waiter Account")
        self.root.geometry("300x200")

        # Connect to MongoDB
        self.client = pymongo.MongoClient(
            "mongodb+srv://agrawalkanhaiya552:Agrawal88628@cluster0.jcaswif.mongodb.net/"
        )
        self.db = self.client["RAS"]
        self.collection = self.db["waiters"]

        # Retrieve waiter names from MongoDB
        self.waiter_names = self.get_waiter_names()

        # Dropdown for selecting waiter name
        self.selected_waiter_name = StringVar()
        waiter_name_label = Label(root, text="Select Waiter Name:")
        waiter_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.waiter_name_dropdown = ttk.Combobox(
            root, textvariable=self.selected_waiter_name, values=self.waiter_names
        )
        self.waiter_name_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Button to search for waiter
        self.search_btn = Button(root, text="Search", command=self.search_waiter)
        self.search_btn.grid(row=1, column=0, columnspan=2, pady=10)

        # Labels and Entries for Waiter Details
        self.username_label = Label(root, text="Username:")
        self.username_label.grid(row=2, column=0, padx=10, pady=5)
        self.username_entry = Entry(root)
        self.username_entry.grid(row=2, column=1, padx=10, pady=5)

        self.password_label = Label(root, text="Password:")
        self.password_label.grid(row=3, column=0, padx=10, pady=5)
        self.password_entry = Entry(root)
        self.password_entry.grid(row=3, column=1, padx=10, pady=5)

        # Button to update waiter details
        self.update_btn = Button(root, text="Update", command=self.update_waiter)
        self.update_btn.grid(row=4, column=0, columnspan=2, pady=10)

    def get_waiter_names(self):
        waiter_names = [
            waiter["waiter_name"]
            for waiter in self.collection.find({}, {"waiter_name": 1})
        ]
        return waiter_names

    def search_waiter(self):
        waiter_name = self.selected_waiter_name.get()
        waiter_data = self.collection.find_one({"waiter_name": waiter_name})
        if waiter_data:
            self.username_entry.insert(0, waiter_data["username"])
            self.password_entry.insert(0, waiter_data["password"])
        else:
            messagebox.showerror("Error", "Waiter name not found.")

    def update_waiter(self):
        waiter_name = self.selected_waiter_name.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if waiter_name:
            update_data = {}
            if username:
                update_data["username"] = username
            if password:
                update_data["password"] = password
            if update_data:
                self.collection.update_one(
                    {"waiter_name": waiter_name}, {"$set": update_data}
                )
                messagebox.showinfo("Success", "Waiter details updated successfully.")
            else:
                messagebox.showerror("Error", "Please fill in at least one field.")
        else:
            messagebox.showerror("Error", "Please select a waiter name.")


if __name__ == "__main__":
    root = Tk()
    app = EditWaiterWindow(root)
    root.mainloop()
