import time

import allure
import pytest

from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # 登陆听见账号 - 关闭自动上传设置
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_login(self):
        self.page.local_record_page.click_navigation_bar_mine()
        self.page.local_my_page.click_Information_portal()
        self.page.personal_information_page.click_log_out()
        self.page.personal_information_page.click_personal_confirm()
        user_name = 15737523750
        password = 'yc111111'
        self.page.login_page.switch_login_mode()
        self.page.login_page.input_phone(user_name)
        self.page.login_page.input_password(password)
        self.page.login_page.click_login()
        # self.driver.get_screenshot_as_file("./screenshot/xxx.png")
        # with open("./screenshot/xxx.png", 'rb') as f:
        #     allure.attach('描述', f.read(), allure.attach_type.PNG)

        allure.attach("登录截图：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)
        # self.page.login_page.is_login_enabled()

