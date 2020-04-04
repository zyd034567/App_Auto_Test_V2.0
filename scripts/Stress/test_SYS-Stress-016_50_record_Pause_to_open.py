# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestRecordPauseToOpen:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 开启录音后马上暂停并恢复录音，重复50次
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_record_pause_to_open_50(self):
        for i in range(50):
            self.page.local_record_page.click_standard()
            self.page.record_page.click_pause()
            self.page.record_page.click_continue()
            self.page.record_page.click_accomplish()
            self.page.record_page.click_save()





