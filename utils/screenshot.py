import time

def capture_screenshot(driver):
    filename = f"screenshots/failure_{int(time.time())}.png"
    driver.save_screenshot(filename)