txt="Lorem ipsum dolor sit amet, consectur adipiscing elit, sed do"
print(txt.find('do')) #   البحث عن كلمة باستخدام دالة find سيتم طباعة رقم الاندكس في حال وجوده
print(txt.find('why')) # سيتم طباعة -١ في حالة عدم وجود الكلمة
print(txt.rfind('do')) # تعطي رقم الاندكس لآخر تطابق
print(txt.rfind('why')) # سيتم طباعة -١ في حالة عدم وجود الكلمة
print(txt.rfind('Do')) # سيتم طباعة -١ في حالة عدم وجود الكلمة
print(txt.rfind('it',50,60)) #البحث عن كلمة في نطاق معين



text= 'A,B,C'
string_to_list=text.split() # تحويل النص الى قائمة
print(string_to_list)

words= 'This is a string'
string_to_list=words.split('s') # # يقتص حرف s عن الجملة ويطبعها
#string_to_list=words.split('s',1) # عدد مرات فصل الحرف
print(string_to_list)


alphabet= 'C, D, E ,F '
to_string=alphabet.split(',')
to_string=''.join(to_string) # تتحول الى نص
#to_string='#'.join(to_string) # تتحول الى نص
print(to_string)



values= 'A987'
#values= 'A9 87' # false ما تحتسب المسافة
print(values.isalnum()) # للتحقق من وجود النص

value='987'
print(value.isdigit()) # التحقق من انه digit


val='1\n2\n3\n4\n5\n6'
print(val.replace('\n', ',')) #  العنصر المراد استبداله\n ، البديل ,


txxt='          Python Course'
print(txxt.strip()) # للتخلص من المسافات

t='          Python Course      '
print(t.lstrip()) # للتخلص من المسافات من اليسار
#print(t.rstrip()) #للتخلص من المسافات من اليمين


str='This is Python Course'
print('The lower case converted string is: '+str.lower()) # التلاعب في النص وتحويله الى احرف صغيره
#print('The lower case converted string is: '+str.upper()) # التلاعب في النص وتحويله الى احرف كبيرة
#print('The lower case converted string is: '+str.swapcase()) # التلاعب في النص وتحويل الاحرف الكبيرة الى صغيرة والعكس
#print('The lower case converted string is: '+str.title()) # التلاعب في النص وتحويل بداية حرف كل كلمة الى حرف كبير



first_name= 'Najwa'
last_name= ' Almalki'
age=25
print('My name is {} {}, and Iam {} years old'.format(first_name,last_name,age)) # format







