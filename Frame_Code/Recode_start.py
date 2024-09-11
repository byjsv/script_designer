import win32api
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from action.ASCII_Turn import get_virtual_key_code

from UI.dialog_recode import Ui_Recoding
from action.Listening_QThread import jb_Listening


class recode_dialog(QtWidgets.QDialog, Ui_Recoding):
    def __init__(self, parent=None):
        super(recode_dialog, self).__init__(parent)
        self.thread = None
        self.startFlag = False
        self.setupUi(self)
        self.filePath = ''

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_key_state)
        self.finished.connect(self.stop_thread)

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
            if self.thread is not None:
                self.startFlag = False
                self.thread.save()
                self.stop_thread()

    # 初始化打开线程
    def start_thread(self):
        if self.thread is None or not self.thread.isRunning():
            self.startFlag = True
            print('start')
            self.state_label.setText('正在运行')
            self.thread = jb_Listening()
            self.thread.init_param(self.filePath)

            self.thread.finished.connect(self.stop_thread)
            self.thread.start()

    def stop_thread(self):
        if self.thread is not None:
            print('end')
            self.thread.stop()
            self.state_label.setText('未运行')
            self.thread = None
