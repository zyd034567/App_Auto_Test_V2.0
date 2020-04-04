import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestSearchTagsAndPlayAudios:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 搜索录音文件名，播放
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_search_tags_and_play_audios(self):
        self.page.local_record_page.click_navigation_bar_my_document()
        self.page.local_my_document_page.click_search()
        self.page.my_document_search_page.click_search_text()
        self.page.my_document_search_page.enter_search_text("标准")
        self.page.my_document_search_page.click_search_result()







        
