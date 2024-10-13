class Dog:              #Ví dụ DEMO về phương thức dựng sẵn của lớp

    DogCount = 0
    #Hàm khởi tạo đối tượng
    def __init__(self, name, size, age, color):
        self.name = name            #Thuộc tính của đối tượng (object)
        self.size = size
        self.age  = age
        self.color= color
#--------------------End Class Dog----------------------
bull = Dog("Bull", "large", 2, "Yellow")

#In ra thuộc tính name của đối tượng bull
print(getattr(bull, 'name'))

#Gọi phương thức setattr() để gán lại giá trị age cho đối tượng 
setattr(bull, 'age', 3)
#In ra gias trị tuổi của bull
print("Con chó Bull bây giờ đã", getattr(bull, 'age'), "tuổi.")

#Kiểm tra đối tượng có thuộc tính 'color' hay không ?!
print(hasattr(bull, 'color'))

#Xóa đi thuộc tính 'age'
delattr(bull, 'age')

#kích hoạt Lỗi nếu thuộc tính "age" đã bị xóa 
print(bull.age)