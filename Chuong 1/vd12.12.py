class Dog:

    DogCount  = 0                       #Thuộc tính của lớp/class
    #Hàm khởi tạo đối tượng
    def __init__(self, name, size, age, color):
        self.name = name                #Thuộc tính của đối tượng (object)
        self.size = size                
        self.age  = age
        self.color= color

    def Go(self):
        print("I'm going ...")          #Hành vi/ hoạt động :"Đi"

    def Stay(self, place):              #Hành vi/ hoạt động :"Ở tại"
        print("I'm staying at {}".format(place))

    def Lie(self, place):               #Hành vi/hoạt động :"Nằm"
        print("I'm lying at {}".format(place))

    def Bark(self):                     #Hành vi/hoạt động :"Sủa"
        print("Whoop,...")

    def Eat(self, food):                #Hành vi/hoạt động "Ăn"
        print("I'm eating {}".format(food))
#--------------------------End Class Dog-----------------------------
#Khởi tạo đối tượng 
Bull = Dog("Bull","large", 2, "Yellow")
Bull.Stay("garden")
Bull.Bark()