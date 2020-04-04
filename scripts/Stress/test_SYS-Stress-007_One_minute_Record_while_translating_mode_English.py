# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestRecordWhileTranslatingModeEnglish:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在主屏进入边录边译，点击英文录制音频1分钟，连续录制50个
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_one_minute_record_while_translating_mode_english(self):
        for i in range(50):
            self.page.local_record_page.click_navigation_bar_Translate_while_recording()
            self.page.local_translate_while_recording_page.click_replace()
            time.sleep(60)
            self.page.record_page.click_accomplish()
            self.page.record_page.click_save()
            self.page.record_page.click_save()
            self.page.local_record_page.click_navigation_bar_record()
