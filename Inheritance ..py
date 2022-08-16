
class Car:
    def __init__(self,company,owner,color,speed):
        self.company=company
        self.owner=owner
        self.color=color
        self.speed=speed

    def move(self):
        pass
    def stop(self):
        pass



class Truck:
    def __init__(self,company,owner,color,speed):
        self.company = company
        self.owner = owner
        self.color = color
        self.speed = speed
    def move(self):
        pass

    def stop(self):
        pass



class Vehicle:
    def __init__(self,company,owner,color,speed):
        self.company = company
        self.owner = owner
        self.color = color
        self.speed = speed

    def move(self):
        print('The car has moved')
    def stop(self):
        print('The car has moved')

class car(Vehicle):
    def disply(self):
        print('This is the car class')

car1= Car('jeep','nada','black',0)
print(car1.company)
car1.move()





class Animal:
    def __init__(self,name,color):...

    def run(speed):...

    def make_sound(self):
        print('sound...')

class Cat(Animal): # Overriding
    def make_sound(self):
        print('mew')

cat1= Cat('lili','brown')
cat1.make_sound()







class Grandparent:#Multilevel Inheritance
    def g_display(self):
        print('This is Grandparent class')

class Parent(Grandparent):
    def p_display(self):
        print('This is parent class')

class Child(Parent):
    def c_display(self):
        print('This is Child class')

child1= Child()
child1.c_display()
child1.p_display()
child1.g_display()



class Polygon:
    def p_display(self):
        print('This is polygon')

class Shape:
    def sh_display(self):
        print('This is shape class')

class Square(Polygon,Shape):
    def s_display(self):
        print('This is Square class')

sq= Square()
sq.s_display()
sq.sh_display()
sq.p_display()




class A: # MRO
    def do_this(self):
        print('Doing this in class A')

class B(A):
    pass

class C:
    def do_this(self):
        print('Doing this in class C')

class D(B,C):
    pass

obj= D()
obj.do_this()

print(D.mro()) # ترتيب الكلاسات حسب الاولوية






class Person:
    def __init__(self,first_name,surname,tel):
        self.first_name=first_name
        self.surname=surname
        self.tel=tel

    def full_name(self):
        return self.first_name+ " "+self.surname

class Employee(Person):
    def __init__(self,first_name,surname,tel,salary):
      super().__init__(self,first_name,surname,tel)
      self.salary=salary


    def give_raise(self,amount):
        self.salary=self.salary+ amount


emp1= Employee(1700,'Ali','Ahmed','+96655xxxxxxxx')




class Student:
    def print_info(self):
        print('This is the code for class Student')

class Teacher:
    def print_info(self):
        print('This is the code for class Teacher')

student1= Student()
teacher1= Teacher()

student1.print_info()
teacher1.print_info()



class Circle: #Polymorphism
    def draw(self):
        print('The code for drawing the circle')

class Square:
    def draw(self):
        print('The code for drawing the square')

class Triangle:
    def draw(self):
        print('The code for drawing the triangle')

circle1= Circle()
square1=Square()
triangle1=Triangle()

shapes= [circle1,square1,triangle1]


for sh in shapes:
    sh.draw()

