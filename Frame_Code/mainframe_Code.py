from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from UI.mainframe import Ui_MainWindow
from .RecodeFrame_Code import record_jb
from .jbdesigner_Code import jb_Dialog
from .startframe_Code import start_menu
from .input_correct import *


# 主程序部分
# 此部分主要包含运行和选择脚本
# 以及启动编辑
#
#
#
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.frame3 = None
        self.thread = None
        self.frame1 = None
        self.frame2 = None
        self.setupUi(self)

        self.Button_new.clicked.connect(self.new_jb)
        self.Button_edit.clicked.connect(self.edit_jb)
        self.comboBox.currentTextChanged.connect(self.last_jb)
        self.Button_record.clicked.connect(self.record)
        self.Button_start.clicked.connect(self.start)

        self.update_comboBox()

    # 开始函数，运行指定路径脚本
    def start(self):
        if self.lineEdit_Filepath.text() != '' and is_accessible_path(self.lineEdit_Filepath.text()):  # 文件路径判断
            if not if_ASCII(self.lineEdit_startkey.text()) or not if_ASCII(self.lineEdit_endkey.text()):
                QMessageBox.information(self, '提示', '错误的热键设置')
                return
            if not only_num(self.lineEdit_count.text()):
                QMessageBox.information(self, '提示', '循环次数应该为数字')
                return
            self.frame3 = start_menu()
            self.frame3.filePath = self.lineEdit_Filepath.text()
            self.frame3.setWindowTitle(self.lineEdit_Filepath.text())
            self.frame3.show()
            self.hide()

            self.frame3.startKey.setText(self.lineEdit_startkey.text())
            self.frame3.endKey.setText(self.lineEdit_endkey.text())
            self.frame3.label_count.setText(self.lineEdit_count.text())

            self.frame3.finished.connect(self.save_startFilePath)
        else:
            QMessageBox.information(self, '提示', '不存在或错误的文件名称和路径')

    # 录制函数，打开另一个界面开始录制
    def record(self):
        self.frame2 = record_jb()
        self.frame2.show()
        self.hide()

        self.frame2.finished.connect(self.save_recodeFilepath)

    # 新建脚本
    def new_jb(self):
        self.frame1 = jb_Dialog()
        self.frame1.show()
        self.hide()

        self.frame1.finished.connect(self.set_filePath)

    # 编辑指定脚本
    # 需要实现文件里的字符串转化成item
    def edit_jb(self):
        if self.lineEdit_Filepath.text() != '' and is_accessible_path(self.lineEdit_Filepath.text()):  # 文件路径判断
            self.frame1 = jb_Dialog()
            self.frame1.lineEdit.setText(self.lineEdit_Filepath.text())

            # 文件读取后，将所有行的内容读取存到下一个窗口的eventList列表里面
            # 然后通过函数更新，就有对应的事件对象
            with open(self.lineEdit_Filepath.text(), 'r') as file:
                index = 0
                for i in file.readlines():
                    lstr = i.split()
                    if int(lstr[0]) == -256:
                        break
                    if i != '\0':
                        self.frame1.listWidget.addItem(' ')
                    if int(lstr[0]) > 0:
                        QMessageBox.information(self, '提示', '该脚本为录制脚本，不可编辑')
                        return
                    if len(lstr) == 2:
                        # 单行字符串两条时
                        self.frame1.eventList.append([index, int(lstr[0]), lstr[1], ''])
                    elif len(lstr) == 3:
                        # 单行字符串三条
                        if int(lstr[0]) == -1:  # 专门对按键事件处理
                            self.frame1.eventList.append([index, int(lstr[0]), chr(int(lstr[1])), lstr[2]])
                        else:
                            self.frame1.eventList.append([index, int(lstr[0]), lstr[1], lstr[2]])
                    index += 1

            self.frame1.update_list()

            self.frame1.show()
            self.hide()

            self.frame1.finished.connect(self.set_filePath)
        else:
            QMessageBox.information(self, '提示', '不存在或错误的文件名称和路径')

    def set_filePath(self):
        if self.frame1.save_flag:
            self.lineEdit_Filepath.clear()
            self.lineEdit_Filepath.setText(self.frame1.lineEdit.text())
            self.save(self.frame1.lineEdit.text())  # 执行一次保存操作
        self.show()
        self.frame1 = None
        self.update_comboBox()

    def save_startFilePath(self):
        self.lineEdit_Filepath.clear()
        self.lineEdit_Filepath.setText(self.frame3.filePath)
        self.save(self.frame3.filePath)  # 执行一次保存操作
        self.show()
        self.frame3 = None
        self.update_comboBox()

    def save_recodeFilepath(self):
        self.lineEdit_Filepath.clear()
        self.lineEdit_Filepath.setText(self.frame2.lineEdit_filePath.text())
        self.save(self.frame2.lineEdit_filePath.text())  # 执行一次保存操作
        self.show()
        self.frame2 = None
        self.update_comboBox()

    # 查看最后使用的脚本，路径存储在另一个文件，编辑和运行脚本都应该保存一次
    def last_jb(self):
        self.lineEdit_Filepath.setText(self.comboBox.currentText())

    # 按文件顺序刷新控件
    def update_comboBox(self):
        self.comboBox.clear()
        with open('filePath.ini', 'r') as file:
            for i in file.readlines():
                text = i.rstrip('\n')
                self.comboBox.addItem(text)

    # 此函数用于保存使用的路径
    # 具体存在filePath.ini中
    def save(self, filename):
        ls = []  # 临时存储所有文件路径(每行字符串)
        lstr = filename + '\n'  # 当前名称字符串

        with open('filePath.ini', 'r') as file:
            ls.insert(0, lstr)
            for i in file:
                if i != lstr:  # 发现相同的路径名称
                    ls.append(i)

        with open('filePath.ini', 'w') as file:
            for i in ls:
                file.write(i)

        self.update_comboBox()  # 刷新以在最近中显示文件
