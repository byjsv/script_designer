import pyautogui as Pkey
import numpy as np
import tkinter as tk

window = tk.Tk()
window.title('mouseRGB')
window.geometry('600x50')

label = tk.Label(window, font=("Arial Bold", 25))
label.pack()


# 定义更新标签文本的函数
def update_label():
    # 获取鼠标指针位置
    x, y = Pkey.position()

    mouseRGB = Pkey.screenshot(region=(x, y, x + 1, y + 1))
    rgb_array = np.array(mouseRGB.convert('RGB'))
    # 更新标签文本
    label.config(text="X:" + str(x) + " Y:" + str(y) + " RGB:" + str(rgb_array[0][0]))

    # 每隔 0.1 秒更新一次标签文本
    label.after(100, update_label)


# 启动更新标签文本的函数
update_label()

# 运行窗口
window.mainloop()
