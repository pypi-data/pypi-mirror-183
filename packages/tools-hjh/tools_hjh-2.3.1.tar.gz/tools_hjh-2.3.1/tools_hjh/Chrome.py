# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Chrome():
    """ 使用浏览器解析url，返回源码
        __init__.param：
            chrome_path: chrome.exe路径
            chromedriver_path: chromedriver.exe路径
    """

    def __init__(self, chrome_path, chromedriver_path, is_hidden=False, is_display_picture=True, proxies=None):
        
        chrome_options = Options()
        if is_hidden:
            chrome_options.add_argument("--headless")
        chrome_options.binary_location = chrome_path
        if not is_display_picture:
            chrome_options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
        self.chrome = webdriver.Chrome(chromedriver_path, options=chrome_options)
        
    def close(self):
        self.chrome.close()
        
    def get(self, url, headers=None, data=None):
        self.chrome.get(url)
        return self.chrome.page_source

