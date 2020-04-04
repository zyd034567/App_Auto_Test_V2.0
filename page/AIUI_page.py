# -- coding: utf-8 --
import time
import os

import allure
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class AIUIPage(BaseAction):


    # 关闭AIUI"X"符号
    close_AIUI_button = By.ID, "com.iflyrec.smartrecorder:id/aiui_close_btn"
    # 你可以这样问我"?"符号
    you_can_ask_me_button = By.ID, "com.iflyrec.smartrecorder:id/aiui_help_btn"

    # 长按AIUI键
    def long_AIUI(self):

        self.driver.long_press_keycode(170)
        # TouchAction(self.driver).press(x=250, y=1200).release().perform()
        # os.system("adb shell sendevent  /dev/input/event0 1 170 1")
        # os.system("adb shell sendevent  /dev/input/event0 0 0 0")
        # time.sleep(3)
        # print("按下")
        # os.system("adb shell sendevent  /dev/input/event0 1 170 0")
        # os.system("adb shell sendevent  /dev/input/event0 0 0 0")
        # time.sleep(2)
        # print("松开")



        '''
        os.system("adb shell sendevent  /dev/input/event0 1 116 1")
        os.system("adb shell sendevent  /dev/input/event0 0 0 0")
        time.sleep(10)   # 实现长按关机操作
        
         '''

    # 关闭AIUI
    @allure.step(title="点击关闭AIUI按钮")
    def click_close_AIUI(self):
        self.click(self.close_AIUI_button)

    # 开启你可以这样问我？
    @allure.step(title="点击开启你可以这样问我？")
    def click_you_can_ask_me(self):
        self.click(self.you_can_ask_me_button)

    # 检查toast文本
    @allure.step(title="检查toast文本")
    def check_toast_text(self):
        self.find_toast("此页面暂不支持语音控制")



