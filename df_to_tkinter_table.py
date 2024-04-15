import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import pymongo


class DfToTkinterTable:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.pack_propagate(False)
        self.root.resizable(0, 0)

        # MongoDB connection
        self.client = pymongo.MongoClient(
            "mongodb+srv://agrawalkanhaiya552:Agrawal88628@cluster0.jcaswif.mongodb.net/"
        )
        self.db = self.client["RAS"]
        self.collection = self.db["menu"]

        # Frame for TreeView
        frame1 = tk.LabelFrame(root, text="Menu Data")
        frame1.place(height=250, width=500)

        # Frame for open file dialog
        file_frame = tk.LabelFrame(root, text="Open File")
        file_frame.place(height=100, width=400, rely=0.65, relx=0)

        # Buttons
        button1 = tk.Button(
            file_frame, text="Load Data", command=lambda: self.Load_menu_data()
        )
        button1.place(rely=0.65, relx=0.50)

        # The file/file path text
        self.label_file = ttk.Label(file_frame, text="MongoDB")
        self.label_file.place(rely=0, relx=0)

        self.tv1 = ttk.Treeview(frame1)
        self.tv1.place(relheight=1, relwidth=1)

        treescrolly = tk.Scrollbar(frame1, orient="vertical", command=self.tv1.yview)
        treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=self.tv1.xview)
        self.tv1.configure(
            xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set
        )
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")

    def Load_menu_data(self):
        """Load data from MongoDB collection 'menu' into the Treeview"""
        try:
            # Query MongoDB for menu data
            menu_data = self.collection.find()

            # Convert cursor to DataFrame
            df = pd.DataFrame(list(menu_data))

            self.clear_data()
            self.tv1["column"] = list(df.columns)
            self.tv1["show"] = "headings"
            for column in self.tv1["columns"]:
                self.tv1.heading(column, text=column)

            df_rows = df.to_numpy().tolist()
            for row in df_rows:
                self.tv1.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_data(self):
        """Clear the Treeview data"""
        self.tv1.delete(*self.tv1.get_children())


if __name__ == "__main__":
    root = tk.Tk()
    obj = DfToTkinterTable(root)
    root.mainloop()
