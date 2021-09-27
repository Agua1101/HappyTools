import requests
from tools import imgAutoCick
import pyautogui
import time
import pyperclip
import keyboard




def auto_create_account(name):
    # 点击头像
    pyautogui.moveTo(x=1535, y=110,duration=0.1, tween=pyautogui.linear)
    pyautogui.click()
    time.sleep(0.5)
    # 点击创建账户
    imgAutoCick(r'D:\AI\yolo5\project_all\money_script\pic\fox\create_admin.png',pyautogui.click)
    time.sleep(0.5)
    pyperclip.copy(name)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    # 点击创建按钮
    imgAutoCick(r'D:\AI\yolo5\project_all\money_script\pic\fox\create_button.png',pyautogui.click)
    time.sleep(1)




for i in range(66,1001):
    name = f't{i}'
    auto_create_account(name)
    try:
        if keyboard.is_pressed('q'):  # it will stop working by clicking q you can change to to any key
            break
        else:
            pass
    except:
        pass
