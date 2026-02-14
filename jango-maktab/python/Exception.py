#Exception

TypeError    #تایپ اشتباهی وارد شده برای مثال به جای عدد رشته واردشده
#print(2 + '2')

ValueError   #تایپ ها قابلیت تبدیل شدن به هم رو ندارند
#print(int('a'))

try:
    print(int('a'))
except:
    print("value Error")

try:
    print(2 + '2')
except TypeError:
    print("TypeError")
finally:                               #در هر صورت این قسمت انجام میشه چه ارور ایجاد بشه چه ایجاد نشه
    print("text")

while True:
    try:
        old= float(input("how old are you: "))
        break
    except:
        print("لطفا سن خود راوارد کنید")
        