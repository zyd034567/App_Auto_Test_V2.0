# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestUploadAudioFilesToCloud:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在我的音频中批量上传录音文件到云空间
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_upload_audio_files_to_cloud(self):
        self.page.local_record_page.click_navigation_bar_my_document()
        for i in range(3):
            self.page.local_my_document_page.click_select()
            self.page.local_my_document_page.click_check_all()
            self.page.local_my_document_page.click_uploading()
            self.page.local_record_page.swipe_unlock()
