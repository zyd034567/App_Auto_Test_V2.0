import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LoginPage(BaseAction):
    # 听见账号登录按钮
    switch_login_mode_button =By.XPATH, "//*[@text='听见账号登录']"
    # 账号输入框
    phone_edit_text = By.ID, "com.iflyrec.smartrecorder:id/login_password_phone"
    # 密码输入框
    password_edit_text = By.ID, "com.iflyrec.smartrecorder:id/login_password_password"
    # 登录按钮
    login_button = By.ID, "com.iflyrec.smartrecorder:id/login_password_make_sure"
    # 显示密码按钮
    show_password_button = By.ID, "com.iflyrec.smartrecorder:id/btn_psd_clear"

    # 切换听见账号登录
    @allure.step(title="切换听见账号登录")
    def switch_login_mode(self):
        self.click(self.switch_login_mode_button)

    # 输入账号
    @allure.step(title="输入账号")
    def input_phone(self, text):
        self.click(self.phone_edit_text)
        self.clear(self.phone_edit_text)
        allure.attach('输入内容', text, allure.attach_type.TEXT)
        self.input(self.phone_edit_text, text)

    # 输入密码
    @allure.step(title="输入密码")
    def input_password(self, text):
        self.click(self.password_edit_text)
        allure.attach('输入内容', text, allure.attach_type.TEXT)
        self.input(self.password_edit_text, text)

    # 点击登录
    @allure.step(title="点击点击登录")
    def click_login(self):
        self.click(self.login_button)

    @allure.step(title='登录注册 - 点击显示密码')
    def click_show_password(self):
        self.click(self.show_password_button)

    def is_login_success(self, content):
        """
        根据toast的部分内容，判断是否提示登录成功
        :param content:
        :return:
        """
        try:
            self.find_toast(content)
            return True
        except Exception:
            return False

    def is_login_enabled(self):
        """
        判断 登录按钮中的 enabled 属性值 是不是 可用的
        true 表示可用
        false 表示不可用
        :return: 是否可用
        """
        return self.find_element(self.login_button).get_attribute("enabled") == "true"

        # if self.find_element(self.login_button).get_attribute("enabled") == "true":
        #     return True
        # else:
        #     return False

    def is_password_exist(self, password):
        """
        根据传入的密码，判断是否和密码框上的密码一致
        :param password: 传入的密码
        :return: 是否一致
        """
        return self.find_element(self.password_edit_text).text == password

        # try:
        #     self.find_element((By.XPATH, "//*[@text='" + password + "']"))
        #     return True
        # except:
        #     return False


