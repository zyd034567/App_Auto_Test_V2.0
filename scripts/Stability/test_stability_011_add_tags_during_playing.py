# coding=utf-8
import time
import pytest
from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestAddTagsDuringPlaying:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 播放已录制的音频，播放中插入标签并命名
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_add_tags_during_playing(self):
        data = ["标准模式0","标准模式1","标准模式2","标准模式3","标准模式4"]
        self.page.local_record_page.click_navigation_bar_my_document()
        self.page.local_my_document_page.click_play_one()
        for a in range(5):
            for i in data:
                self.page.my_document_play_page.click_add_label_play()
                self.page.my_document_play_page.input_label_name_play(i)
        self.page.my_document_play_page.click_return_button()
