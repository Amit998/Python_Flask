from PyPDF2 import PdfFileReader,PdfFileWriter



def cropper(start,end,file):
    inputPdf=PdfFileReader(open(file,'rb'))
    outPdf=PdfFileWriter()

    ostream=open(file.split('.')[0]+"_cropped_"+".pdf",'wb')


    while start <= end:
        outPdf.addPage(inputPdf.getPage(start))
        outPdf.write(ostream)

        start+=1
    ostream.close()

# cropper(1,2,"sample2.pdf")