import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestChangeWifiInSettings:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在主屏进入系统设置，切换wifiAP
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_change_wifi_in_settings(self):
        password = "myoffice"
        self.page.local_record_page.click_navigation_bar_mine()
        self.page.local_my_page.click_setting()
        self.page.settings_page.click_network_settings()
        time.sleep(2)
        self.page.settings_network_page.click_new_wifi_network()
        self.page.settings_network_page.input_password_entry_box(password)
        time.sleep(2)
        self.page.settings_page.click_return()
        self.page.settings_page.click_return()


