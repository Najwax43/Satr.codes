# List 2D

values=[1,True,'Python']
#values=[[1,2,3],True,'Python'] # عند طباعة العنصر 0 تكون النتيجة[1,2,3]
#print(values[0][2]) # النتيجة 3
print(values[0]) # يطبع على حسب رقم الاندكس


val= [[1,2,4], # index 0
        [4,5,6], # index 1
         [7,8,9]  # index 2
         ]

print(val[1][0]) # index number of list , cell index



ages= [30,9,15,22,17,44,26,5]

def flitered_ages(age):
    return age>=18
print(list(filter(flitered_ages,ages))) # Filter


numbers=[5,10,20,25,50]
sq_numbers= [] # الجذر التربيعي
def square(numbers):
    for num in numbers:
        sq_numbers.append(num**2)

    return sq_numbers
print(square(numbers))

# طريقة مختصره لايجاد التربيع باستخدام map

numbers=[5,10,20,25,50]
def square(num):
    return num**2
print(list (map(square,numbers)))


list_one=[9,5,1,8] # دالة sort لترتيب الارقام تصاعديا
list_two=['Khadijah','Asmaa','Zainab'] # دالة sort لترتيب الاستنرق ابجدياً
list_one.sort()
#list_one.sort(reverse=True) # ترتيب تنازلي
#list_two.sort(reverse=True) # ترتيب تصاعدي
print(list_one)
print(list_two)


list=[1,2,3,4]
multiplied_list=[num*2 for num in list ] # list comprehension
print(multiplied_list)

