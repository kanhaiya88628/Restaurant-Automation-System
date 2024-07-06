import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pymongo


class MenuUpdation:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1230x590+0+0")
        self.root.title("Add to Menu")

        self.client = pymongo.MongoClient(
            "mongodb+srv://agrawalkanhaiya552:Agrawal88628@cluster0.jcaswif.mongodb.net/"
        )
        self.db = self.client["RAS"]
        self.collection = self.db["menu"]

        self.var_item = tk.StringVar()
        self.var_disc = tk.StringVar()
        self.var_price = tk.StringVar()
        self.var_raw = tk.StringVar()

        img1 = Image.open(
            r"images/vecteezy_wood-table-top-for-display-with-blurred-restaurant-background_1948406.jpg"
        )
        img1 = img1.resize((410, 130), Image.AFFINE)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = tk.Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=410, height=130)

        img2 = Image.open(
            r"images/vecteezy_wood-table-top-for-display-with-blurred-restaurant-background_1948406.jpg"
        )
        img2 = img2.resize((410, 130), Image.AFFINE)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = tk.Label(self.root, image=self.photoimg2)
        f_lbl.place(x=410, y=0, width=410, height=130)

        img3 = Image.open(
            r"images/vecteezy_wood-table-top-for-display-with-blurred-restaurant-background_1948406.jpg"
        )
        img3 = img3.resize((410, 130), Image.AFFINE)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = tk.Label(self.root, image=self.photoimg3)
        f_lbl.place(x=820, y=0, width=410, height=130)

        img4 = Image.open(r"images/download.jpg")
        img4 = img4.resize((1230, 460), Image.AFFINE)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = tk.Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1230, height=460)

        title_lbl = tk.Label(
            bg_img,
            text="Restaurant Automation System",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="black",
        )
        title_lbl.place(x=0, y=0, width=1230, height=45)

        main_frame = tk.Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1200, height=390)

        left_frame = tk.LabelFrame(
            main_frame,
            bd=2,
            relief=tk.RIDGE,
            text="Add to Menu",
            bg="black",
            fg="white",
            font=("times new roman", 12, "bold"),
        )
        left_frame.place(x=10, y=10, width=570, height=360)

        item_name_label = tk.Label(
            left_frame,
            text="Item Name",
            font=("times new roman", 12),
            fg="white",
            bg="black",
        )
        item_name_label.grid(row=4, column=0, padx=10, sticky=tk.W)
        self.item_name_entry = ttk.Entry(
            left_frame,
            textvariable=self.var_item,
            width=20,
            font=("times new roman", 12),
        )
        self.item_name_entry.grid(row=4, column=1, padx=2, pady=10, sticky=tk.W)

        price_label = tk.Label(
            left_frame,
            text="Price",
            font=("times new roman", 12),
            fg="white",
            bg="black",
        )
        price_label.grid(row=5, column=0, padx=10, sticky=tk.W)
        self.price_entry = ttk.Entry(
            left_frame,
            textvariable=self.var_price,
            width=20,
            font=("times new roman", 12),
        )
        self.price_entry.grid(row=5, column=1, padx=2, pady=10, sticky=tk.W)

        discount_label = tk.Label(
            left_frame,
            text="Discount",
            font=("times new roman", 12),
            fg="white",
            bg="black",
        )
        discount_label.grid(row=3, column=0, padx=10, sticky=tk.W)
        self.discount_entry = ttk.Entry(
            left_frame,
            textvariable=self.var_disc,
            width=20,
            font=("times new roman", 12),
        )
        self.discount_entry.grid(row=3, column=1, padx=2, pady=10, sticky=tk.W)

        raw_materials_label = tk.Label(
            left_frame,
            text="Raw Materials",
            font=("times new roman", 12),
            fg="white",
            bg="black",
        )
        raw_materials_label.grid(row=6, column=0, padx=10, sticky=tk.W)
        raw_materials_entry = ttk.Entry(
            left_frame,
            textvariable=self.var_raw,
            width=20,
            font=("times new roman", 12),
        )
        raw_materials_entry.grid(row=6, column=1, padx=2, pady=10, sticky=tk.W)

        view_btn = tk.Button(
            left_frame,
            text="View Menu",
            command=self.view_menu,
            width=15,
            font=("times new roman", 13),
            bg="white",
            fg="black",
        )
        view_btn.grid(row=3, column=2)

        reset_btn = tk.Button(
            left_frame,
            text="Reset",
            command=self.reset_data,
            width=15,
            font=("times new roman", 13),
            bg="white",
            fg="black",
        )
        reset_btn.grid(row=8, column=2)

        add_btn = tk.Button(
            left_frame,
            text="Add to Menu",
            command=self.add_to_menu,
            width=15,
            font=("times new roman", 13),
            bg="darkgreen",
            fg="black",
        )
        add_btn.grid(row=6, column=2, padx=28, pady=4)

        # Right
        right_frame = tk.LabelFrame(
            main_frame,
            bd=2,
            relief=tk.RIDGE,
            text="Menu Details",
            font=("times new roman", 12, "bold"),
            bg="black",
            fg="white",
        )
        right_frame.place(x=600, y=10, width=570, height=360)

        # table frame
        table_frame = tk.LabelFrame(
            right_frame,
            bd=2,
            relief=tk.RIDGE,
            text="Table Frame",
            font=("times new roman", 13, "bold"),
        )
        table_frame.place(x=5, y=5, width=550, height=330)

        scroll_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)
        self.menu_table = ttk.Treeview(
            table_frame,
            columns=(
                "item_name",
                "price",
                "discount",
                "raw_materials",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.menu_table.xview)
        scroll_y.config(command=self.menu_table.yview)

        self.menu_table.heading("item_name", text="Item Name")
        self.menu_table.heading("price", text="Price")
        self.menu_table.heading("discount", text="Discount")
        self.menu_table.heading("raw_materials", text="Raw Materials")

        self.menu_table["show"] = "headings"
        self.menu_table.pack(fill=tk.BOTH, expand=1)

        self.menu_table.column("item_name", width=150)
        self.menu_table.column("price", width=150)
        self.menu_table.column("discount", width=150)
        self.menu_table.column("raw_materials", width=150)

        self.menu_table.pack(fill=tk.BOTH, expand=1)

    def add_to_menu(self):
        item = self.var_item.get()
        price = self.var_price.get()
        discount = self.var_disc.get()
        raw_materials = self.var_raw.get()

        menu_item = {
            "item_name": item,
            "price": price,
            "discount": discount,
            "raw_materials": raw_materials,
        }

        self.collection.insert_one(menu_item)

        self.view_menu()

    def view_menu(self):

        for row in self.menu_table.get_children():
            self.menu_table.delete(row)

        menu_data = self.collection.find()

        for item in menu_data:
            self.menu_table.insert(
                "",
                "end",
                values=(
                    item["item_name"],
                    item["price"],
                    item["discount"],
                    item["raw_materials"],
                ),
            )

    def reset_data(self):
        self.var_item.set("")
        self.var_disc.set("")
        self.var_price.set("")
        self.var_raw.set("")


if __name__ == "__main__":
    root = tk.Tk()
    obj = MenuUpdation(root)
    root.mainloop()
