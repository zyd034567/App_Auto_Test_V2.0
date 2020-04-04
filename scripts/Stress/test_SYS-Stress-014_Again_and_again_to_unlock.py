# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestAgainAndAgainToUnlock:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 录音30分钟的过程中反复灭屏 / 亮屏解锁（间隔10秒）
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_again_and_again_to_unlock(self):
        self.page.local_record_page.click_standard()
        for i in range(180):
            self.driver.press_keycode(26)
            time.sleep(2)
            self.driver.press_keycode(26)
            self.page.local_record_page.swipe_unlock()
            time.sleep(1)
            self.page.local_record_page.swipe_unlock()
            for i in range(4):
                self.page.local_record_page.click_enter_password_to_unlock()
            time.sleep(10)
        self.page.record_page.click_accomplish()
        self.page.record_page.click_save()






