from tkinter import *
import os


class InventoryManagerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Manager")
        self.root.geometry("300x200")

        self.add_btn = Button(
            root, text="Add Inventory", command=self.open_add_inventory
        )
        self.add_btn.pack(pady=10)

        self.edit_btn = Button(
            root, text="Edit Inventory", command=self.open_edit_inventory
        )
        self.edit_btn.pack(pady=10)

        self.delete_btn = Button(
            root, text="Delete Inventory", command=self.open_delete_inventory
        )
        self.delete_btn.pack(pady=10)

        self.view_btn = Button(
            root, text="View Inventory", command=self.open_view_inventory
        )
        self.view_btn.pack(pady=10)

    def open_add_inventory(self):
        os.system("python add_inventory.py")

    def open_edit_inventory(self):
        os.system("python edit_inventory.py")

    def open_delete_inventory(self):
        os.system("python delete_inventory.py")

    def open_view_inventory(self):
        os.system("python view_inventory.py")


if __name__ == "__main__":
    root = Tk()
    app = InventoryManagerWindow(root)
    root.mainloop()
