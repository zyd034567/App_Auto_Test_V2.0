from page.AIUI_page import AIUIPage
from page.local_my_page import LocalMyPage
from page.local_mydocument_page import LocalMyDocumentPage
from page.local_record_page import LocalRecordPage
from page.local_translate_while_recording_page import LocalTranslateWhileRecordingPage
from page.login_page import LoginPage
from page.mydocument_play_page import MyDocumentPlayPage
from page.mydocument_search_page import MyDocumentSearchPage
from page.personal_information_page import PersonalInformation
from page.record_Translate_while_recording_page import RecordTranslateWhileRecordingPage
from page.record_page import RecordPage
from page.settings_network_page import SeettingNetworkPage
from page.settings_page import SeettingPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def login_page(self):
        return LoginPage(self.driver)

    @property
    def AIUI_page(self):
        return AIUIPage(self.driver)

    @property
    def record_page(self):
        return RecordPage(self.driver)

    @property
    def personal_information_page(self):
        return PersonalInformation(self.driver)

    @property
    def local_record_page(self):
        return LocalRecordPage(self.driver)

    @property
    def local_my_document_page(self):
        return LocalMyDocumentPage(self.driver)

    @property
    def local_translate_while_recording_page(self):
        return LocalTranslateWhileRecordingPage(self.driver)

    @property
    def local_my_page(self):
        return LocalMyPage(self.driver)

    @property
    def my_document_play_page(self):
        return MyDocumentPlayPage(self.driver)

    @property
    def my_document_search_page(self):
        return MyDocumentSearchPage(self.driver)

    @property
    def record_translate_while_recording_page(self):
        return RecordTranslateWhileRecordingPage(self.driver)

    @property
    def settings_page(self):
        return SeettingPage(self.driver)

    @property
    def settings_network_page(self):
        return SeettingNetworkPage(self.driver)



