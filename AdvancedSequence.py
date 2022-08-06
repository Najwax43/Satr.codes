# Advanced Sequence
alphabet='abcdefghijklmnopqrstuvwxyz'
print(alphabet[2])

the_list=[1,2,3]
the_tuple=(1,2,3)
print(the_list[0:1:2]) #  index with step (2)
print(the_tuple[2]) #index


text='This is python course'
print(text[8:14]) # لطباعة حروف في نطاق معين ( from:to)
print(text[8:]) # من العنصر الثامن الى الاخير
print(text[:7]) # من البداية الئ العنصر السابع
print(text[:]) # يطبع الحروف جميعها
print(text[-6:]) # يبدأ العد من آخر عنصر من اليمين الى يسار


letters='qeroykislswex'
s=slice(0,5) # slice by another way
print(letters[s])



the_list=[1,2,3]
the_tuple=(1,2,3)
s=slice(0,5,2) # slice by another way
print(the_list[s])
print(the_tuple[s])


txt="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do"
the_list=[1,2,3,4]
the_tuple=(4,5)
print(txt.index('do')) # للتحقق من وجود العنصر في الجملة
print(len(txt)) # معرفة عدد عناصر التكست
print('do'in txt ) # للتحقق من وجود كلمة في الجملة
print('Do'not in txt ) # للتحقق من عدم وجود كلمة في الجملة





list=[1,2,3,4,5]
tuple=(1,2,3,4,5)
print(list.index(4)) # سيتم طباعة رقم الاندكس المخصص للرقم المراد طباعته
print(tuple.index(2))  # سيتم طباعة رقم الاندكس المخصص للرقم المراد طباعته


words= 'This is the student Noora'
print(words.count('s')) # لمعرفة كم مرة تكرر حرف معين



first_name= ' Najwa '
Second_name= 'Anwar'
print(first_name+''+Second_name) # الدمج
print(first_name*3) # للتكرار
