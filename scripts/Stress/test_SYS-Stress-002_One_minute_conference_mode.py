# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestConferenceRecord:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 点击会议录音录制50个
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_conference_record(self):
        for i in range(50):
            self.page.local_record_page.click_conference()
            time.sleep(60)
            self.page.record_page.click_accomplish()
            self.page.record_page.click_save()
            self.page.local_record_page.click_navigation_bar_record()
