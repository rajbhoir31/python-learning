class Student:
    total_students = 0

    def __init__(self, name, roll, marks, stream):
        self.name = name
        self.roll = roll
        self._marks = marks
        self.stream = stream
        Student.total_students += 1

    def __str__(self):
        return f"{self.name} | Roll: {self.roll} | Stream: {self.stream}"

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, new_marks):
        if any(m < 0 for m in new_marks):
            raise ValueError("Marks cannot be negative.")
        self._marks = new_marks

    @property
    def total_marks(self):
        return sum(self._marks)

    @property
    def average(self):
        return round(sum(self._marks) / len(self._marks), 2)

    @classmethod
    def get_total_students(cls):
        return cls.total_students

    @staticmethod
    def is_valid_stream(stream):
        return stream in ["Science", "Commerce", "Arts"]

s1 = Student("Raj", 101, [85, 90, 92], "Science")
s2 = Student("Anjali", 102, [78, 81, 88], "Commerce")

print(s1)
print("Total Marks:", s1.total_marks)
print("Average:", s1.average)

print(Student.get_total_students())   # 2
print(Student.is_valid_stream("Arts"))  # True

# Update marks safely
s1.marks = [88, 91, 94]
print("Updated Total:", s1.total_marks)

# s2.marks = [75, -80, 82]  # ❌ Will raise ValueError
