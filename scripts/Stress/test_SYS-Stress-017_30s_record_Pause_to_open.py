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

    # 录音30分钟的过程中反复暂停 / 恢复录音（间隔30秒）
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_record_pause_to_open_30s(self):
        self.page.local_record_page.click_standard()
        for i in range(60):
            self.page.record_page.click_pause()
            time.sleep(30)
            self.page.record_page.click_continue()
        self.page.record_page.click_accomplish()
        self.page.record_page.click_save()





