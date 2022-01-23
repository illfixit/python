import PyPDF2
import copy


pdf_file = "original.pdf"
background = "background.pdf"
merged_file = "merged.pdf"


with open(pdf_file, 'rb') as pdf_file, open(background, 'rb') as background:
  pdf_file_pypdf = PyPDF2.PdfFileReader(pdf_file)
  background_pypdf = PyPDF2.PdfFileReader(background)

  print(pdf_file_pypdf.getNumPages(), background_pypdf.getNumPages())
  output = PyPDF2.PdfFileWriter()
  background_page = background_pypdf.getPage(0)

  # for i in range(pdf_file_pypdf.getNumPages()):
  for i in range(10,16):


    print('Page', i)

    temp_page = copy.copy(background_page)
    # copy.deepcopy(x)

    pdf_page = pdf_file_pypdf.getPage(i)

    temp_page.mergePage(pdf_page)
    output.addPage(temp_page)
  
  with open("merged.pdf",'wb') as merged_file:
    output.write(merged_file)
