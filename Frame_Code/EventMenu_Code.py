from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from UI.EventMenu import Ui_Ui_EventMenu
from .input_correct import if_ASCII, only_num, is_accessible_path


# 事件窗口
# 主要用于自定义事件
# 需要对用户详细引导
#
#


class Event_menu(QtWidgets.QDialog, Ui_Ui_EventMenu):
    def __init__(self, parent=None):
        super(Event_menu, self).__init__(parent)
        self.setupUi(self)
        self.one_event = []
        self.save_flag = False

        self.Button_acept.clicked.connect(self.send_event)
        self.comboBox.currentTextChanged.connect(self.select_action)

    # 控制选择事件类型的输入内容提示
    def select_action(self):
        # 清除已有输入
        self.lineEdit.clear()
        self.lineEdit_2.clear()

        # 当不需要参数2时隐藏控件，需要时重新展示
        if self.comboBox.currentText() == '按键':
            self.label_3.setText('按键')
            self.label_4.show()
            self.lineEdit_2.show()
            self.label_4.setText('状态')
        elif self.comboBox.currentText() == '鼠标移动':
            self.label_3.setText('X坐标')
            self.label_4.show()
            self.lineEdit_2.show()
            self.label_4.setText('Y坐标')
        elif self.comboBox.currentText() == '延时':
            self.label_3.setText('延时时间')
            self.label_4.hide()
            self.lineEdit_2.hide()
        elif self.comboBox.currentText() == '运行指定脚本':
            self.label_3.setText('脚本路径')
            self.label_4.hide()
            self.lineEdit_2.hide()

    # 当保存时，对内置的列表对象赋对应值
    def send_event(self):
        if self.comboBox.currentIndex() < 2 and self.lineEdit_2.text() == '':
            QMessageBox.information(self, '提示', '未输入参数')
        elif self.lineEdit.text() == '':
            QMessageBox.information(self, '提示', '未输入参数')
        elif self.comboBox.currentIndex() == 0 and not if_ASCII(self.lineEdit.text()):
            QMessageBox.information(self, '提示', '非按键')
        elif self.comboBox.currentIndex() == 1 and (not only_num(self.lineEdit.text()) or not only_num(self.lineEdit_2.text())):
            QMessageBox.information(self, '提示', '非坐标')
        elif self.comboBox.currentIndex() == 2 and not only_num(self.lineEdit.text()):
            QMessageBox.information(self, '提示', '非时间数字')
        elif self.comboBox.currentIndex() == 3 and not is_accessible_path(self.lineEdit.text()):
            QMessageBox.information(self, '提示', '不存在的路径或名称')
        else:
            self.save_flag = True
            self.one_event = [self.spinBox.value(), -(self.comboBox.currentIndex() + 1),
                              self.lineEdit.text(), self.lineEdit_2.text()]
            print(self.one_event)
            self.close()

