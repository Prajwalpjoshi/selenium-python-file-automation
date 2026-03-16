from utils.screenshot import capture_screenshot

try:
    assert message == "File Uploaded!"
except:
    capture_screenshot(driver)
    raise