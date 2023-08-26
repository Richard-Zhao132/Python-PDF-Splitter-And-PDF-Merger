#Title: Python PDF Merger and Splitter
#Richard Zhao
#NOTE: This program can merge 2 given PDF files together, or split 1 given PDF file into 1 or 2 PDF files


import PyPDF2
import sys
import os


#PDF Mergering
merger = PyPDF2.PdfMerger()


#Example: "C:/Users/richard/OneDrive/Desktop/Python Projects/PDF Merger and Splitter/PDF Merger folder"
#Enter The System Path Location Of Desired PDF Files to Merge 
dirPath_Merging = "Enter your path location here"
#Enter The System Path Location Of Desired PDF file to Split
dirPath2_Splitting = "Enter your path location here"



#Merging Function
def mergerfunc():
    #file 1 to merger
    #Enter file name, EX: '/Richard Zhao - Resume.pdf'
    merger.append(dirPath_Merging + 'Enter you pdf file 1 name here')
    merger.append(dirPath_Merging + 'Enter your pdf file 2 name here')

    #Creates New PDF File
    merger.write(dirPath_Merging + "\\" + "CombinedPdf.pdf")
    print("Done")
    #Closer Merger
    merger.close()


    '''
    #TEST CASE, DOES NOT WORK, REPEATS FIRST FILE MERGERINGS
    for file in os.listdir(dirPath):
        if file.endswith(".pdf"):
            absfile = os.path.join(dirPath, file)
            merger.append(absfile)
        merger.write(dirPath + "\\" + "CombinedPdf.pdf")
        print("Done")
    merger.close()
    '''



#PDF Splitter Function
def splitter():
    #NOTE: Page 1 Of PDF Is Index 0, So Here Is Page 2 And 3
    pages = [1, 2]
    pages2 = []


    #Opens Path To PDF
    #Enter The Name Of The File You Want To Split, Example Name: '/resume.pdf'
    with open(dirPath2_Splitting +"Enter Name of pdf", 'rb') as f:

        #Creating Reader And Writer Functions
        reader = PyPDF2.PdfReader(f)
        writer = PyPDF2.PdfWriter()

        #Use Rest Writer If You Want To Split To 2 PDF, ex: Use Pages2
        rest_writer = PyPDF2.PdfWriter()
        total_pages = len(reader.pages)
        for page in range(len(reader.pages)):
            if page in pages:
                writer.add_page(reader.pages[page])
            #else:
                #rest_writer.addPage(reader.getPage(page))


        #Create New PDF With Selected Pages, save name as 'selected.pdf'
        with open(dirPath2+"/selected.pdf", "wb") as f2:
            writer.write(f2)

        #with open(dirPath2+"/rest.pdf", "wb") as f2:
            #rest_writer.write(f2)

        




#Call Functions Here When Needed
def main():
    splitter()

main()

