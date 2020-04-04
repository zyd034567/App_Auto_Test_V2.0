# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestBlueToothSwitchTimes:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 点击蓝牙开关50次
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_blue_tooth_switch_50_times(self):
        self.page.local_record_page.drop_down_shortcuts()
        for i in range(50):
            self.page.local_record_page.click_blue_tooth()
            time.sleep(1)
