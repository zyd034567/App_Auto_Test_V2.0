import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestCheckAllSettings:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在主屏进入系统设置，遍历所有设置菜单
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_check_all_settings(self):
        self.page.local_record_page.drop_down_shortcuts()
        self.page.local_my_page.click_setting()
        self.page.settings_page.click_network_settings()
        self.page.settings_page.click_return()
        self.page.settings_page.click_blue_tooth()
        self.page.settings_page.click_return()
        self.page.settings_page.click_inform()
        self.page.settings_page.click_return()
        self.page.settings_page.click_time()
        self.page.settings_page.click_return()
        self.page.settings_page.click_batteries_and_storage()
        self.page.settings_page.click_return()
        self.page.settings_page.click_privacy_and_security()
        self.page.settings_page.click_return()
        self.page.settings_page.click_about_the_machine()
        self.page.settings_page.click_return()
        self.page.settings_page.click_return()






