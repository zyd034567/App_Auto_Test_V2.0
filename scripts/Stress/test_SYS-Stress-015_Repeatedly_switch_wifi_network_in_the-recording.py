# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestRepeatedlySwitchWifiNetworkInIheRecording:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在录音30分钟的过程中，反复在2个wifi网络中进行切换（间隔1分钟）
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_repeatedly_switch_wifi_network_in_the_recording(self):
        password = "myoffice"
        self.page.local_record_page.click_standard()
        self.page.local_record_page.drop_down_shortcuts()
        self.page.local_record_page.click_seeting()
        time.sleep(2)
        self.page.settings_page.click_network_settings()
        time.sleep(2)
        for i in range(5):
            self.page.settings_network_page.click_new_wifi_network()
            self.page.settings_network_page.input_password_entry_box(password)
            time.sleep(60)
            self.page.settings_network_page.click_new_wifi_network_yeacen()
            time.sleep(60)
        self.driver.press_keycode(170)
        self.driver.press_keycode(170)






