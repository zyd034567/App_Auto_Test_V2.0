import allure
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class SeettingNetworkPage(BaseAction):
    mobile_network_button = By.ID, "com.android.settings:id/rl_setting_datatraffic"
    wifi_network_button = By.ID, "com.android.settings:id/switchbar"
    # 切换wifiAP, #选择奕辰WiFi
    new_wifi_network_yeacen = By.XPATH, "//*[contains(@text,'yeacen')]"
    new_wifi_network_MWFS = By.XPATH, "//*[contains(@text,'MWFS')]"

    password_entry_box = By.ID, "com.android.settings:id/password"
    submit_password = By.ID, "android:id/button1"    #"对号"
    close_password = By.ID, "android:id/button2"    #"错号"

    # 移动网络开关按钮
    @allure.step(title="点击移动网络开关按钮")
    def click_mobile_network(self):
        self.click(self.mobile_network_button)

    # WiFi开关按钮
    @allure.step(title="点击WiFi开关按钮")
    def click_wifi_network(self):
        self.click(self.wifi_network_button)

    # 点击奕辰WiFi名称
    @allure.step(title="点击奕辰WiFi名称")
    def click_new_wifi_network_yeacen(self):
        self.click(self.new_wifi_network_yeacen)

    # 点击"MWFS" wifi名称
    @allure.step(title="点击'MWFS'wifi名称")
    def click_new_wifi_network_MWFS(self):
        self.click(self.new_wifi_network_MWFS)

    # 输入提交密码
    @allure.step(title="输入提交密码")
    def input_password_entry_box(self,text):
        self.click(self.password_entry_box)
        allure.attach('输入内容', text, allure.attach_type.TEXT)
        self.input(self.password_entry_box, text)
        self.click(self. submit_password)

    # 点击返回
    @allure.step(title="点击返回")
    def click_return (self):
        TouchAction(self.driver).press(x=36, y=110).release().perform()


