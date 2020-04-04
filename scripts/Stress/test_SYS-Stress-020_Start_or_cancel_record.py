# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestStartOrCancelRecord:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 开启录音后快速取消录音，重复50次
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_start_or_cancel_record(self):
        for i in range(50):
            self.page.local_record_page.click_standard()
            self.page.record_page.click_return()
            self.page.record_page.click_quit_record()
            time.sleep(1)





