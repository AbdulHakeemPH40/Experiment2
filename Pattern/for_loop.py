# for variable in iterable:
    # code block to execute

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

for char in 'Python':
    print(char)

person = {'name': 'John', 'age': 30}
for key, value in person.items():
    print(f'{key}: {value}')

for i in range(5):  # Iterates from 0 to 4
    print(i)
print("="*50)
for i in range(1, 10, 2):  # Iterates from 1 to 9 with a step of 2
    print(i)

print("="*50)

for number in range(10):
    if number == 5:
        break
    print(number)  # Prints numbers 0 to 4

print("="*50)

for number in range(10):
    if number % 2 == 0:
        continue
    print(number)  # Prints odd numbers only

print("="*50)

for number in range(3):
    print(number)
else:
    print("Loop completed without break.")

print("="*50)

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)  # Prints pairs of i and j

print("="*50)

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f'Index {index}: {fruit}')

print("="*50)