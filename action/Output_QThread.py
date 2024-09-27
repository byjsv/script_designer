import json

import win32api
import win32con
import win32gui
import random

from PyQt5.QtCore import QThread
from pynput.mouse import Button, Controller
from pyautogui import write
import time


class jb_Output(QThread):
    def __init__(self, parent=None):
        super(jb_Output, self).__init__(parent)
        self._running = True
        self.workList = []
        self.FullWindowRect = [0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)]
        self.windowRect = [0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)]
        self.hwnd = None
        self.turn_times = 1
        self.filepath = ''

    def set_messageList(self):
        """ 从文件中读取工作列表 """
        with open(self.filepath, 'r') as file:
            self.workList = json.load(file)
            """
            for i in file.readlines():
                lstr = i.split()
                if int(lstr[0]) == -4:
                    xstr = [int(lstr[0]), lstr[1]]
                else:
                    xstr = [int(x) for x in lstr]
                self.workList.append(xstr)
"""
    def updateRect(self):
        """ 更新窗口矩形区域 """
        if self.hwnd is not None:
            client_rect = win32gui.GetClientRect(self.hwnd)
            client_top_left = win32gui.ClientToScreen(self.hwnd, (client_rect[0], client_rect[1]))
            client_bottom_right = win32gui.ClientToScreen(self.hwnd, (client_rect[2], client_rect[3]))

            # 更新窗口矩形
            self.windowRect = [
                client_top_left[0],  # x1
                client_top_left[1],  # y1
                client_bottom_right[0],  # x2
                client_bottom_right[1]  # y2
            ]

    def setGameWindow(self, gameName):
        """ 设置游戏窗口并更新窗口矩形区域 """
        if gameName is None:
            print('未配置窗口名称，当前为屏幕坐标系')
            self.windowRect = [0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)]
            self.FullWindowRect = self.windowRect  # 初始化为屏幕全范围
        else:
            self.hwnd = win32gui.FindWindow(None, gameName)
            self.updateRect()
            self.FullWindowRect = self.windowRect  # 设置全窗口矩形区域


    def sleep(self, t):
        """ 等待指定时间或直到按下退出按键 """
        startTime = time.time()
        while self._running:
            if time.time() - startTime >= t:
                print("已等待{:.2f}秒".format(time.time() - startTime))
                break

    def press_key(self, key, mode):
        """模拟键盘或鼠标按键事件
        key: 按键的标识符, 如果大于6则视为键盘按键, 否则视为鼠标按键
        mode: 模拟事件的模式, 0为按下, 1为释放"""
        if key > 6:
            win32api.keybd_event(key, 0, mode, 0)
        else:
            if key == 1:  # 左键
                if mode == 0:
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                else:
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            elif key == 2:  # 右键
                if mode == 0:
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                else:
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
            elif key == 5:  # X1鼠标按钮
                mouse = Controller()
                if mode == 0:
                    mouse.press(Button.x1)
                else:
                    mouse.release(Button.x1)

    def press_once(self, key):
        """单次按下按键
        key: 要按下的键的标识符"""
        t1 = random.randint(10, 30) / 100
        t2 = random.randint(30, 60) / 100
        t3 = random.randint(10, 20) / 100
        self.sleep(t1)
        self.press_key(key, 0)
        self.sleep(t2)
        self.press_key(key, 2)
        self.sleep(t3)

    def select_key(self, key, mod):
        """选择按键模式，主要分支单次按下和按住弹起
        key: 按键的标识符
        mod: 模式标识符，1为单次按下，其他值为按住/释放模式"""
        if mod == 1:
            self.press_once(key)
        else:
            self.press_key(key, mod)

    def writeText(self, string):
        """写字操作，只能输入英文
        string: 要输入的字符串"""
        write(string, interval=0.1)

    def moveto(self, x, y):
        """鼠标移动事件
        x: 目标x坐标
        y: 目标y坐标"""
        if not hasattr(self, 'FullWindowRect'):
            raise ValueError("FullWindowRect not set. Call setGameWindow() first.")

        # 校准成对应窗口的相对坐标
        judgeX = (self.windowRect[2] - self.windowRect[0]) / (self.FullWindowRect[2] - self.FullWindowRect[0])
        judgeY = (self.windowRect[3] - self.windowRect[1]) / (self.FullWindowRect[3] - self.FullWindowRect[1])

        # 计算屏幕坐标
        screenX = int(x * judgeX + self.windowRect[0])
        screenY = int(y * judgeY + self.windowRect[1])

        # 移动鼠标
        win32api.SetCursorPos((screenX, screenY))

    def run(self):
        for i in range(self.turn_times):
            if not self._running:
                break
            self.startAction()

    ##############################
    #     读取脚本的数据格式说明
    #   参数1，参数2，参数3均为数字
    # 参数1为时间片，同时在自定脚本中为负数，用于取代脚本指令的序号
    # 自定脚本中 三个参数分别为：指令函数序号，参数1，参数2
    # 录制脚本中 三个参数分别为：时间片，参数1，参数2
    # 按键事件的参数为：键码，状态
    # 鼠标移动事件的参数为：x坐标，y坐标
    # 延时事件的参数为：时间/s，空
    # 运行其他脚本的参数为：文件名/路径文件名，空
    ##############################
    def startAction(self):
        """ 执行工作列表中的事件 """
        print('正在执行 {} 事件'.format(self.filepath))
        zeroTime = time.time()
        line = 0  # 执行位置
        while self._running:
            currentTime = int((time.time() - zeroTime) * 1000000)  # 当前时间

            if currentTime % 1000000 == 1:  # 1秒更新一次窗口尺寸
                if self.hwnd is not None:
                    self.updateRect()

            if line >= len(self.workList) or self.workList[line][1] == -256:
                print('当前事件已执行完毕')
                break

            if self.workList[line]["timeSeq"] < currentTime:
                if self.workList[line]["eventType"] == "keyEvent":
                    self.select_key(self.workList[line]["keyOrd"], self.workList[line]["statu"])
                elif self.workList[line]["eventType"] == "mouseMove":
                    self.moveto(self.workList[line]["posX"], self.workList[line]["posY"])
                elif self.workList[line]["eventType"] == "Delay":
                    self.sleep(self.workList[line]["time"])
                elif self.workList[line]["eventType"] == "runFile":
                    jb = jb_Output()
                    jb.filepath = self.workList[line]["fileName"]
                    jb.set_messageList()
                    jb.run()
                elif self.workList[line]["eventType"] == "end":
                    break

                line += 1

    def stop(self):
        self._running = False
        self.wait()  # 等待线程结束
