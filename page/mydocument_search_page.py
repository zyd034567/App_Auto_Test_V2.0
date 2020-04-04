# -- coding: utf-8 --
import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MyDocumentSearchPage(BaseAction):

    # 搜索界面界面按钮
    search_input_box = By.ID, "com.iflyrec.smartrecorder:id/customedittext_search"
    cancel_button = By.XPATH, "//*[@text='取消']"
    search_button = By.XPATH, "//*[@text='搜索文件']"
    # 搜索结果
    search_result = By.XPATH, "//*[contains(@text,'aac')]"
    # "搜索文本后"X"符号"
    empty_button = By.ID, "	com.iflyrec.smartrecorder:id/iv_clear"

    # 系统设置刷新按钮
    system_setup_refresh_button = By.ID, "com.iflyrec.smartrecorder:id/btn_refresh"
    # 历史记录删除按钮
    deletion_record_button = By.ID, "com.iflyrec.smartrecorder:id/btn_delete"
    # 文件标签进入详情页按钮"＞"
    file_tabs_button = By.ID, "com.iflyrec.smartrecorder:id/btn_more"
    # file_tabs_button = By.XPATH, "//*[(@resource-id,'com.iflyrec.smartrecorder:id/btn_more')]"
    All_tags_button = By.XPATH, "//*[contains(@text,'快乐')]"




    # 点击搜索文字
    @allure.step(title="点击搜索文字")
    def click_search_text (self):
        self.click(self.search_input_box)

    @allure.step(title="输入搜索文本")
    def enter_search_text (self,text):
        allure.attach('输入内容', text, allure.attach_type.TEXT)
        self.input(self.search_input_box, text)

    # 点击搜索结果
    @allure.step(title="点击搜索结果")
    def click_search_result(self):
        self.click(self.search_result)

    # 取消按钮
    @allure.step(title="点击取消按钮")
    def click_cancel(self):
        self.click(self.cancel_button)

    # 全部暂停按钮
    @allure.step(title="全部暂停按钮")
    def click_search(self):
        self.click(self.search_button)

    # 清空按钮
    @allure.step(title="点击清空按钮")
    def click_empty(self):
        self.click(self.empty_button)

    # 点击系统刷新
    @allure.step(title="点击系统刷新")
    def click_system_setup_refresh(self):
        self.click(self.system_setup_refresh_button)

    # 点击历史记录删除按钮
    @allure.step(title="点击历史记录删除按钮")
    def click_deletion_record(self):
        self.click(self.deletion_record_button)



    # 文件标签进入详情页按钮"＞"
    @allure.step(title="点击文件标签进入详情页按钮'＞'")
    def click_file_tabs(self):
        self.click(self.file_tabs_button)

    # 点击标签
    @allure.step(title="点击标签")
    def click_tags_text(self):
        self.click(self.All_tags_button)