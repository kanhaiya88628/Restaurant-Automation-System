from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import requests
import pandas as pd
from df_to_tkinter_table import DfToTkinterTable
from df_to_excel_resolver import df_to_excel


class MenuUpdation:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1230x590+0+0")
        self.root.title("Add to Menu")

        # Variables
        self.var_item = StringVar()
        self.var_disc = StringVar()
        self.var_price = StringVar()
        self.var_raw = StringVar()

        img1 = Image.open(
            r"images/vecteezy_wood-table-top-for-display-with-blurred-restaurant-background_1948406.jpg"
        )
        img1 = img1.resize((410, 130), Image.AFFINE)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=410, height=130)

        img2 = Image.open(
            r"images/vecteezy_wood-table-top-for-display-with-blurred-restaurant-background_1948406.jpg"
        )
        img2 = img2.resize((410, 130), Image.AFFINE)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=410, y=0, width=410, height=130)

        img3 = Image.open(
            r"images/vecteezy_wood-table-top-for-display-with-blurred-restaurant-background_1948406.jpg"
        )
        img3 = img3.resize((410, 130), Image.AFFINE)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=820, y=0, width=410, height=130)

        img4 = Image.open(r"images/download.jpg")
        img4 = img4.resize((1230, 460), Image.AFFINE)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1230, height=460)

        title_lbl = Label(
            bg_img,
            text="TABLE TECH",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="black",
        )
        title_lbl.place(x=0, y=0, width=1230, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1200, height=390)

        # label frames
        # left
        left_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Add to Menu",
            bg="black",
            fg="white",
            font=("times new roman", 12, "bold"),
        )
        left_frame.place(x=10, y=10, width=570, height=360)

        item_name_label = Label(
            left_frame,
            text="Item Name",
            font=("times new roman", 12),
            fg="white",
            bg="black",
        )
        item_name_label.grid(row=4, column=0, padx=10, sticky=W)
        self.item_name_entry = ttk.Entry(
            left_frame,
            textvariable=self.var_item,
            width=20,
            font=("times new roman", 12),
        )
        self.item_name_entry.grid(row=4, column=1, padx=2, pady=10, sticky=W)

        price_label = Label(
            left_frame,
            text="Price",
            font=("times new roman", 12),
            fg="white",
            bg="black",
        )
        price_label.grid(row=5, column=0, padx=10, sticky=W)
        self.price_entry = ttk.Entry(
            left_frame,
            textvariable=self.var_price,
            width=20,
            font=("times new roman", 12),
        )
        self.price_entry.grid(row=5, column=1, padx=2, pady=10, sticky=W)

        discount_label = Label(
            left_frame,
            text="Discount",
            font=("times new roman", 12),
            fg="white",
            bg="black",
        )
        discount_label.grid(row=3, column=0, padx=10, sticky=W)
        self.discount_entry = ttk.Entry(
            left_frame,
            textvariable=self.var_disc,
            width=20,
            font=("times new roman", 12),
        )
        self.discount_entry.grid(row=3, column=1, padx=2, pady=10, sticky=W)

        raw_materials_label = Label(
            left_frame,
            text="Raw Materials",
            font=("times new roman", 12),
            fg="white",
            bg="black",
        )
        raw_materials_label.grid(row=6, column=0, padx=10, sticky=W)
        raw_materials_entry = ttk.Entry(
            left_frame,
            textvariable=self.var_raw,
            width=20,
            font=("times new roman", 12),
        )
        raw_materials_entry.grid(row=6, column=1, padx=2, pady=10, sticky=W)

        view_btn = Button(
            left_frame,
            text="View Menu",
            command=self.view_menu,
            width=15,
            font=("times new roman", 13),
            bg="darkblue",
            fg="black",
        )
        view_btn.grid(row=3, column=2)

        reset_btn = Button(
            left_frame,
            text="Reset",
            command=self.reset_data,
            width=15,
            font=("times new roman", 13),
            bg="darkblue",
            fg="black",
        )
        reset_btn.grid(row=8, column=2)

        add_btn = Button(
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
        right_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Menu Details",
            font=("times new roman", 12, "bold"),
            bg="black",
            fg="white",
        )
        right_frame.place(x=600, y=10, width=570, height=360)

        # table frame
        table_frame = LabelFrame(
            right_frame,
            bd=2,
            relief=RIDGE,
            text="Table Frame",
            font=("times new roman", 13, "bold"),
        )
        table_frame.place(x=5, y=5, width=550, height=330)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(
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
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("item_name", text="Item Name")
        self.student_table.heading("price", text="Price")
        self.student_table.heading("discount", text="Discount")
        self.student_table.heading("raw_materials", text="Raw Materials")

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.column("item_name", width=150)
        self.student_table.column("price", width=150)
        self.student_table.column("discount", width=150)
        self.student_table.column("raw_materials", width=150)

        self.student_table.pack(fill=BOTH, expand=1)

    def add_to_menu(self):
        url = "https://bigquery-cloudbuild-f7q24pru5q-ey.a.run.app/bigquery_operation_results"
        headers = {"Content-type": "application/json"}
        _dict = {
            "query": f"""
                            INSERT INTO  
                             `sandbox-381608.ras.menu`
                            VALUES(
                             "{self.var_item.get()}",
                             "{self.var_price.get()}",
                             "{self.var_disc.get()}",
                             "{self.var_raw.get()}"
                            );
                        """,
            "gbq_table_id": "sandbox-381608.ras.menu",
        }
        _response = requests.post(url, headers=headers, json=_dict)
        _result = _response.json()
        df = pd.DataFrame.from_records(_result.get("query_results").get("results"))
        df_to_excel(df)
        self.new_window = Toplevel(self.root)
        self.app = DfToTkinterTable(self.new_window)

    def view_menu(self):
        url = "https://bigquery-cloudbuild-f7q24pru5q-ey.a.run.app/bigquery_operation_results"
        headers = {"Content-type": "application/json"}
        _dict = {
            "query": f"""
                            SELECT *
                            FROM    
                             `sandbox-381608.ras.menu`;
                        """,
            "gbq_table_id": "sandbox-381608.ras.menu",
        }
        _response = requests.post(url, headers=headers, json=_dict)
        _result = _response.json()
        df = pd.DataFrame.from_records(_result.get("query_results").get("results"))
        df_to_excel(df)
        self.new_window = Toplevel(self.root)
        self.app = DfToTkinterTable(self.new_window)

    # Reset Function
    def reset_data(self):
        self.var_item.set("")
        self.var_disc.set("")
        self.var_price.set("")
        self.var_raw.set("")


if __name__ == "__main__":
    root = Tk()
    obj = MenuUpdation(root)
    root.mainloop()
