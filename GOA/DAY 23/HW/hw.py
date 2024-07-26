def descending_order(num):
    num = str(num)
    num = list(num)
    
    new_arr = []
    for x in num:
        new_arr.append(int(x))
    new_arr.sort(reverse = True)
    
    res_str = ""
    for i in new_arr:
        res_str += str(i)
    return int(res_str)





def square_digits(num):
    res_str = ""
    num_str = str(num)
    for i in num_str:
        res_str += str(int(i)**2)
    return int(res_str)



def bmi(weight, height):
    body_mass_syntax = weight/(height ** 2)
    if body_mass_syntax <= 18.5:
        return "Underweight"
    elif body_mass_syntax <= 25.0:
        return "Normal"
    elif body_mass_syntax <= 30.0:
        return "Overweight"
    else:
        return "Obese"
    



def grow(arr):
    product = 1
    for num in arr:
        product *= num
    return product