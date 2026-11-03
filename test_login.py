from selenium import webdriver
from urllib.parse import quote  #hàm quote để mã hóa các ký tự trong chuỗi rồi đưa vào url 

def dien_thong_tin(driver, username, password):   #biến driver để gọi đến trình duyệt mà selenium đang điều khiển
    user = quote(username, safe="")               #mã hóa tên người dùng
    pwd = quote(password, safe="")                #mã hóa mật khẩu
    url = f"https://{user}:{pwd}@the-internet.herokuapp.com/basic_auth"       #đẩy thông tin đã mã hóa vào url
    driver.get(url)                               #mở trang với thông tin đã có


#Trường hợp 1: đăng nhập thành công (đúng tên người dùng và đúng mật khẩu)
# def test_login_success():
#     driver = webdriver.Chrome()

#     dien_thong_tin(driver, "admin", "admin")

#     assert "Congratulations! You must have the proper credentials." in driver.page_source

#     driver.quit()

#Trường hợp 2: đăng nhập không thành công (sai tên người dùng, đúng mật khẩu)
# def test_username_wrong():
#     driver = webdriver.Chrome()

#     dien_thong_tin(driver, "ad", "admin")

#     assert "Congratulations! You must have the proper credentials." not in driver.page_source

#     driver.quit()

#Trường hợp 3: đăng nhập không thành công (đúng tên người dùng, sai mật khẩu)
# def test_password_wrong():
#     driver = webdriver.Chrome()

#     dien_thong_tin(driver, "admin", "ad")

#     assert "Congratulations! You must have the proper credentials." not in driver.page_source

#     driver.quit()

#Trường hợp 4: đăng nhập không thành công (sai cả tên người dùng và mật khẩu)
def test_all_wrong():
    driver = webdriver.Chrome()

    dien_thong_tin(driver, "ad", "ad")

    assert "Congratulations! You must have the proper credentials." not in driver.page_source

    driver.quit()