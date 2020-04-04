# -- coding: utf-8 --
import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LocalMyPage(BaseAction):

    # 个人信息入口
    Information_portal_button = By.ID, "com.iflyrec.smartrecorder:id/my_account_name"

    transfer_button = By.XPATH, "//*[@text='转写设置']"
    help_button = By.XPATH, "//*[@text='帮助与反馈']"
    service_button = By.XPATH, "//*[@text='联系客服']"
    versions_button = By.XPATH, "//*[@text='关于录音笔']"
    setting_button = By.ID, "com.iflyrec.smartrecorder:id/iv_setting"
    cloud_button = By.XPATH, "//*[@text='我的云空间']"
    information_button = By.ID, "com.iflyrec.smartrecorder:id/my_account_name"



    # 点击个人信息入口
    @allure.step(title="点击个人信息入口")
    def click_Information_portal(self):
        self.click(self.Information_portal_button)

    # 转写设置按钮
    @allure.step(title="点击转写设置按钮")
    def click_transfer(self):
        self.click(self.transfer_button)

    # 帮助与反馈按钮
    @allure.step(title="点击帮助与反馈按钮")
    def click_help(self):
        self.click(self.help_button)

    # 联系客服按钮
    @allure.step(title="点击联系客服按钮")
    def click_service(self):
        self.click(self.service_button)

    # 关于录音笔按钮
    @allure.step(title="点击关于录音笔按钮")
    def click_versions(self):
        self.click(self.versions_button)

    # 系统设置图标按钮
    @allure.step(title="点击系统设置图标按钮")
    def click_setting(self):
        self.click(self.setting_button)

    # 我的云空间按钮
    @allure.step(title="点击我的云空间按钮")
    def click_cloud(self):
        self.click(self.cloud_button)

    # 个人信息按钮
    @allure.step(title="点击个人信息按钮")
    def click_information(self):
        self.click(self.information_button)

