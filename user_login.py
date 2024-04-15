from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymongo
from take_order import TakeOrder


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Waiter Login")
        self.root.geometry("1230x590+0+0")

        self.username = StringVar()
        self.password = StringVar()

        img = Image.open(
            r"images/vecteezy_wood-table-top-for-display-with-blurred-restaurant-background_1948406.jpg"
        )
        img = img.resize((1230, 590), Image.AFFINE)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        self.root2 = Frame(self.root, bd=2, bg="black")
        self.root2.place(x=484, y=115, width=270, height=332)

        img1 = Image.open(r"images/user-modified.png")
        img1 = img1.resize((79, 74), Image.AFFINE)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1, bg="black", borderwidth=0)
        f_lbl.place(x=579, y=125, width=79, height=74)

        get_str = Label(
            self.root2,
            text="Get Started",
            font=("lucida handwriting", 12, "bold"),
            fg="white",
            bg="black",
        )
        get_str.place(x=80, y=85)

        username_lbl = Label(
            self.root2,
            text="Username",
            font=("lucida handwriting", 10),
            fg="white",
            bg="black",
        )
        username_lbl.place(x=20, y=125)

        self.user_entry = ttk.Entry(
            self.root2,
            textvariable=self.username,
            width=37,
            font=("times new roman", 10),
        )
        self.user_entry.place(x=20, y=145)

        pass_lbl = Label(
            self.root2,
            text="Password",
            font=("lucida handwriting", 10),
            fg="white",
            bg="black",
        )
        pass_lbl.place(x=20, y=175)

        self.pass_entry = ttk.Entry(
            self.root2,
            textvariable=self.password,
            width=37,
            font=("times new roman", 10),
            show="*",
        )
        self.pass_entry.place(x=20, y=195)

        login_btn = Button(
            self.root2,
            text="Login",
            command=self.login,
            width=14,
            font=("times new roman", 13),
            bg="red",
            fg="white",
            activeforeground="white",
            activebackground="red",
        )
        login_btn.place(x=70, y=230)

    def login(self):
        if self.user_entry.get() == "" or self.pass_entry.get() == "":
            messagebox.showerror("Error", "All fields required.")
        else:
            # MongoDB connection
            client = pymongo.MongoClient(
                "mongodb+srv://agrawalkanhaiya552:Agrawal88628@cluster0.jcaswif.mongodb.net/"
            )
            db = client["RAS"]
            collection = db["waiters"]

            # Query MongoDB for user
            user_query = {
                "username": self.username.get(),
                "password": self.password.get(),
            }
            user = collection.find_one(user_query)

            if user:
                self.new_window = Toplevel(self.root)
                self.app = TakeOrder(self.new_window)
            else:
                messagebox.showerror("Error", "Invalid username and password.")


if __name__ == "__main__":
    root = Tk()
    obj = LoginWindow(root=root)
    root.mainloop()
