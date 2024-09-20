from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():

    pdf.add_page()

    # sets font for everything below until a new set_font function is called
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    # h recommended to be set to the same as the font size above
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)

    # add extra pages, -1 is because we already added the first page above
    for i in range(row["Pages"]-1):
        pdf.add_page()



pdf.output("output.pdf")
