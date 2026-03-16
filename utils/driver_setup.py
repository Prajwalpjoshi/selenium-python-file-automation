from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

def get_driver():

    options = webdriver.ChromeOptions()

    # Required for GitHub Actions Linux environment
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    download_path = os.path.abspath("downloads")

    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()

    return driver