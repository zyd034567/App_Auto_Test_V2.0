# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestStandardRecord:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 点击标准录音录制50个
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_standard_record(self):
        for i in range(50):
            self.page.local_record_page.click_standard()
            time.sleep(2)
            for a in range(3):
                self.page.record_page.select_connection_failed_click_refresh()
                self.page.record_page.connection_failed_click_refresh()
            time.sleep(60)
            self.page.record_page.click_accomplish()
            self.page.record_page.click_save()
            self.page.local_record_page.click_navigation_bar_record()
