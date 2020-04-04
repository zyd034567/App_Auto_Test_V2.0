import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestPlayAllAudiosInMyAudio:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 反复播放录制的音频30分钟，期间进行暂停 / 恢复播放（间隔1分钟）
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_play_all_audios_in_my_audio(self):
        self.page.local_record_page.click_navigation_bar_my_document()
        self.page.local_my_document_page.click_play()
        for i in range(0,10):
            self.page.my_document_play_page.click_play_or_pause()
            time.sleep(60)
        self.page.my_document_play_page.click_return()





