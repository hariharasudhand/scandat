from datetime import date
import re
import cv2
import numpy 
import pytesseract
from pytesseract import Output
from matplotlib import pyplot as plt
import xml.dom.minidom
from csv import writer
from csv import reader
from PIL import Image
from os import listdir
from os.path import isfile, join
import numpy
import cv2
import constants
import os


#TO:DO Check if this is needed and remove
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
xmin= ymin = xmax = ymax = 0



def plotAndExtractText(x, y, w, h, image, clone_image, fieldname):
 #print(' ploting at cordinates : ', str(x), str(y), str(w), str(h))
 image = cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)

# extract text per word as plotted in image
 thresh = 255 - cv2.threshold(clone_image, 0, 255,
 cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

 ROI = thresh[y:h, x:w]
 data = pytesseract.image_to_string(ROI, config='-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.$₹%&*@#!,/\;- --psm 6')
 # if image == None:
 #     print("the image is in correct size")
 # else:
 #     print("it is good size")
 print (data)

 file_object = open('result.csv', 'a')
 file_object.write(fieldname + '   :    ' + data)
 file_object.close()

 return data

def showImage(image):
 file1 = open('file.txt', 'r')
 Lines = file1.readlines()
 b, g, r = cv2.split(image)
 rgb_img = cv2.merge([r, g, b])
 plt.figure(figsize=(16, 12))
 plt.imshow(rgb_img)
 for line in Lines:  # <---
     img_path = (line.strip())
     fle = img_path.split("/")
     img_name = (fle[-1])
     plt.title('SAMPLE INVOICE WITH WORD LEVEL BOXES')
     filepath = (constants.plot_image_dir+'/'+img_name)
     plt.savefig(filepath)


def loadBoxXML(configXml):

 docs = xml.dom.minidom.parse(configXml)
 fileName = docs.getElementsByTagName("filename")[0].firstChild.nodeValue
 folderName = docs.getElementsByTagName("folder")[0].firstChild.nodeValue
 imagePath = docs.getElementsByTagName("path")[0].firstChild.nodeValue
 imageWidth = int(docs.getElementsByTagName("width")[0].firstChild.nodeValue)
 imageHeight = int(docs.getElementsByTagName("height")[0].firstChild.nodeValue)

 #resize image based on xml configuration
 dsize = (imageWidth, imageHeight)

 # Load images
 imag = cv2.imread(imagePath)
 image = cv2.resize(imag, dsize)
 clone_image = cv2.imread(imagePath, 0)
 clone_image = cv2.resize(clone_image, dsize)

 #********* LOOP OVER  all <Object> elements and iterating it through *****************
 objectList = docs.getElementsByTagName("object")
 for objectElement in objectList:

  #  print("Node Name : ",objectElement.nodeName)
   objChildNodes = objectElement.childNodes
   for childNode in objChildNodes:

     #This is he node inside <Object>..</Object>
     objSubNode = childNode.nodeName
     if objSubNode == 'name':
       #<name>company name</name>
       fieldName = childNode.firstChild.nodeValue
       print(fieldName,"=")
     if objSubNode == 'bndbox':
       bndBoxChildren = childNode.childNodes
       for bndChild in bndBoxChildren:
         bdnchildNname = bndChild.nodeName
         if bdnchildNname == 'xmin':
           global xmin
           xmin = int(bndChild.firstChild.nodeValue)

         if bdnchildNname == 'ymin':
           global ymin
           ymin =int(bndChild.firstChild.nodeValue)
           #print("y :: ",ymin)
         if bdnchildNname == 'xmax':
           global xmax
           xmax = int(bndChild.firstChild.nodeValue)
           #print("width:",xmax)
         if bdnchildNname == 'ymax':
           global ymax
           ymax = int(bndChild.firstChild.nodeValue)
           #print("height:",ymax)
       #print("Plotting x ::,y,w,h ",xmin,ymin,xmax,ymax)
       if xmin != 0:
        plotAndExtractText(xmin,ymin,xmax, ymax,  image, clone_image, fieldName)
 showImage(image)




