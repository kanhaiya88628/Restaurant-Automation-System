from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


class TakeOrder:
    def __init__(self, root):
        self.root = root
        self.root.title("Take Order")
        self.root.geometry("1230x590+0+0")

        img = Image.open(
            r"images/vecteezy_wood-table-top-for-display-with-blurred-restaurant-background_1948406.jpg"
        )
        img = img.resize((1230, 590), Image.AFFINE)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        self.root2 = Frame(self.root, bd=2, bg="black")
        self.root2.place(x=484, y=115, width=350, height=380)

        order_label = Label(
            self.root2,
            text="Item Name",
            font=("times new roman", 12),
            fg="white",
            bg="black",
        )
        order_label.grid(row=5, column=0, padx=10, pady=100, sticky=W)
        self.order_entry = ttk.Entry(self.root2, width=20, font=("times new roman", 12))
        self.order_entry.grid(row=5, column=1, padx=2, pady=100, sticky=W)

        view_btn = Button(
            self.root2,
            text="Deliver",
            command=self.view_menu,
            width=15,
            font=("times new roman", 13),
            bg="darkblue",
            fg="black",
        )
        view_btn.grid(row=7, column=1)

    def view_menu(self):
        pass


if __name__ == "__main__":
    root = Tk()
    obj = TakeOrder(root=root)
    root.mainloop()
