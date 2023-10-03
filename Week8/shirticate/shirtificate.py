from fpdf import FPDF

def main():
    name=input("Name: ")
    convert(name)

def convert(s):
    pdf=FPDF(unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 40)
    pdf.cell(txt='CS50 Shirtificate',align='C',center=True)
    pdf.ln(130)
    pdf.image('shirtificate.png',x=10,y=70,w=190)
    pdf.set_font("helvetica", "B", 30)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(txt=f'{s} took CS50',align='C',center=True)

    pdf.output("shirtificate.pdf")

if __name__=="__main__":
    main()