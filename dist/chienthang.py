# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChienThang.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChienThang(object):
    def setupUi(self, ChienThang):
        ChienThang.setObjectName("ChienThang")
        ChienThang.resize(614, 344)
        ChienThang.setStyleSheet("")
        self.frame = QtWidgets.QFrame(ChienThang)
        self.frame.setGeometry(QtCore.QRect(0, 0, 621, 341))
        self.frame.setStyleSheet("background-color: #FFD700;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnChoiLai = QtWidgets.QPushButton(self.frame)
        self.btnChoiLai.setGeometry(QtCore.QRect(40, 250, 151, 61))
        self.btnChoiLai.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnChoiLai.setStyleSheet("QPushButton{\n"
"font: 15pt \"Consolas\";\n"
"border: 3px solid black;\n"
"border-radius: 10px;\n"
"color: white;\n"
"background-color: rgb(153,153,255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 15pt \"Consolas\";\n"
"border: 3px solid green;\n"
"border-radius: 20px;\n"
"color: white;\n"
"background-color:rgb(102,255,178);\n"
"}")
        self.btnChoiLai.setObjectName("btnChoiLai")
        self.lbChienThang = QtWidgets.QLabel(self.frame)
        self.lbChienThang.setGeometry(QtCore.QRect(150, 160, 320, 60))
        self.lbChienThang.setStyleSheet("font: 15pt \"Consolas\";\n"
"color: green;")
        self.lbChienThang.setText("")
        self.lbChienThang.setPixmap(QtGui.QPixmap(":/newPrefix/icon/cooltext437840599315509 (1).png"))
        self.lbChienThang.setObjectName("lbChienThang")
        self.btnBangXepHang = QtWidgets.QPushButton(self.frame)
        self.btnBangXepHang.setGeometry(QtCore.QRect(210, 250, 201, 61))
        self.btnBangXepHang.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBangXepHang.setStyleSheet("QPushButton{\n"
"font: 14pt \"Consolas\";\n"
"border: 3px solid black;\n"
"border-radius: 10px;\n"
"color: white;\n"
"background-color: rgb(153,153,255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 14pt \"Consolas\";\n"
"border: 3px solid orange;\n"
"border-radius: 20px;\n"
"color: white;\n"
"background-color: rgb(255, 204,153);\n"
"}")
        self.btnBangXepHang.setObjectName("btnBangXepHang")
        self.btnThoat = QtWidgets.QPushButton(self.frame)
        self.btnThoat.setGeometry(QtCore.QRect(430, 250, 161, 61))
        self.btnThoat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnThoat.setStyleSheet("QPushButton{\n"
"font: 15pt \"Consolas\";\n"
"border: 3px solid black;\n"
"border-radius: 10px;\n"
"color: white;\n"
"background-color: rgb(153,153,255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 15pt \"Consolas\";\n"
"border: 3px solid red;\n"
"border-radius: 20px;\n"
"color: white;\n"
"background-color: rgb(255,102,102);\n"
"}")
        self.btnThoat.setObjectName("btnThoat")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(220, 20, 180, 120))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/icon/congratulation (1).png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(460, 60, 120, 80))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/icon/balloon (1).png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 120, 80))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/icon/fireworks (1).png"))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(ChienThang)
        QtCore.QMetaObject.connectSlotsByName(ChienThang)

    def retranslateUi(self, ChienThang):
        _translate = QtCore.QCoreApplication.translate
        ChienThang.setWindowTitle(_translate("ChienThang", "Dialog"))
        self.btnChoiLai.setText(_translate("ChienThang", "Chơi Mới"))
        self.btnBangXepHang.setText(_translate("ChienThang", "Bảng Xếp Hạng"))
        self.btnThoat.setText(_translate("ChienThang", "Thoát"))
import src_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChienThang = QtWidgets.QDialog()
    ui = Ui_ChienThang()
    ui.setupUi(ChienThang)
    ChienThang.show()
    sys.exit(app.exec_())
