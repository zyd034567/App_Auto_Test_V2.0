# -- coding: utf-8 --
import allure
from appium.webdriver.common.touch_action import TouchAction

from base.base_action import BaseAction
from selenium.webdriver.common.by import By


class PersonalInformation(BaseAction):
    # 个人信息界面左上角返回
    return_button = By.ID, "com.iflyrec.smartrecorder:id/tv_left"
    # 手机号
    iphone_number = By.ID, "com.iflyrec.smartrecorder:id/tv_right_sth"
    # 昵称
    nickname = By.ID, "com.iflyrec.smartrecorder:id/et_nick_name"
    # 性别选中
    Select_the_gender = By.ID, "com.iflyrec.smartrecorder:id/rb_female"
    # 性别未选中
    Unselected_sex = By.ID, "com.iflyrec.smartrecorder:id/rb_male"

    # 生日按钮
    birthday_button = By.ID, "com.iflyrec.smartrecorder:id/item_birthday"
    # 生日的年月日
    year_scroll_bar = By.ID, "com.iflyrec.smartrecorder:id/year"
    month_scroll_bar = By.ID, "com.iflyrec.smartrecorder:id/month"
    day_scroll_bar = By.ID, "com.iflyrec.smartrecorder:id/day"

    # 地区按钮
    district_button = By.ID, "com.iflyrec.smartrecorder:id/item_address"
    # 地区省市及取消与确定按钮
    province_scroll_bar = By.ID, "com.iflyrec.smartrecorder:id/options1"
    city_scroll_bar = By.ID, "com.iflyrec.smartrecorder:id/options2"
    # 取消与确定
    cancel_button = By.ID, "com.iflyrec.smartrecorder:id/btnCancel"
    submit_button = By.ID, "com.iflyrec.smartrecorder:id/btnSubmit"


    #职业按钮
    profession_button = By.ID, "com.iflyrec.smartrecorder:id/item_job"
    # 选择职业
    teacher_button = By.XPATH, "//*[@text='教师']"
    student_button = By.XPATH, "//*[@text='学生']"
    clerk_button = By.XPATH, "//*[@text='文员']"
    solicitor_button = By.XPATH, "//*[@text='律师']"
    journalist_button = By.XPATH, "//*[@text='记者']"
    compile_button = By.XPATH, "//*[@text='编辑']"
    other_button = By.XPATH, "//*[@text='其它']"
    profession_input_box = By.XPATH, "//*[@text='职业 (非必选)']"

    log_out_button = By.XPATH, "//*[@text='退出登录']"
    # 确定退出登录弹窗
    personal_cancel_login_button = By.XPATH, "//*[@text='取消']"
    personal_confirm__login_button = By.XPATH, "//*[@text='确定']"

    # 确定保存个人信息弹窗
    personal_cancel_button = By.XPATH, "//*[@text='取消']"
    personal_confirm_button = By.XPATH, "//*[@text='确定']"

    # 点击返回
    @allure.step(title="点击返回")
    def click_return (self):
        self.click(self.return_button)

    # 修改昵称
    @allure.step(title="修改昵称")
    def recompose_nickname(self,text):
        self.click(self.nickname)
        self.clear(self.nickname)
        allure.attach('输入内容', text, allure.attach_type.TEXT)
        self.input(self.nickname,text)

    # 点击生日
    @allure.step(title="点击生日")
    def click_birthday(self):
        self.click(self.birthday_button)

    # 选择生日
    @allure.step(title="选择生日")
    def select_birthday(self):
        self.driver.swipe(130,1100,130,800,1000)  #更改年
        self.driver.swipe(360,1100,360,800,1000)  #更改月
        self.driver.swipe(600,1100,600,800,1000)  #更改日


    # 点击地区
    @allure.step(title="点击地区")
    def click_district(self):
        self.click(self.district_button)

    # 选择地区
    @allure.step(title="选择地区")
    def select_district(self):
        self.driver.swipe(180, 1100, 180, 800)  # 更改省份
        self.driver.swipe(530, 1100, 530, 800)  # 更改市区

    # 点击确认
    @allure.step(title="点击确认")
    def click_submit(self):
        self.click(self.submit_button)

    # 点击取消
    @allure.step(title="点击取消")
    def click_cancel(self):
        self.click(self.cancel_button)

    # 点击职业
    @allure.step(title="点击职业")
    def click_profession(self):
        self.click(self.profession_button)

    # 选择职业
    @allure.step(title="点击教师")
    def select_teacher(self):  #选择教师
        self.click(self.teacher_button)

    @allure.step(title="点击学生")
    def select_student(self):  #选择学生
        self.click(self.student_button)

    @allure.step(title="点击文员")
    def select_clerk(self):  #选择文员
        self.click(self.clerk_button)

    @allure.step(title="点击律师")
    def select_solicitor(self):  #选择律师
        self.click(self.solicitor_button)

    @allure.step(title="点击记者")
    def select_journalist(self):  #选择记者
        self.click(self.journalist_button)

    @allure.step(title="点击编辑")
    def select_compile(self):  #选择编辑
        self.click(self.compile_button)

    @allure.step(title="点击其它")
    def profession_input(self,text):   #选择其它
        self.input(self.profession_input_box, text)

    # 更改性别
    @allure.step(title="更改性别")
    def change_the_gender(self):
        self.click(self.Unselected_sex)

    # 点击退出登录
    @allure.step(title="点击退出登录")
    def click_log_out(self):
        self.click(self.log_out_button)

    # 确认个人信息保存弹窗
    @allure.step(title="确认个人信息保存弹窗-取消")
    def click_personal_cancel(self):   #取消
        self.click(self.personal_cancel_button)

    @allure.step(title="确认个人信息保存弹窗-确定")
    def click_personal_confirm(self):    #确定
        self.click(self.personal_confirm_button)

    # 退出登录弹窗
    @allure.step(title="退出登录弹窗-取消")
    def click_personal_login_cancel(self):  # 取消
        self.click(self.personal_cancel_login_button)

    @allure.step(title="退出登录弹窗-确定")
    def click_personal_login_confirm(self):  # 确定
        self.click(self.personal_cancel_login_button)