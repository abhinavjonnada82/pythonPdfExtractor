# importing required modules
import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
 

#open allows you to read the file
pdfFileObj = open('para01.pdf', 'rb')
#The pdfReader variable is a readable object that will be parsed
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#discerning the number of pages will allow us to parse through all #the pages
num_pages = pdfReader.numPages
count = 0
text = ""
text = textract.process("/Users/abhinavjonnada/Desktop/Python Test", method='tesseract', language='eng')
#The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=10
    text += pageObj.extractText()
#This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
if text != "":
   text = text
#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
else:
   text = textract.process("/Users/abhinavjonnada/Desktop/Python Test/para01.pdf", method='tesseract', language='eng')

# tokens = word_tokenize(text)
# #we'll create a new list which contains punctuation we wish to clean
# punctuations = ['(',')',';',':','[',']',',']
# #We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords
# stop_words = stopwords.words('english')
# #We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
#  keywords = [word for word in tokens if not word in stop_words and  not word in string.punctuation]

# import PyPDF2
 
# # creating a pdf file object
# pdfFileObj = open('rtu.pdf', 'rb')
 
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# # printing number of pages in pdf file
# print(pdfReader.numPages)
 
# # creating a page object
# pageObj = pdfReader.getPage(0)
 
# # extracting text from page
# print(pageObj.extractText())
 
# # closing the pdf file object
# pdfFileObj.close()