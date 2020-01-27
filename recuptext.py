# importing required modules
import PyPDF2, hashlib, math

# creating a pdf file object
pdf_file = open('INFO_Maupassant_Bel_Ami.pdf', 'rb')

# creating a pdf reader object
read_pdf = PyPDF2.PdfFileReader(pdf_file)

count = 0
count2 = 0
block = ''


for x in range (read_pdf.numPages):
    # creating a page object
    content = read_pdf.getPage(x)
    # extracting text from page
    text = content.extractText()+ "\n"
    block += text
    # Counter to group pages by 5
    count += 1

    #
    count2 += 1
    if count==5:
        print("Content Block ##\n", block, "\n")
        #hash du bloc
        hash = hashlib.sha256()
        hash.update(block.encode('UTF-8'))
        print("Content hash ##\n", hash.hexdigest() + "\n")
        count = 0
        block = ''
    elif count2 == read_pdf.numPages:
        print("Content Block ##\n", block, "\n")
        hash = hashlib.sha256()
        hash.update(block.encode('UTF-8'))
        print("Content hash ##\n", hash.hexdigest() + "\n")




