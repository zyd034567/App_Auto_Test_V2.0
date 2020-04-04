# -- coding: utf-8 --
import time

import allure
from appium.webdriver.common.touch_action import TouchAction

from base.base_action import BaseAction
from selenium.webdriver.common.by import By

"""
包含标准,会议,采访,演讲,音乐,备忘
"""

class RecordPage(BaseAction):

    return_button = By.ID, "com.iflyrec.smartrecorder:id/tv_left"

    roger_button = By.XPATH, "//*[@text='知道了']"
    no_longer_remind_button = By.XPATH, "//*[@text='不再提醒']"
    refresh_button = By.XPATH, "//*[@text='刷新']"

    cancel_record_button = By.ID, "com.iflyrec.smartrecorder:id/dialog_remind_cancel"
    quit_record_button = By.XPATH, "//*[@text='退出']"
    accomplish_button = By.XPATH, "//*[@text='完成']"
    pause_button = By.XPATH, "//*[@text='暂停']"
    continue_button = By.XPATH, "//*[@text='继续']"
    add_bookmark_button = By.XPATH, "//*[@text='添加书签']"
    gain_adjustment_button = By.XPATH, "//*[@text='调节增益']"
    font_size_button = By.ID, "com.iflyrec.smartrecorder:id/bt_textsize"  # 调节字体大小
    font_size_button_middle = By.XPATH, "//*[@text='中']"  # 选择中体字
    font_size_button_big = By.XPATH, "//*[@text='大']"  # 选择大体字

    switch_language_button = By.ID, "com.iflyrec.smartrecorder:id/bt_language"
    continue_transfer_button = By.ID, "com.iflyrec.smartrecorder:id/notice_top_forward_btn"
    add_label_button = By.ID, "com.iflyrec.smartrecorder:id/click_to_add_label_layout"
    label_input_box = By.ID, "com.iflyrec.smartrecorder:id/edit_label_name"
    add_name_button = By.ID, "com.iflyrec.smartrecorder:id/editName"
    save_button = By.XPATH, "//*[@text='保存']"
    cancel_save_button = By.XPATH, "//*[@text='取消']"
    # 服务器连接失败点击刷新
    server_connection_failed_click_refresh_button = By.ID, "com.iflyrec.smartrecorder:id/notice_top_forward_btn"

    # 返回按钮
    @allure.step(title="点击返回按钮")
    def click_return(self):
        self.click(self.return_button)

    # 点击知道了
    @allure.step(title="点击知道了")
    def click_roger_return(self):
        self.click(self.roger_button)

    # 点击不再提醒
    @allure.step(title="点击不再提醒")
    def click_no_longer_remind(self):
        self.click(self.no_longer_remind_button)

    # 点击刷新
    @allure.step(title="点击刷新")
    def click_refresh(self):
        self.click(self.refresh_button)

    # 取消录音
    @allure.step(title="取消录音")
    def click_cancel_record(self):
        self.click(self.cancel_record_button)

    # 退出录音
    @allure.step(title="退出录音")
    def click_quit_record(self):
        self.click(self.quit_record_button)

    # 点击暂停
    @allure.step(title="点击暂停")
    def click_pause(self):
        self.click(self.pause_button)

    # 点击完成
    @allure.step(title="点击完成")
    def click_accomplish(self):
        self.click(self.accomplish_button)

    # 点击继续
    @allure.step(title="点击继续")
    def click_continue(self):
        self.click(self.continue_button)

    # 点击保存
    @allure.step(title="点击保存")
    def click_save(self):
        self.click(self.save_button)

    # 添加书签按钮
    @allure.step(title="添加书签按钮")
    def click_add_bookmark(self):
        self.click(self.add_bookmark_button)

    # 调节增益按钮
    @allure.step(title="调节增益按钮")
    def click_gain_adjustment(self):
        self.click(self.gain_adjustment_button)

    # 选择增益
    @allure.step(title="选择增益-低")
    def select_gain_adjustment_tall(self):
        window_size = self.driver.get_window_size()
        width = window_size["width"]
        height = window_size["height"]
        TouchAction(self.driver).press(x=width*0.95, y=height*0.3).release().perform()  # 选择高

    @allure.step(title="选择增益-中")
    def select_gain_adjustment_middle(self):
        window_size = self.driver.get_window_size()
        width = window_size["width"]
        height = window_size["height"]
        TouchAction(self.driver).press(x=width * 0.95, y=height * 0.5).release().perform()  # 选择中

    @allure.step(title="选择增益-高")
    def select_gain_adjustment_low(self):
        window_size = self.driver.get_window_size()
        width = window_size["width"]
        height = window_size["height"]
        TouchAction(self.driver).press(x=width * 0.95, y=height * 0.7).release().perform()

    # 调节字体
    @allure.step(title="调节字体")
    def click_font_size(self):
        self.click(self.font_size_button)

    @allure.step(title="选择中体字")
    def select_font_size_middle(self):  # 选择中体字
        self.click(self.font_size_button_middle)

    @allure.step(title="选择大体字")
    def select_font_size_big(self):  # 选择大体字
        self.click(self.font_size_button_big)

    # 转换语言
    @allure.step(title=" 转换语言")
    def click_switch_language(self):
        self.click(self.switch_language_button)

    # 继续转写
    @allure.step(title="继续转写")
    def click_continue_transfer(self):
        self.click(self.continue_transfer_button)

    # 点击添加标签
    @allure.step(title="点击添加标签")
    def click_add_label(self):
        self.click(self.add_label_button)

    # 添加标签
    @allure.step(title="添加标签")
    def input_label_name(self,text):
        self.input(self.label_input_box,text)

    # 点击名称输入框
    @allure.step(title="点击名称输入框")
    def click_add_name(self):
        self.click(self.add_name_button)

    # 清除名称
    @allure.step(title=" 清除名称")
    def clear_add_name(self):
        self.clear(self.add_name_button)

    # 输入名称
    @allure.step(title="输入名称")
    def input_add_name(self, text):
        self.input(self.add_name_button,text)

    # 取消保存
    @allure.step(title="取消保存")
    def click_cancel_save(self):
        self.click(self.cancel_save_button)

    # 服务器连接失败点击刷新
    def server_connection_failed_click_refresh(self, feature):

        """
        出现服务器连接失败则点击刷新，如果没有结束
        :param feature: 元素的特征
        :return: 元素
        """
        while True:

            source = self.driver.page_source
            try:
                return self.find_element(feature)
            except OSError:
                if source == self.driver.page_source:
                    pass
                continue
            finally:
                break

    def select_connection_failed_click_refresh(self):
        self.server_connection_failed_click_refresh(self.server_connection_failed_click_refresh_button)

    def connection_failed_click_refresh(self):
        self.click(self.server_connection_failed_click_refresh_button)

