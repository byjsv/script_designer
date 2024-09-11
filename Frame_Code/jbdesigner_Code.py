from PyQt5 import QtWidgets
from PyQt5.QtGui import QBrush, QColor, QFont, QIcon
from PyQt5.QtWidgets import QListWidgetItem, QMessageBox

from .EventMenu_Code import Event_menu
from UI.jbdesigner import Ui_Ui_jbdesigner
from .input_correct import is_valid_path


# 脚本窗口
# 主要是对单独脚本进行编辑
# 有保存操作和新建事件
#
#
class jb_Dialog(QtWidgets.QDialog, Ui_Ui_jbdesigner):
    def __init__(self, parent=None):
        super(jb_Dialog, self).__init__(parent)
        self.frame1 = None
        self.setupUi(self)
        self.eventList = []
        self.save_flag = False

        self.addButton.clicked.connect(self.add_event)
        self.pushButton.clicked.connect(self.save_all)
        self.removeButton.clicked.connect(self.remove_event)

        self.update_list()

    # 添加一个事件
    def add_event(self):
        current_row = self.listWidget.currentRow()
        self.frame1 = Event_menu()
        if current_row == -1:
            self.frame1.spinBox.setValue(len(self.eventList) + 1)
        else:
            self.frame1.spinBox.setValue(current_row + 2)
        self.frame1.show()

        self.frame1.finished.connect(self.save_event)

    # 删除指定事件
    def remove_event(self):
        current_row = self.listWidget.currentRow()
        if current_row >= 0:
            self.eventList.pop(current_row)
            item = self.listWidget.takeItem(current_row)
            del item
        self.update_list()

    # 更新列表
    def update_list(self):
        # 遍历所有项，并更新每一项的文本
        for i in range(self.listWidget.count()):
            selectMode = ''
            icon_path = ''
            # 改变显示的item的名称和图片
            if self.eventList[i][1] == -1:
                selectMode = '按键'
                icon_path = './picture/keyboard.jpg'
            elif self.eventList[i][1] == -2:
                selectMode = '鼠标移动'
                icon_path = './picture/mouse.jpg'
            elif self.eventList[i][1] == -3:
                selectMode = '延时'
                icon_path = './picture/clock.jpg'
            elif self.eventList[i][1] == -4:
                selectMode = '运行指定脚本'
                icon_path = './picture/file.jpg'
            strI = '{}  {} {} {}'.format(str(i + 1), selectMode, self.eventList[i][2], self.eventList[i][3])

            # 配置一个item
            item = self.listWidget.item(i)  # 赋值对应item
            item.setBackground(QBrush(QColor('lightgreen')))  # 设置背景色
            item.setForeground(QBrush(QColor('blue')))  # 设置字体颜色
            item.setFont(QFont('Arial', 9, QFont.Bold))  # 设置字体及其样式
            item.setIcon(QIcon(icon_path))  # 设置图片
            # 更新每个项的文本
            item.setText(strI)

            self.eventList[i][0] = i

    # 保存事件函数，将在窗口关闭时调用
    def save_event(self):
        # 判断事件窗口是否确认保存
        if self.frame1.save_flag:
            item = QListWidgetItem(' ')
            # listWidget添加item
            self.listWidget.insertItem(self.frame1.spinBox.value() - 1, item)
            # 事件列表添加事件的参数列表[]
            self.eventList.insert(self.frame1.spinBox.value() - 1, self.frame1.one_event)

            # 遍历所有项，并更新文本
            self.update_list()
            # 销毁小窗口
            self.frame1 = None

    def load_jb(self):
        pass

    # 保存，实际上是创建文件
    def save_all(self):
        if self.lineEdit.text() != '' and is_valid_path(self.lineEdit.text()):  # 文件路径判断
            with open(self.lineEdit.text(), 'w') as file:

                # 遍历事件列表，将列表元素拼接成字符串
                for i in self.eventList:
                    if i[1] == -1:
                        lstr = '{} {} {}\n'.format(str(i[1]), ord(i[2]), i[3])
                    else:
                        lstr = '{} {} {}\n'.format(i[1], i[2], i[3])
                    file.write(lstr)
                file.write('-256 0 0') # 封顶事件，结束标志
            self.save_flag = True
            self.close()
        else:
            QMessageBox.information(self, '提示', '未输入或错误的文件名称和路径')
