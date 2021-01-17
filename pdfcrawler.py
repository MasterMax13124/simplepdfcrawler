import pdfplumber
import os

#os.chdir("tgnotes")


pdflist = os.listdir()
megafile = open("megafile.txt", "w+")
index = 0

for filename in pdflist:
    if filename[-3:] == "pdf":

        print(index)
        pdf = pdfplumber.open(pdflist[index])
        text = pdf.pages[0].extract_text()
        print("Error occured in file " + index + " " + filename)

        megafile.write("\n\n Text from " + filename + "\n" + text)

        pdf.close()
    index = index +1


megafile.close()