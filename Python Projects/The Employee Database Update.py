employee = {
    "name": "Osama",
    "age": 32,
    "skills": ["HTML", "CSS", "JS"],
    "rating": 8.5,
    "is_manager": False
}
employee.setdefault("country", "Egypt")
employee["skills"].append("Python")
employee["rating"] = 10
employee["is_manager"] = True
print("updated Keys: {}".format(employee.keys()))
print("Updated Values: {}".format(employee.values()))