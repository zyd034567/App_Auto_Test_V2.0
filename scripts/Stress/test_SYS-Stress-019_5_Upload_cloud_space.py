# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestAllUploadCloudSpace:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 选中5个录音文件（30分钟），反复上传云空间50次（间隔1分钟）
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_5_upload_cloud_space(self):
        self.page.local_record_page.click_navigation_bar_my_document()
        for i in range(50):
            self.page.my_document_play_page.click_select()
            self.page.my_document_play_page.click_check_all()
            self.page.my_document_play_page.click_play_one()
            self.page.my_document_play_page.click_play_two()
            self.page.my_document_play_page.click_play_three()
            self.page.my_document_play_page.click_play_four()
            self.page.local_record_page.swipe_unlock()
            self.page.my_document_play_page.click_play_five()
            self.page.my_document_play_page.click_uploading()
            time.sleep(60)
