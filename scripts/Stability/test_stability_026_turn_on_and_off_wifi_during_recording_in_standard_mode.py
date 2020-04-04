# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestTurnOnAndOffWifiDuringRecordingInStandard:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在标准模式下录音30分钟，录音过程中呼出系统设置并进入wifi设置，打开和关闭wifi(间隔5分钟）
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_turn_on_and_off_wifi_during_recording_in_standard(self):

        self.page.local_record_page.click_standard()
        self.page.local_record_page.drop_down_shortcuts()
        self.page.local_record_page.click_seeting()
        self.page.settings_page.click_network_settings()
        for a in range(0,60):
            self.page.settings_network_page.click_WiFi_network()
            time.sleep(300)
        self.page.settings_network_page.click_WiFi_network()
        self.page.settings_network_page.click_return()
        self.page.settings_network_page.click_return()
        self.page.record_page.click_accomplish()
        self.page.record_page.click_save()
