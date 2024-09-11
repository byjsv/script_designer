import win32api

from Output_QThread import jb_Output

lss = jb_Output()
lss.updateRect()
"""
print(lss.FullWindowRect)
print(lss.windowRect)
"""
while True:
    x, y = win32api.GetCursorPos()  # 获取鼠标位置
    print(x, y)

