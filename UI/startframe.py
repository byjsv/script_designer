# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startframe.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_startmenu(object):
    def setupUi(self, startmenu):
        startmenu.setObjectName("startmenu")
        startmenu.resize(296, 174)
        self.widget = QtWidgets.QWidget(startmenu)
        self.widget.setGeometry(QtCore.QRect(40, 20, 171, 121))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.state_label = QtWidgets.QLabel(self.widget)
        self.state_label.setObjectName("state_label")
        self.gridLayout.addWidget(self.state_label, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_count = QtWidgets.QLabel(self.widget)
        self.label_count.setObjectName("label_count")
        self.gridLayout.addWidget(self.label_count, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.startKey = QtWidgets.QLabel(self.widget)
        self.startKey.setObjectName("startKey")
        self.gridLayout.addWidget(self.startKey, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.endKey = QtWidgets.QLabel(self.widget)
        self.endKey.setObjectName("endKey")
        self.gridLayout.addWidget(self.endKey, 3, 1, 1, 1)

        self.retranslateUi(startmenu)
        QtCore.QMetaObject.connectSlotsByName(startmenu)

    def retranslateUi(self, startmenu):
        _translate = QtCore.QCoreApplication.translate
        startmenu.setWindowTitle(_translate("startmenu", "开始"))
        self.label.setText(_translate("startmenu", "当前状态:"))
        self.state_label.setText(_translate("startmenu", "未运行"))
        self.label_3.setText(_translate("startmenu", "循环次数:"))
        self.label_count.setText(_translate("startmenu", "1"))
        self.label_4.setText(_translate("startmenu", "启动热键："))
        self.startKey.setText(_translate("startmenu", "F9"))
        self.label_5.setText(_translate("startmenu", "结束热键："))
        self.endKey.setText(_translate("startmenu", "F10"))
