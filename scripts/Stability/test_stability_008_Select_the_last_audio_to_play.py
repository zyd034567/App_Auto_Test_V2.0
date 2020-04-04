# -- coding: utf-8 --

import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestSelectTheLastAudioToPlay:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在我的文件中滑动到音频最下面，播放最后一个音频15分钟后退出
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_select_the_last_audio_to_play(self):
        self.page.local_record_page.click_navigation_bar_my_document()
        self.page.local_my_document_page.select_all_loadedy_text()
        self.page.local_my_document_page.select_audio_play()
        time.sleep(900)
        self.page.my_document_play_page.click_return_button()