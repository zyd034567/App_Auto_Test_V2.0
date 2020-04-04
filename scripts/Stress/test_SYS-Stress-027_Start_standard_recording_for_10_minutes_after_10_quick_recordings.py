# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestStartStandardRecordingFor10MinutesAfter10QuickRecordings:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 启动快速录音10次后，启动标准模式录音10分钟。
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_start_standard_recording_for_10_minutes_after_10_quick_recordings(self):
        for i in range(20):
            self.driver.press_keycode(170)
            self.driver.press_keycode(170)
            time.sleep(5)
        self.page.local_record_page.click_standard()
        time.sleep(600)
        self.page.record_page.click_accomplish()
        self.page.record_page.click_save()




