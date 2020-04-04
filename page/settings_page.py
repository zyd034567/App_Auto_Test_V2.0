import allure
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class SeettingPage(BaseAction):
    network_settings_button = By.XPATH, "//*[@text='网络设置']"
    blue_tooth_button = By.XPATH, "//*[@text='蓝牙']"
    inform_button = By.XPATH, "//*[@text='通知']"
    time_settings_button = By.XPATH, "//*[@text='时间设置']"
    batteries_and_storage_button = By.XPATH, "//*[@text='电池与储存']"
    privacy_and_security_button = By.XPATH, "//*[@text='隐私与安全']"
    about_the_machine_button = By.XPATH, "//*[@text='关于本机']"

    # 网络设置按钮
    @allure.step(title="点击网络设置按钮")
    def click_network_settings(self):
        self.click(self.network_settings_button)

    # 蓝牙按钮
    @allure.step(title="点击蓝牙按钮")
    def click_blue_tooth(self):
        self.click(self.blue_tooth_button)

    # 通知按钮
    @allure.step(title="点击通知按钮")
    def click_inform(self):
        self.click(self.inform_button)

    # 时间设置按钮
    @allure.step(title="点击时间设置按钮")
    def click_time(self):
        self.click(self.time_settings_button)

    # 电池与储存按钮
    @allure.step(title="点击电池与储存按钮")
    def click_batteries_and_storage(self):
        self.click(self.batteries_and_storage_button)

    # 隐私与安全按钮
    @allure.step(title="点击隐私与安全按钮")
    def click_privacy_and_security(self):
        self.click(self.privacy_and_security_button)

    # 关于本机按钮
    @allure.step(title="点击关于本机按钮")
    def click_about_the_machine(self):
        self.click(self.about_the_machine_button)

    # 点击返回
    @allure.step(title="点击返回")
    def click_return (self):
        TouchAction(self.driver).press(x=36, y=110).release().perform()


