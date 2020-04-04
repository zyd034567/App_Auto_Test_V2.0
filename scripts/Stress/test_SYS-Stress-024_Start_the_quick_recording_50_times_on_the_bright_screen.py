# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestStartTheQuickRecording50TimesOnTheBrightScreen:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在主屏亮屏状态下，启动快速录音50次
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_start_the_quick_recording_50_times_on_the_bright_screens(self):
        for i in range(50):
            self.driver.press_keycode(170)
            self.driver.press_keycode(170)
            time.sleep(10)
            self.driver.press_keycode(170)
            self.driver.press_keycode(170)
            time.sleep(2)






