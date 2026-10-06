def func(x): #hàm này trả về giá trị bằng biến ban đầu + 1
    return x + 1

def test_answer(): #hàm để kiểm tra xem giá trị trả về có bằng giá trị dự đoán hay không 
    assert func(3) == 5