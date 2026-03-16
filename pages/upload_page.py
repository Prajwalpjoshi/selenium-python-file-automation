from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UploadPage:

    def __init__(self, driver):
        self.driver = driver

    upload_input = (By.ID, "file-upload")
    upload_button = (By.ID, "file-submit")
    success_text = (By.TAG_NAME, "h3")

    def upload_file(self, file_path):

        self.driver.find_element(*self.upload_input).send_keys(file_path)
        self.driver.find_element(*self.upload_button).click()

    def get_success_message(self):

        wait = WebDriverWait(self.driver, 10)

        message = wait.until(
            EC.visibility_of_element_located(self.success_text)
        )

        return message.text