# simplepdfcrawler
Short python script that will extract all text from all pdf files in a given directory and combine it into a single txt.

## Usage:
Make sure that you have Python 3 installed. Then install [pdfplumber](https://github.com/jsvine/pdfplumber) like so:

`pip install pdfplumber`

Next clone this repository:

`git clone https://github.com/MasterMax13124/simplepdfcrawler`

Then simply execute the script:

`python3 simplepdfcrawler/pdfcrawler.py`

When asked for the path to the directory with the PDF files, either paste in the path relative to the directory from which you called the script, or the absolute path from the route of your drive.

## Thanks to:
The actual extraction of text is done entirely by pdfplumber. Find it here:

[pdfplumber github repo](https://github.com/jsvine/pdfplumber)
