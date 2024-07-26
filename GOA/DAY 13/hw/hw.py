for i in range(1,10 + 1):
    print(i)



for i in range(1,10 + 1):
        if i %2 == 0:
         print(i , "is even")




num = float(input("enter your number : "))
if num > 0:
    print("positive number")
elif num < 0:
    print("negatitive number")
else:
    print("zero")        




user_name = input("enter your name :")
password = input("enter your password :")
if user_name == "andria" and password == "abc123":
    print("login sucsesful")
else:
    print("login failed")



i = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
while i:
    print(i)
    break
if i == 5:
    print("stop")
else:
    print("nothing")




for i in range(1,10 + 1):
    print(i)
if i %3:
    print("fizz")
elif i %5:
    print("buzz")
elif i %3 or 5:
    print("fizz buzz")