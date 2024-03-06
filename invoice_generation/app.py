# from datetime import date
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import cm

# import tkinter as tk
# from tkinter import ttk, simpledialog


# #######################################
# # The main function 'generate_invoice'
# # sets up a simple tkinter form,
# # gets the invoice info, and generates
# # a PDF based on the entered info
# #######################################
# def generate_pdf(event=None):
#     # Get the invoice amount from the GUI
#     invoice_amount = int(invoice_amount_entry.get())

#     # Create a PDF file
#     c = canvas.Canvas("invoice.pdf")

#     # Add the invoice header
#     c.setFont("Times-Bold", 18)
#     c.drawCentredString(10 * cm, 2.5 * cm, "Invoice")

#     # Add the invoice details
#     c.setFont("Times-Roman", 12)
#     c.setLineWidth(0.5)
#     c.rect(0.2 * cm, 3.0 * cm, 19.8 * cm, 26.5 * cm)
#     c.drawString(1 * cm, 5 * cm, "Invoice Number: {}".format("Your invoice number"))
#     c.drawString(1 * cm, 6 * cm, "Date: {}".format(date.today().strftime("%Y-%m-%d")))
#     c.drawString(1 * cm, 7 * cm, "Amount: $ {}".format(invoice_amount))

#     # Save and close the PDF file
#     c.showPage()
#     c.save()

#     # Display a success message
#     tk.messagebox.showinfo(
#         title="Invoice Generated", message="Invoice generated successfully!"
#     )

#     # Destroy the window
#     root.destroy()


# root = tk.Tk()
# root.title("Invoice Generator")
# root.geometry("500x300")

# tk.Label(root, text="Invoice Amount:").grid(row=0, sticky="w")
# invoice_amount_entry = tk.Entry(root, width=15)
# invoice_amount_entry.focus()
# invoice_amount_entry.grid(row=0, column=1)

# generate_btn = tk.Button(root, text="Generate Invoice", command=generate_pdf)
# generate_btn.grid(row=1, column=0, columnspan=2, sticky="w")
# cancel_btn = tk.Button(root, text="Cancel", command=root.destroy)
# cancel_btn.grid(row=2, column=0, columnspan=2, sticky="w")


# # Start the program
# if __name__ == "__main__":
#     root.mainloop()
import tkinter as tk
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from tkinter import Tk, Entry, StringVar, Label, Button


def generate_invoice():
    # Get the invoice amount from the entry
    invoice_amount = float(invoice_amount_entry.get())

    # Get the current date
    today = date.today()

    # Create a PDF file
    c = canvas.Canvas("invoice.pdf")

    # Add the invoice header
    c.setFont("Times-Bold", 18)
    c.drawCentredString(10 * cm, 2.5 * cm, "Invoice")

    # Add the invoice details
    c.setFont("Times-Roman", 12)
    c.setLineWidth(0.5)
    c.rect(0.2 * cm, 3.0 * cm, 19.8 * cm, 26.5 * cm)
    c.drawString(1 * cm, 5 * cm, "Invoice Number: {}".format("Your invoice number"))
    c.drawString(1 * cm, 6 * cm, "Date: {}".format(today.strftime("%Y-%m-%d")))
    c.drawString(1 * cm, 7 * cm, "Amount: $ {}".format(invoice_amount))

    # Save and close the PDF file
    c.showPage()
    c.save()


def create_ui():
    global invoice_amount_entry, generate_invoice_btn
    # Create tkinter window
    window = Tk()
    window.title("Invoice Generator")

    # Create label for entering the invoice amount
    invoice_amount_lbl = Label(
        window, text="Enter the invoice amount:  ", justify="left", font="Times 10 bold"
    )
    invoice_amount_lbl.pack()

    # Create entry for entering the invoice amount
    invoice_amount_entry = Entry(
        window, font="Times 12", width=20, justify="center", textvariable=StringVar()
    )
    invoice_amount_entry.pack()

    # Create generate button
    generate_invoice_btn = Button(
        window, text="Generate Invoice", command=generate_invoice
    )
    generate_invoice_btn.pack(pady=(2, 3))

    # Start the tkinter event loop
    window.mainloop()


if __name__ == "__main__":
    create_ui()
