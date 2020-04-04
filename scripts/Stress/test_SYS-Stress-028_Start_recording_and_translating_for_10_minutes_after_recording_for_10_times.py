# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestStartRecordingAndTranslatingFor10MinutesAfterRecordingFor10Times:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 启动快速录音10次后，启动边录边译录音10分钟。
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_start_recording_and_translating_for_10_minutes_after_recording_for_10_times(self):
        for i in range(20):
            self.driver.press_keycode(170)
            self.driver.press_keycode(170)
            time.sleep(5)
        self.page.local_record_page.click_navigation_bar_Translate_while_recording()
        self.page.local_translate_while_recording_page.click_confirm()
        time.sleep(600)
        self.page.record_page.click_save()
        self.page.record_page.click_save()




