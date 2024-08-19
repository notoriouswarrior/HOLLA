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

# r = 7 {S}")
# C = r * 2 * math.pi
# S = math.pow(r,2) * math.pi
# print(f"периметр = {C}\nплощадь = 

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

# #5
# try:
#     value = int(input("Enter the text "))
# except ValueError:
#     print("You did smth wrong!")
# else:
#         print(f"{value} well said")
# finally:
#     print("Your mission comleted")

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
# elif index == you/bin/python3 "/home/ismail/Рабочий стол/bernard/holla.py"
#     print("It's draw!")
# else:
#     print("You lost!")


# filename = "file.txt"
# num1 = int(input("give first number: "))
# num2 = int(input("give second number: "))
# condition = input("какую операцию вы хотите сделать ? a = +, b = -, c = *, d = /")
# if condition == "a":
#     sum = num1 + num2
#     result = f"{num1} + {num2} = {sum}" 
# elif condition == "b":
#     min = num1 - num2
#     result = f"{num1} - {num2} = {min}"
# elif condition == "c":
#     umn = num1 * num2
#     result = f"{num1} + {num2} = {umn}"
# elif condition == "c":
#     div = num1 / num2
#     result = f"{num1} + {num2} = {div}"
# else:
#     print("you have written wrong argument")

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# randomisor_l = random.randint(1,64)
# randomisor_n_s = random.randint(1,9)

# password = ""
# for i in range(1,nr_letters +1):
#     ranlett = random.choice(letters)
#     password += ranlett
 
# for i in range (1, nr_numbers +1):
#     rannum = random.choice(numbers)
#     password += rannum

# for i in range(1,nr_symbols +1):
#     ransym = random.choice(symbols)
#     password += ransym


# print(password)  


# import triangle_checker
# triangle_checker.TriangleChecker
     
# try:     
#     first = float(input("Введите значение а: "))
#     second = float(input("Введите значение b: "))
#     third = float(input("Введите значение с: "))
#     values = TriangleChecker(first,second,third)
#     if first < 0 or second < 0 or third < 0:
#         print("Сотрицательными числам ничего не выйдет")
#     else:
#         print(values.is_triangle()) 
# except ValueError:
#     print("Нужно вводить только числа!")


# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b 
#         self.c = c
#     def is_triangle(self):
#         if self.a + self.b > self.c:
#             return "Ура, можно построить треугольник"
#         elif self.a + self.c > self.b:
#             return "Ура, можно построить треугольник"
#         elif self.b + self.c > self.a:
#             return "Ура, можно построить треугольник"
#         else:
#             return "Жаль, но из этого треугольник нельзя сделать"
    
# try:     
#     first = float(input("Введите значение а: "))
#     second = float(input("Введите значение b: "))
#     third = float(input("Введите значение с: "))
    
#     if first <= 0 or second <= 0 or third <= 0:
#         print("С отрицательными числами ничего не выйдет")
#     else:
#         values = TriangleChecker(first, second, third)
#         print(values.is_triangle()) 

# except ValueError:
#     print("Нужно вводить только числа!")

class Nikola:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def argument(self):
        if self.name == "Николай":
            return f"Меня зовут {self.name}, мне {self.age}"
        else:
            return f"Я не '{self.name}', я Николай"
user_name = input("Как вас зовут ?: ").capitalize().strip()
user_age = input("Сколько вам лет ?: ")
values = Nikola(user_name, user_age)
print(values.argument())

        

    












