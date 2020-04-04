# -- coding: utf-8 --
import allure

from base.base_action import BaseAction
from selenium.webdriver.common.by import By


class RecordTranslateWhileRecordingPage(BaseAction):
    return_button = By.ID, "com.iflyrec.smartrecorder:id/tv_left"
    cancel_record_button = By.ID, "com.iflyrec.smartrecorder:id/dialog_remind_cancel"
    quit_record_button = By.XPATH, "//*[@text='退出']"
    accomplish_button = By.XPATH, "//*[@text='完成']"
    pause_button = By.XPATH, "//*[@text='暂停']"
    Continue_button = By.XPATH, "//*[@text='继续']"
    continue_transfer_button = By.ID, "com.iflyrec.smartrecorder:id/notice_top_forward_btn"
    add_label_button = By.CLASS_NAME, "android.widget.EditText"
    add_name_button = By.CLASS_NAME, "android.widget.ImageView"
    save_button = By.XPATH, "//*[@text='保存']"
    cancel_save_button = By.XPATH, "//*[@text='取消']"

    # 返回按钮
    @allure.step(title="点击返回按钮")
    def click_return(self):
        self.click(self.return_button)

    # 取消录音
    @allure.step(title="取消录音")
    def click_cancel_record(self):
        self.click(self.cancel_record_button)

    # 退出录音
    @allure.step(title="退出录音")
    def click_quit_record(self):
        self.click(self.quit_record_button)

    # 继续转写
    @allure.step(title="继续转写")
    def click_continue_transfer(self):
        self.click(self.continue_transfer_button)

    # 点击完成
    @allure.step(title=" 点击完成")
    def click_accomplish(self):
        self.click(self.accomplish_button)

    # 点击保存
    @allure.step(title="点击保存")
    def click_save(self):
        self.click(self.save_button)

    # 添加标签
    @allure.step(title=" 添加标签")
    def input_label(self, text):
        allure.attach('输入内容', text, allure.attach_type.TEXT)
        self.input(self.add_label_button, text)

    # 清除名称
    @allure.step(title="清除名称")
    def clear_name(self, text):
        self.clear(self.add_name_button, text)

    # 输入名称
    @allure.step(title="输入名称")
    def input_name(self, text):
        allure.attach('输入内容', text, allure.attach_type.TEXT)
        self.input(self.add_name_button, text)

    # 取消保存
    @allure.step(title="取消保存")
    def click_cancel_save(self):
        self.click(self.cancel_save_button)


