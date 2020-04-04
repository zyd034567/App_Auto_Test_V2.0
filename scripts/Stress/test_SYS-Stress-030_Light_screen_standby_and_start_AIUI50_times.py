# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLightScreenStandbyAndStartAIUI50Times:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在亮屏待机状态下，启动AIUI50次
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_light_screen_standby_and_start_aiui_50_times(self):
        for i in range(50):
            self.page.AIUI_page.long_AIUI()
            time.sleep(5)
            # self.page.AIUI_page.close_AIUI_button()
            # time.sleep(2)




