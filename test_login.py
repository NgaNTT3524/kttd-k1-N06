
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait


def test_login():
    # Cấu hình Android Emulator
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    options.set_capability("appWaitActivity", "*")

    # Kết nối Appium
    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    try:
        # Nhập username
        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-Username"
        ).send_keys("standard_user")

        # Nhập password
        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-Password"
        ).send_keys("secret_sauce")

        # Nhấn nút Login
        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-LOGIN"
        ).click()

        # Chờ tối đa 10 giây để tiêu đề PRODUCTS xuất hiện
        products = WebDriverWait(driver, 10).until(
            lambda d: d.find_element(
                AppiumBy.XPATH,
                "//*[contains(@text, 'PRODUCTS')]"
            )
        )

        # Xác nhận đăng nhập thành công
        assert products.is_displayed()

    finally:
        driver.quit()
