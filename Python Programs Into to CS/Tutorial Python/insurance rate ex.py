age = 31
if age < 18:
    rate = 450
else:
    if age > 90:
        rate = 500
    else:
        if age < 25:
            rate = 400
        else:
            rate = 300
print(rate)