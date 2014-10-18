# general syntax/usages
# variables
name = 'Hans'
age = 54
size = 1.86
pets = ['cat', 'dog', 'fish']
children = {
	'Petra' : 19,
	'Gudrun' : 16,
	'Alfred' : 9
}

# if-else
x = 2
y = 4
if x == y:
	print(x, " equal to ", y)
elif x < y:
	print(x, " smaller than ", y)
else:
	print(x, " bigger than ", y)

# while-loop
while x < y:
	print(x, " smaller than ", y)
	x += 1

# for-loop
for i in range(0, 10):
	print("i: %d" % i)

for name in ['Hans', 'Karl', 'Peter']:
	print name

dict = {'key_1' : 'var_1', 'key_2' : 'var_2'}
for key in dict:
	print key, ":", dict[key]

for key, value in dict.items():
	print key + ": " + value


# calling functions
print "hello world"
print("hello world")

# print function knowledge
print("double: %d, float: %f, float-with-2-comma: %.2f" % (10, 1.42, 1.54321))

# defining functions
def printWord(word):
	print word

printWord("word - foo")

# classes
class FooClass:
	class_var = 'foo'
	def __init__ (self, x):
		self.inst_var = x

print "FooClass.class_var:", FooClass.class_var
# will cause error: print FooClass.inst_var
foo = FooClass(12)
print "foo.class_var:", foo.class_var
print "foo.inst_var:", foo.inst_var

class Person:
	def __init__ (self, name, age, size):
		self.name = name
		self.age = age
		self.size = size
		self.pets = []
		self.children = {} 
	
	def sayName(self):
		print "Hi my name is", self.name
	
	def oldEnough(self, reqAge):
		return reqAge <= self.age

hans = Person('Hans', 15, 1.74)
print 14, '?', hans.oldEnough(14)
print 15, '?', hans.oldEnough(15)
print 16, '?', hans.oldEnough(16)

# class inheritance
class Vehicle:
	def __init__ (self):
		self.isVehicle = True
		print "Vehicle"

class MotorVehicle(Vehicle):
	def __init__ (self):
		Vehicle.__init__(self)
		self.hasMotor = True
		print "MotorVehicle"

class WheelVehicle(Vehicle):
	def __init__ (self):
		Vehicle.__init__(self)
		self.hasWheels = True
		print "WheelVehicle"

class Car(MotorVehicle, WheelVehicle):
	def __init__ (self):
		MotorVehicle.__init__(self)
		WheelVehicle.__init__(self)
		print "Car"
	
	def sayType(self):
		print "isVehicle?", self.isVehicle
		print "hasMotor?", self.hasMotor
		print "hasWheels?", self.hasWheels
