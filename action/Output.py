from sys import exit
import win32api
import win32con
import win32gui
import random
from pynput.mouse import Button, Controller
from pyautogui import write
import time

startKey = 120  # 开始键的ASCII，目前为F9
endKey = 121  # 结束键的ASCII，目前为F10

workList = []  # 先存储文件内容信息

FullWindowRect = [0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)]  # 保存当前屏幕尺寸
windowRect = [0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)]  # 游戏屏幕尺寸左上右下
hwnd = None  # 游戏窗口句柄


def updateRect():  # 更新窗口的坐标
    # 获取窗口客户区域的矩形坐标
    client_rect = win32gui.GetClientRect(hwnd)
    # 将客户区域坐标转换为屏幕坐标
    client_top_left = win32gui.ClientToScreen(hwnd, (client_rect[0], client_rect[1]))
    client_bottom_right = win32gui.ClientToScreen(hwnd, (client_rect[2], client_rect[3]))
    windowRect[0] = client_top_left[0]
    windowRect[1] = client_top_left[1]
    windowRect[2] = client_bottom_right[0]
    windowRect[3] = client_bottom_right[1]


# 设置窗口名称，以查找句柄
def setGameWindow(gameName):
    global windowRect
    global hwnd
    if gameName is None:
        print('未配置窗口名称，当前为屏幕坐标系')
        windowRect = [0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)]
    else:
        hwnd = win32gui.FindWindow(None, gameName)
        updateRect()


# 睡眠函数，非阻塞性，可快捷键退出程序执行
def sleep(t):
    startTime = time.time()
    while True:
        if time.time() - startTime >= t:
            print("已等待{:.2f}秒".format(time.time() - startTime))
            break
        if win32api.GetKeyState(endKey) & 0x8000:  # 单独检测一次结束按键
            print("已强制结束")
            exit()


# 模拟按键函数
def press_key(key, mode):  # 模式0为按下，模式2为弹起
    if key > 6:
        win32api.keybd_event(key, 0, mode, 0)
        return
    else:  # 0~6为预留的鼠标按键事件范围
        if key == 1:
            if mode == 0:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            else:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        elif key == 2:
            if mode == 0:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            else:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
        elif key == 5:
            mouse = Controller()  # 用于执行鼠标操作
            if mode == 0:
                mouse.press(Button.x1)
            else:
                mouse.release(Button.x1)


# 单次按下按键
def press_once(key):
    t1 = random.randint(10, 30) / 100
    t2 = random.randint(30, 60) / 100
    t3 = random.randint(10, 20) / 100
    sleep(t1)
    press_key(key, 0)
    sleep(t2)
    press_key(key, 2)
    sleep(t3)


# 选择按键模式，主要分支单次按下和按住弹起
def select_key(key, mod):
    if mod == 1:
        press_once(key)
    else:
        press_key(key, mod)


# 写字操作，只能输入英文
def writeText(string):
    write(string, interval=0.1)


def moveto(x, y):  # 鼠标移动事件
    # 校准成对应窗口的相对坐标
    judgeX = (windowRect[2] - windowRect[0]) / FullWindowRect[2]
    judgeY = (windowRect[3] - windowRect[1]) / FullWindowRect[3]
    # 移动鼠标
    win32api.SetCursorPos((int(x * judgeX + windowRect[0]), int(y * judgeY + windowRect[1])))


# 用于阻塞程序，只有当启动按键按下整个程序才开始执行
def wait_start(str_key):
    print("按{}启动脚本".format(str_key))
    while True:
        if win32api.GetKeyState(ord(str_key)) & 0x8000:  # F9键开始
            print("开始执行")
            break


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
def startAction(filename):
    global windowRect
    print('正在执行 {} 事件'.format(filename))
    zeroTime = time.time()
    # 读取脚本信息并转换格式
    with open(filename, 'r') as file:

        for i in file.readlines():
            lstr = i.split()
            if int(lstr[0]) == -4:  # 单独对打开脚本操作做字符串存储操作
                xstr = [int(lstr[0]), lstr[1]]
            else:
                xstr = [int(x) for x in lstr]  # 全部转化成int
            workList.append(xstr)
        # 初始化内容完成

    # 循环开始---------------------------------------------------------------
    line = 0  # 执行位置
    while True:
        currentTime = int((time.time() - zeroTime) * 1000000)  # 当前时间

        if currentTime % 1000000 == 1:  # 1秒更新一次窗口尺寸
            if hwnd is not None:
                updateRect()

        if win32api.GetKeyState(endKey) & 0x8000:  # 单独检测一次结束按键
            print("已强制结束")
            exit()

        if line >= len(workList) or workList[line][1] == -256:
            print('{} 事件已执行完毕'.format(filename))
            break

        # 当计时经过了对应的时间刻，检测事件
        if workList[line][0] < currentTime:

            # 当时间小于0时，说明为自定事件，无视时间刻执行
            # 大于0时，说明为录制事件，按时间刻执行
            if workList[line][0] < 0:
                if workList[line][0] == -1:  # 按键操作
                    select_key(workList[line][1], workList[line][2])
                elif workList[line][0] == -2:  # 鼠标移动
                    moveto(workList[line][1], workList[line][2])
                elif workList[line][0] == -3:  # 延时
                    sleep(workList[line][1])
                elif workList[line][0] == -4:  # 运行指定脚本
                    startAction(workList[line][1])
                line += 1

            else:
                # 区分一下按键事件和鼠标移动事件，调用函数
                if workList[line][1] < 0:
                    if workList[line][1] == -256:
                        break
                    press_key(0 - workList[line][1], workList[line][2])
                else:

                    moveto(workList[line][1], workList[line][2])

                line += 1
