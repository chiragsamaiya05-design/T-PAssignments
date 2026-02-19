class Car:
   total_car = 0

   def __init__(self,brand,model):#constructor
      self.__brand = brand
      self.__model = model
      Car.total_car += 1

   def get_brand(self):
      return self.__brand

   def full_name(self):
      return f"{self.__brand}{self.__model}"
   
   def fuel_type(self):
      return "petrol or diesel"
   
   @staticmethod  #Decorators
   def general_descrip():
      return "Car is a big Toy"

   @property
   def model(self):
      return self.__model
   




class ElectricCar(Car):
   total_Elec_Car =0
   def __init__(self, brand, model,battSize):#new Attri is battSize
      super().__init__(brand, model)
      self.battSize = battSize
      ElectricCar.total_Elec_Car +=1


   def fuel_type(self):
      return "Electric Charge"
   
"""""
my_car = Car( "Toyota","Hilux")
#my_car.model = "  Fortuner"
print(my_car.full_name())

print(my_car.model)
"""""
""""
my_sec_car = Car("Tata","Safari")

print(my_sec_car.brand)
print(my_sec_car.model)


my_Elec_car = ElectricCar("Tesla","S",5000)
print(isinstance(my_Elec_car,ElectricCar))

print(my_Elec_car.battSize)
print(my_Elec_car.model)
print(my_Elec_car.brand)
print(my_Elec_car.full_name())

print(my_Elec_car.get_brand())
#print(my_Elec_car.__brand)#not access outside the class(private)
print(my_Elec_car.fuel_type())

car1 = Car("tata","Nexon")
car2 = Car("Tata","Punch")
car3 = Car("kia","Seltos")

print("no. of Car: "+f"{Car.total_car}")

test = Car("test","test")
print("No. of  Cars: "+f"{test.total_car}")

print("no. of  Electric Car: "+f"{ElectricCar.total_Elec_Car}")
"""""

print(Car.general_descrip())

