import os
import logging
import time
from trace import Ignore

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    # 因为这个类中的其他对象方法需要使用driver对象
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=5.0, poll=1.0):
        """
        根据元素的从特征（元组），定位对应的元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 每多久照一次
        :return: 找到元素本身
        """
        # by = feature[0]
        # value = feature[1]
        # by, value = feature
        # element = self.driver.find_element(by, value)
        by, value = feature
        logging.info("location={}".format(feature))
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))
        return element



    def find_elements(self, feature, timeout=5.0, poll=1.0):
        """
        根据元素的从特征（元组），定位符合特征条件的多个元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 每多久照一次
        :return: 列表，符合条件的元素
        """
        by, value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))
        return element

    def click(self, feature, timeout=5.0, poll=1.0):
        """
        根据传进来的特征，去找对应的元素，并且点击
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 每多久照一次
        """
        self.find_element(feature, timeout, poll).click()

    def input(self, feature, text, timeout=5.0, poll=1.0):
        """
        根据传进来的特征，去找对应的元素，并且输入文字
        :param feature: 特征
        :param text: 要输入的文字
        :param timeout: 超时时间
        :param poll: 每多久照一次
        """
        self.find_element(feature, timeout, poll).send_keys(text)

    def clear(self, feature, timeout=5.0, poll=1.0):
        """
        根据传进来的特征，去找对应的元素，并且清空
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 每多久照一次
        """
        self.find_element(feature, timeout, poll).clear()

    def find_toast(self, content):
        """
        根据部分toast内容，获取全部的toast内容
        :param content: 部分内容
        :return: 全部内容
        """
        feature = By.XPATH, "//*[contains(@text,'" + content + "')]"
        return self.find_element(feature, 5, 0.1).text

    def scroll_page_one_time(self, dir="down"):
        """
        滑动 半屏 从 4/3 到 4/1
        :param dir: 反向
            up: 从上往下
            down: 从下往上
            left: 从左往右
            right: 从右往左
        """
        window_size = self.driver.get_window_size()
        width = window_size["width"]
        height = window_size["height"]
        top_x = width * 0.5
        # top_y = height * 0.25
        top_y = height * 0.1
        bottom_x = top_x
        # bottom_y = width * 0.75
        bottom_y = width * 0.9
        left_x = width * 0.25
        left_y = height * 0.5
        right_x = width * 0.75
        right_y = left_y

        if dir == "down":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y)
        elif dir == "up":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y)
        elif dir == "left":
            self.driver.swipe(left_x, left_y, right_x, right_y)
        elif dir == "right":
            self.driver.swipe(right_x, right_y, left_x, left_y)
        else:
            raise Exception("请传入正确的参数 up/down/left/right")

    def scroll_find_element(self, feature, dir="down"):
        """
        边滑边找，如果找到则返回，如果没有找到则抛异常
        :param feature: 元素的特征
        :return: 元素
        """
        while True:

            source = self.driver.page_source
            try:
                return self.find_element(feature)
            except Exception:
                self.scroll_page_one_time(dir)
                if source == self.driver.page_source:
                    # 到底了
                    raise Exception("滑动到底")

    def save_screenshot(self):
        """
        保存截图
        """
        file_path = os.getcwd() + '/Screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logging.info("开始截图并保存")

        except Exception as e:
            logging.error("出现异常", format(e))
















