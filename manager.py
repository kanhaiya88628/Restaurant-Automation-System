from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import os
from add_to_menu import MenuUpdation
from create_account import WaiterCreateAccount
from invoice import InvoiceGenerator
from update_menu import MenuUpdater
from inventory_manager import InventoryManagerWindow
from general_report import GeneralReport
from update_waiter import EditWaiterWindow


class Manager:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1230x590+0+0")
        self.root.title("Manager Portal")

        img1 = Image.open(r"images/TLL.jpg")
        img1 = img1.resize((410, 130), Image.AFFINE)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=410, height=130)

        img2 = Image.open(r"images/TC.jpg")
        img2 = img2.resize((410, 130), Image.AFFINE)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=410, y=0, width=410, height=130)

        img3 = Image.open(r"images/TR.jpg")
        img3 = img3.resize((410, 130), Image.AFFINE)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=820, y=0, width=410, height=130)

        img4 = Image.open(
            r"images/vecteezy_wood-table-top-for-display-with-blurred-restaurant-background_1948406.jpg"
        )
        img4 = img4.resize((1230, 590), Image.AFFINE)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        img5 = Image.open(r"images/StudentDetails.jpg")
        img5 = img5.resize((140, 110), Image.AFFINE)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(
            bg_img, image=self.photoimg5, command=self.create_account, cursor="hand2"
        )
        b1.place(x=180, y=120, width=140, height=100)
        b1_1 = Button(
            bg_img,
            text="Create Account",
            command=self.create_account,
            cursor="hand2",
            font=("lucida handwriting", 10),
            bg="white",
            fg="black",
        )
        b1_1.place(x=180, y=220, width=140, height=40)

        img6 = Image.open(r"images/FD.jpg")
        img6 = img6.resize((140, 110), Image.AFFINE)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(
            bg_img, image=self.photoimg6, cursor="hand2", command=self.update_account
        )
        b1.place(x=400, y=120, width=140, height=100)
        b1_1 = Button(
            bg_img,
            text="Update Account",
            cursor="hand2",
            command=self.update_account,
            font=("lucida handwriting", 10),
            bg="white",
            fg="black",
        )
        b1_1.place(x=400, y=220, width=140, height=40)

        img7 = Image.open(r"images/Attendance.png")
        img7 = img7.resize((140, 110), Image.AFFINE)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.attend)
        b1.place(x=620, y=120, width=140, height=100)
        b1_1 = Button(
            bg_img,
            text="Generate Report",
            cursor="hand2",
            command=self.attend,
            font=("lucida handwriting", 10),
            bg="white",
            fg="black",
        )
        b1_1.place(x=620, y=220, width=140, height=40)

        img8 = Image.open(r"images/Help.jpg")
        img8 = img8.resize((140, 110), Image.AFFINE)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(
            bg_img, image=self.photoimg8, cursor="hand2", command=self.check_inventory
        )
        b1.place(x=840, y=120, width=140, height=100)
        b1_1 = Button(
            bg_img,
            text="Check Inventory",
            cursor="hand2",
            command=self.check_inventory,
            font=("lucida handwriting", 10),
            bg="white",
            fg="black",
        )
        b1_1.place(x=840, y=220, width=140, height=40)

        img9 = Image.open(r"images/Train.jpg")
        img9 = img9.resize((140, 110), Image.AFFINE)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 = Button(
            bg_img, image=self.photoimg9, cursor="hand2", command=self.add_to_menu
        )
        b1.place(x=180, y=310, width=140, height=100)
        b1_1 = Button(
            bg_img,
            text="Add to Menu",
            cursor="hand2",
            command=self.add_to_menu,
            font=("lucida handwriting", 10),
            bg="white",
            fg="black",
        )
        b1_1.place(x=180, y=410, width=140, height=40)

        img10 = Image.open(r"images/Photos.jpg")
        img10 = img10.resize((140, 110), Image.AFFINE)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(
            bg_img, image=self.photoimg10, cursor="hand2", command=self.update_menu
        )
        b1.place(x=400, y=310, width=140, height=100)
        b1_1 = Button(
            bg_img,
            text="Update Menu",
            cursor="hand2",
            command=self.update_menu,
            font=("lucida handwriting", 10),
            bg="white",
            fg="black",
        )
        b1_1.place(x=400, y=410, width=140, height=40)

        img11 = Image.open(r"images/Developer.jpg")
        img11 = img11.resize((140, 110), Image.AFFINE)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1 = Button(
            bg_img, image=self.photoimg11, cursor="hand2", command=self.generate_invoice
        )
        b1.place(x=620, y=310, width=140, height=100)
        b1_1 = Button(
            bg_img,
            text="Generate Invoice",
            cursor="hand2",
            command=self.generate_invoice,
            font=("lucida handwriting", 10),
            bg="white",
            fg="black",
        )
        b1_1.place(x=620, y=410, width=140, height=40)

        img12 = Image.open(r"images/exit.jpg")
        img12 = img12.resize((140, 110), Image.AFFINE)
        self.photoimg12 = ImageTk.PhotoImage(img12)
        b1 = Button(bg_img, image=self.photoimg12, cursor="hand2", command=self.exit)
        b1.place(x=840, y=310, width=140, height=100)
        b1_1 = Button(
            bg_img,
            text="Exit",
            cursor="hand2",
            command=self.exit,
            font=("lucida handwriting", 10),
            bg="white",
            fg="black",
        )
        b1_1.place(x=840, y=410, width=140, height=40)

    def exit(self):
        self.exit = tkinter.messagebox.askyesno(
            "Exit", "Are you sure you want to exit?", parent=self.root
        )
        if self.exit > 0:
            self.root.destroy()
        else:
            return

    def create_account(self):
        self.new_window = Toplevel(self.root)
        self.app = WaiterCreateAccount(self.new_window)

    def add_to_menu(self):
        self.new_window = Toplevel(self.root)
        self.app = MenuUpdation(self.new_window)

    def update_account(self):
        self.new_window = Toplevel(self.root)
        self.app = EditWaiterWindow(self.new_window)

    def attend(self):
        self.new_window = Toplevel(self.root)
        self.app = GeneralReport(self.new_window)

    def generate_invoice(self):
        self.new_window = Toplevel(self.root)
        self.app = InvoiceGenerator(self.new_window)

    def check_inventory(self):
        self.new_window = Toplevel(self.root)
        self.app = InventoryManagerWindow(self.new_window)

    def update_menu(self):
        self.new_window = Toplevel(self.root)
        self.app = MenuUpdater(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Manager(root)
    root.mainloop()
