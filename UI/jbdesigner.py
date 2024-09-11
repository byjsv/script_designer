# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jbdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ui_jbdesigner(object):
    def setupUi(self, Ui_jbdesigner):
        Ui_jbdesigner.setObjectName("Ui_jbdesigner")
        Ui_jbdesigner.resize(504, 472)
        self.label = QtWidgets.QLabel(Ui_jbdesigner)
        self.label.setGeometry(QtCore.QRect(20, 50, 72, 15))
        self.label.setObjectName("label")
        self.addButton = QtWidgets.QToolButton(Ui_jbdesigner)
        self.addButton.setGeometry(QtCore.QRect(430, 20, 21, 21))
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QToolButton(Ui_jbdesigner)
        self.removeButton.setGeometry(QtCore.QRect(460, 20, 21, 21))
        self.removeButton.setObjectName("removeButton")
        self.listWidget = QtWidgets.QListWidget(Ui_jbdesigner)
        self.listWidget.setGeometry(QtCore.QRect(230, 40, 256, 401))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setLineWidth(1)
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(Ui_jbdesigner)
        self.pushButton.setGeometry(QtCore.QRect(20, 380, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Ui_jbdesigner)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 410, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(Ui_jbdesigner)
        self.widget.setGeometry(QtCore.QRect(20, 80, 191, 24))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../picture/help.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(16, 16))
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)

        self.retranslateUi(Ui_jbdesigner)
        self.pushButton_2.clicked.connect(Ui_jbdesigner.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Ui_jbdesigner)

    def retranslateUi(self, Ui_jbdesigner):
        _translate = QtCore.QCoreApplication.translate
        Ui_jbdesigner.setWindowTitle(_translate("Ui_jbdesigner", "脚本编辑"))
        self.label.setText(_translate("Ui_jbdesigner", "当前脚本："))
        self.addButton.setToolTip(_translate("Ui_jbdesigner", "<html><head/><body><p>新增事件</p></body></html>"))
        self.addButton.setText(_translate("Ui_jbdesigner", "+"))
        self.removeButton.setToolTip(_translate("Ui_jbdesigner", "<html><head/><body><p>删除选中事件</p></body></html>"))
        self.removeButton.setText(_translate("Ui_jbdesigner", "-"))
        self.pushButton.setText(_translate("Ui_jbdesigner", "保存"))
        self.pushButton_2.setText(_translate("Ui_jbdesigner", "退出"))
        self.lineEdit.setPlaceholderText(_translate("Ui_jbdesigner", "请输入脚本名称"))
        self.toolButton.setToolTip(_translate("Ui_jbdesigner", "<html><head/><body><p>文件路径提示：当前文件路径直接使用文件名称</p><p>当前目录文件路径使用 ./ 代替前置目录</p><p>绝对路径使用 C:\\PycharmProjects\\脚本\\测试1</p></body></html>"))
        self.toolButton.setText(_translate("Ui_jbdesigner", "?"))
