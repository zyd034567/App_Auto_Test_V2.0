import allure
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LocalRecordPage(BaseAction):

    # 录音本地界面按钮
    standard_button = By.XPATH, "//*[@text='标准']"
    interview_button = By.XPATH, "//*[@text='采访']"
    conference_button = By.XPATH, "//*[@text='会议']"
    speech_button = By.XPATH, "//*[@text='演讲']"
    memo_button = By.XPATH, "//*[@text='备忘']"
    music_button = By.XPATH, "//*[@text='音乐']"
    navigation_bar_record_button = By.XPATH, "//*[@text='录音']"
    navigation_bar_my_document_button = By.XPATH, "//*[@text='我的文件']"
    navigation_bar_Translate_while_recording_button = By.XPATH, "//*[@text='边录边译']"
    navigation_bar_mine_button = By.XPATH, "//*[@text='我的']"

    # 快捷栏网络按钮
    WLAN_button = By.XPATH, "//*[contains(@content-desc,'WLAN')]"
    # 快捷栏蓝牙按钮
    blue_tooth_button = By.XPATH, "//*[contains(@content-desc,'蓝牙')]"
    # 快捷栏省电按钮
    power_saving_button = By.XPATH, "//*[contains(@content-desc,'省电')]"
    # 快捷栏设置按钮
    seeting_button = By.XPATH, "//*[contains(@content-desc,'反色')]"

    #解锁密码 数字“1”
    enter_password_to_unlock_button = By.XPATH, '//android.view.ViewGroup[@content-desc="1"]/android.widget.TextView'

    # 标准按钮
    @allure.step(title="点击标准按钮")
    def click_standard(self):
        self.click(self.standard_button)

    # 采访按钮
    @allure.step(title="点击采访按钮")
    def click_interview(self):
        self.click(self.interview_button)

    # 会议按钮
    @allure.step(title="点击会议按钮")
    def click_conference(self):
        self.click(self.conference_button)

    # 演讲按钮
    @allure.step(title="点击演讲按钮")
    def click_speech(self):
        self.click(self.speech_button)

    # 备忘按钮
    @allure.step(title="点击备忘按钮")
    def click_memo(self):
        self.click(self.memo_button)

    # 音乐按钮
    @allure.step(title="点击音乐按钮")
    def click_music(self):
        self.click(self.music_button)

    # 底部导航栏录音按钮
    @allure.step(title="点击底部导航栏录音按钮")
    def click_navigation_bar_record(self):
        self.click(self.navigation_bar_record_button)

    # 底部导航栏我的文件按钮
    @allure.step(title="点击底部导航栏我的文件按钮")
    def click_navigation_bar_my_document(self):
        self.click(self.navigation_bar_my_document_button)

    # 底部导航栏边录边译按钮
    @allure.step(title="点击底部导航栏边录边译按钮")
    def click_navigation_bar_Translate_while_recording(self):
        self.click(self.navigation_bar_Translate_while_recording_button)

    # 底部导航栏我的按钮
    @allure.step(title="点击 底部导航栏我的按钮")
    def click_navigation_bar_mine(self):
        self.click(self.navigation_bar_mine_button)

    # 下拉快捷栏
    @allure.step(title="下拉快捷栏")
    def drop_down_shortcuts(self):
        self.driver.swipe(250, 10, 250, 250)

    # 点击网络
    @allure.step(title="点击网络")
    def click_network(self):
        self.click(self.WLAN_button)

    # 点击蓝牙
    @allure.step(title="点击蓝牙")
    def click_blue_tooth(self):
        self.click(self.blue_tooth_button)

    # 点击省电
    @allure.step(title="点击省电")
    def click_power_saving(self):
        self.click(self.power_saving_button)

    # 点击设置
    @allure.step(title="点击设置")
    def click_seeting(self):
        self.click(self.seeting_button)

    # 退出快捷栏
    @allure.step(title="退出快捷栏")
    def quit_shortcuts(self):
        TouchAction(self.driver).press(x=300, y=600).release().perform()

    # 滑屏解锁
    @allure.step(title="滑屏解锁")
    def swipe_unlock(self):
        # self.driver.swipe(200, 800, 200, 400, 2000) #701
        self.driver.swipe(200, 600, 200, 300, 2000) #501


        # self.scroll_page_one_time(dir="up")
        # window_size = self.driver.get_window_size()
        # width = window_size["width"]
        # height = window_size["height"]
        # top_x = width * 0.5
        # top_y = height * 0.1
        # bottom_x = top_x
        # bottom_y = width * 0.9
        # self.driver.swipe(bottom_x, bottom_y, top_x, top_y,2000)
        # self.scroll_page_one_time()

    # 输入密码解锁
    @allure.step(title="点击密码")
    def click_enter_password_to_unlock(self):
        self.click(self.enter_password_to_unlock_button)

