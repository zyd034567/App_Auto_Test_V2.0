# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestStartTheStandardRecordingFor10MinutesAfterStartingAIUI:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 启动AIUI10次后，启动标准模式录音10分钟。
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_start_the_standard_recording_for_10_minutes_after_starting_aiui(self):
        for i in range(10):
            self.page.AIUI_page.long_AIUI()
            time.sleep(5)
            self.page.AIUI_page.close_AIUI_button()
            time.sleep(2)
        self.page.local_record_page.click_standard()
        time.sleep(600)
        self.page.record_page.click_accomplish()
        self.page.record_page.click_save()




