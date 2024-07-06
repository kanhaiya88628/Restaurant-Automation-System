from tkinter import *
from tkinter import messagebox
import pymongo


class InventoryManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")
        self.root.geometry("400x350")

        self.client = pymongo.MongoClient(
            "mongodb+srv://agrawalkanhaiya552:Agrawal88628@cluster0.jcaswif.mongodb.net/"
        )
        self.db = self.client["RAS"]
        self.collection = self.db["inventory"]

        self.item_name_label = Label(root, text="Item Name:")
        self.item_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.item_name_entry = Entry(root)
        self.item_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.quantity_label = Label(root, text="Quantity:")
        self.quantity_label.grid(row=1, column=0, padx=10, pady=10)
        self.quantity_entry = Entry(root)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10)

        self.cost_price_label = Label(root, text="Cost Price:")
        self.cost_price_label.grid(row=2, column=0, padx=10, pady=10)
        self.cost_price_entry = Entry(root)
        self.cost_price_entry.grid(row=2, column=1, padx=10, pady=10)

        self.total_price_label = Label(root, text="Total Price:")
        self.total_price_label.grid(row=3, column=0, padx=10, pady=10)
        self.total_price_value = Label(root, text="")
        self.total_price_value.grid(row=3, column=1, padx=10, pady=10)

        self.add_btn = Button(root, text="Add Ingredient", command=self.add_ingredient)
        self.add_btn.grid(row=4, columnspan=2, padx=10, pady=10)

    def add_ingredient(self):
        item_name = self.item_name_entry.get()
        quantity = self.quantity_entry.get()
        cost_price = self.cost_price_entry.get()

        if item_name and quantity and cost_price:

            total_price = float(quantity) * float(cost_price)
            ingredient = {
                "item_name": item_name,
                "quantity": int(quantity),
                "cost_price": float(cost_price),
                "total_price": total_price,
            }

            self.collection.insert_one(ingredient)
            messagebox.showinfo(
                "Success", "Ingredient added to inventory successfully."
            )

            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def clear_entries(self):
        self.item_name_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
        self.cost_price_entry.delete(0, END)
        self.total_price_value.config(text="")


if __name__ == "__main__":
    root = Tk()
    app = InventoryManager(root)
    root.mainloop()
