from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
import sys
import csv
import os
import constants
import image_plotting
from labelImg import Window2


class Window3(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scandat Studio")
        self.setGeometry(20, 30, 1300, 800)
        self.setStyleSheet("background:#669999")

        self.label_4 = QLabel(' FILE EXECUTION ', self)
        self.label_4.move(360, 665)
        self.label_4.setGeometry(500, 100, 170, 30)
        self.label_4.setStyleSheet("background:#ed4037")


        Go_Back = QPushButton('GO BACK', self)
        Go_Back.setGeometry(650, 650, 100, 30)
        Go_Back.setStyleSheet("background:#18b0b8")



        file = open("G:/Scandat/sacndat_studio/Output_text/ashok.jpg.csv")
        csvreader = csv.reader(file)
        rows = []
        for row in csvreader:
            rows.append(row)
        # print(rows)
        file.close()

        self.scale = 1
        # self.listview = QListView(self)
        # self.fileModel = QFileSystemModel()


    # def conditions(self, image_name):
    #     img_folder_path = constants.plot_image_dir
    #     dirListing = os.listdir(img_folder_path)
    #     output_csv = constants.CSV_dir
    #     csv_list = os.listdir(output_csv)
    #     file1 = open('file.txt', 'r')
    #     Lines = file1.readlines()
    #     for line in Lines:
    #         img_path = (line.strip())
    #         fle = img_path.split("/")
    #         img_name = (fle[-1])
    #         # print(img_name)
    #         for img in dirListing:
    #             # print(i)
    #             for csr in csv_list:
    #                 cs = csr.split('.')[0]
    #                 name_csv = (cs + ".jpg")
    #                 # print(cs+".jpg")
    #                 if image_name == img and image_name == name_csv:
    #                     print(img, 'is equal', img_name, 'is also equal', name_csv)



    def Image_text_loading(self, Image_Name):
        file = open(constants.CSV_dir+'/'+Image_Name+'.csv')
        csvreader = csv.reader(file)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)
        file.close()
        self.listview2 = QLabel(self)
        self.listview2.move(800, 190)
        self.listview2.setStyleSheet('background:white')
        self.listview2.setStyleSheet("border :3px solid black;")
        self.listview2.resize(400, 450)
        self.listview2.setText(str(rows))
        self.im = QPixmap(constants.plot_image_dir+'/'+Image_Name)
        self.listview = QLabel(self)
        self.listview.setScaledContents(True)
        self.listview.setMinimumSize(650, 450)
        self.fileModel = QFileSystemModel()
        self.listview.move(80, 190)
        self.listview.setStyleSheet("border :3px solid black;")
        self.listview.resize(370, 400)
        self.listview.setPixmap(self.im)

        return Image_Name

# if __name__=="__main__":
#     app = QApplication(sys.argv)
#     win = Window3()
#     win.show()
#     sys.exit(app.exec_())

def ShowWindow():
    app = QApplication(sys.argv)
    win = Window3()
    win.show()
    sys.exit(app.exec_())


# ShowWindow()

# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
#
# class MyApp(QWidget):
#
#     def __init__(self, *args):
#         super().__init__(*args)
#
#         self.layout = QHBoxLayout()
#         self.setLayout(self.layout)
#
#         self.button_zoom_in = QPushButton('Zoom IN', self)
#         self.button_zoom_in .setGeometry(120, 600, 100, 30)
#         self.button_zoom_in.clicked.connect(self.on_zoom_in)
#         self.layout.addWidget(self.button_zoom_in)
#
#         self.button_zoom_out = QPushButton('Zoom OUT', self)
#         self.button_zoom_out.setGeometry(220, 600, 100, 30)
#         self.button_zoom_out.clicked.connect(self.on_zoom_out)
#         self.layout.addWidget(self.button_zoom_out)
#
#         self.pixmap = QPixmap('G:/Scandat/sacndat_studio/plotted_images/dhivya.jpg')
#
#         self.label = QLabel(self)
#         self.label.setPixmap(self.pixmap)
#         self.layout.addWidget(self.label)
#
#         self.scale = 1
#
#         self.show()
#
#     def on_zoom_in(self, event):
#         self.scale *= 2
#         self.resize_image()
#
#     def on_zoom_out(self, event):
#         self.scale /= 2
#         self.resize_image()
#
#     def resize_image(self):
#         size = self.pixmap.size()
#
#         scaled_pixmap = self.pixmap.scaled(self.scale * size)
#
#         self.label.setPixmap(scaled_pixmap)
#
# # --- main ---
#
# app = QApplication([])
# win = MyApp()
# app.exec()