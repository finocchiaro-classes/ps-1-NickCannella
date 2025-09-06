def heart_rate(age, goal):
    max_HR = 220 - age
    print (f"Your maximum heart rate is: {max_HR}")
    if goal == "S":
        lower = .80*max_HR
        upper = max_HR
        print ("Your target heart rate is between", float(lower), "and", int(upper))
    elif goal == "E":
        lower = .60*max_HR
        upper = .80*max_HR
        print("Your target heart rate is between", float(lower), "and", float(upper))
    

user_age = int(input("What is your age? "))
user_goal = input("Is your goal speed (S) or endurance (E)? ")

heart_rate(user_age, user_goal)
