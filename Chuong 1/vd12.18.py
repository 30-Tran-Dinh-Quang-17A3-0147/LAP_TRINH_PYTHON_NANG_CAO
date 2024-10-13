class Dog:              
    "'Ví dụ minh họa các hàm thuộc tính lớp tích hợp.'"
    #Hàm khởi tạo đối tượng
    def __init__(self, name, size, age, color):
        self.name = name            #Thuộc tính của đối tượng (object)
        self.size = size
        self.age  = age
        self.color= color

    def display_details(self):
        print("Name : %s, size:%s, age:%s, color:%s"%(self.name, self.size, self.age, self.color))
#-----------------------------------End class Dog------------------------------
bull = Dog("Dom", "Large", 2, "Yellow")
print(bull.__doc__)
print(bull.__dict__)
print(bull.__module__)