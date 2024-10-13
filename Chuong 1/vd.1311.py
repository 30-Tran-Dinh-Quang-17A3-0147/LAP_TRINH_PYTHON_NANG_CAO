class Dog:                  #Ví dụ minh họa về ENCAPSULATION
    # Thuộc tính lớp/Thuộc tính tĩnh
    __DogCount = 0                  #DocCount là thuộc tính private
    def __init__(self, name, size, age, color):
        self._name = name      #Thuộc tính protected đối tượng (object)
        self._size = size      #Thuộc tính protected đối tượng (object)
        self.__age = age       #private
        self.__color = color   #private
        Dog.DogCount = Dog.__DogCount + 1
#-----------------------------------End class Dog---------------------------------
#Tạo các đối tượng Dog
obj = Dog("Bull", "large", 2, "yellow")

print("Number of dogs :{}".format(Dog.__DogCount))