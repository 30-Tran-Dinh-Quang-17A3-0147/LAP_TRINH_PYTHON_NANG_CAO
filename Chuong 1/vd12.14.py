#Ví dụ demo về constructor (hàm tạo) có tham số
class Dog:
    #Constructor có tham số
    def __init__(self, name):
        print("Đây là constructor CÓ tham số!")
        self.name = name

    def display(self):
        print("Hello",self.name)
#-----------------------End Class Dog-----------------------
bull = Dog("The Dom")
bull.display()