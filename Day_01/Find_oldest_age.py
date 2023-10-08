# input
age_1 = int(input('enter 1st birth year'))
age_2 = int(input('enter 2nd birth year'))
age_3 = int(input('enter 3rd birth year'))

# Compare all ages to find the oldest age using min function
old_age = min(age_1, age_2, age_3)

print("Oldest birth year is:", old_age)