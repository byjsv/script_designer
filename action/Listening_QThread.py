import win32api
import time
import win32gui
import json
from PyQt5.QtCore import QThread

"""
data = {
    "eventType": "mouseMove",
    "timeSeq": 0,
    "posX": 0
}
"""


class jb_Listening(QThread):
    def __init__(self, parent=None):
        super(jb_Listening, self).__init__(parent)
        self._running = True  # 线程运行标志位
        self.event_list = []  # 存储事件清单
        self.keyDir = {}  # 键码和值
        self.filename = ''  # 存储的文件路径名称
        self.currentTime = 0

    def init_param(self, fName):
        self.filename = fName
        self.loadFile_to_Dir()

    def save(self):
        endEvent = {"timeSeq": self.currentTime, "eventType": "end"}
        self.event_list.append(endEvent)
        print('脚本{}已录制完毕，总时长为{}秒\n'.format(self.filename, self.currentTime / 1000000))
        with open(self.filename, 'w') as file:
            json.dump(self.event_list, file, indent=4)

    def loadFile_to_Dir(self):
        with open('./action/常用按键的ASCII值', 'r') as loadfile:
            for line in loadfile:
                key = int(line.strip())
                self.keyDir[key] = 0

    def run(self):
        print('run')
        self.sumScript()

    def stop(self):
        self._running = False
        self.wait()  # 等待线程结束

    def sumScript(self):

        x0 = y0 = 0

        start_x, start_y = win32api.GetCursorPos()

        event = {"timeSeq": 0, "eventType": "mouseMove", "posX": start_x, "posY": start_y}
        self.event_list.append(event)  # 存储一个起始坐标

        print('正在执行 {} 录制，按F9开始'.format(self.filename))

        zeroTime = time.time()
        startTime = int((time.time() - zeroTime) * 1000000)

        while self._running:

            self.currentTime = int((time.time() - zeroTime) * 1000000)

            if self.currentTime - startTime > 100:
                startTime = self.currentTime

                for key in self.keyDir:  # 获取按键操作
                    if win32api.GetKeyState(key) & 0x8000:  # ASCII码
                        if self.keyDir[key] == 0:  # 下降沿，输出到文本
                            event = {"timeSeq": self.currentTime, "eventType": "keyEvent", "keyOrd": key, "statu": 0}
                            print(event)
                            self.event_list.append(event)
                        self.keyDir[key] = 1  # 置为高位

                    else:
                        if self.keyDir[key] == 1:  # 上升沿，输出到文本
                            event = {"timeSeq": self.currentTime, "eventType": "keyEvent", "keyOrd": key, "statu": 2}
                            print(event)
                            self.event_list.append(event)
                        self.keyDir[key] = 0  # 置为低位

                x, y = win32api.GetCursorPos()  # 获取鼠标位置
                if x != x0 or y != y0:
                    event = {"timeSeq": self.currentTime, "eventType": "mouseMove", "posX": x, "posY": y}# 时间 x坐标+ y坐标+
                    x0 = x
                    y0 = y
                    print(event)
                    self.event_list.append(event)


def getHwnd(windowName):
    hwnd = win32gui.FindWindow(None, windowName)
    return win32gui.GetWindowRect(hwnd)
