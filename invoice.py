from tkinter import *
from tkinter import ttk
import pymongo
from bson import ObjectId
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


class InvoiceGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoice Generator")
        self.root.geometry("400x200")

        # Connect to MongoDB
        self.client = pymongo.MongoClient(
            "mongodb+srv://agrawalkanhaiya552:Agrawal88628@cluster0.jcaswif.mongodb.net/"
        )
        self.db = self.client["RAS"]
        self.orders_collection = self.db["orders"]
        self.menu_collection = self.db["menu"]

        # Retrieve order IDs from MongoDB
        self.order_ids = self.get_order_ids()

        # Dropdown menu to select order ID
        self.selected_order_id = StringVar()
        order_id_label = Label(self.root, text="Select Order ID:")
        order_id_label.grid(row=0, column=0, padx=10, pady=10)
        self.order_id_dropdown = ttk.Combobox(
            self.root,
            textvariable=self.selected_order_id,
            values=self.order_ids,
            width=30,  # Set the width of the dropdown field
        )
        self.order_id_dropdown.grid(row=0, column=1, padx=10, pady=10)
        self.order_id_dropdown.bind("<<ComboboxSelected>>", self.order_id_selected)

        # Button to generate invoice
        generate_btn = Button(
            self.root, text="Generate Invoice", command=self.generate_invoice
        )
        generate_btn.grid(row=1, column=0, columnspan=2, pady=10)

    def get_order_ids(self):
        # Query MongoDB for order IDs
        order_ids = [
            str(order["_id"]) for order in self.orders_collection.find({}, {"_id": 1})
        ]
        return order_ids

    def order_id_selected(self, event):
        # Callback function when order ID is selected
        pass

    def generate_invoice(self):
        # Generate invoice based on the selected order ID
        selected_order_id = self.selected_order_id.get()
        print("Selected Order ID:", selected_order_id)  # Debugging statement

        if selected_order_id:
            # Retrieve order details from MongoDB based on the selected order ID and generate the invoice
            order_details = self.orders_collection.find_one(
                {"_id": ObjectId(selected_order_id)}
            )
            print("Order Details:", order_details)  # Debugging statement

            if order_details:
                # Here you can generate the invoice using the order details
                self.generate_pdf_invoice(order_details, selected_order_id)
                print("Invoice generated for Order ID:", selected_order_id)
            else:
                print("Order details not found for Order ID:", selected_order_id)
        else:
            print("Please select an Order ID.")

    def generate_pdf_invoice(self, order_details, order_id):
        # Generate PDF invoice
        pdf_filename = f"Invoice_{order_id}.pdf"
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
        table_data = [["Item", "Quantity", "Price"]]
        total_amount = 0
        for item in order_details["order_items"]:
            item_name = item["item"]
            quantity = item["quantity"]
            item_details = self.menu_collection.find_one({"item_name": item_name})
            if item_details:
                price = float(item_details.get("price", 0))
                total_amount += price * quantity
                table_data.append([item_name, str(quantity), f"{price:.2f}"])
        table_data.append(["Total", "", f"{total_amount:.2f}"])  # Add total amount row
        table = Table(table_data)
        style = TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("BACKGROUND", (0, 1), (-1, -2), colors.beige),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ]
        )
        table.setStyle(style)
        doc.build([table])
        print(f"Invoice saved as {pdf_filename}")


if __name__ == "__main__":
    root = Tk()
    obj = InvoiceGenerator(root)
    root.mainloop()
