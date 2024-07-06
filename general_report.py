from tkinter import *
from tkinter import ttk
import pymongo


class GeneralReport:
    def __init__(self, root):
        self.root = root
        self.root.title("General Report")
        self.root.geometry("400x300")

        self.client = pymongo.MongoClient(
            "mongodb+srv://agrawalkanhaiya552:Agrawal88628@cluster0.jcaswif.mongodb.net/"
        )
        self.db = self.client["RAS"]
        self.order_collection = self.db["orders"]

        self.order_data = self.fetch_order_data()

        self.report_table = ttk.Treeview(self.root)
        self.report_table["columns"] = ("item_name", "num_orders")
        self.report_table.heading("item_name", text="Item Name")
        self.report_table.heading("num_orders", text="Number of Orders")
        self.report_table.column("item_name", width=200)
        self.report_table.column("num_orders", width=150)
        self.report_table.grid(row=0, column=0, padx=10, pady=10)

        self.populate_report()

    def fetch_order_data(self):
        order_data = self.order_collection.aggregate(
            [
                {"$unwind": "$order_items"},
                {"$group": {"_id": "$order_items.item", "count": {"$sum": 1}}},
            ]
        )
        return order_data

    def populate_report(self):
        for row in self.order_data:
            self.report_table.insert("", "end", values=(row["_id"], row["count"]))


if __name__ == "__main__":
    root = Tk()
    app = GeneralReport(root)
    root.mainloop()
