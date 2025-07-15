#EASY

# Q1: Create a list of 5 fruits and print the 3rd fruit.
fruits = ['mango', 'apple', 'banana', 'pineapple', 'grape']
print(fruits[2])
print(len(fruits))


# Q2: Create a dictionary of your profile (name, age, language) and print your name.
profile = {
  'name' : 'Raj',
  'age' : 22,
  'language' : 'marathi'
}
print(profile['name'])


#MEDIUM
# Q3: Create a set with duplicate items and print the result.
set1 = {1, 3, 5, 5, 3, 6, 8, 10}
print(set1) #Output is {1, 3, 5, 6, 8, 10}


# Q4: Use a loop to print even numbers from 1 to 20.
for i in range(2, 21, 2):
  print(i)


# Q5: Write a program that checks if a number is positive, negative, or zero.
num = int(input("Enter a number : "))
if num > 0:
  print("Positive")
elif num < 0:
  print("Negative")
elif num == 0:
  print("Zero")
else:
  print("Error!!!")


#HARD
# Q6: Make a program that takes 5 student names and scores as input and stores them in a dictionary.
students = {}
for i in range(5):
  name = input(f"Enter name of student {i+1}: ")
  score = int(input(f"Enter score of {name}: "))
  students[name] = score
print("\nStudent Record:")
for name, score in students.items():
    print(f"{name}: {score}")


# Q7: Write a program using while loop to reverse a number (e.g., 12345 -> 54321)
#cant do it