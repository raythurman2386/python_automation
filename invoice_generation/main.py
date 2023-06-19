from reportlab.pdfgen import canvas
from datetime import date
import os
# Playing around with a script to create my invoice for work each month.
# If no additional charges are needed it will create a basic Invoice.
# I should be able to alter this to potentially use it for customer invoicing as well so I can break away from paid services
# for my own custom solution

# Define the layout of the invoice
def create_invoice(canvas):
    # Add the company logo
    # canvas.drawImage('', 50, 750, 100, 100)

    # Add the invoice number and date
    canvas.setFont('Helvetica-Bold', 16)
    canvas.drawString(400, 750, 'Invoice #12345')
    canvas.setFont('Helvetica', 12)
    canvas.drawString(400, 725, 'Date: {}'.format(date.today().strftime('%m/%d/%Y')))

        # Add customer information
    canvas.setFont('Helvetica-Bold', 14)
    canvas.drawString(50, 650, 'Bill To:')
    canvas.setFont('Helvetica', 12)
    canvas.drawString(50, 625, 'Customer Name')
    canvas.drawString(50, 600, '123 Main St')
    canvas.drawString(50, 575, 'Anytown, USA 12345')

        # Add itemized list of charges
    canvas.setFont('Helvetica-Bold', 14)
    canvas.drawString(50, 500, 'Description')
    canvas.drawString(300, 500, 'Amount')
    canvas.setFont('Helvetica', 12)
    canvas.drawString(50, 475, 'Product 1')
    canvas.drawString(300, 475, '$100.00')
    canvas.drawString(50, 450, 'Product 2')
    canvas.drawString(300, 450, '$50.00')

        # Add total amount due
    canvas.setFont('Helvetica-Bold', 16)
    canvas.drawString(50, 400, 'Total Amount Due:')
    canvas.drawString(300, 400, '$150.00')

# Create a new PDF document and add the invoice
pdf_filename = 'invoice.pdf'
with open(pdf_filename, 'wb') as f:
    canvas = canvas.Canvas(f)
    create_invoice(canvas)
    canvas.save()

# Open the created PDF file
os.startfile(pdf_filename)