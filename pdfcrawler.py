import pdfplumber
import sys
import os

pathname = input("Please input the path to your pdf folder: ")
if pathname.find("/") == -1:
    pathname = os.getcwd() + "/" + pathname
os.chdir(pathname)

pdflist = os.listdir()
print("Found " + str(len(pdflist)) + " pdf-files")

if os.path.isfile(pathname + "/megafile.txt"):
    yesno = input("Do you want to overwrite the existing megafile.txt? (Y/n)")
    if yesno.lower() == "no" or yesno.lower() == "n":
        print("Exiting...")
        sys.exit()


megafile = open("megafile.txt", "w+")
index = 0

for filename in pdflist:
    if filename[-3:] == "pdf":
        #print(index)
        print("Reading file " + filename)
        pdf = pdfplumber.open(filename)
        text = pdf.pages[0].extract_text()
        megafile.write("Text from " + filename + "\n\n" + text + "\n\n\n")
        pdf.close()
    index = index +1


megafile.close()
