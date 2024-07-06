from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from user_login import LoginWindow
from manager_login import ManagerLogin


class Manager:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1230x590+0+0")
        self.root.title("Restaurant Automation System")

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
            bg_img, image=self.photoimg5, command=self.manager_window, cursor="hand2"
        )
        b1.place(x=380, y=120, width=140, height=100)
        b1_1 = Button(
            bg_img,
            text="Manager",
            command=self.manager_window,
            cursor="hand2",
            font=("lucida handwriting", 10),
            bg="white",
            fg="black",
        )
        b1_1.place(x=380, y=220, width=140, height=40)

        img6 = Image.open(r"images/FD.jpg")
        img6 = img6.resize((140, 110), Image.AFFINE)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(
            bg_img, image=self.photoimg6, cursor="hand2", command=self.waiter_window
        )
        b1.place(x=600, y=120, width=140, height=100)
        b1_1 = Button(
            bg_img,
            text="Waiter",
            cursor="hand2",
            command=self.waiter_window,
            font=("lucida handwriting", 10),
            bg="white",
            fg="black",
        )
        b1_1.place(x=600, y=220, width=140, height=40)

    def exit(self):
        self.exit = tkinter.messagebox.askyesno(
            "Exit", "Are you sure you want to exit?", parent=self.root
        )
        if self.exit > 0:
            self.root.destroy()
        else:
            return

    def manager_window(self):
        self.new_window = Toplevel(self.root)
        self.app = ManagerLogin(self.new_window)

    def waiter_window(self):
        self.new_window = Toplevel(self.root)
        self.app = LoginWindow(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Manager(root)
    root.mainloop()
