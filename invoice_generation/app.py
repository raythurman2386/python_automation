from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

# Set the invoice amount
invoice_amount = 6253

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
# from PyPDF2 import PdfFileWriter, PdfFileReader

# # Create the contents of your PDF
# mytext = "$6253"

# # Open the file to be written and store it in a variable
# myfile = open("invoice.pdf", "w+b")

# # Create the PdfFileWriter object that represents the new PDF
# # with this command any existing file is overwritten
# writer = PdfFileWriter()

# # Create an invoice object
# invoice = writer.create_pdf_invoice(mytext)

# # Write your new PDF in the file
# writer.write(myfile)

# # Close the file
# myfile.close()

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase

# # Create an email message
# msg = MIMEMultipart()
# msg['From'] = "your email address"
# msg['To'] = "receiver email address"
# msg['Subject'] = "Your Invoice"

# # Attach your new PDF
# att = MIMEBase("application", "octet-stream")
# att.set_payload(open("invoice.pdf", "rb").read())
# att.add_header("Content-Disposition", "attachment"; filename="invoice.pdf")
# msg.attach(att)

# # Send email
# smtp_server = "your smtp_server"
# s = smtplib.SMTP(smtp_server)
# s.starttls()
# s.sendmail("from", "to", msg.as_string())
# s.quit()

# from schedule import every

# every().month.on(15).at(“09:00”).do(automate_invoice_creation)
# schedule.run_pending()
