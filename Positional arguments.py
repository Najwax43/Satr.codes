def info(name,age):
    print('My name is',name,'and I am',age,'Years old')

info('Najwa',25) # لازم نفس عدد البراميتر في الفانكشن
#info ( name=' Najwa' , age= 25) # Key words
#info ( name=' Najwa' , 25) # خطأ لازم البوسشنال ارقمنت يكون في البداية ويتنفذ
#info(25, name=' Najwa')  # لازم نغير ترتيب البراميتر في الفانكشن (العمر ثم الاسم)


def info(name=' Nai',age=25,course ='python'):

    print('My name is'+name,' I am ',age,' Years old and im taking '+course +' course')

info() # ديفولت - ولو كتبنا قيمة بداخل الاقواس يتم طباعتها


def avg(*args): # Argument packing
    total= sum(args)
    leng= len(args)

    average=total / leng
    print(average)
avg(2,6) # عدد لا محدود من الارقمنت




def my_func(*items):
    print(items)

items= ['a','b','c']
my_func(*items) # بدون الاستار يطبعها (['a', 'b', 'c'],)



def info(**kwargs): # Dictionary Packing
    print(kwargs)
    print(type(kwargs))
info(name= 'Ali', age=17 )



