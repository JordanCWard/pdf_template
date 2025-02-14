from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

# Pages shouldn't be broken automatically
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():

    pdf.add_page()

    # Sets font for everything below until a new set_font function is called
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    # Height (h) recommended to be set to the same as the font size above
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    """Add lines all the way to the end of the page.
    Start at 20 mm, end at 298, add 10 each time.
    """
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    """Sets the footer. ln adds 265 mm of break lines to move text to the
    bottom of the page.
    """
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # add extra pages, -1 is because we already added the first page above
    for i in range(row["Pages"]-1):
        pdf.add_page()

        """Sets the footer. ln adds 277 mm of break lines to move text to the
        bottom of the page.
        """
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        """Add lines all the way to the end of the page.
        Start at 20 mm, end at 298, add 10 each time.
        """
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")
