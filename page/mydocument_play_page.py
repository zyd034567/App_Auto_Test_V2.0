# -- coding: utf-8 --
import allure
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MyDocumentPlayPage(BaseAction):


    # 播放界面
    add_label_button = By.ID, "com.iflyrec.smartrecorder:id/click_to_add_label_layout"
    label_input_box = By.ID, "com.iflyrec.smartrecorder:id/edit_label_name"
    # To_eliminate_content = By.ID, "com.iflyrec.smartrecorder:id/emptySpeechLL"
    Exit_the_editor_label = By.ID, "com.iflyrec.smartrecorder:id/tv_title"


    # 点击播放或暂停
    Play_or_pause_button = By.ID, "com.iflyrec.smartrecorder:id/play_btn"
    # 返回
    return_button = By.ID, "com.iflyrec.smartrecorder:id/tv_left"



    # 点击添加标签
    @allure.step(title="点击添加标签")
    def click_add_label_play(self):
        self.click(self.add_label_button)

    # 点击返回
    @allure.step(title="点击返回")
    def click_return_button(self):
        self.click(self.return_button)

    # 添加标签内容
    @allure.step(title="点击添加标签内容")
    def input_label_name_play(self, text):
        self.input(self.label_input_box, text)
        self.click(self.Exit_the_editor_label)

    # 点击播放或暂停
    @allure.step(title="点击播放或暂停")
    def click_play_or_pause(self):
        self.click(self.Play_or_pause_button)

    # 调节音频进度
    def adjust_audio_speed_right(self):
        # window_size = self.driver.get_window_size()
        # width = window_size["width"]
        # height = window_size["height"]
        # left_x = width * 0.2
        # left_y = height * 0.1
        # right_x = width * 0.4
        # right_y = left_y
        # self.driver.swipe(right_x, right_y, left_x, left_y)  # 向右滑动
        TouchAction(self.driver).press(x=110, y=750).wait(100).move_to(x=300, y=750).release().perform()
        # TouchAction(self.driver).press(x=500, y=1200).release().perform()

    def adjust_audio_speed_left(self):
        # window_size = self.driver.get_window_size()
        # width = window_size["width"]
        # height = window_size["height"]
        # left_x = width * 0.2
        # left_y = height * 0.1
        # right_x = width * 0.4
        # right_y = left_y
        # self.driver.swipe(left_x, left_y, right_x, right_y)  # 向左滑动
        TouchAction(self.driver).press(x=300, y=750).wait(100).move_to(x=110, y=750).release().perform()

        # TouchAction(self.driver).press(x=250, y=1200).release().perform()

    # 返回按钮
    def click_return(self):
        self.click(self.return_button)

