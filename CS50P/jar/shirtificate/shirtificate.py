from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", style="B", size=50)
pdf.cell(0, 40, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", x=3, y=50)
pdf.set_font("helvetica", size=30)
pdf.set_text_color(r=255, g=255, b=255)
pdf.cell(-175, 230, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")
