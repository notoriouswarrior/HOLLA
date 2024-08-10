# class Car():
#     def __init__(self, made, model, year):
#         self.made = made
#         self.model = model
#         self.year = year 
    
#     def CarPark(self):
#         return f"{self.made},{self.model}"
    

# # class Shape():
#     def __init__(self):
#         pass
#     def area(self)
    
# class Task():
#     def __init__(self, title, description, status) -> None:
#         self.title = title 
#         self.description = description
#         self.status = status

#     def scentence(self):
#         return (f"TASK - {self.title} \nDESCRIPTION - {self.description} \nSTATUS - {self.status}")

# c = input("Status \n")
# b = input("Description\n")
# c = input("Status \n")
# result = Task(a,b,c)
# print(result.scentence)


# import math
# a = 3
# b = 4
# gepotenuzakv = (math.pow(a,2) + math.pow(b,2))
# gepotenuza = math.sqrt(gepotenuzakv)
# print(gepotenuza)


# import math

# x = math.pi/4
# f = math.sin(x) + math.cos(x)
# print(f)

# import math

# r = 7 
# C = r * 2 * math.pi
# S = math.pow(r,2) * math.pi
# print(f"периметр = {C}\nплощадь = {S}")

# a = int(input(f"enter the number to check\n"))
# if a % 2 == 0:
#     print(f"the number {a} is even")
# else:
#     print("theh number {a} is odd")    


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: " )

# bill = 0 
# if size == "S":
#     bill+= 15 
# elif size == "M":
#     bill+= 20
# elif size == "L":
#     bill+= 25
# else:
#     "We don't have pzza with such size"

# print(f"${bill}")
# peperoni = input("Do you want peperoni in your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese in your pizza? Y or N: ")
# if peperoni == "Y":
#     bill += 3
# if extra_cheese == "Y":
#     bill += 1

# print(f"${bill}")

# try:
#     file_txt = input("Write your own essay")
#     if file_txt:
#         with open('example.txt', 'w') as file:
#             content = file.write(file_txt)
#             if (content):
#                 print(f"Your file is created!")
#             else:
#                 print("Something went wrong")
#     else:
#         print("Write one more time")
#         file = input("Write your own essay")
# except FileNotFoundError:
#     print("Sorry. Your file is not readable")
# except IOError:
#     print("Error!")
# finally:
#     print("Thank you good bye!")

# try:
#     num1 = int(input("enter first number: "))
#     num2 = int(input("enter second numner: "))
#     result = num1 / num2
#     print(f"{num1} / {num2} = {result}")
# except ZeroDivisionError:
#     print("learn math!")    


# try:
#     with open('file') as file:
#         print("We found file")
# except FileNotFoundError:
#     print("Something went wrong")

# try:
#     num1 = 100
#     num2 = int(input("100 / "))
#     result = num1 / num2
#     print(f"{num1} / {num2} = {result}")
# except ZeroDivisionError:
#     print("it is impossible to divide to 0") 
# except ValueError:
#     print("you entered wrong value")

# try:
#     text = input("Add text to the file: ")
#     with open('file', "w") as file:
#         content =  file.write(text)
# except FileNotFoundError:
#     print("You have not created file")

# try:
#     value = int(input("Enter the text "))
#     if (value):
#         pass
#     else:
#         print("smth went wrong")
# finally:
#     print("Your mission comleted")