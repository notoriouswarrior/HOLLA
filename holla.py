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

#1
# try:
#     num1 = int(input("enter first number: "))
#     num2 = int(input("enter second numner: "))
#     result = num1 / num2
#     print(f"{num1} / {num2} = {result}")
# except ZeroDivisionError:
#     print("learn math!")    

#2
# try:
#     with open('file') as file:
#         print("We found file")
# except FileNotFoundError:
#     print("Something went wrong")

#3
# try:
#     num1 = 100
#     num2 = int(input("100 / "))
#     result = num1 / num2
#     print(f"{num1} / {num2} = {result}")
# except ZeroDivisionError:
#     print("it is impossible to divide to 0") 
# except ValueError:
#     print("you entered wrong value")

#4
# try:
#     text = input("Add text to the file: ")
#     with open('file', "w") as file:
#         content =  file.write(text)
# except FileNotFoundError:
#     print("You have not created file")

#5
# try:
#     value = int(input("Enter the text "))
# except ValueError:
#     print("You did smth wrong!")
# else:
#         print(f"{value} well said")
# finally:
#     print("Your mission comleted")
#     else:

# num = int(input("Please enter the number:  "))
# if num % 2 == 0:
#     print(f"{num} - is odd")
# else:
#     print(f"{num}- is even") 

# list = []
# ammount = int(input("Enter the number of elemets in list: "))
# for i in range(1, ammount+1):
#     number = int(input("Enter the number: "))
#     list.append(number)

# print(f"the smallest number is {min(list)}")

# word = input("Enter the word and we will check if it is polyndrom.\nWord: ")
# lenth = len(word)
# for i in range(1,lenth + 1):
#     for n in range(i):
# n = int(input("Enter the number: "))
# sum = n * (n + 1) / 2
# print(sum)

# word = input("Enter the word: ")
# reversed = word[::-1]
# if reversed == word:
#     print("The word is polydrom")
# else:
#     print("the word is not polydrom")

# n = int(input("enter the number: "))
# list = 1
# while list <= n:
#     print(list)
#     list 

# rock =   """  _
# ___________
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)"""
# paper =  """"
# ___________
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)"""
# scissors =  """"
# __________
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___) """

# import random
# variants= [rock, paper, scissors]
# you = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
# user = variants[you]
# print(f"You choose {user}")
# index = random.randint(a=0,b=2)
# computer = variants[index]
# print(f"Computer choose {computer}")
# if index == 0 and you == 1:
#     print("You win!")
# elif index == 1 and you == 2:
#     print("You win!")
# elif index == 2 and you == 0:
#     print("You win!")
# elif index == you:
#     print("It's draw!")
# else:
#     print("You lost!")


filename = "file.txt"
num1 = int(input("give first number: "))
num2 = int(input("give second number: "))
condition = input("какую операцию вы хотите сделать ? a = +, b = -, c = *, d = /")
with open(filename,'w') as file:
    if condition == "a":
        sum = num1 + num2
        file.write(f"{num1} + {num2} = {sum}" )
    elif condition == "b":
        min = num1 - num2
        file.write(f"{num1} - {num2} = {min}")
    elif condition == "c":
        umn = num1 * num2
        file.write(f"{num1} + {num2} = {umn}")
    elif condition == "c":
        div = num1 / num2
        file.write(f"{num1} + {num2} = {div}")
    else:
        print("you have written wrong argument")
    
    
                   