# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestStartRecording50TimesWhileRecordingAndTranslating:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在边录边译录音时，启动快速录音50次
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_start_recording_50_times_while_recording_and_translating(self):
        for i in range(50):
            self.page.local_record_page.click_navigation_bar_Translate_while_recording()
            self.page.local_translate_while_recording_page.click_confirm()
            time.sleep(5)
            for a in range(3):
                self.driver.press_keycode(170)
                self.driver.press_keycode(170)
                time.sleep(5)





