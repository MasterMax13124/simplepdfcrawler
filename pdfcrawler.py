import pdfplumber
import os

os.chdir("tgnotes")

megafile = open("megafile.txt", "w+")

pdflist = os.listdir()
index = 0
for filename in pdflist:
    print(index)
    pdf = pdfplumber.open(pdflist[index])
    try:
        text = pdf.pages[0].extract_text()
    except:
        print("Error occured in file " + index + " " + filename)

    megafile.write("\n\n Text from " + filename + "\n" + text)

    pdf.close()
    index = index +1

megafile.close()