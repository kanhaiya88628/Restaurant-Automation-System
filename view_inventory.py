from tkinter import *
from tkinter import ttk
import pymongo


class InventoryViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Viewer")
        self.root.geometry("400x400")

        # Connect to MongoDB
        self.client = pymongo.MongoClient(
            "mongodb+srv://agrawalkanhaiya552:Agrawal88628@cluster0.jcaswif.mongodb.net/"
        )
        self.db = self.client["RAS"]
        self.collection = self.db["inventory"]

        # Table to display inventory
        self.inventory_table = ttk.Treeview(
            self.root, columns=("Item Name", "Quantity", "Cost Price", "Total Price")
        )
        self.inventory_table.heading("#0", text="ID")
        self.inventory_table.heading("Item Name", text="Item Name")
        self.inventory_table.heading("Quantity", text="Quantity")
        self.inventory_table.heading("Cost Price", text="Cost Price")
        self.inventory_table.heading("Total Price", text="Total Price")
        self.inventory_table.pack(pady=10)

        # Button to refresh inventory
        refresh_btn = Button(self.root, text="Refresh", command=self.refresh_inventory)
        refresh_btn.pack(pady=10)

        # Populate inventory initially
        self.refresh_inventory()

    def refresh_inventory(self):
        # Clear existing inventory table
        for record in self.inventory_table.get_children():
            self.inventory_table.delete(record)

        # Retrieve inventory items from MongoDB
        inventory_items = self.collection.find()

        # Populate inventory table
        for idx, item in enumerate(inventory_items, start=1):
            self.inventory_table.insert(
                "",
                "end",
                text=str(idx),
                values=(
                    item["item_name"],
                    item["quantity"],
                    item["cost_price"],
                    item["total_price"],
                ),
            )


if __name__ == "__main__":
    root = Tk()
    app = InventoryViewer(root)
    root.mainloop()
