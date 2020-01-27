import PyPDF2, hashlib, math

pdf_file = open('INFO_Maupassant_Bel_Ami.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)

count = 0
block = ''

for x in range (read_pdf.numPages):

    content = read_pdf.getPage(x)
    text = content.extractText()+ "\n"
    block += text
    count += 1
    number_of_pages = read_pdf.numPages
    if count==5:
        print("Content Block ##\n", block, "\n")
        hash = hashlib.sha256()
        hash.update(block.encode('UTF-8'))
        print("Content hash ##\n", hash.hexdigest() + "\n")
        count = 0
        block = ''

    elif count < 5:
        print("Content Block ##\n", block, "\n")
        hash = hashlib.sha256()
        hash.update(block.encode('UTF-8'))
        print("Content hash ##\n", hash.hexdigest() + "\n")



