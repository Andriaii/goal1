# def start_to_finish(start,end,step):
#     numbers =[]

#     while start < end:
#         numbers.append(start)
#         start = start + step
#     return numbers


# print(start_to_finish(10,50 + 0,4))






# ჩვენ return ფუნქცია იმაში გვჭირდება იმისათვის რომ ჩვენ გამვიტანოთ 
# ის ფუნქციები რომელსაც print ფუნქციით ვერ გამოვიტანთ და range 
# ფუნქციით კი ჩვენ გამოგვაქვს დასაწყისი რიცხვიდან დასამთავრებელ 
# რიცხვამდე გამოაქვს 






# def filter(collection,meaning):
#     stuff = ["house","decor","bed","couch"]
#     while stuff > collection:
#         stuff = ["house","decor"]
#     for stuff in meaning:
#         return stuff
    
# def triangle_formula(formula,triangle_formula):
#     triangle = int(input("pls enter a num for a triangle :"))
#     if triangle * 3:
#         return triangle
    

# print("a^2 + b^2 = c^2")







# def name_leangth(small_name,big_name):
#     name = input("pls enter youre name :")

#     if name == 5:
#         print(big_name)

#     elif name == 4:
#         print(small_name)
#     else:
#         print("small or big")





# def manual_sum(number_list, starting_value = 0):
#     result = starting_value

#     for num in number_list:
#         result = result + num
    
#     return result


# print(manual_sum([1,2,3,4,5]))





# def manual_max(number_list):
#     max_value = number_list[0]

#     for num in number_list:
#         if max_value < num:
#             max_value = num
    
#     return max_value

# print(manual_max([1,2,3,4,5]))



# def manual_min(number_list):
#     min_value = number_list[0]

#     for num in number_list:
#         if min_value > num:
#             min_value = num
    
#     return min_value

# print(manual_min([1,2,3,4,5]))




# def manual_len(collection):
#     count = 0

#     for _ in collection:
#         count = count + 1
    
#     return count

# print(manual_len([1,2,3,4,5]))
# print(manual_len("Luka"))
# print(manual_len(range(10)))





def minimum(arr):
    mini = arr[0]
    if mini == arr :
        mini = mini - 1
    return mini








