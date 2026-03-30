num_1 = 250
num_2 = 150

num_3 = num_1 + num_2
print(num_3)

num_3 = num_1 - num_2
print(num_3)

num_3 = num_1 * num_2
print(num_3)

num_3 = num_1 / num_2
print(num_3)

num_1 = 10
num_2 = 5

num_3 = num_1 / num_2
num_4 = num_1 // num_2
print(num_3, num_4)

num_1 = 8
num_2 = 2

num_3 = num_1 ** num_2
print(num_3)

num_1 = 15
num_2 = 4

num_3 = num_1 % num_2
print(num_3)

num_1 = 9
num_2 = 5

num_3 = num_1 % num_2
print(num_3)

num_1 = 20
num_2 = 10

num_3 = num_1 == num_2
print(num_3)

num_3 = num_1 != num_2
print(num_3)

num_3 = num_1 < num_2
print(num_3)

num_3 = num_1 > num_2
print(num_3)

name = "Alisa"
num = 25

result = name == "Alisa" and num > 10
print(result)

result = name == "Marc" or num == 25
print(result)

result = name == "Alisa" and num < 10
print(result)

message = "Hello Alisa, you my best friend!"
print(name in message)
print(name not in message)

name = "Rita"
age = 18
animal = "cat"
print("Rita" in name and age == 18 and animal == "cat")
print("t" not in name or age == 18 and animal != "bird")
print("Rita" in name or age >= 18 and animal == "cat")
print("a" in name and age > 10 and animal == "cat")
print("Rita" in name and age == 18 or "dog" in animal)