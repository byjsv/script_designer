from pynput.mouse import Button, Controller
import time

time.sleep(3)

mouse = Controller()

# 模拟侧键点击
mouse.press(Button.x1)  # 模拟按下侧键
time.sleep(1)
mouse.release(Button.x1)  # 模拟释放侧键
