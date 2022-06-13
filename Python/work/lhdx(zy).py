# class vehicle(object):
#     def printm(self):
#         print("%s"%"能移动")
# class train(vehicle):
#     def printm(self):
#         print("%s"%"有轨道")
# class automobile(vehicle):
#     def printm(self):
#         print("%s"%"有笼子")

# class aircraft(vehicle):
#     def printf(self):
#         print("%s"%"有翅膀")

# class car(automobile):
#     def printf(self):
#         print("%s"%"只载人")

# class truck(automobile):
#     def printf(self):
#         print("%s"%"可以载货物")


class Vehicle:
    def move(self):
        print('我是交通工具，我能移动')
 
		
class Train(Vehicle):
	def track(slef):
		print('我可以在轨道上高速行驶')
 
		
class Automobile(Vehicle):
	def tire(self):
		print('我是汽车，我有轮胎')
 
		
class Aircraft(Vehicle):
	def wing(self):
		print('我有翅膀，我会飞')
 
		
class Car(Automobile):
	def __init__(self, color):
		self.color = color
	def manned(self):
		print('我是客车，只能载客')
 
		
class Truck(Automobile):
	def van(self):
		print('我是卡车，可以载货')
 
		
class AircraftCar(Aircraft, Car):
	def __init__(self, color):
		super(AircraftCar, self).__init__(color)
 
		
train = Train()
train.move()

train.track()

ab = Automobile()
ab.move()

ab.tire()

plane = Aircraft()
plane.move()

plane.wing()

car = Car('red')
car.move()

car.tire()

car.manned()

t = Truck()
t.move()

t.tire()

t.van()

ac = AircraftCar('red')
ac.move()

ac.tire()

ac.wing()

ac.manned()

ac.color
'red'