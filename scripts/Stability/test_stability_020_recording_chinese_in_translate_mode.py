# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestRecordingChineseInTranslateMode:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在主屏进入边录边译，点击英文录制音频30分钟
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_recording_chinese_in_translate_mode(self):
        self.page.local_record_page.click_navigation_bar_Translate_while_recording()
        self.page.local_translate_while_recording_page.click_confirm()
        for i in range(3):
            time.sleep(602)
            self.page.record_translate_while_recording_page.click_continue_transfer()
        self.page.record_page.click_save()
        self.page.record_page.click_save()





