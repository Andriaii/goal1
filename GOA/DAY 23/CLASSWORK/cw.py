# def my_replace(word, replace_char, input_char):
#     changed_word = ''
    
#     for char in word:
#         if char == replace_char:
#             changed_word = changed_word + input_char
#         else:
#             changed_word = changed_word + char
    
#     return changed_word

# print(my_replace("lukaak", "a", "d"))









# # "luuuka".count("u") --> result: 3

# def my_count(collection, count_element):
#     count = 0
    
#     for element in collection:
#         if element == count_element:
#             count = count + 1
    
#     return count

# print(my_count("luuuka", "u"))










# def my_find(collection, value):
#     for index in range(len(collection)):
#         if collection[index] == value:
#             return index
#     return -1

# print(my_find([1,2,3,4,5], 8))





# #1)

# def my_list(list , list_element):
#     for index in range(len(list)):
#         if list [index] == 0 + 2:
#             return [index]
#         return -1
# print(my_list[1,2,3,4,5,6,7,8,9] , 2)



#2)

# def my_count(collection, count_element):
#     count = 0
    
#     for element in collection:
#         if element == count_element:
#             count = count + 2
    
#     return count

# print(my_count(["1","2","3","4","5","6","7","8","9","10"],"2" ,"3"))


#3)

# def my_find(find , index_find):
#     for index in range(len(find)):
#         if index == find:
#             return find
# print(my_find("1,2,3,4,5,6,7,8" , "2"))



def my_join(join_str, strings_list):
    joined_elemnts = ''
    
    for word in strings_list:
        joined_elemnts += join_str + word
    
    return joined_elemnts

print(my_join("+", ["1","2","3"]).slice(0)) 






