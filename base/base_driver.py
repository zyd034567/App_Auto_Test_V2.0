# -- coding: utf-8 --
from appium import webdriver


def init_driver():
    """
    只要调用，就可以打开对应的应用程序
    :return:
    """
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1.0'
    desired_caps['deviceName'] = '221906280000171'

    # app的信息
    desired_caps['appPackage'] = 'com.iflyrec.smartrecorder'
    desired_caps['appActivity'] = 'com.iflyrec.module.main.MainPageActivity'
    # desired_caps['appActivity'] = 'com.iflyrec.module_login.mvp.ui.AuthLoginActivity'

    # 延迟appium休眠时长
    desired_caps['newCommandTimeout'] = 2000
    # 不要重置应用
    desired_caps['noReset'] = True
    # toast
    desired_caps['automationName'] = 'Uiautomator2'
    # 解决中文问题
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明我们的driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


# import threading
#
# from appium import webdriver
#
# import time
#
# def init_driver(port="4723"):
#     # server 启动参数
#     desired_caps = {}
#     # 设备信息
#     # 大小写无所谓
#     desired_caps['platformName'] = 'Android'
#     # 比如版本是5.2.3，可以写成 “5.2.3”，“5.2”，“5”
#     desired_caps['platformVersion'] = '5.1'
#     # android随便写，但是不能不写，也不能为空字符串
#     # iOS不能随便写，写成“iPhone 8”
#     desired_caps['deviceName'] = '192.168.56.101:5555'
#     # app信息
#     desired_caps['appPackage'] = 'com.android.settings'
#     desired_caps['appActivity'] = '.Settings'
#
#     return webdriver.Remote('http://localhost:' + port + '/wd/hub', desired_caps)
#
#
#

# 跳转AIUI界面
# driver.start_activity(' com.iflyrec.smartrecorder','com.iflyrec.module.aiui.view.AiuiMainActivity')
# time.sleep(2)
# # 跳转录音界面
# driver.start_activity('com.iflyrec.smartrecorder','com.iflyrec.module.record.RecordActivity')
# time.sleep(2)
# 跳转快速保存界面
# driver.start_activity('  com.iflyrec.smartrecorder','com.iflyrec.module.record.view.LockscreenRecordTipsActivity')
# time.sleep(2)
# # 跳转至系统设置
# driver.start_activity(' com.android.settings','.xf.SettingsActivity')
# time.sleep(2)
# # 跳转至本地界面
# driver.start_activity('  com.iflyrec.smartrecorder','com.iflyrec.module.main.MainPageActivity')
# time.sleep(2)



# app的信息 讯飞APK-开机引导界面
# desired_caps['appPackage'] = 'com.iflyrec.smartrecorder'
# desired_caps['appActivity'] = 'com.iflyrec.module.setupwizard.BootSetupActivity'
#  app的信息 讯飞APK-录音界面
# desired_caps['appPackage'] = 'com.iflyrec.smartrecorder'
# desired_caps['appActivity'] = 'com.iflyrec.module.record.RecordActivity'
# # app的信息 讯飞APK-播放界面
# desired_caps['appPackage'] = 'com.iflyrec.smartrecorder'
# desired_caps['appActivity'] = 'com.iflyrec.player.mr4.PlayerMr5Activity'
# # app的信息 系统设置-APK
# desired_caps['appPackage'] = 'com.android.settings'
# desired_caps['appActivity'] = '.xf.SettingsActivity'
# app的信息 讯飞APK-AIUI
# desired_caps['appPackage'] = ' com.iflyrec.smartrecorder'
# desired_caps['appActivity'] = 'com.iflyrec.module.aiui.view.AiuiMainActivity'
# desired信息 讯飞APK-边录边译
# desired_caps['appPackage'] = '  com.iflyrec.smartrecorder'
# desired_caps['appActivity'] = 'com.iflyrec.module.main.MainPageActivity'
# desired信息 讯飞APK-快速保存
# desired_caps['appPackage'] = '  com.iflyrec.smartrecorder'
# desired_caps['appActivity'] = 'com.iflyrec.module.record.view.LockscreenRecordTipsActivity'

