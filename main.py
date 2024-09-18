from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

# sets font for everything below until a new set_font function is called
pdf.set_font(family="Times", style="B", size=12)

# h recommended to be set to the same as the font size above
pdf.cell(w=0, h=12, txt="Hello there!", align="L", ln=1, border=1)
pdf.cell(w=0, h=12, txt="Hey!", align="L", ln=1, border=1)

pdf.output("output.pdf")
