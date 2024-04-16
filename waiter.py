from tkinter import *
from PIL import Image, ImageTk
import os


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("600x400+300+100")

        img = Image.open("images/restaurant.jpg")
        img = img.resize((600, 400), Image.AFFINE)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        take_order_btn = Button(
            self.root,
            text="Take Order",
            command=self.open_take_order_window,
            width=20,
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        take_order_btn.place(x=100, y=150)

        view_orders_btn = Button(
            self.root,
            text="View Orders",
            command=self.view_orders,
            width=20,
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        view_orders_btn.place(x=100, y=250)

    def open_take_order_window(self):
        os.system("python take_order.py")

    def view_orders(self):
        os.system("python view_orders.py")


if __name__ == "__main__":
    root = Tk()
    obj = MainMenu(root=root)
    root.mainloop()
