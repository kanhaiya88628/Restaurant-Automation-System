from tkinter import *
from tkinter import ttk
import pymongo
from tkinter import messagebox


class InventoryDeleter:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Deleter")
        self.root.geometry("400x200")

        self.client = pymongo.MongoClient(
            "mongodb+srv://agrawalkanhaiya552:Agrawal88628@cluster0.jcaswif.mongodb.net/"
        )
        self.db = self.client["RAS"]
        self.collection = self.db["inventory"]

        self.item_names = self.get_item_names()

        self.item_name_label = Label(root, text="Select Item:")
        self.item_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.item_name_var = StringVar()
        self.item_name_dropdown = ttk.Combobox(
            root, textvariable=self.item_name_var, values=self.item_names, width=30
        )
        self.item_name_dropdown.grid(row=0, column=1, padx=10, pady=10)

        self.delete_btn = Button(root, text="Delete Item", command=self.delete_item)
        self.delete_btn.grid(row=1, columnspan=2, padx=10, pady=10)

    def get_item_names(self):

        item_names = [
            item["item_name"] for item in self.collection.find({}, {"item_name": 1})
        ]
        return item_names

    def delete_item(self):
        selected_item = self.item_name_var.get()

        if selected_item:
            item = self.collection.find_one({"item_name": selected_item})

            if item:
                confirmation = messagebox.askyesno(
                    "Confirm Deletion",
                    f"Are you sure you want to delete item '{selected_item}'?",
                )

                if confirmation:
                    self.collection.delete_one({"item_name": selected_item})
                    messagebox.showinfo(
                        "Success", f"Item '{selected_item}' deleted successfully."
                    )
                    self.refresh_dropdown()
            else:
                messagebox.showerror(
                    "Error", f"Item '{selected_item}' does not exist in the inventory."
                )
        else:
            messagebox.showerror("Error", "Please select an item.")

    def refresh_dropdown(self):
        self.item_names = self.get_item_names()
        self.item_name_dropdown["values"] = self.item_names
        self.item_name_var.set("")


if __name__ == "__main__":
    root = Tk()
    app = InventoryDeleter(root)
    root.mainloop()
