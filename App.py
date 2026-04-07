# 1 Full name string

s = "Huzaima Siddiq"
print(s)


# 2 Sentence length

s = "Python is a powerful programming language"
print(len(s))


# 3 Check data type

text = "Hello Python"
print(type(text))


# 4 First character

word = "Python"
print(word[0])


# 5 Last character

text = "Programming"
print(text[-1])


# 6 Second last character

language = "Machine"
print(language[-2])


# 7 First character into new variable

fruit = "Apple"
x = fruit[0]
print(x)


# 8 Last character into new variable

city = "Karachi"
y = city[-1]
print(y)


# 9 Character at index 3

course = "Python"
print(course[3])


# 10 Character at index -4

framework = "TensorFlow"
print(framework[-4])


# 11 Swap first & last characters

tool = "GitHub"
new_string = tool[-1] + tool[1:-1] + tool[0]
print(new_string)


# 12 Middle character

animal = "Elephant"
middle = animal[len(animal)//2]
print(middle)


# 13 Replace first character

device = "Laptop"
new_device = "M" + device[1:]
print(new_device)


# 14 First four characters

word = "Developer"
print(word[:4])


# 15 Characters index 3 to 8

name = "University"
print(name[3:8])


# 16 Middle three characters

language = "JavaScript"
mid = len(language)//2
print(language[mid-1:mid+2])


# 17 Excluding first three characters

fruit = "Pineapple"
print(fruit[3:])


# 18 Excluding last four characters

city = "Islamabad"
print(city[:-4])


# 19 Every second character

framework = "Django"
print(framework[::2])


# 20 Every third character

animal = "Kangaroo"
print(animal[::3])


# 21 Reverse skipping two characters

vehicle = "Motorcycle"
print(vehicle[::-3])


# 22 Index 1 to 7 skipping 2

word = "Innovation"
print(word[1:7:2])


# 23 Every third character from index 1

language = "PythonProgramming"
print(language[1::3])


# 24 Characters from -10 to -5

text = "ArtificialIntelligence"
print(text[-10:-5])


# 25 Last four characters reversed

city = "Islamabad"
print(city[:-5:-1])


# 26 Reverse string

tool = "VisualStudio"
print(tool[::-1])


# 27 Except last three characters

company = "Facebook"
print(company[:-3])


# 28 Characters from -8 to -3 skipping 1

device = "Smartphone"
print(device[-8:-3:2])


# 29 Last six characters

word = "Innovation"
print(word[-6:])


# 30 Characters from -7 to -3

fruit = "Blueberry"
print(fruit[-7:-3])


# 31 Concatenate strings

word1 = "Hello"
word2 = "World"
print(word1 + word2)


# 32 Repeat string 3 times

text = "Python"
print(text * 3)


# 33 Uppercase

fruit = "Apple"
print(fruit.upper())


# 34 Lowercase

city = "Karachi"
print(city.lower())


# 35 Starts with D

framework = "Django"
print(framework.startswith("D"))


# 36 Ends with b

tool = "GitHub"
print(tool.endswith("b"))


# 37 Count “o”

company = "Google"
print(company.count("o"))


# 38 Alphabetic check

subject = "Mathematics"
print(subject.isalpha())


# 39 Replace bike → cycle

vehicle = "Motorbike"
print(vehicle.replace("bike","cycle"))


# 40 Index of p

device = "Smartphone"
print(device.index("p"))


# 41 Count n

word = "Innovation"
print(word.count("n"))


# 42 Numeric check

name = "Algorithm"
print(name.isnumeric())


# 43 Replace Blue → Red

fruit = "Blueberry"
print(fruit.replace("Blue","Red"))


# 44 Contains Prog

language = "PythonProgramming"
print("Prog" in language)


# 45 Remove spaces

name = "   Data Science   "
print(name.strip())


# 46 Split string

fruit = "Apple,Banana,Cherry"
print(fruit.split(","))


# 47 Join list

city = ["Karachi","Lahore","Islamabad"]
print("-".join(city))


# 48 Capitalize

company = "google"
print(company.capitalize())


# 49 Uppercase check

animal = "ELEPHANT"
print(animal.isupper())


# 50 Email lowercase

email = input("Enter email: ")
print(email.lower())


# 51 Remove extra spaces

country = input("Enter country name: ")
print(country.strip())


# 52 Username alphabet check

username = input("Enter username: ")
print(username.isalpha())


# 53 Digit check

number = input("Enter number: ")
print(number.isdigit())


# 54 Replace spaces with underscores

sentence = input("Enter sentence: ")
print(sentence.replace(" ","_"))


# 55 Replace old word with new

sentence = input("Enter sentence: ")
old = input("Old word: ")
new = input("New word: ")
print(sentence.replace(old,new))


# 56 Count character occurrences

word = input("Enter word: ")
char = input("Enter character: ")
print(word.count(char))


# 57 Swap case

word = input("Enter word: ")
print(word.swapcase())


# 58 Billing system

price = float(input("Enter item price: "))
total = price * 3
print(total)


# 59 Age registration check

age = int(input("Enter age: "))
print(age >= 18)


# 60 Temperature check

temp = float(input("Enter temperature: "))
print(temp > 37)


# 61 Discount calculator

price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))
final_price = price - (price * discount / 100)
print(final_price)


# 62 Apples remaining
# Operator used: subtraction (-)

total = int(input("Total apples: "))
given = int(input("Given apples: "))
print(total - given)


# 63 Who is older
# Operator used: greater than (>)

age1 = int(input("Age friend 1: "))
age2 = int(input("Age friend 2: "))

if age1 > age2:
    print("Friend 1 is older")
else:
    print("Friend 2 is older")


# 64 Name & age (f-string)

name = input("Enter name: ")
age = input("Enter age: ")
print(f"Hello, my name is {name} and I am {age} years old.")


# 65 Price formatting

price = float(input("Enter price: "))
print(f"The price of the product is ${price:.2f}")


# 66 City temperature (format)

city = input("Enter city: ")
temp = input("Enter temperature: ")
print("The temperature in {} is {}°C today.".format(city,temp))


# 67 Distance traveled

speed = float(input("Enter speed: "))
time = float(input("Enter time: "))
distance = speed * time
print(distance)