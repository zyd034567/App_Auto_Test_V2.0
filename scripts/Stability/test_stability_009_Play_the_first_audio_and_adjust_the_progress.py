# coding=utf-8
import time
import pytest
from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestPlayTheFirstAudioAndAdjustTheProgress:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在我的文件中播放第一个音频，播放5分钟后调节播放进度3次，继续播放5分钟后退出
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_play_the_first_audio_and_adjust_the_progress(self):
        self.page.local_record_page.click_navigation_bar_my_document()
        self.page.local_my_document_page.select_audio_play()
        time.sleep(300)
        for i in range(3):
            self.page.my_document_play_page.adjust_audio_speed_right()
            time.sleep(2)
            self.page.my_document_play_page.adjust_audio_speed_left()
        time.sleep(300)
        self.page.my_document_play_page.click_return_button()
