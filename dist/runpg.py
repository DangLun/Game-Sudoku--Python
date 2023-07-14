import sys
from PyQt5 import QtMultimedia
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import *
from sudoku import Ui_Form
from thongbaothoat import Ui_Dialog
from chienthang import Ui_ChienThang
import alogrithm as al
from dokusan import generators
import numpy as np
from collections import defaultdict
import tkinter as tk
import tkinter.messagebox as messagebox
import mysql.connector


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMaximumSize(1009, 782)
        self.form = Ui_Form()
        self.dialog = Ui_Dialog()
        self.dialogWin = Ui_ChienThang()
        self.main_dialogwin = QMainWindow()
        self.main_dialog = QMainWindow()
        self.dialog.setupUi(self.main_dialog)
        self.dialogWin.setupUi(self.main_dialogwin)
        self.form.setupUi(self)
        self.main_dialog.setWindowFlags(Qt.FramelessWindowHint)
        self.main_dialogwin.setWindowFlags(Qt.FramelessWindowHint)
        self.kq = []
        self.dashowKQ = 0
        self.startTime = 0
        self.cur_row = 0
        self.dabatdau = 0
        self.choilai = 0
        self.daWin = 0
        self.Rating = []
        self.cur_rank = 0
        self.Not = []
        self.NotTmp = []
        # Kết nối đến cơ sở dữ liệu MySQL
        self.cnx = mysql.connector.connect(
            host="localhost",     # Địa chỉ host MySQL server
            user="root",      # Tên đăng nhập MySQL
            password="root",  # Mật khẩu MySQL
            database="sudoku"   # Tên cơ sở dữ liệu MySQL
        ) 
        # map
        self.map =[[self.form.l1, self.form.l2, self.form.l3, self.form.l4, self.form.l5, self.form.l6, self.form.l7, self.form.l8, self.form.l9]
        , [self.form.l10, self.form.l11, self.form.l12, self.form.l13, self.form.l14, self.form.l15, self.form.l16, self.form.l17, self.form.l18]
        , [self.form.l19, self.form.l20, self.form.l21, self.form.l22, self.form.l23, self.form.l24, self.form.l25, self.form.l26, self.form.l27]
        , [self.form.l28, self.form.l29, self.form.l30, self.form.l31, self.form.l32, self.form.l33, self.form.l34, self.form.l35, self.form.l36]
        , [self.form.l37, self.form.l38, self.form.l39, self.form.l40, self.form.l41, self.form.l42, self.form.l43, self.form.l44, self.form.l45]
        , [self.form.l46, self.form.l47, self.form.l48, self.form.l49, self.form.l50, self.form.l51, self.form.l52, self.form.l53, self.form.l54]
        , [self.form.l55, self.form.l56, self.form.l57, self.form.l58, self.form.l59, self.form.l60, self.form.l61, self.form.l62, self.form.l63]
        , [self.form.l64, self.form.l65, self.form.l66, self.form.l67, self.form.l68, self.form.l69, self.form.l70, self.form.l71, self.form.l72]
        , [self.form.l73, self.form.l74, self.form.l75, self.form.l76, self.form.l77, self.form.l78, self.form.l79, self.form.l80, self.form.l81]]
        self.khoidonggame()
        self.timePhatLaisound()
        root = tk.Tk()
        root.withdraw() 
        self.form.leTenNhanVat.setMaxLength(20)
        self.form.btnshowKQ.clicked.connect(lambda : self.hienthikq())
        self.form.btnNewGame.clicked.connect(lambda: self.start())
        self.form.btnHideKQ.clicked.connect(lambda: self.hidekq())
        self.form.btnPlay.clicked.connect(lambda: self.BtnPlay())
        self.form.btnPrevious_index1.clicked.connect(lambda: self.btntrove_page1())
        self.form.btnPrevious_index2.clicked.connect(lambda: self.btntrove_page2())
        self.form.btnPrevious_index3.clicked.connect(lambda: self.btntrove_page3())
        self.form.btnPrevious_index4.clicked.connect(lambda: self.btntrove_page4())
        self.form.btnQuit.clicked.connect(lambda: self.ClickBtnQuit())
        self.form.checkBoxAmThanhNhac.toggled.connect(lambda: self.disableAmthanhFORM())
        self.form.checkbox_amnhac_home.toggled.connect(lambda: self.disableAmNhacFormHome())
        self.form.checkbox_amnhac_inputname.toggled.connect(lambda: self.disableAmnhacFromInput())
        self.form.btnNext.clicked.connect(lambda: self.checktennhanvat())
        self.form.leTenNhanVat.textChanged.connect(lambda: self.checkInputTenNhanVat())
        self.form.btnAbout.clicked.connect(lambda: self.aboutGame())
        self.form.btnRating.clicked.connect(lambda: self.rating())
        self.form.tableRating.itemClicked.connect(lambda: self.showdialog())
        #self.form.btn_newRating.clicked.connect(lambda: self.lamMoiRating())
        # dialog chien thang 
        self.dialogWin.btnChoiLai.clicked.connect(lambda: self.diaLogChoiLai())
        self.dialogWin.btnBangXepHang.clicked.connect(lambda: self.dialogbangxephang())
        self.dialogWin.btnThoat.clicked.connect(lambda: self.dialogThoat())  
        self.form.btnNewGame.setStyleSheet("QPushButton{\n"
"font: 75 15pt \"Consolas\";\n"
"border-radius: 20px;\n"
"border: 3px solid black;\n"
"color: black;\n"
"background-color: rgb(0,255,128);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(172,178,255);\n"
"color: rgb(96,96,96);\n"
"border: 3px solid white;\n"
"}")
        self.form.btnshowKQ.setStyleSheet("QPushButton{\n"
"font: 75 15pt \"Consolas\";\n"
"border-radius: 20px;\n"
"border: 3px solid black;\n"
"color: white;\n"
"background-color: rgb(102,102,255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(172,178,255);\n"
"color: black;\n"
"border: 3px solid white;\n"
"}")
        self.form.btnHideKQ.setStyleSheet("QPushButton{\n"
"font: 75 15pt \"Consolas\";\n"
"border-radius: 20px;\n"
"border: 3px solid black;\n"
"color: white;\n"
"background-color: rgb(102,102,255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(172,178,255);\n"
"color: black;\n"
"border: 3px solid white;\n"
"}")
        
    def showdialog(self):
        reply = QMessageBox.question(main_win, "Thông báo xóa", "Bạn có muốn xóa thật không?",
                             QMessageBox.Ok | QMessageBox.Cancel)
        if reply == QMessageBox.Ok:
            
            text = self.form.tableRating.item(self.form.tableRating.currentRow(), 4).text()
            if text == "Chưa Hoàn Thành":
                self.Not.remove(self.Not[self.form.tableRating.currentRow() - len(self.Rating)])
                self.cur_row -= 1
                cs = self.cnx.cursor()
                query = "delete from sudoku.rating where tennd = %s"
                tennd = self.form.tableRating.item(self.form.tableRating.currentRow(), 0).text()
                cs.execute(query, (tennd,))
                self.cnx.commit()
                self.UpdateRating()
            elif text == "Đã Hoàn Thành":
                self.Rating.remove(self.Rating[self.form.tableRating.currentRow()])
                self.cur_row -= 1
                cs = self.cnx.cursor()
                query = "delete from sudoku.rating where tennd = %s"
                tennd = self.form.tableRating.item(self.form.tableRating.currentRow(), 0).text()
                cs.execute(query, (tennd,))
                self.cnx.commit()
                self.UpdateRating()
    
    
     
    def ClickBtnQuit(self):
        self.UpdateRating()
        main_win.close()
    
    def loadData(self):
        cs = self.cnx.cursor()
        query = "SELECT * FROM rating"
        cs.execute(query)
        results = cs.fetchall()
        for row in results:
            if row[4] == "Đã Hoàn Thành":
                self.Rating.append({"Tên Nhân Vật": row[1], "Độ Khó": row[2], "Thời gian": row[3], "Trạng thái": row[4]})
            elif row[4] == "Chưa Hoàn Thành":
                self.Not.append({"Tên Nhân Vật": row[1], "Độ Khó": row[2], "Thời gian": row[3], "Trạng thái": row[4]})
            self.cur_row += 1
    def BtnPlay(self):
        self.form.stackedWidget.setCurrentIndex(1)
        self.form.leTenNhanVat.clear()
        self.form.lb_thongbao.clear()
        self.form.leTenNhanVat.setStyleSheet("font: 20pt \"Consolas\";\n"
"border-radius: 20px;\n"
"border: 3px solid black;")
        self.form.leTenNhanVat.setFocus()
    def dialogThoat(self):
        self.dabatdau = 0
        self.main_dialogwin.close()
        self.form.lbTime.setText("00:00")
        self.startTime = 0
        self.kq.clear
        self.timer.stop()
        for i in range(9):
            for j in range(9):
                self.map[i][j].clear()
        column_names = ["Tên Nhân Vật", "Độ Khó", "Thời Gian", "Xếp Hạng","Tình Trạng"]
        self.form.tableRating.setHorizontalHeaderLabels(column_names)
        self.form.tableRating.setColumnWidth(0, 300)
        self.form.tableRating.setColumnWidth(1, 200)
        self.form.tableRating.setColumnWidth(2, 100)
        self.form.tableRating.setColumnWidth(3, 100)
        self.form.tableRating.setColumnWidth(4, 300)
        self.form.stackedWidget.setCurrentIndex(0)
    def dialogbangxephang(self):
        self.dabatdau = 0
        self.main_dialogwin.close()
        self.form.lbTime.setText("00:00")
        self.startTime = 0
        self.kq.clear
        self.timer.stop()
        for i in range(9):
            for j in range(9):
                self.map[i][j].clear()
        self.UpdateRating()
        self.form.stackedWidget.setCurrentIndex(4)
        column_names = ["Tên Nhân Vật", "Độ Khó", "Thời Gian", "Xếp Hạng","Tình Trạng"]
        self.form.tableRating.setHorizontalHeaderLabels(column_names)
        self.form.tableRating.setColumnWidth(0, 300)
        self.form.tableRating.setColumnWidth(1, 200)
        self.form.tableRating.setColumnWidth(2, 100)
        self.form.tableRating.setColumnWidth(3, 100)
        self.form.tableRating.setColumnWidth(4, 300)
    def diaLogChoiLai(self):
        self.dabatdau = 0
        self.main_dialogwin.close()
        self.form.lbTime.setText("00:00")
        self.startTime = 0
        self.kq.clear
        self.timer.stop()
        for i in range(9):
            for j in range(9):
                self.map[i][j].clear()
        self.form.stackedWidget.setCurrentIndex(2)
    def checkWin(self):
        self.timer2 = QTimer()
        self.timer2.timeout.connect(lambda: self.checkwin())
        self.timer2.start(1000)
    def checkwin(self):
        win = True
        for i in range(9):
            for j in range(9):
                if self.map[i][j].text() != str(self.kq[i][j]):
                    win = False
                    return
        if win == True and self.dashowKQ == 0:
            self.timer2.stop()
            self.timer.stop()
            self.daWin = 1
            cs = self.cnx.cursor()
            query = "call themdulieu(%s, %s, %s, %s)"
            data = (self.form.leTenNhanVat.text(), self.form.comboBox.currentText(), self.form.lbTime.text(), "Đã Hoàn Thành")
            cs.execute(query, data)
            self.cnx.commit()
            self.Rating.append({"Tên Nhân Vật": self.form.leTenNhanVat.text(), "Độ Khó": self.form.comboBox.currentText(), "Thời gian": self.form.lbTime.text(), "Trạng thái": "Đã Hoàn Thành"})
            self.main_dialogwin.show()
    def updateTable_IN_Rating(self):
        self.form.tableRating.clear()
        column_names = ["Tên Nhân Vật", "Độ Khó", "Thời Gian", "Xếp Hạng","Tình Trạng"]
        self.form.tableRating.setHorizontalHeaderLabels(column_names)
        style_sheet = """
            QHeaderView::section {
                background-color: #f2f2f2;
                color: #333333;
                font-weight: bold;
                padding: 5px;
                border-bottom: 1px solid #cccccc;
            }
        """
        self.form.tableRating.horizontalHeader().setStyleSheet(style_sheet)
        self.form.tableRating.setRowCount(self.cur_row)
    def UpdateRating(self):
        self.updateTable_IN_Rating()
        for i in range(self.cur_row):
            self.form.tableRating.setItem(i, 3, QTableWidgetItem(str(i + 1)))
        if len(self.Rating) > 0:
            self.Rating.sort(key=lambda x: x["Thời gian"])
        if len(self.Not) > 0:
            self.Not.sort(key=lambda x: x["Thời gian"])
        for i in range(len(self.Rating)):
            self.form.tableRating.setItem(i, 0, QTableWidgetItem(self.Rating[i]["Tên Nhân Vật"]))
            self.form.tableRating.setItem(i, 1, QTableWidgetItem(self.Rating[i]["Độ Khó"]))
            self.form.tableRating.setItem(i, 4, QTableWidgetItem(self.Rating[i]["Trạng thái"]))
            self.form.tableRating.setItem(i, 2, QTableWidgetItem(self.Rating[i]["Thời gian"]))
        row = len(self.Rating)
        
        for i in range(row, row + len(self.Not)):
            self.form.tableRating.setItem(i, 0, QTableWidgetItem(self.Not[i - row]["Tên Nhân Vật"]))
            self.form.tableRating.setItem(i, 1, QTableWidgetItem(self.Not[i - row]["Độ Khó"]))
            self.form.tableRating.setItem(i, 4, QTableWidgetItem(self.Not[i - row]["Trạng thái"]))
            self.form.tableRating.setItem(i, 2, QTableWidgetItem(self.Not[i - row]["Thời gian"]))
    def rating(self):
        self.UpdateRating()
        column_names = ["Tên Nhân Vật", "Độ Khó", "Thời Gian", "Xếp Hạng","Tình Trạng"]
        self.form.tableRating.setHorizontalHeaderLabels(column_names)
        self.form.tableRating.setColumnWidth(0, 300)
        self.form.tableRating.setColumnWidth(1, 200)
        self.form.tableRating.setColumnWidth(2, 100)
        self.form.tableRating.setColumnWidth(3, 100)
        self.form.tableRating.setColumnWidth(4, 300)
        self.form.stackedWidget.setCurrentIndex(4) 
    def aboutGame(self):
        self.form.stackedWidget.setCurrentIndex(3)
    def checkInputTenNhanVat(self):
        if self.form.leTenNhanVat.text() != "":
            self.form.leTenNhanVat.setStyleSheet("font: 20pt \"Consolas\";\n"
"border-radius: 20px;\n"
"border: 3px solid black;")
    
    
    def checktennhanvat(self):
        if self.form.leTenNhanVat.text() == "":
            self.form.leTenNhanVat.setStyleSheet("font: 20pt \"Consolas\";\n"
"border-radius: 20px;\n"
"border: 3px solid red;")
            if(self.form.leTenNhanVat.text() == ""):
                self.form.lb_thongbao.setText("Không được để trống tên nhân vật !")
        else:
            self.form.stackedWidget.setCurrentIndex(2)
    def ButtonSound(self):
        self.form.btnPlay.clicked.connect(lambda: self.soundButtonPlay("sound\\Btn.mp3"))
        self.form.btnRating.clicked.connect(lambda: self.soundButtonRating("sound\\Btn.mp3"))
        self.form.btnAbout.clicked.connect(lambda: self.soundButtonAbout("sound\\Btn.mp3"))
        self.form.btnQuit.clicked.connect(lambda: self.soundButtonQuit("sound\\Btn.mp3"))
        self.form.btnPrevious_index1.clicked.connect(lambda: self.soundButtonPre1("sound\\Btn.mp3"))
        self.form.btnPrevious_index2.clicked.connect(lambda: self.soundButtonPre2("sound\\Btn.mp3"))
        self.form.btnNewGame.clicked.connect(lambda: self.soundButtonnewgame("sound\\Btn.mp3"))
        self.form.btnHideKQ.clicked.connect(lambda: self.soundButtonhide("sound\\Btn.mp3"))
        self.form.btnNext.clicked.connect(lambda: self.soundButtonNext("sound\\Btn.mp3"))
        self.form.btnshowKQ.clicked.connect(lambda: self.soundButtonshow("sound\\Btn.mp3")) 
        self.dialog.btnOK.clicked.connect(lambda: self.soundButtondialogbtnOK("sound\\Btn.mp3"))
        self.dialog.btnCancel.clicked.connect(lambda: self.soundButtondialogbtncancel("sound\\Btn.mp3"))
        self.form.btnPrevious_index3.clicked.connect(lambda: self.soundButtonpre3("sound\\Btn.mp3"))  
        self.form.btnPrevious_index4.clicked.connect(lambda: self.soundButtonpre4("sound\\Btn.mp3"))
        self.dialogWin.btnChoiLai.clicked.connect(lambda: self.soundButtondialogChoiLai("sound\\Btn.mp3"))
        self.dialogWin.btnBangXepHang.clicked.connect(lambda: self.soundButtondialogbxh("sound\\Btn.mp3"))
        self.dialogWin.btnThoat.clicked.connect(lambda: self.soundButtondialogthoat("sound\\Btn.mp3"))
    def timePhatLaisound(self):
        self.timer1 = QTimer()
        self.timer1.timeout.connect(lambda: self.soundForm("sound\\sound-form.mp3"))
        self.timer1.start(85000)
    def khoidonggame(self):
        self.setStart()
        self.loadData()
        self.form.stackedWidget.setCurrentIndex(0)
        self.form.checkBoxAmThanhNhac.toggle()
        self.form.checkbox_amnhac_home.toggle()
        self.form.checkbox_amnhac_inputname.toggle()
        self.soundForm("sound\\sound-form.mp3")
        self.ButtonSound()
    def disableAmthanhFORM(self):
        if self.form.checkBoxAmThanhNhac.isChecked():
            self.soundForm("sound\\sound-form.mp3")
            self.form.checkbox_amnhac_home.setChecked(True)
            self.form.checkbox_amnhac_inputname.setChecked(True)
        else:
            self.button1.setMuted(True)
            self.form.checkbox_amnhac_home.setChecked(False)
            self.form.checkbox_amnhac_inputname.setChecked(False)
    def disableAmNhacFormHome(self):
        if self.form.checkbox_amnhac_home.isChecked():
            self.soundForm("sound\\sound-form.mp3")
            self.form.checkBoxAmThanhNhac.setChecked(True)
            self.form.checkbox_amnhac_inputname.setChecked(True)
        else:
            self.button1.setMuted(True)
            self.form.checkBoxAmThanhNhac.setChecked(False)
            self.form.checkbox_amnhac_inputname.setChecked(False)
            
    def disableAmnhacFromInput(self):
        if self.form.checkbox_amnhac_inputname.isChecked():
            self.soundForm("sound\\sound-form.mp3")
            self.form.checkbox_amnhac_home.setChecked(True)
            self.form.checkBoxAmThanhNhac.setChecked(True)
        else:
            self.button1.setMuted(True)
            self.form.checkbox_amnhac_home.setChecked(False)
            self.form.checkBoxAmThanhNhac.setChecked(False)
    def btntrove_page1(self):
        self.form.stackedWidget.setCurrentIndex(0)
    def btntrove_page2(self):
        if self.dabatdau >= 1:
            self.main_dialog.show()
            self.dialog.btnOK.clicked.connect(lambda: self.clickOkINdialog())
            self.dialog.btnCancel.clicked.connect(lambda: self.clickcancelINdialog())
        else: 
            self.form.leTenNhanVat.clear()
            self.form.lb_thongbao.clear()
            self.form.leTenNhanVat.setStyleSheet("font: 20pt \"Consolas\";\n"
"border-radius: 20px;\n"
"border: 3px solid black;")
            self.form.stackedWidget.setCurrentIndex(1)
    def btntrove_page3(self):
        self.form.stackedWidget.setCurrentIndex(0)      
    def btntrove_page4(self):
        self.form.stackedWidget.setCurrentIndex(0)
        
    def clickOkINdialog(self):
        self.form.leTenNhanVat.clear()
        self.form.lb_thongbao.clear()
        self.form.leTenNhanVat.setStyleSheet("font: 20pt \"Consolas\";\n"
"border-radius: 20px;\n"
"border: 3px solid black;")
        if self.dabatdau >= 1:
            self.timer2.stop()
            for i in range(9):
                for j in range(9):
                    self.map[i][j].clear()
            self.kq.clear()
            cs = self.cnx.cursor()
            query = "call themdulieu(%s, %s, %s, %s)"
            data = (self.form.leTenNhanVat.text(), self.form.comboBox.currentText(), self.form.lbTime.text(), "Chưa Hoàn Thành")
            cs.execute(query, data)
            self.cnx.commit()
            self.Not.append({"Tên Nhân Vật": self.form.leTenNhanVat.text(), "Độ Khó": self.form.comboBox.currentText(), "Thời gian": self.form.lbTime.text(), "Trạng thái": "Chưa Hoàn Thành"})
            self.form.lbTime.setText("00:00")
            self.timer.stop()
            self.dabatdau = 0
        self.main_dialog.close()
        self.form.stackedWidget.setCurrentIndex(1)
    
    def clickcancelINdialog(self):
        self.main_dialog.close()
    def keyReleaseEvent(self, x) -> None:
        self.checkAndMove(x.key())
    def move(self, a, b, phia):
        # up
        if phia == 16777235:
            if a > 0:
                if not self.map[a - 1][b].focusPolicy():
                    for i in range(a - 2, -1, -1):
                        if self.map[i][b].focusPolicy():
                            self.map[i][b].setFocus()
                            break
                else:
                    self.map[a-1][b].setFocus()
        # down
        elif phia == 16777237:
            if a< 8:
                if not self.map[a+1][b].focusPolicy():
                    for i in range(a + 2, 9):
                        if self.map[i][b].focusPolicy():
                            self.map[i][b].setFocus()
                            break
                else:
                    self.map[a+1][b].setFocus()
        # left
        elif phia== 16777234:
            if b > 0:
                if not self.map[a][b - 1].focusPolicy():
                    t = False
                    for i in range(b - 2, -1, -1):
                        if self.map[a][i].focusPolicy():
                            self.map[a][i].setFocus()
                            t = True
                            break
                    if t == False:
                        if not self.map[a-1][8].focusPolicy():
                            for i in range(7, -1, -1):
                                if self.map[a-1][i].focusPolicy():
                                    self.map[a-1][i].setFocus()
                                    break
                        else:
                            self.map[a-1][8].setFocus()
                else:
                    self.map[a][b - 1].setFocus()
            else:
                if a > 0:
                    if not self.map[a-1][8].focusPolicy():
                        for i in range(7, -1, -1):
                            if self.map[a-1][i].focusPolicy():
                                self.map[a-1][i].setFocus()
                                break
                    else:
                        self.map[a-1][8].setFocus()
                    
        # right
        elif phia == 16777236:
            if b < 8:
                if not self.map[a][b + 1].focusPolicy():
                    t = False
                    for i in range(b + 2, 9):
                        if self.map[a][i].focusPolicy():
                            self.map[a][i].setFocus()
                            t = True
                            break
                    if t == False:
                        if(a < 8):
                            if not self.map[a+1][0].focusPolicy():
                                for i in range(1, 9):
                                    if self.map[a+1][i].focusPolicy():
                                        self.map[a+1][i].setFocus()
                                        break
                            else:
                                self.map[a+1][0].setFocus()
                else:
                    self.map[a][b + 1].setFocus()
            else:
                if(a < 8):
                    if not self.map[a+1][0].focusPolicy():
                        for i in range(1, 9):
                            if self.map[a+1][i].focusPolicy():
                                self.map[a+1][i].setFocus()
                                break
                    else:
                        self.map[a+1][0].setFocus()
    def checkAndMove(self, phia):
        for i in range(9):
            for j in range(9):
                if self.map[i][j].hasFocus() == True:
                    self.move(i, j, phia)
                    return     
    def soundButtonPlay(self, x):
        self.urlplay = QUrl.fromLocalFile(x)
        self.contentplay = QtMultimedia.QMediaContent(self.urlplay)
        self.buttonplay = QtMultimedia.QMediaPlayer()
        self.buttonplay.setMedia(self.contentplay)
        self.buttonplay.play()
    def soundButtonRating(self, x):
        self.urlrating = QUrl.fromLocalFile(x)
        self.contentrating = QtMultimedia.QMediaContent(self.urlrating)
        self.buttonrating = QtMultimedia.QMediaPlayer()
        self.buttonrating.setMedia(self.contentrating)
        self.buttonrating.play()
    def soundButtonAbout(self, x):
        self.urlabout = QUrl.fromLocalFile(x)
        self.contentabout = QtMultimedia.QMediaContent(self.urlabout)
        self.buttonabout = QtMultimedia.QMediaPlayer()
        self.buttonabout.setMedia(self.contentabout)
        self.buttonabout.play()
    def soundButtonPre1(self, x):
        self.urlpre1 = QUrl.fromLocalFile(x)
        self.contentpre1 = QtMultimedia.QMediaContent(self.urlpre1)
        self.buttonpre1 = QtMultimedia.QMediaPlayer()
        self.buttonpre1.setMedia(self.contentpre1)
        self.buttonpre1.play()
    def soundButtonNext(self, x):
        self.urlnext = QUrl.fromLocalFile(x)
        self.contentnext = QtMultimedia.QMediaContent(self.urlnext)
        self.buttonnext = QtMultimedia.QMediaPlayer()
        self.buttonnext.setMedia(self.contentnext)
        self.buttonnext.play()
    def soundButtonPre2(self, x):
        self.urlpre2 = QUrl.fromLocalFile(x)
        self.contentpre2 = QtMultimedia.QMediaContent(self.urlpre2)
        self.buttonpre2 = QtMultimedia.QMediaPlayer()
        self.buttonpre2.setMedia(self.contentpre2)
        self.buttonpre2.play()
    def soundButtonpre3(self, x):
        self.urlpre3 = QUrl.fromLocalFile(x)
        self.contentpre3 = QtMultimedia.QMediaContent(self.urlpre3)
        self.buttonpre3 = QtMultimedia.QMediaPlayer()
        self.buttonpre3.setMedia(self.contentpre3)
        self.buttonpre3.play()
    def soundButtondialogbtnOK(self, x):
        self.urldialogbtnOK = QUrl.fromLocalFile(x)
        self.contentdialogbtnOK = QtMultimedia.QMediaContent(self.urldialogbtnOK)
        self.buttondialogbtnOk = QtMultimedia.QMediaPlayer()
        self.buttondialogbtnOk.setMedia(self.contentdialogbtnOK)
        self.buttondialogbtnOk.play()
    def soundButtondialogbtncancel(self, x):
        self.urldialogbtncancel = QUrl.fromLocalFile(x)
        self.contentdialogbtncancel = QtMultimedia.QMediaContent(self.urldialogbtncancel)
        self.buttondialogbtncancel = QtMultimedia.QMediaPlayer()
        self.buttondialogbtncancel.setMedia(self.contentdialogbtncancel)
        self.buttondialogbtncancel.play()
    def soundButtonnewgame(self, x):
        self.urlnewgame = QUrl.fromLocalFile(x)
        self.contentnewgame = QtMultimedia.QMediaContent(self.urlnewgame)
        self.buttonnewgame = QtMultimedia.QMediaPlayer()
        self.buttonnewgame.setMedia(self.contentnewgame)
        self.buttonnewgame.play()
    def soundButtonshow(self, x):
        self.urlshow = QUrl.fromLocalFile(x)
        self.contentshow = QtMultimedia.QMediaContent(self.urlshow)
        self.buttonshow = QtMultimedia.QMediaPlayer()
        self.buttonshow.setMedia(self.contentshow)
        self.buttonshow.play()
    def soundButtonhide(self, x):
        self.urlhide = QUrl.fromLocalFile(x)
        self.contenthide = QtMultimedia.QMediaContent(self.urlhide)
        self.buttonhide = QtMultimedia.QMediaPlayer()
        self.buttonhide.setMedia(self.contenthide)
        self.buttonhide.play()                     
    def soundButtonQuit(self, x):
        self.urlquit = QUrl.fromLocalFile(x)
        self.contentquit = QtMultimedia.QMediaContent(self.urlquit)
        self.buttonquit = QtMultimedia.QMediaPlayer()
        self.buttonquit.setMedia(self.contentquit)
        self.buttonquit.play()
    def soundButtonpre4(self, x):
        self.urlpre4 = QUrl.fromLocalFile(x)
        self.contentpre4 = QtMultimedia.QMediaContent(self.urlpre4)
        self.buttonpre4 = QtMultimedia.QMediaPlayer()
        self.buttonpre4.setMedia(self.contentpre4)
        self.buttonpre4.play()
    def soundButtondialogChoiLai(self, x):
        self.urldialogChoiLai = QUrl.fromLocalFile(x)
        self.contentdialogchoilai = QtMultimedia.QMediaContent(self.urldialogChoiLai)
        self.buttondialogchoilai = QtMultimedia.QMediaPlayer()
        self.buttondialogchoilai.setMedia(self.contentdialogchoilai)
        self.buttondialogchoilai.play()
    def soundButtondialogbxh(self, x):
        self.urldialogbxh = QUrl.fromLocalFile(x)
        self.contentdialogbxh = QtMultimedia.QMediaContent(self.urldialogbxh)
        self.buttondialogbxh = QtMultimedia.QMediaPlayer()
        self.buttondialogbxh.setMedia(self.contentdialogbxh)
        self.buttondialogbxh.play()
    def soundButtondialogthoat(self, x):  
        self.urldialogthoat = QUrl.fromLocalFile(x)
        self.contentdialogthoat = QtMultimedia.QMediaContent(self.urldialogthoat)
        self.buttondialogthoat = QtMultimedia.QMediaPlayer()
        self.buttondialogthoat.setMedia(self.contentdialogthoat)
        self.buttondialogthoat.play()
    def soundForm(self, x):
        if self.form.checkBoxAmThanhNhac.isChecked():
            self.url1 = QUrl.fromLocalFile(x)
            self.content1 = QtMultimedia.QMediaContent(self.url1)
            self.button1 = QtMultimedia.QMediaPlayer()
            self.button1.setMedia(self.content1)
            self.button1.play()

    # hiển thị con trỏ ở nơi khoảng trống đầu tiên
    def setStart(self):
        for i in range(9):
            for j in range(9):
                if self.map[i][j].text() == "":
                    self.map[i][j].setFocus()
                    break
            break
        for i in range(9):
            for j in range(9):
                validator = QIntValidator(1,9)
                self.map[i][j].setValidator(validator)
                self.map[i][j].setMaxLength(1)
                
    def time(self):
        self.form.lbTime.setText("00:00")
        self.startTime = 1
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.showTime())
        self.timer.start(1000)
    def showTime(self):
        self.cnt +=1
        phut = self.cnt % 3600 // 60
        giay = self.cnt % 60
        if phut < 10:
            phut = "0" + str(phut)
        if giay < 10:
            giay = "0" + str(giay)
        self.form.lbTime.setText(str(phut) + ":" + str(giay))
    # ẩn kết qủa
    def hidekq(self):
        if self.dashowKQ == 1:
            for i in range(9):
                for j in range(9):
                    text_color = self.map[i][j].palette().text().color()
                    if text_color == QColor(Qt.red):
                        self.map[i][j].setText("")
                        self.map[i][j].setStyleSheet("color: black")
    # hiển thị kết quả
    def hienthikq(self):
        self.dashowKQ = 1
        if self.dabatdau >= 1:
            for i in range(9):
                for j in range(9):
                    if self.map[i][j].text() == "":
                        self.map[i][j].setText(str(self.kq[i][j]))
                        self.map[i][j].setStyleSheet("color: red")
    # random Map
    def randomMAP(self, x):
        # random map
        random_map = np.array(list(str(generators.random_sudoku(avg_rank=x)))).reshape(9, 9)
        for i in range(9):
            for j in range(9):
                if random_map[i][j] == '0':
                    self.map[i][j].setText("")
                else:
                    self.map[i][j].setText(random_map[i][j])
                    self.map[i][j].setStyleSheet("color: rgb(0, 204, 204)")
                    self.map[i][j].setFocusPolicy(0)
    # chế độ chơi
    def start(self):
        self.dabatdau +=1
        if self.dabatdau == 1:
            self.cur_row+=1
            self.form.tableRating.setRowCount(self.cur_row)
            self.cur_rank += 1
        # xóa toàn bộ kết quả cũ
        self.kq.clear()
        for i in range(9):
            for j in range(9):
                self.map[i][j].setFocusPolicy(3)
                self.map[i][j].setStyleSheet("color: black;")
                self.map[i][j].setText("")
        if self.form.comboBox.currentText() == "Dễ":
            self.randomMAP(150)
        elif self.form.comboBox.currentText() == "Trung bình":
            self.randomMAP(150000)
        elif self.form.comboBox.currentText() == "Khó":
            self.randomMAP(150000000)
        elif self.form.comboBox.currentText() == "Siêu Khó":
            self.randomMAP(15000000000)
        # tạo kết quả cho game mới 
        self.create()
        # khởi tạo lại thời gian cho game mới
        self.cnt = 0
        self.time()
        self.setStart()
        self.checkWin()
    # tạo kết quả
    def create(self):
        
        self.dashowKQ = 0
        def checkvalid(a, x, y, k):
            for i in range(0, 9):
                if a[x][i] == k:
                    return False
            for i in range(0, 9):
                if a[i][y] == k:
                    return False
            start_x = int(x / 3) * 3
            start_y = int(y / 3) * 3
            for i in range(start_x, start_x + 3):
                for j in range(start_y, start_y + 3):
                    if a[i][j] == k:
                        return False
            return True
        def savekq(a):
            for i in a:
                tam = []
                for j in i:
                    tam.append(j)
                self.kq.append(tam)

        def solve(a, x, y):
            if y == 9:
                if x == 8:
                    savekq(a)
                    return
                else:
                    solve(a, x + 1, 0)
            elif a[x][y] == 0:
                for i in range(1, 10):
                    if checkvalid(a, x, y, i):
                        a[x][y] = i
                        solve(a, x, y + 1)
                        a[x][y] = 0
            else:
                solve(a, x, y + 1)
        tablePlayer = []
        for i in range(9):
            cur = []
            for j in range(9):
                if self.map[i][j].text() != "":
                    cur.append(int(self.map[i][j].text()))
                elif self.map[i][j].text() == "":
                    cur.append(0)
            tablePlayer.append(cur)
        solve(tablePlayer, 0, 0)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = main()
    main_win.show()
    sys.exit(app.exec())
