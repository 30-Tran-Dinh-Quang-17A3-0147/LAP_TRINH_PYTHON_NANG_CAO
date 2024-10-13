#Ví dụ demo về constructor (hàm tạo) không có tham số
class Dog:
    #Constructor Không có tham số
    def __init__(self):
        print("Đây là constructor KHÔNG CÓ tham số!")

    def display(self, name):
        print("Hello", name)
#-----------------------End Class Dog-----------------------
bull = Dog()
bull.display("The Dom!")