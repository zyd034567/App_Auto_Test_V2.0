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

    # 所有录音文件全选上传到云空间
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def testall_upload_cloud_space(self):
        self.page.local_record_page.click_navigation_bar_my_document()
        self.page.local_my_document_page.click_select()
        for i in range(5):
            self.page.local_record_page.swipe_unlock()
            time.sleep(2)
        self.page.local_my_document_page.click_check_all()
        self.page.local_my_document_page.click_uploading()

