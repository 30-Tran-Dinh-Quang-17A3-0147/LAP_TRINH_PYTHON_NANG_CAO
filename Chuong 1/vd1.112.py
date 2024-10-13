class Dog:                  #Ví dụ minh họa về thuộc tính tĩnh static attribute
    # Thuộc tính lớp - Thuộc tính tĩnh
    DogCount = 0
    def __init__(self, name, size, age, color):
        self.name = name # Thuộc tính đối tượng
        self.size = size 
        self.age = age 
        self.color = color 
        Dog.DogCount = Dog.DogCount + 1

    def __del__(self):
        print("A dog object is being deleted!!!")
        Dog.DogCount = Dog.DogCount - 1
#-----------------------------------End class Dog---------------------------------
#Tạo các đối tượng Dog
obj1 = Dog("Bull", "large", 2, "yellow")
obj2 = Dog("Poodle", "small", 1, "white")

print("Number of dogs : {}".format(Dog.DogCount))