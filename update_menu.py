from tkinter import *
from tkinter import ttk
import pymongo
from tkinter import messagebox


class MenuUpdater:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Updater")
        self.root.geometry("400x300")

        self.client = pymongo.MongoClient(
            "mongodb+srv://agrawalkanhaiya552:Agrawal88628@cluster0.jcaswif.mongodb.net/"
        )
        self.db = self.client["RAS"]
        self.collection = self.db["menu"]

        self.item_names = self.get_item_names()

        self.item_name_label = Label(root, text="Item Name:")
        self.item_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.selected_item = StringVar()
        self.item_name_dropdown = ttk.Combobox(
            root, textvariable=self.selected_item, values=self.item_names
        )
        self.item_name_dropdown.grid(row=0, column=1, padx=10, pady=10)

        self.price_label = Label(root, text="Price:")
        self.price_label.grid(row=1, column=0, padx=10, pady=10)
        self.price_entry = Entry(root)
        self.price_entry.grid(row=1, column=1, padx=10, pady=10)

        self.add_btn = Button(root, text="Add Item", command=self.add_item)
        self.add_btn.grid(row=2, columnspan=2, padx=10, pady=10)

        self.edit_btn = Button(root, text="Edit Item", command=self.edit_item)
        self.edit_btn.grid(row=3, columnspan=2, padx=10, pady=10)

        self.delete_btn = Button(root, text="Delete Item", command=self.delete_item)
        self.delete_btn.grid(row=4, columnspan=2, padx=10, pady=10)

    def get_item_names(self):
        item_names = [
            item["item_name"]
            for item in self.collection.find({}, {"_id": 0, "item_name": 1})
        ]
        return item_names

    def add_item(self):
        item_name = self.selected_item.get()
        price = self.price_entry.get()

        if item_name and price:
            item = {"item_name": item_name, "price": float(price)}
            self.collection.insert_one(item)
            messagebox.showinfo("Success", "Item added to menu successfully.")
            self.clear_entries()
            # Update item names in dropdown
            self.item_names = self.get_item_names()
            self.item_name_dropdown["values"] = self.item_names
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def edit_item(self):
        item_name = self.selected_item.get()
        price = self.price_entry.get()

        if item_name and price:
            updated_item = {"$set": {"price": float(price)}}
            self.collection.update_one({"item_name": item_name}, updated_item)
            messagebox.showinfo("Success", "Item updated successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def delete_item(self):
        item_name = self.selected_item.get()

        if item_name:
            self.collection.delete_one({"item_name": item_name})
            messagebox.showinfo("Success", "Item deleted successfully.")
            self.clear_entries()

            self.item_names = self.get_item_names()
            self.item_name_dropdown["values"] = self.item_names
        else:
            messagebox.showerror("Error", "Please select an item to delete.")

    def clear_entries(self):
        self.selected_item.set("")
        self.price_entry.delete(0, END)


if __name__ == "__main__":
    root = Tk()
    app = MenuUpdater(root)
    root.mainloop()
