import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestStandardRecordingWithAdjustableGainRangeRor10Minutes:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 启动标准模式下录音，调节增益幅度，每个幅度下录音10分钟
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_standard_recording_with_adjustable_gain_range_for_10_minutes(self):
        self.page.local_record_page.click_standard()
        time.sleep(600)
        self.page.record_page.click_gain_adjustment()
        self.page.record_page.select_gain_adjustment_tall()
        time.sleep(600)
        self.page.record_page.select_gain_adjustment_low()
        time.sleep(600)
        self.driver.press_keycode(170)
        self.driver.press_keycode(170)










