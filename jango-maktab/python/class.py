#list
'''
list_t= [1,2,3,"amir",[1,2,3]]
print(dir(list_t)), print(30*'-')
print(list_t[0])
list_t[3]= 4
print(list_t)
list_t.append(5)
list_t.insert(0, 1)
print(list_t)
print(list_t[0:5])

tuple_t= tuple(list_t)
print(tuple_t)

lst= [1,2,3,4,5,6,"amir"]
print(lst[::2])             #list[start,stop,step]
print(lst[::-2])
print(lst[6][::-1])
'''
#-------------------------------------------------------
#set
'''
list_t = [1,2,3,4,5]
set_t = {1,2,3,4,5,5,5,5}    #set = از تکرار جلوگیری میکنه

set_t.add(6)
print(set_t)

set_1= {1,2,3,4,4,5}
set_2= {4,5,6,7,8}

print(set_1 | set_2) # | = اجتماع
print(set_1 & set_2) # &(اند) = اشتراک ها
print(set_1 - set_2) 
print(set_2 - set_1)
print(set_1 ^ set_2) # ^ = اجتماع - اشتراک

#-------------------------------------------------------
#dictionary

dict_t = {'key':'name', 'value':'last name'}
#print(dict_t['key'])

dict_t['key'] = 'amir'
#print(dict_t['key'])

dict_t.get('value')
dict_t.update({'key':'hassan', 'value':'keahany', 'name':'ali'})    #برای تغیرات زیاد در دیکشنری
print(dict_t)

print(dict_t.items())
for k,v in dict_t.items():
    print(k,v)
'''
#-------------------------------------------------------
#function

def print_hello():
    even = []
    odd = []
    for item in range(0, 25):
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    print(even)
    print(odd)

print_hello()

def test(*args):
    print(args)

test(1,2,3,4)

def test(**kwargs):
    print(kwargs)

test(name='amir', lastname="hossein")
#---------------------------

def intiger():
    lst_int= input("list_number: ").split(',')
    lst_even= []
    lst_odd= []
    for it in lst_int:
        item= int(it)
        if item % 2==0:
            lst_even.append(item)
        if item % 2:
            lst_odd.append(item)
    print(f"even={lst_even}")
    print(f"odd= {lst_odd}")

intiger()

input_number = [int(item) for item in input('number: ').split(',')]
even = list(filter(lambda x: x % 2==0, input_number))
print(even)

odd = list(filter(lambda x: x % 2, input_number))
print(odd)

#-------------------------------------------------------
string = "amir, ali, hossein"
print(string[0])

string = "amir, ali, hossein"
print(string[0])

print(string.replace('a', 'm')), print(30*'-')
print(string.replace('a', 'm', 1))
#-------------------------------------------------------
#python -m pip install --upgrade pip
#pip freeze= لیستس از بسته هایی رو نمایش میده که مستقیما توسط کاربر نصب شدد
#pip list= لیستی از تمام بسته های نصب شده در محیط پایتون را نمایش میدهد
#scripts activate  our   deactivate
#python -m venv venv
#pip freeze > requirements.txt
#pip install -i https://mirror-pypi.runflare.com/simple requests

#-------------------------------------------------------
#madule
#import pyttsx3 = برای تبدیل متن به صدا
