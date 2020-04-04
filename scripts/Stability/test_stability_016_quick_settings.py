import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestQuickSettings:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在主屏呼出快捷开关，打开 / 关闭所有开关
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_quick_settings(self):
        self.page.local_record_page.drop_down_shortcuts()
        for i in range(10):
            self.page.local_record_page.click_network()
            self.page.local_record_page.click_network()
            self.page.local_record_page.click_blue_tooth()
            self.page.local_record_page.click_power_saving()
        self.page.local_record_page.quit_shortcuts()










        