###################################################################
#     # 模拟手指触摸屏
#     def tap(self, feature, timeout=5.0, poll=1.0,x=None,y=None):
#         # TouchAction(self.driver).tap(self.find_element(feature, timeout, poll)).perform()
#         TouchAction(self.driver).tap(x, y).perform()
#         # TouchAction(driver).tap(x=155, y=250).perform()
#     # 短按：模拟手指按住一个元素，或者坐标
#     def press(self, feature, timeout=5.0, poll=1.0):
#         TouchAction(self.driver).press(self.find_element(feature, timeout, poll)).perform()
#
#     # 释放手指(抬起手指)
#     def release(self):
#         TouchAction(self.driver).release().perform()
#
#     # 先按下后抬起
#     def press_release(self, feature, timeout=5.0, poll=1.0):
#         TouchAction(self.driver).press(self.find_element(feature, timeout, poll)).release().perform()
#
#     # 长按：模拟按住一个元素，或者坐标
#     def long_press(self, feature, duration=1000):
#         TouchAction(self.driver).long_press(self.find_element(feature, duration)).release().perform()
#
#     # 按住元素后的等待时间
#     def wait(self,feature):
#         TouchAction(self.driver).press(self.find_element(feature)).wait(5000).perform()
#
#     # 移动手指到另外一个元素，或者坐标，注意这里坐标不是绝对坐标，是偏移量
#     def move_to(self, x=None, y=None):
#         TouchAction(self.driver).press(self.find_element(x, y)).wait(100).move_to(x, y).release().perform()
#
#
# ###################################################################################
#
#
#     # 获取元素 文本值封装
#     def base_get_text(self,loc):
#         return self.find_element(loc).text
#
#     # 获取元素 文本值封装
#     def base_get_text2(self,el):
#         return el.text
#
#     # 获取一组元素
#     def base_get_sms_list(self,loc):
#         return self.find_elements(loc)
#
#     # 长按方法 封装
#     def base_long_press_element(self,el):
#         TouchAction(self.driver).long_press(el,duration=2000).release().perform()
#
#     # 单独封装个Xpath语句
#     def base_xpath_click(self,text):
#         self.click((By.XPATH,"//*[contains(@text,'"+text+"')]"))
#
# #############################################################################












    # def tap(self, position=(None, None), locator=None, element=None, driver=None):
    #     '''单点触摸元素'''
    #     driver = self._get_driver(driver)
    #     if locator and locator[0] == 'image':
    #         position = self.get_image_location(isearch=locator[1])
    #     else:
    #         element = self._get_element(locator, element, driver)
    #     TouchAction(driver).tap(element=element, x=position[0], y=position[1]).perform()
    #     self.logger.info("tap元素%s，坐标%s" % (element, position))
    # def press(self, position=(None, None), locator=None, element=None, driver=None):
    #     '''按压元素'''
    #     driver = self._get_driver(driver)
    #     element = self._get_element(locator, element, driver)
    #     TouchAction(driver).press(el=element, x=position[0], y=position[1]).perform()
    #     self.logger.info("按压元素%s，坐标%s" % (element, position))
    # def long_press(self, position=(None, None), locator=None, element=None, duration=1000, driver=None):
    #     '''长按元素'''
    #     driver = self._get_driver(driver)
    #     element = self._get_element(locator, element, driver)
    #     TouchAction(driver).long_press(el=element, x=position[0], y=position[1], duration=duration).perform()
    #     self.logger.info("长按元素%s，坐标%s" % (element, position))
    # def swipe(self, from_position, to_position, duration=None, driver=None):
    #     '''根据坐标滑动'''
    #     driver = self._get_driver(driver)
    #     driver.swipe(from_position[0], from_position[1], to_position[0], to_position[1], duration=duration)
    #     self.logger.info("滑动%s --> %s" % (from_position, to_position))
    # def swipe_up(self, duration=None, driver=None):
    #     '''向上滑动'''
    #     driver = self._get_driver(driver)
    #     x = self.get_phone_size('width', driver=driver) / 2
    #     height = self.get_phone_size('height', driver=driver)
    #     from_y = height / 10 * 9
    #     to_y = height / 10
    #     self.swipe((x, from_y), (x, to_y), duration=duration, driver=driver)
    #     self.logger.info("向上滑动")
    # def swipe_down(self, duration=None, driver=None):
    #     '''向下滑动'''
    #     driver = self._get_driver(driver)
    #     x = self.get_phone_size('width', driver=driver) / 2
    #     height = self.get_phone_size('height', driver=driver)
    #     from_y = height / 10
    #     to_y = height / 10 * 9
    #     self.swipe((x, from_y), (x, to_y), duration=duration, driver=driver)
    #     self.logger.info("向下滑动")
    # def swipe_left(self, duration=None, driver=None):
    #     '''向左滑动'''
    #     driver = self._get_driver(driver)
    #     width = self.get_phone_size('width', driver=driver)
    #     from_x = width / 10 * 9
    #     to_x = width / 10
    #     y = self.get_phone_size('height', driver=driver) / 2
    #     self.swipe((from_x, y), (to_x, y), duration=duration, driver=driver)
    #     self.logger.info("向左滑动")
    # def swipe_right(self, duration=None, driver=None):
    #     '''向右滑动'''
    #     driver = self._get_driver(driver)
    #     width = self.get_phone_size('width', driver=driver)
    #     from_x = width / 10
    #     to_x = width / 10 * 9
    #     y = self.get_phone_size('height', driver=driver) / 2
    #     self.swipe((from_x, y), (to_x, y), duration=duration, driver=driver)
    #     self.logger.info("向右滑动")
    # def contexts(self, driver=None):
    #     '''获取当前页面的contexts，返回list'''
    #     driver = self._get_driver(driver)
    #     contexts = driver.contexts
    #     self.logger.info("获取当前页面contexts：%s" % contexts)
    #     return contexts
    # def switch_to_context(self, context, driver=None):
    #     '''native和webview切换'''
    #     driver = self._get_driver(driver)
    #     driver.switch_to.context(context)
    #     self.logger.info("切换到context：%s" % context)
    # def switch_to_native(self, driver=None):
    #     '''切换回到native'''
    #     driver = self._get_driver(driver)
    #     driver.switch_to.context("NATIVE_APP")
    #     self.logger.info("切换到native app")
    # def mult_tap(self, positions, duration=None, driver=None):
    #     '''多点触摸positions  # 需要传list 做多传5个坐标  [(1,2),(3,4)]'''
    #     driver = self._get_driver(driver)
    #     driver.tap(positions=positions, duration=duration)
    #     self.logger.info("触摸：%s，持续：%s毫秒" % (positions, duration))
    # def wait_activity(self, activity, timeout=10, interval=0.5, driver=None):
    #     '''等待activity出现，返回bool，#安卓特有'''
    #     driver = self._get_driver(driver)
    #     res = driver.wait_activity(activity=activity, timeout=timeout, interval=interval)
    #     self.logger.info("等待activity：%s %s" % (activity, res))
    #     return res
    # def current_activity(self, driver=None):
    #     '''获取当前activity, #安卓特有'''
    #     driver = self._get_driver(driver)
    #     current_activity = driver.current_activity
    #     self.logger.info("获取当前activity：%s" % current_activity)
    #     return current_activity
    # def is_toast_exist(self, text, timeout=10, poll_frequency=0.5, driver=None):
    #     '''
    #     toast元素检查
    #     cap里面需要加 “automationName”: "Uiautomator2"
    #     '''
    #     driver = self._get_driver(driver)
    #     try:
    #         toast_loc = ("xpath", ".//*[contains(@text, '%s')]" % text)
    #         toast_ele = WebDriverWait(driver, timeout, poll_frequency).until(
    #             EC.presence_of_element_located(toast_loc))
    #         self.logger.info("检查 %s toast，存在%s" % (text, toast_ele))
    #         return toast_ele
    #     except:
    #         self.logger.info("检查 %s toast，不存在" % text)
    #         return False
    # def always_allows(self, num=5, driver=None):
    #     '''安卓启动App 获取权限的弹框 点击始终允许'''
    #     driver = self._get_driver(driver)
    #     for i in range(num):
    #         loc = ("xpath", "//*[@text='始终允许']")
    #         try:
    #             element = WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located(loc))
    #             element.click()
    #             self.logger.info("权限获取，点击始终允许")
    #         except:
    #             pass
    # def get_screenshot_as_base64(self, driver=None):
    #     '''截图'''
    #     driver = self._get_driver(driver)
    #     pic_base64 = driver.get_screenshot_as_base64()
    #     self.logger.info("截图")
    #     return pic_base64
    # def get_screenshot_as_file(self, file, driver=None):
    #     '''截图png,包存起来'''
    #     driver = self._get_driver(driver)
    #     res = driver.get_screenshot_as_file(file)
    #     if res:
    #         self.logger.info("%s保存图片" % file)
    #         return True
    #     else:
    #         self.logger.info("%s图片保存失败" % file)
    #         return False
    # def get_image_location(self, isearch, driver=None):
    #     '''获取 模板图片在原图片的中间坐标 (36.5, 79.5)'''
    #     driver = self._get_driver(driver)
    #     file = os.path.join(self.path_screenshot,
    #                         "i" + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + ".png")
    #     self.get_screenshot_as_file(file, driver=driver)  # 原始图像
    #     imsrc = ac.imread(file)  # 原始图像
    #     imsch = ac.imread(os.path.join(self.path_imlocator, isearch.split("/")[0], isearch.split("/")[1]))  # 带查找的部分
    #     posi = ac.find_sift(imsrc, imsch)
    #     if posi:
    #         self.logger.info("查找到图片的坐标：%s" % str(posi['result']))
    #         return posi['result']
    #     else:
    #         self.logger.info("Error没有找到图片的坐标：%s" % isearch)
    #         return False
    # def exec_adb(self, command):
    #     '''执行adb命令'''
    #     os.system(command)
    #     self.logger.info("执行command：%s" % command)
    # def close_app(self, driver=None):
    #     '''关闭App'''
    #     driver = self._get_driver(driver)
    #     driver.close_app()
    #     self.logger.info("关闭App")
    # def launch_app(self, driver=None):
    #     driver = self._get_driver(driver)
    #     driver.launch_app()
    #     self.logger.info("启动App")