from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from UI.RecodeFrame import Ui_Recode_Frame
from .Recode_start import recode_dialog
from .input_correct import if_ASCII


# 脚本录制窗口
class record_jb(QtWidgets.QDialog, Ui_Recode_Frame):
    def __init__(self, parent=None):
        super(record_jb, self).__init__(parent)
        self.frame1 = None
        self.thread = None
        self.setupUi(self)

        self.Botton_start.clicked.connect(self.start)

    def start(self):
        if self.lineEdit_filePath.text() != '':
            if not if_ASCII(self.lineEdit_startkey.text()) or not if_ASCII(self.lineEdit_endkey.text()):
                QMessageBox.information(self, '提示', '错误的热键设置')
                return
            self.frame1 = recode_dialog()
            # 对frame1属性设置
            self.frame1.startKey.setText(self.lineEdit_startkey.text())
            self.frame1.endKey.setText(self.lineEdit_endkey.text())
            self.frame1.filePath = self.lineEdit_filePath.text()
            self.frame1.setWindowTitle(self.lineEdit_filePath.text())
            # 初始化结束

            self.frame1.show()
            self.hide()
            self.frame1.finished.connect(self.show)
        else:
            QMessageBox.information(self, '提示', '未输入文件名称和路径')
