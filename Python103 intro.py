class Student: # انشاء كلاس
    def __init__(self,name,age,id,grades):
       self.name= name
       self.age=age
       self.id=id
       self.grades=grades

    def talk(self):
         print('My name is:  ', self.name)

std1= Student('Nouf',21,'xx00',95) #  انشاء اوبجكت
print(std1.name)
std1.talk()



class Student:
    def talk(self): # الاوبجكت اللذي قام بإستدعاء المثود في هذي النقطة
        print(self) # ممكن نعطيها اي اسم بدل self

std1= Student()
std2 = Student()

std1.talk()
std2.talk()


class Student:
    def __init__(self,name,age,id,grades): # constructor
        self.name= name
        self.age= age
        self.id= id
        self.grades= grades
    def talk(self):
        print('My name is:  ', self.name)
std1= Student('Njwa',21,'xx00',95)
print(std1.name)
