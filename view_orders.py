from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import pymongo


class ViewOrders:
    def __init__(self, root):
        self.root = root
        self.root.title("View Orders")
        self.root.geometry("800x600+250+50")

        self.client = pymongo.MongoClient(
            "mongodb+srv://agrawalkanhaiya552:Agrawal88628@cluster0.jcaswif.mongodb.net/"
        )
        self.db = self.client["RAS"]
        self.collection = self.db["orders"]

        img = Image.open("images/restaurant.jpg")
        img = img.resize((800, 600), Image.AFFINE)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        self.orders_table = ttk.Treeview(
            self.root, columns=("order_id", "item", "quantity")
        )
        self.orders_table.heading("order_id", text="Order ID")
        self.orders_table.heading("item", text="Item")
        self.orders_table.heading("quantity", text="Quantity")
        self.orders_table.column("order_id", width=150)
        self.orders_table.column("item", width=300)
        self.orders_table.column("quantity", width=150)
        self.orders_table.pack(fill=BOTH, expand=1)

        self.populate_orders()

    def populate_orders(self):
        for row in self.orders_table.get_children():
            self.orders_table.delete(row)

        orders_data = self.collection.find()

        for order in orders_data:
            order_id = str(order.get("_id", ""))
            order_items = order.get("order_items", [])
            self.orders_table.insert("", "end", values=((order_id, "", ""),))

            for item in order_items:
                item_name = item.get("item", "")
                quantity = item.get("quantity", "")
                self.orders_table.insert(
                    "",
                    "end",
                    values=("", item_name, quantity),
                )


if __name__ == "__main__":
    root = Tk()
    obj = ViewOrders(root=root)
    root.mainloop()
