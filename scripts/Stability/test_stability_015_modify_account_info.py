import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestModifyAccountInfo:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在主屏进入账号信息，修改账号信息
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_modify_account_info(self):
        self.page.local_record_page.click_navigation_bar_mine()
        self.page.local_my_page.click_Information_portal()
        self.page.personal_information_page.recompose_nickname("张三")
        self.page.personal_information_page.change_the_gender()

        self.page.personal_information_page.click_birthday()
        self.page.personal_information_page.select_birthday()
        self.page.personal_information_page.click_submit()

        self.page.personal_information_page.click_district()
        self.page.personal_information_page.select_district()
        self.page.personal_information_page.click_submit()

        self.page.personal_information_page.click_profession()
        self.page.personal_information_page.select_solicitor()
        self.page.personal_information_page.click_return()

        self.page.personal_information_page.click_return()
        self.page.personal_information_page.click_personal_confirm()




