s1 = float(input("Enter The First Side: "))
s2 = float(input("Enter The Second Side: "))
s3 = float(input("Enter The Third Side: "))
if s1 == s2 == s3:
    print("This is Equilateral")
elif s1 == s2 or s1 == s3 or s2 == s3:              # AI Correction
    print("This is Isosceles")
else:
    print("This is Scalene")
