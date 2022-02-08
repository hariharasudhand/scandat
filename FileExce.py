import constants
from bs4 import BeautifulSoup
import image_plotting
import xml.etree.ElementTree as ET
import os
from csv import writer
from csv import reader



def File_exe(XmlPath):
    count = 0
    file1 = open('Good_quality.txt', 'r')
    Lines = file1.readlines()
    with open(XmlPath, 'r') as f:
        tree = ET.parse(XmlPath)
        root = tree.getroot()
        data = f.read()
        Bs_data = BeautifulSoup(data, "xml")
    for line in Lines:
        count += 1
        # print( line.strip())
        img_path = (line.strip())
        fle = img_path.split("/")
        img_name = (fle[-1])
        print(img_name)
        for elem in root.iter('path'):
            elem.text = img_path
        tree.write(XmlPath)
        image_plotting.loadBoxXML(XmlPath)

        save_path = constants.CSV_dir

        completeName = os.path.join(save_path, img_name + ".csv")

        with open('result.csv', 'r') as read_obj, \
                open(completeName, 'w', newline='', encoding="utf-8") as write_obj:
            csv_reader = reader(read_obj)
            csv_writer = writer(write_obj)
            for row in csv_reader:
                csv_writer.writerow(row)
                f = open('result.csv', "w+")
                f.close()
