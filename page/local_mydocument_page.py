# -- coding: utf-8 --
import time

import allure
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LocalMyDocumentPage(BaseAction):

    # 我的文件本地按钮
    # 第1个音频路径
    one_audio_file = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup"
    # 第2个音频路径
    two_audio_file = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup"
    # 第3个音频路径
    three_audio_file = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup"
    # 第4个音频路径
    four_audio_file = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.view.ViewGroup"
    # 第5个音频路径
    five_audio_file = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.view.ViewGroup"

    # 单个音频处理
    classify_button_one = By.XPATH, "//*[@text='分类']"
    redact_button_one = By.XPATH, "//*[@text='编辑']"
    delete_button_one = By.XPATH, "//*[@text='删除']"

    # 音频编辑弹窗
    name_button_one = By.ID, "com.iflyrec.smartrecorder:id/editName"   #初始弹窗
    input_name_button_one = By.ID, "com.iflyrec.smartrecorder:id/click_to_add_label_layout"   #添加第一个标签
    input_name_button_box_one = By.ID, "com.iflyrec.smartrecorder:id/edit_label_name"   #第一个标签输入框
    save_button_one = By.XPATH, "//*[@text='保存']"
    cancel_button_one = By.XPATH, "//*[@text='取消']"

    select_audio_button = By.XPATH, "//*[contains(@text,'.aac')]" #选择音频
    # 音频处理":"的处理
    select_button = By.ID, "com.iflyrec.smartrecorder:id/file_management"
    cancel_button = By.XPATH, "//*[@text='取消']"
    check_all_button = By.XPATH, "//*[@text='全选']"
    uploading_button = By.XPATH, "//*[@text='上传']"
    delete_button = By.XPATH, "//*[@text='删除']"

    # 删除文件弹窗
    cancel_delete_button = By.ID, "com.iflyrec.smartrecorder:id/dialog_remind_cancel"
    confirm_delete_button = By.ID, "com.iflyrec.smartrecorder:id/dialog_remind_confirm"

    # 搜索"放大镜"按钮
    search_button = By.ID, "com.iflyrec.smartrecorder:id/file_search"
    # 云空间按钮
    cloud_button = By.ID, "com.iflyrec.smartrecorder:id/upload_to_cloud_space"

    # 全部文件按钮
    classify_button = By.XPATH, "//*[@text='全部文件']"

    all_loadedy_text = By.XPATH, "//*[@text='已全部加载完']"


    # 点击播放第1个音频
    @allure.step(title="点击播放第1个音频")
    def click_play_one(self):
        self.click(self.one_audio_file)

    # 点击播放第2个音频
    @allure.step(title="点击播放第2个音频")
    def click_play_two(self):
        self.click(self.two_audio_file)

    # 点击播放第3个音频
    @allure.step(title="点击播放第3个音频")
    def click_play_three(self):
        self.click(self.three_audio_file)

    # 点击播放第4个音频
    @allure.step(title="点击播放第4个音频")
    def click_play_four(self):
        self.click(self.four_audio_file)

    # 点击播放第5个音频
    @allure.step(title="点击播放第5个音频")
    def click_play_five(self):
        self.click(self.five_audio_file)

    # 向左滑动第二个音频
    @allure.step(title="向左滑动第二个音频")
    def slide_the_second_audio_to_the_left(self):
        TouchAction(self.driver).press(x=430, y=380).move_to(x=200, y=380).release().perform()

    # 单个音频处理
    @allure.step(title="点击音频分类")
    def click_classify_button_one(self):   # 音频分类
        self.click(self.classify_button_one)

    @allure.step(title="点击音频编辑")
    def click_redact_button_one(self):   # 音频编辑
        self.click(self.redact_button_one)

    @allure.step(title="点击名称编辑")
    def click_name_button_one(self,text):  # 名称编辑
        self.click(self.name_button_one)
        self.clear(self.name_button_one)
        allure.attach('输入内容', text, allure.attach_type.TEXT)
        self.input(self.name_button_one,text)

    @allure.step(title="点击添加标签编辑")
    def click_input_name_button_one(self,text):  # 添加标签编辑
        self.click(self.input_name_button_one)
        allure.attach('输入内容', text, allure.attach_type.TEXT)
        self.input(self.input_name_button_box_one,text)

    @allure.step(title="保存编辑内容")
    def click_save_button_one(self):  # 保存编辑内容
        self.click(self.save_button_one)

    @allure.step(title="音频删除")
    def click_delete_button_one(self):    # 音频删除
        self.click(self.delete_button_one)

    # 点击搜索"放大镜"按钮
    @allure.step(title="点击搜索'放大镜'按钮")
    def click_search(self):
        self.click(self.search_button)

    # 云空间按钮
    @allure.step(title="点击云空间按钮")
    def click_cloud(self):
        self.click(self.cloud_button)

    # 文件选择按钮":"按钮
    @allure.step(title="点击文件选择按钮'...'按钮")
    def click_select(self):
        self.click(self.select_button)

    # 点击全部文件按钮
    @allure.step(title="点击点击全部文件按钮")
    def click_classify(self):
        self.click(self.classify_button)

    # 取消按钮
    @allure.step(title="点击取消按钮")
    def click_cancel(self):
        self.click(self.cancel_button)

    # 全选按钮
    @allure.step(title="点击全选按钮")
    def click_check_all(self):
        self.click(self.check_all_button)

    # 上传按钮
    @allure.step(title="点击上传按钮")
    def click_uploading(self):
        self.click(self.uploading_button)

    # 滑动音频文件
    @allure.step(title="滑动音频文件")
    def scroll_page_one_time_record(self):
        self.scroll_page_one_time()

    # 底部删除按钮
    @allure.step(title="点击底部删除按钮")
    def click_delete(self):
        self.click(self.delete_button)

    # 删除弹出窗
    @allure.step(title="点击取消删除")
    def click_cancel_delete(self):  # 取消删除
        self.click(self.cancel_delete_button)

    @allure.step(title="点击确定删除")
    def click_confirm_delete(self):  # 确定删除
        self.click(self.confirm_delete_button)

    @allure.step(title="点击选择音频播放")
    def select_audio_play(self):  # 选择音频播放
        self.click(self.select_audio_button)




    # 选择当前屏幕最后一个音频
    # def select_the_last_audio_to_play(self):
        # window_size = self.driver.get_window_size()
        # width = window_size["width"]
        # height = window_size["height"]
        # top_x = width * 0.5
        # top_y = height * 0.1
        # bottom_x = top_x
        # bottom_y = width * 0.9
        # TouchAction(self.driver).press(bottom_x, bottom_y).release().perform()

        # window_size = self.driver.get_window_size()
        # width = window_size["width"]
        # height = window_size["height"]
        # bottom_x = width * 0.5
        # bottom_y = height * 0.9
        # TouchAction(self.driver).press(bottom_x, bottom_y).release().perform()

    def swipe_unlock(self):
        window_size = self.driver.get_window_size()
        width = window_size["width"]
        height = window_size["height"]
        top_x = width * 0.5
        top_y = height * 0.1
        bottom_x = top_x
        bottom_y = width * 0.9
        self.driver.swipe(bottom_x, bottom_y, top_x, top_y,2000)

    # 变滑边找"已全部加载完"
    @allure.step(title="变滑边找'已全部加载完'")
    def select_all_loadedy_text(self):
        self.scroll_find_element(self.all_loadedy_text)

        # while True:
        #     try:
        #         if self.find_element(self.all_loadedy_text):
        #             break
        #         else:
        #             self.swipe_unlock()
        #     except:
        #         return "到底啦"

