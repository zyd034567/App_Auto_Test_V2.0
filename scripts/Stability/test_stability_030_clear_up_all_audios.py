# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestClearUpAllAudios:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 删除录制的音频文件
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_clear_up_all_audios(self):
        self.page.local_record_page.click_navigation_bar_my_document()
        self.page.local_my_document_page.click_select()
        for i in range(5):
            self.page.local_record_page.swipe_unlock()
            time.sleep(2)
        self.page.local_my_document_page.click_check_all()
        self.page.local_my_document_page.click_delete()
        self.page.local_my_document_page.click_confirm_delete()

