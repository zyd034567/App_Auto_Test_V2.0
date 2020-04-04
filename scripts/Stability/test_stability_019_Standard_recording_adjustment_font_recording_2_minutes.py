import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestStandardRecordingAdjustmentFontRecording2Minutes:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 启动标准模式下录音，调节显示字体，调节字体大后录音2分钟；再调节字体小后录音2分钟。
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_standard_recording_adjustment_font_recording_2_minutes(self):
        self.page.local_record_page.click_standard()
        time.sleep(120)
        self.page.record_page.click_font_size()
        for i in range(5):
            self.page.record_page.select_font_size_big()
            time.sleep(120)
            self.page.record_page.select_font_size_middle()
            time.sleep(120)
        self.driver.press_keycode(170)
        self.driver.press_keycode(170)










