import win32api
import time
import win32gui

startKey = 120  # 开始键的ASCII，目前为F9
endKey = 121  # 结束键的ASCII，目前为F10

event_list = []


def getHwnd(windowName):
    hwnd = win32gui.FindWindow(None, windowName)
    return win32gui.GetWindowRect(hwnd)


def sumScript(filename):
    keyDir = {}
    # keyList = []
    with open('常用按键的ASCII值', 'r') as loadfile:  # 初始化需要监听的按键列表
        keyList = [int(x) for x in loadfile.readlines()]

    for i in keyList:
        keyDir[i] = 0

    x0 = y0 = 0

    start_x, start_y = win32api.GetCursorPos()
    lsr = '{} {} {}\n'.format(0, start_x, start_y)
    event_list.append(lsr)  # 存储一个起始坐标

    print('正在执行 {} 录制，按F9开始'.format(filename))

    exitNum = 0
    """while True:
        time.sleep(0.01)
        if win32api.GetKeyState(startKey) & 0x8000:  # F9键开始
            print("现在开始录制")
            break"""

    zeroTime = time.time()
    startTime = int((time.time() - zeroTime) * 1000000)

    while True:

        currentTime = int((time.time() - zeroTime) * 1000000)

        if currentTime - startTime > 1000:
            startTime = currentTime

            print(1)

            if win32api.GetKeyState(endKey) & 0x8000:  # 判断按键结束
                lstr = '{} -256 0'.format(currentTime)
                event_list.append(lstr)
                print('脚本{}已录制完毕，总时长为{}秒\n'.format(filename, currentTime / 1000000))
                break

            for key in keyList:  # 获取按键操作
                if win32api.GetKeyState(key) & 0x8000:  # ASCII码
                    if keyDir[key] == 0:  # 下降沿，输出到文本
                        lstr = '{} {} {}\n'.format(currentTime, -key, 0)  # 分别是时间 按键 按下(模式)
                        print(lstr)
                        event_list.append(lstr)
                    keyDir[key] = 1  # 置为高位

                else:
                    if keyDir[key] == 1:  # 上升沿，输出到文本
                        lstr = '{} {} {}\n'.format(currentTime, -key, 2)  # 分别是时间 按键 弹起(模式)
                        print(lstr)
                        event_list.append(lstr)
                    keyDir[key] = 0  # 置为低位

            if exitNum:
                break

            x, y = win32api.GetCursorPos()  # 获取鼠标位置
            if x != x0 or y != y0:
                strMouse = '{} {} {}\n'.format(currentTime, x, y)  # 时间 x坐标+ y坐标+
                x0 = x
                y0 = y
                event_list.append(strMouse)

    with open(filename, 'w') as file:
        for line in event_list:
            file.write(line)
