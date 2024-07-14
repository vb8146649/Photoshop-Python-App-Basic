from rembg import remove
from PIL import Image
import numpy as np
import sys
import cv2
import PyQt5
from PyQt5 import QtGui 
from PyQt5.QtGui import QIcon , QPixmap
import os

from PyQt5.QtWidgets import QApplication , QMainWindow
from app import Ui_MainWindow
class my_window(QMainWindow):
    def __init__(self):
        super(my_window,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.change.clicked.connect(self.but_press_chname)
        self.ui.pushButton.clicked.connect(self.but_press_img)
        self.ui.rm_bg.clicked.connect(self.but_press_fun)
        self.ui.invert.clicked.connect(self.but_press_fun)
        self.ui.pushButton_4.clicked.connect(self.but_press_fun)
        self.ui.gray.clicked.connect(self.but_press_fun)
        self.ui.pushButton_2.clicked.connect(self.save)
        self.ui.image=0
        self.ui.image_r=0
        self.ui.button_pressed=0
    
    def but_press_chname(self):
        print("button Worked")
        self.ui.dis_img_name.setText("name: "+self.ui.img_name_.text())


    def but_press_img(self):
        print("button Worked")
        path=repr(self.ui.path_.text())
        path=path[2:-2]
        self.ui.image=cv2.imread(path, cv2.IMREAD_COLOR)
        self.pixmap=self.cvt_qt(self.ui.image ,341 ,241 )
        self.ui.img_.setPixmap(self.pixmap)

    
    def cvt_qt(self, img , width , height):
        rgb_image = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(width, height, PyQt5.QtCore.Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
        
    def but_press_fun(self):
        print("Button Worked")
        sender=self.sender()
        self.ui.button_pressed=0
        self.ui.image_r=self.ui.image
        if(sender.text()=="Remove BackGround"):
            self.ui.image_r=cv2.cvtColor(self.ui.image_r,cv2.COLOR_RGB2BGR)
            self.ui.image_r=remove(Image.fromarray(self.ui.image_r))
            self.ui.button_pressed=1
        elif(sender.text()=="Invert"):    
            self.ui.image_r=cv2.cvtColor(self.ui.image_r,cv2.COLOR_RGB2BGR)
        elif(sender.text()=="Blur"):
            self.ui.image_r=cv2.blur(self.ui.image_r , (5,5))
        elif(sender.text()=="Gray Scale"):
            self.ui.image_r=cv2.cvtColor(self.ui.image_r,cv2.COLOR_BGR2GRAY)
        output_np = np.array(self.ui.image_r)

        # If the original image was in RGBA format, convert it to BGR
        if(len(output_np.shape)>=3):
            if output_np.shape[2] == 4:
                output_np = cv2.cvtColor(output_np, cv2.COLOR_RGBA2BGR)
        self.pixmap2=self.cvt_qt(output_np,341 , 241)
        self.ui.label.setPixmap(self.pixmap2)

    def save(self):
        print("Button Worked")
        img=self.ui.image_r
        if(self.ui.button_pressed == 0):
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img=Image.fromarray(img)
        img.save(self.ui.img_name_.text())

def open_file_in_same_directory(file_name):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   file_path = os.path.join(script_dir, file_name)
   return file_path

def window():
    app=QApplication(sys.argv)
    win=my_window()
    win.setWindowIcon(QIcon(open_file_in_same_directory("icon.png")))
    win.setWindowTitle("Python App")
    win.show()
    sys.exit(app.exec_())


window()