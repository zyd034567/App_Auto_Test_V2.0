# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestDeleteAllAudio:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 连续删除所有录制音频
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_delete_all_audio(self):
        self.page.local_record_page.click_navigation_bar_my_document()
        for i in range(5):
            self.page.local_my_document_page.click_select()
            self.page.local_my_document_page.click_check_all()
            self.page.local_my_document_page.click_delete()
            self.page.local_my_document_page.click_confirm_delete()
