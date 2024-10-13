class Dog:                  #Ví dụ minh họa về phương tĩnh static method
    # Thuộc tính lớp
    DogCount = 0
    def __init__(self, name, size, age, color):
        self.name = name # Thuộc tính đối tượng
        self.size = size 
        self.age = age 
        self.color = color 
        Dog.DogCount = Dog.DogCount + 1

    @staticmethod
    def Report():
        print("Tổng số đối tượng Dog : {}".format(Dog.DogCount))
#-----------------------------------End class Dog---------------------------------
#Tạo các đối tượng Dog
doc1 = Dog("Buddy", "Medium", 5, "brown")

doc2 = Dog("Max", "small", 3, "black")

#Sử dụng phương tĩnh Report() để lấy/báo cáo số lượng Dog  được tạo ra
doc1.Report()