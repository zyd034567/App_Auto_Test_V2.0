# coding=utf-8
import time
import pytest
from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestPlayTheSecondAudioToEditTheMessage:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在我的文件中播放第二个音频，编辑音频信息，添加标签，修改音频文件名称。
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_play_the_second_audio_to_edit_the_message(self):
        self.page.local_record_page.click_navigation_bar_my_document()
        self.page.local_my_document_page.slide_the_second_audio_to_the_left()
        self.page.local_my_document_page.click_redact_button_one()
        self.page.local_my_document_page.click_name_button_one("张三")
        self.page.local_my_document_page.click_input_name_button_one("张三")
        self.page.local_my_document_page.click_save_button_one()



