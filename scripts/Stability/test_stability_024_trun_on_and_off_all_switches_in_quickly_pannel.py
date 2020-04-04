# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestTrunOnAndOffAllSwitchesInQuicklyPannel:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在标准模式下录音30分钟，通过快捷开关，打开和关闭Wifi
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_trun_on_and_off_all_switches_in_quickly_pannel(self):
        self.page.local_record_page.click_standard()
        time.sleep(10)
        self.page.local_record_page.drop_down_shortcuts()
        for a in range(30):
            self.page.local_record_page.click_network()
            time.sleep(60)
        self.page.local_record_page.quit_shortcuts()
        self.page.record_page.click_accomplish()
        self.page.record_page.click_save()
