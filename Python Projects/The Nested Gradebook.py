# List of [Name, Math, Science]
students = [
    ["Ahmed", 80, 90],
    ["Mona", 70, 85],
    ["Ali", 60, 75]
]
print(f"Mona's Science Grade: {students[1][2]}")
students[2][1] = 65
ahmed = students[0][1] + students[0][2]
ahmed_avg = ahmed / 2
print(f"Ahmed's Average Was: {ahmed_avg}")

students.append(["Sara", 95, 99])
students.pop(0)
print(students)
