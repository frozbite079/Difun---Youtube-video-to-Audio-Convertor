from PySide6.QtCore import *
from PySide6.QtWidgets import  *
from PySide6.QtGui import *
import sys
from pytube.__main__ import YouTube
from youtube_dl import YoutubeDL
import pytube
import requests
import os
from  BlurWindow.blurWindow import GlobalBlur, blur 
import time

def build():
    app = QApplication(sys.argv)
    win = QWidget()
    win2 = QWidget()
    dio = QMessageBox(win2)
    
    
    hwnd = win.winId()
    print(hwnd)
    blur(hwnd)
    previousprogress = 0    


   
    img = "folder1.png"
    
    img1 = "difun.png"

    def url_file():
        try:
            fname = QFileDialog.getExistingDirectory(win,'select a directory')
            fname = QDir.toNativeSeparators(fname)
            inter1.setText(str(fname))
            print(str(fname))
        except Exception as e:
            dio.setText(str(e))
            dio.show()
            dio.setAttribute(Qt.WA_TranslucentBackground)

            
        
    def progress(stream, chunk, bytes_remaining,previousprogress = 0):
     try:        
        total_size = stream.filesize
        bytes_download = total_size - bytes_remaining
        
        liveprogress = (int)(bytes_download / total_size * 100)
        if liveprogress > previousprogress:
            previousprogress = liveprogress
            pro.setValue(liveprogress)
            print(liveprogress) 
            
     except Exception as e:
        dio.setText(str(e))
        dio.show()
        dio.setWindowTitle("Genrated Error")
        dio.setAttribute(Qt.WA_TranslucentBackground)
                    
    def con_ver():
        try:
            down_om = inter.text()
            ranloc = inter1.text()  
            
            youtube = pytube.YouTube(down_om) 
            video = youtube.streams.first() 
            rand= video.download(ranloc)
            
            yt = YouTube(inter.text())
            yt.register_on_progress_callback(progress)
            yt.streams.filter(only_audio=True).first().download()
            
            base, ext = os.path.splitext(rand)
            
            new_file = base + '.mp3'
            os.rename(rand, new_file)
            
            dio = QMessageBox(win)
            dio.setText("Data has been Downloaded successfully")
            dio.show()
            
                
          
        except Exception as e:
            
            
            dio = QMessageBox(win)
           
            dio.setStyleSheet("background-color:white;color:black")
            dio.setWindowOpacity(0.89)
            dio.setText(str(e))
            dio.setAttribute(Qt.WA_TranslucentBackground)

            dio.show()

            
            
        
        
        
        
        
        
    
    
    
    title = QLabel(win)
    title.setText("difun")
    title.setFont(QFont("segoe print",40))
    title.move(400,10)
    title.setStyleSheet("font-weight:bold;background-color:white;color:white;border-radius:10px")
    title.setAttribute(Qt.WA_TranslucentBackground)
    title.show()
    
    
    l1 = QLabel(win)
    l1.setText("Url")
    l1.setFont(QFont("segoe print",20))
    l1.setStyleSheet("color:White;font-weight:bold")
    l1.move(130,180)
    
    inter = QLineEdit(win)
    inter.setPlaceholderText("Enter video url")
    inter.setFont(QFont("arial",20))
    inter.setFixedHeight(50)
    inter.setFixedWidth(500)
    inter.setStyleSheet("background-color:white;border-radius:20px;color:black")
    inter.setWindowOpacity(0.89)
    inter.move(230,180)
    
    bu1 = QPushButton(win)
    bu1.setIcon(QIcon(img))
    hud = bu1.winId()
    blur(hud)
    bu1.setFixedHeight(50)
    bu1.setFixedWidth(50)
    bu1.setIconSize(QSize(50,50))
    bu1.setStyleSheet("border-radius:10px;background-color:white;border-radius:20px")
    bu1.setAttribute(Qt.WA_TranslucentBackground)
    bu1.move(760,250)
    bu1.clicked.connect(url_file)
    
    l2 = QLabel(win)
    l2.setText("Path")
    l2.setFont(QFont("segoe print",20))
    l2.setStyleSheet("color:white;font-weight:bold")
    l2.move(130,250)
    
    
    inter1 = QLineEdit(win)
    inter1.setPlaceholderText("Enter File Location")
    inter1.setFont(QFont("arial",20))
    inter1.setFixedHeight(50)
    inter1.setFixedWidth(500)
    inter1.setStyleSheet("background-color:white;border-radius:20px;color:black")
    inter1.setWindowOpacity(0.89)
    inter1.move(230,250)
    
    bu2 = QPushButton(win)
    bu2.setText("Convert")
    bu2.setFont(QFont("segoe print",20))
    bu2.setFixedHeight(80)
    bu2.setStyleSheet("background-color:white;border-radius:10px;color:grey;font-weight:bold;")
    bu2.setFixedWidth(200)
    bu2.move(720,350)
    bu2.clicked.connect(con_ver)
    
    pro = QProgressBar(win)
    pro.setStyleSheet("font-weight:bold;background-color:white;border-radius:10px;color:white")
    pro.setFixedHeight(50)
    pro.setFont(QFont("Arial",20))
    pro.setFixedWidth(540)
    pro.move(130,368)
    
    
    
    
    
    
    
    
    
    win.setFixedHeight(500)
    win.setFixedWidth(1000)
    win.setWindowTitle("Difun")
    win.setWindowIcon(QIcon(img1))
    win.setAttribute(Qt.WA_TranslucentBackground)
    GlobalBlur(win.winId(),Dark = True, QWidget = win)

    win.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    build()    