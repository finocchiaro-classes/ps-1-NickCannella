score = 0
priorarrests = int(input("Prior arrests: "))
reason = input("Prior arrests for local ordinance (Y/N): ")
age = int(input("Age at release: "))


if priorarrests >= 2:
    score = score+1
if priorarrests >= 5:
    score = score+1
if reason == ("Y"):
    score = score+1
if 18 <= age <= 24:
    score = score+1
if age >= 40:
    score = score-1
print(f"The recidivism risk score is {score}")

