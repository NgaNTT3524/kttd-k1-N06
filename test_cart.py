from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait


def test_add_remove_cart():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    options.set_capability("appWaitActivity", "*")

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    try:
        wait = WebDriverWait(driver, 15)

        # 1. Dang nhap
        wait.until(lambda d: d.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-Username"
        )).send_keys("standard_user")

        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-Password"
        ).send_keys("secret_sauce")

        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-LOGIN"
        ).click()

        # 2. Cho man hinh san pham
        wait.until(lambda d: d.find_element(
            AppiumBy.XPATH,
            "//*[contains(@text, 'PRODUCTS')]"
        ))

        # 3. Them san pham vao gio hang
        add_buttons = driver.find_elements(
            AppiumBy.XPATH,
            "//*[contains(@content-desc, 'ADD TO CART')]"
        )

        assert len(add_buttons) > 0, "Khong tim thay nut ADD TO CART"

        add_buttons[0].click()

        # 4. Mo gio hang
        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-Cart"
        ).click()

        # 5. Cho man hinh gio hang hien thi
        wait.until(lambda d: d.find_element(
            AppiumBy.XPATH,
            "//*[contains(@text, 'YOUR CART')]"
        ))

        # 6. Cho nut REMOVE hien thi va co the thao tac
        def tim_nut_remove(driver):
            buttons = driver.find_elements(
                AppiumBy.ACCESSIBILITY_ID, "test-REMOVE"
            )

            for button in buttons:
                if button.is_displayed() and button.is_enabled():
                    return button

            return False

        remove_button = wait.until(tim_nut_remove)

        # 7. Xoa san pham
        remove_button.click()

        # 8. Cho nut REMOVE khong con hien thi
        wait.until(lambda d: not any(
            button.is_displayed()
            for button in d.find_elements(
                AppiumBy.ACCESSIBILITY_ID, "test-REMOVE"
            )
        ))

    finally:
        # 9. Dong ket noi Appium
        driver.quit()