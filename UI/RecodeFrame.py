# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecodeFrame.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Recode_Frame(object):
    def setupUi(self, Recode_Frame):
        Recode_Frame.setObjectName("Recode_Frame")
        Recode_Frame.resize(392, 204)
        self.layoutWidget = QtWidgets.QWidget(Recode_Frame)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 341, 40))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_filePath = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_filePath.setObjectName("lineEdit_filePath")
        self.horizontalLayout.addWidget(self.lineEdit_filePath)
        self.toolButton = QtWidgets.QToolButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../picture/help.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(16, 16))
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.layoutWidget_2 = QtWidgets.QWidget(Recode_Frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 80, 171, 91))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.lineEdit_endkey = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_endkey.setObjectName("lineEdit_endkey")
        self.gridLayout.addWidget(self.lineEdit_endkey, 1, 2, 1, 1)
        self.lineEdit_startkey = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_startkey.setObjectName("lineEdit_startkey")
        self.gridLayout.addWidget(self.lineEdit_startkey, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        self.splitter = QtWidgets.QSplitter(Recode_Frame)
        self.splitter.setGeometry(QtCore.QRect(240, 90, 93, 71))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.Botton_start = QtWidgets.QPushButton(self.splitter)
        self.Botton_start.setObjectName("Botton_start")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Recode_Frame)
        self.pushButton_2.clicked.connect(Recode_Frame.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Recode_Frame)

    def retranslateUi(self, Recode_Frame):
        _translate = QtCore.QCoreApplication.translate
        Recode_Frame.setWindowTitle(_translate("Recode_Frame", "脚本录制"))
        self.label.setText(_translate("Recode_Frame", "保存文件路径:"))
        self.toolButton.setToolTip(_translate("Recode_Frame", "<html><head/><body><p>文件路径提示：当前文件路径直接使用文件名称</p><p>当前目录文件路径使用 ./ 代替前置目录</p><p>绝对路径使用 C:\\PycharmProjects\\脚本\\测试1</p></body></html>"))
        self.toolButton.setText(_translate("Recode_Frame", "?"))
        self.label_2.setText(_translate("Recode_Frame", "开始热键："))
        self.lineEdit_endkey.setText(_translate("Recode_Frame", "F10"))
        self.lineEdit_startkey.setText(_translate("Recode_Frame", "F9"))
        self.label_3.setText(_translate("Recode_Frame", "结束热键："))
        self.Botton_start.setText(_translate("Recode_Frame", "开始"))
        self.pushButton_2.setText(_translate("Recode_Frame", "取消"))
