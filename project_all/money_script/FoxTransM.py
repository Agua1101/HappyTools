import requests
from tools import imgAutoCick,location
import pyautogui
import time
import pyperclip
import keyboard

def moveClick(x=None,y=None,duration=None,tween=pyautogui.linear):
    pyautogui.moveTo(x=x, y=y, duration=duration, tween=tween)
    pyautogui.click()


def trans_money(account,money):
    # 点击头像
    moveClick(x=1535, y=110,duration=0.1, tween=pyautogui.linear)
    time.sleep(0.5)
    # 点击搜索框
    moveClick(x=1330, y=210,duration=0.1, tween=pyautogui.linear)
    '1330,210'
    # 输入账户名称
    pyperclip.copy(account)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    # 点击目标账户
    moveClick(x=1377, y=257,duration=0.1, tween=pyautogui.linear)
    '1377,257'
    time.sleep(0.5)
    # 点击token地址复制
    moveClick(x=956, y=170,duration=0.1, tween=pyautogui.linear)
    '956,170'
    time.sleep(0.5)
    # 点击头像
    moveClick(x=1535, y=110,duration=0.1, tween=pyautogui.linear)
    time.sleep(0.5)
    # 点击总账户
    moveClick(x=1377, y=257,duration=0.1, tween=pyautogui.linear)
    '1377,257'
    time.sleep(0.5)
    # 点击发送
    moveClick(x=948, y=353,duration=0.1, tween=pyautogui.linear)
    '948,353'
    time.sleep(0.5)
    # 直接粘贴
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    # 点击数额输入框
    moveClick(x=911, y=362,duration=0.1, tween=pyautogui.linear)
    '911,362'
    # 输入0.001
    time.sleep(0.5)
    pyperclip.copy(money)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    # 点击下一步
    moveClick(x=1050, y=899,duration=0.1, tween=pyautogui.linear)
    '1050,899'
    time.sleep(1.5)
    # 点击确认（位置不变可以直接点）
    moveClick(x=1050, y=899,duration=0.1, tween=pyautogui.linear)
    '1050,899'
    time.sleep(1)


trans_money('t13','0.001')

# location()
