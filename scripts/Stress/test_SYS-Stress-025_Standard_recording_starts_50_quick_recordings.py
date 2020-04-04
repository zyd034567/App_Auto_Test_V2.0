# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestStandardRecordingStarts50QuickRecordings:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在标准模式录音时，启动快速录音50次
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_standard_recording_starts_50_quick_recordings(self):
        for i in range(50):
            self.page.local_record_page.click_standard()
            time.sleep(5)
            self.driver.press_keycode(170)
            self.driver.press_keycode(170)
            time.sleep(5)
            self.driver.press_keycode(170)
            self.driver.press_keycode(170)
            time.sleep(2)
            self.page.local_record_page.click_navigation_bar_recor()





