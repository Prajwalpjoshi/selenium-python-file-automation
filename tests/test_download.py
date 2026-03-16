import os
import time
from pages.download_page import DownloadPage
from utils.screenshot import capture_screenshot

def test_file_download(driver):

    try:

        driver.get("https://the-internet.herokuapp.com/download")

        download_page = DownloadPage(driver)

        download_page.download_file()

        time.sleep(8)

        file_path = os.path.abspath("downloads/some-file.txt")

        assert os.path.exists(file_path)

    except Exception:

        capture_screenshot(driver)
        raise