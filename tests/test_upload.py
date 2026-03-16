import os
from pages.upload_page import UploadPage
from utils.screenshot import capture_screenshot

def test_file_upload(driver):

    try:

        driver.get("https://the-internet.herokuapp.com/upload")

        file_path = os.path.abspath("testdata/sample.txt")

        upload_page = UploadPage(driver)

        upload_page.upload_file(file_path)

        message = upload_page.get_success_message()

        assert message == "File Uploaded!"

    except Exception:

        capture_screenshot(driver)
        raise