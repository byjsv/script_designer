import win32api
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer

from UI.startframe import Ui_startmenu
from action.ASCII_Turn import get_virtual_key_code
from action.Output_QThread import jb_Output


class start_menu(QtWidgets.QDialog, Ui_startmenu):
    def __init__(self, parent=None):
        super(start_menu, self).__init__(parent)
        self.setupUi(self)
        self.thread = None
        self.filePath = ''
        self.startFlag = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_key_state)

        self.start_key_check()

    def start_key_check(self):
        self.timer.start(1)  # 每1毫秒检查一次

    def check_key_state(self):
        # 读取开始结束键的键码
        start_key_state = win32api.GetKeyState(get_virtual_key_code(self.startKey.text()))
        end_key_state = win32api.GetKeyState(get_virtual_key_code(self.endKey.text()))

        # 判断是否按下，然后改变状态
        if start_key_state & 0x8000 and not self.startFlag:
            self.start_thread()  # 开始线程

        if end_key_state & 0x8000 and self.startFlag:
            self.stop_thread()

    # 初始化打开线程
    def start_thread(self):
        if self.thread is None or not self.thread.isRunning():
            self.startFlag = True
            print('start')
            self.state_label.setText('正在运行')
            self.thread = jb_Output()

            self.thread.turn_times = int(self.label_count.text())   # 设置循环次数
            self.thread.filepath = self.filePath    # 设置打开的脚本文件
            self.thread.set_messageList()           # 初始化读取事件列表

            self.thread.finished.connect(self.stop_thread)
            self.thread.start()

    def stop_thread(self):
        if self.thread is not None:
            self.startFlag = False
            print('end')
            self.thread.stop()
            self.state_label.setText('未运行')
            self.thread = None
