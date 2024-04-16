from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import pymongo


class TakeOrder:
    def __init__(self, root):
        self.root = root
        self.root.title("Take Order")
        self.root.geometry("1230x590+0+0")

        # Connect to MongoDB
        self.client = pymongo.MongoClient(
            "mongodb+srv://agrawalkanhaiya552:Agrawal88628@cluster0.jcaswif.mongodb.net/"
        )
        self.db = self.client["RAS"]
        self.collection = self.db["menu"]

        # Load background image
        img = Image.open(
            "images/vecteezy_wood-table-top-for-display-with-blurred-restaurant-background_1948406.jpg"
        )
        img = img.resize((1230, 590), Image.AFFINE)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame to hold order entry elements
        self.root2 = Frame(self.root, bd=2, bg="black")
        self.root2.place(x=484, y=115, width=500, height=380)

        # Label and dropdown for item selection
        item_label = Label(
            self.root2,
            text="Select Item:",
            font=("times new roman", 12),
            fg="white",
            bg="black",
        )
        item_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.selected_item = StringVar()
        self.item_dropdown = ttk.Combobox(
            self.root2,
            textvariable=self.selected_item,
            width=20,
            font=("times new roman", 12),
            state="readonly",
        )
        self.item_dropdown.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Retrieve items from MongoDB collection and populate the dropdown
        self.populate_menu()

        # Entry for order quantity
        quantity_label = Label(
            self.root2,
            text="Quantity:",
            font=("times new roman", 12),
            fg="white",
            bg="black",
        )
        quantity_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.quantity_entry = ttk.Entry(
            self.root2, width=20, font=("times new roman", 12)
        )
        self.quantity_entry.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Button to add item to cache table
        add_btn = Button(
            self.root2,
            text="Add to Order",
            command=self.add_to_order,
            width=15,
            font=("times new roman", 13),
            bg="white",
            fg="black",
        )
        add_btn.grid(row=2, column=1, padx=10, pady=10)

        # Button to place order
        place_order_btn = Button(
            self.root2,
            text="Place Order",
            command=self.place_order,
            width=15,
            font=("times new roman", 13),
            bg="white",
            fg="black",
        )
        place_order_btn.grid(row=3, column=1, padx=10, pady=10)

        # Table to display cached orders
        self.cache_table = ttk.Treeview(
            self.root2, columns=("item", "quantity"), selectmode="browse"
        )
        self.cache_table.heading("item", text="Item")
        self.cache_table.heading("quantity", text="Quantity")
        self.cache_table.column("item", width=150)
        self.cache_table.column("quantity", width=150)
        self.cache_table.grid(row=4, columnspan=2, padx=10, pady=10)

    def populate_menu(self):
        # Clear any existing values in the dropdown
        self.item_dropdown["values"] = []
        # Retrieve items from MongoDB collection
        menu_data = self.collection.find()
        # Populate the dropdown with item names
        items = [item["item_name"] for item in menu_data]
        self.item_dropdown["values"] = items
        # Set default selection
        if items:
            self.item_dropdown.current(0)

    def add_to_order(self):
        item = self.selected_item.get()
        quantity = self.quantity_entry.get()
        # Add the item and quantity to the cache table
        self.cache_table.insert("", "end", values=(item, quantity))

    def place_order(self):
        # Get all items and quantities from the cache table and process the order
        for child in self.cache_table.get_children():
            item = self.cache_table.item(child)["values"][0]
            quantity = self.cache_table.item(child)["values"][1]
            # Here you can add your code to process the order, e.g., send it to a database
        # Clear the cache table after placing the order
        self.cache_table.delete(*self.cache_table.get_children())


if __name__ == "__main__":
    root = Tk()
    obj = TakeOrder(root=root)
    root.mainloop()
