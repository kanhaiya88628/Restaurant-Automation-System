from tkinter import *
from tkinter import ttk
import pymongo
from tkinter import messagebox


class InventoryEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Editor")
        self.root.geometry("400x200")

        # Connect to MongoDB
        self.client = pymongo.MongoClient(
            "mongodb+srv://agrawalkanhaiya552:Agrawal88628@cluster0.jcaswif.mongodb.net/"
        )
        self.db = self.client["RAS"]
        self.collection = self.db["inventory"]

        # Retrieve item names from the inventory
        self.item_names = self.get_item_names()

        # Label and Dropdown for item names
        self.item_name_label = Label(root, text="Select Item:")
        self.item_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.item_name_var = StringVar()
        self.item_name_dropdown = ttk.Combobox(
            root, textvariable=self.item_name_var, values=self.item_names, width=30
        )
        self.item_name_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Quantity
        self.quantity_label = Label(root, text="Quantity:")
        self.quantity_label.grid(row=1, column=0, padx=10, pady=10)
        self.quantity_entry = Entry(root)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10)

        # Cost Price
        self.cost_price_label = Label(root, text="Cost Price:")
        self.cost_price_label.grid(row=2, column=0, padx=10, pady=10)
        self.cost_price_entry = Entry(root)
        self.cost_price_entry.grid(row=2, column=1, padx=10, pady=10)

        # Edit Button
        self.edit_btn = Button(root, text="Edit Item", command=self.edit_item)
        self.edit_btn.grid(row=3, columnspan=2, padx=10, pady=10)

    def get_item_names(self):
        # Retrieve item names from the inventory
        item_names = [
            item["item_name"] for item in self.collection.find({}, {"item_name": 1})
        ]
        return item_names

    def edit_item(self):
        selected_item = self.item_name_var.get()
        new_quantity = self.quantity_entry.get()
        new_cost_price = self.cost_price_entry.get()

        if selected_item and new_quantity and new_cost_price:
            # Check if the item exists in the inventory
            item = self.collection.find_one({"item_name": selected_item})

            if item:
                # Confirm edit with user
                confirmation = messagebox.askyesno(
                    "Confirm Edit",
                    f"Are you sure you want to edit item '{selected_item}'?",
                )

                if confirmation:
                    # Update item in the inventory
                    self.collection.update_one(
                        {"item_name": selected_item},
                        {
                            "$set": {
                                "quantity": int(new_quantity),
                                "cost_price": float(new_cost_price),
                            }
                        },
                    )
                    messagebox.showinfo(
                        "Success", f"Item '{selected_item}' edited successfully."
                    )
            else:
                messagebox.showerror(
                    "Error", f"Item '{selected_item}' does not exist in the inventory."
                )
        else:
            messagebox.showerror("Error", "Please fill in all fields.")


if __name__ == "__main__":
    root = Tk()
    app = InventoryEditor(root)
    root.mainloop()
