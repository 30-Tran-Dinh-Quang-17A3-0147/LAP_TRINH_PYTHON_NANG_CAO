class Dog:              #Ví dụ DEMO về phương thức hủy Destructor

    DogCount = 0
    #Hàm khởi tạo đối tượng
    def __init__(self, name, size, age, color):
        self.name = name            #Thuộc tính của đối tượng (object)
        self.size = size
        self.age  = age
        self.color= color

    def __del__(self):
        print("A dog object is being delted!!!")
#--------------------End Class Dog----------------------
obj = Dog("Bull", "large", 2, "Yellow")
del obj