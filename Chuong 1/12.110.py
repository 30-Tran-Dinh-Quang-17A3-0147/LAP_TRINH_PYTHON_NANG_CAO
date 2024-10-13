class Dog:
    # Thuộc tính lớp
    DogCount = 0
    def __init__(self, name, size, age, color):
        self.name = name # Thuộc tính đối tượng
        self.size = size 
        self.age = age 
        self.color = color 
        
    @classmethod
    def CreateDog(cls, name, size, age, color):
        cls.DogCount = cls.DogCount + 1
        return cls(name, size, age, color)
    
    @classmethod
    def get_dog_count(cls):
        return cls.DogCount
    
obj = Dog.CreateDog("bull", "large", 2, "yellow")
print("Số lượng đối tượng Dog đã được tạo:",
Dog.get_dog_count())

obj2 = Dog.CreateDog("poodle", "small", 1, "white")
print("Số lượng đối tượng Dog đã được tạo:",
Dog.get_dog_count()) 