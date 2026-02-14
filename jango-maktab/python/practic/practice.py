import random

#odd or even
random_number= random.randint(0,40)
def odd_or_even(random_number):
    if random_number % 2==0:
        return f"even:{random_number}"
    else:
        return f"odd:{random_number}"

print(odd_or_even(random_number)), print(30*'-')

#number range
def input_number(number):
    n= 0
    list_range = [item for item in range(number+1)]
    
    # for item in list_range:
    #     n= n + item

    list = sum(list_range)
    return {"محدوده":list_range, 'مجموع':list}
    
print(input_number(3)), print(30*'-')

#numbers_and_letters
def numbers_and_letters():
    text_input= input("text: ")
    character= []
    number= []
    for item in text_input:
        if item.isalpha():
            character.append(item)
        elif item.isdigit():
            number.append(item)
    return {"character":len(character), "number":len(number)}

print(numbers_and_letters())