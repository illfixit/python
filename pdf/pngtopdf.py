from fpdf import FPDF
pdf = FPDF()
# imagelist is the list with all image filenames

pdf.add_page()
pdf.image('paper.png',0,0)

pdf.output("paper.pdf", "F")