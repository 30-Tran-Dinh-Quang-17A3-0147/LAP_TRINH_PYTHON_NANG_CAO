class Dog:                  #Ví dụ minh họa về đối tượng
    # Thuộc tính lớp/Thuộc tính tĩnh
    DogCount = 0
    species = 'Dog'
    def __init__(self, name, size, age, color):
        self.name = name # Thuộc tính đối tượng (object)
        self.size = size 
        self.age = age 
        self.color = color 
#-----------------------------------End class Dog---------------------------------
#Tạo các đối tượng Dog
obj1 = Dog("Buddy", "Medium", 5, "brown")
obj2 = Dog("Max", "small", 3, "black")

print("obj1 is a {}".format(obj1.__class__.species))
print("obj2 is also a {}".format(obj2.__class__.species))
#Truy cập đến các thuộc tính đối tượng
print("{} is {} year old.".format(obj1.name,obj1.age))
print("{} is {} year old.".format(obj2.name,obj2.age))
print("{} is {} color.".format(obj2.name,obj2.color))