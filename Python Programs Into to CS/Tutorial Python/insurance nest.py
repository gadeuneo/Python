age = 16
while age <= 34:
    if age < 18:
        rate = 450
    elif age > 90:
        rate = 500
    elif age < 25:
        rate = 400
    else:
        rate = 300
    print(age, ":", rate)
    age = age + 1