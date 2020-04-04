# -- coding: utf-8 --

import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestMusicRecord:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 音乐模式下录音30分钟并保存
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(("name", "label"), analyze_file("record_data", "test_music_record"))
    def test_music_record(self, name, label):
        self.page.local_record_page.click_music()
        time.sleep(1800)
        self.page.record_page.click_accomplish()
        self.page.record_page.click_add_name()
        self.page.record_page.clear_add_name()
        self.page.record_page.input_add_name(name)
        self.page.record_page.click_add_label()
        self.page.record_page.input_label_name(label)
        self.page.record_page.click_save()







