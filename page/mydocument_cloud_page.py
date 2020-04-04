# -- coding: utf-8 --
import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MyDocumentCloudPage(BaseAction):

    # 云空间界面按钮
    return_button = By.ID, "com.iflyrec.smartrecorder:id/tv_left"
    continue_button = By.XPATH, "//*[@text='继续上传']"
    pause_button = By.XPATH, "//*[@text='全部暂停']"
    empty_button = By.XPATH, "//*[@text='清空']"

    # 返回按钮
    @allure.step(title="点击返回按钮")
    def click_return(self):
        self.click(self.return_button)

    # 继续上传按钮
    @allure.step(title="点击继续上传按钮")
    def click_continue(self):
        self.click(self.continue_button)

    # 全部暂停按钮
    @allure.step(title="点击全部暂停按钮")
    def click_pause(self):
        self.click(self.pause_button)

    # 清空按钮
    @allure.step(title="点击清空按钮")
    def click_empty(self):
        self.click(self.empty_button)




