#student record system

students = []

while True:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))
    
    students.append({'name': name, 'age': age, 'marks': marks})
    
    more = input("Add more? (y/n): ")
    if more.lower() != 'y':
        break

for s in students:
    print(f"{s['name']} | Age: {s['age']} | Marks: {s['marks']}")
