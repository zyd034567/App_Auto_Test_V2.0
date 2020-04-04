# -- coding: utf-8 --
import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LocalTranslateWhileRecordingPage(BaseAction):

    # 边录边译本地按钮
    replace_button = By.ID, "com.iflyrec.smartrecorder:id/translate_change_btn"
    confirm_button = By.XPATH, "//*[@text='确定']"

    # 切换按钮
    @allure.step(title="点击切换按钮")
    def click_replace(self):
        self.click(self.replace_button)

    # 确定按钮
    @allure.step(title="点击确定按钮")
    def click_confirm(self):
        self.click(self.confirm_button)





