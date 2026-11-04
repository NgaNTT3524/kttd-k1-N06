
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_login import dang_nhap


def test_reset_app_state():

    # 1. Cấu hình Android Emulator 
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"

    # Giữ dữ liệu ứng dụng khi khởi chạy phiên Appium
    options.no_reset = True
    options.set_capability("appWaitActivity", "*")

    # 2. Kết nối Appium
    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    wait = WebDriverWait(driver, 30)   

    try:
        # 3. Chờ màn hình đăng nhập xuất hiện
        username = wait.until(
            EC.presence_of_element_located((
                AppiumBy.ACCESSIBILITY_ID,
                "test-Username"
            ))
        )

        print("Đã mở màn hình đăng nhập")

        # 4. Đăng nhập
        dang_nhap(driver)
        print("Đăng nhập thành công")

        # 5. Tìm các nút ADD TO CART   
        add_buttons = wait.until(
            lambda d: d.find_elements(
                AppiumBy.XPATH,
                "//*[contains(@content-desc, 'ADD TO CART')]"
            )
        )

        assert len(add_buttons) > 0, "Không tìm thấy nút ADD TO CART"

        # Thêm sản phẩm đầu tiên vào giỏ hàng 
        add_buttons[0].click()   #test bình thường không thấy có thay đổi gì, nên em thêm 1 sản phẩm vào giỏ để test xem nó có trở lại như ban đầu không

        print("Đã thêm sản phẩm vào giỏ hàng")

        # 6. Mở Menu
        menu_button = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                "test-Menu"
            ))
        )

        menu_button.click()
        print("Đã mở Menu")

        # 7. Nhấn RESET APP STATE
        reset_button = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                "test-RESET APP STATE"
            ))
        )

        reset_button.click()
        print("Đã nhấn RESET APP STATE")

        # 8. Kiểm tra ứng dụng vẫn hoạt động
        products = wait.until(
            EC.visibility_of_element_located((
                AppiumBy.XPATH,
                "//*[contains(@text, 'PRODUCTS')]"
            ))
        )
        assert products.is_displayed()

        print("PASS: Ứng dụng vẫn hoạt động sau khi Reset")

        # 9. Mở giỏ hàng
        cart_button = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                "test-Cart"
            ))
        )

        cart_button.click()

        # 10. Kiểm tra giỏ hàng không còn sản phẩm
        cart_items = driver.find_elements(
            AppiumBy.ACCESSIBILITY_ID,
            "test-Description"
        )

        assert len(cart_items) == 0, "Giỏ hàng vẫn còn sản phẩm"

        print("PASS: Giỏ hàng đã trống sau khi Reset")

    finally:
        # 11. Đóng phiên kiểm thử
        driver.quit()


#cd D:\A46030_KIEMTHU
#.\npm.cmd exec -- appium


#python -m pytest -v test_state.py