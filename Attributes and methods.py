class Student:
    def __init__(self,name,age,id,grades): # constructor
        self.name= name
        self.age= age
        self.id= id
        self.grades= grades
    def talk(self):
        print('My name is:  ', self.name)
std1= Student('Njwa',21,'xx00',95)
std2= Student('Njoud',19,'x09',99)
print(dir(std2)) # يطبع جميع قيم الاتربيوت على هيئة لست

std2.v_hours= 16  # اضافة اتربيوت جديد
print(dir(std2))

# del std2.v_hours #  حذف اتربيوت



class Student:
    def __init__(self,name,age,id,grades, university_name): # constructor
        self.name= name
        self.age= age
        self.id= id
        self.grades= grades
        self.university_name= university_name
std1= Student('Njwa',21,'xx00',95,'king saud univeristy')
std2= Student('Njoud',21,'xx00',95,'king saud univeristy')

print(std1.university_name) # تطبيق كلاس اتربيوت
print(std2.university_name)




class Myclass:
    def set_val(self,value):
        self.value=value

    def get_val(self):
        return self.value

a=Myclass()
b=Myclass()

a.set_val(10)
a.value ='hello'
b.set_val(100)

print(a.get_val())
print(a.value)
print(b.get_val())







class MyInteger:
    def set_val(self, val):
        if (type(val)== int):
            self.val= val
        else:
            print('The value is not an integer')
    def get_val(self):
        return self.val

    def increment_val(self):
        self.val+=1

i= MyInteger()

i.set_val(9)
print(i.get_val())





class Employee:
    def __init__(self,name):
        self.name= name
        self._tel='+96655xxxxxxx'
        self.__salary=1700

emp1= Employee('Ahmed')

print(emp1.name)
print(emp1._tel)

