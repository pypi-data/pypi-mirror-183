from win32api import mouse_event
from win32con import MOUSEEVENTF_WHEEL
import os
import time
import pyautogui as pag


def scroll(length: int):
    """
    滚动鼠标
    """
    for i in range(1, length): mouse_event(MOUSEEVENTF_WHEEL, 0, 0, -1)


def echo_mouse_pos():
    """
    输出鼠标当前坐标
    """
    try:
        while True:
            print("按下Ctrl + C 结束程序")
            x, y = pag.position()
            posStr = "当前鼠标位置:" + str(x).rjust(4) + ',' + str(y).rjust(4)
            print(posStr)
            time.sleep(1)
            # 清除屏幕
            os.system('cls')
            return posStr
    except KeyboardInterrupt:
        print('已退出')
