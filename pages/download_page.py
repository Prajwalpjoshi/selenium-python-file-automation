from selenium.webdriver.common.by import By

class DownloadPage:

    def __init__(self, driver):
        self.driver = driver

    file_link = (By.LINK_TEXT, "some-file.txt")

    def download_file(self):

        self.driver.find_element(*self.file_link).click()