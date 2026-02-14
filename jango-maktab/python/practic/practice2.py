#Username and password
Username= input("Username: ")
password= input("password: ")

if Username == "admin":
    if password != "admin":
        print("incorrect password")
    else:
        print("successful login")
else:
    print("user not found")
print(30*'-')


#number_range

for item in range(1, 11):
    if item == 5:
        continue
    if item == 8:
        break
    print(item)
    
print(30*'-')

#set_list
List_1= [1,2,3,4,5]
List_2= [4,5,6,7,8]

List_all= List_1 + List_2
lst= list(set(List_all))
print(f"Repetitive: {List_all}")
print(f"No repetition: {lst}")
print(f"First three digits: {lst[0:3]}")


        