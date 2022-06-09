age = input("What is your current age?")

#4680 weeks in 90 years

daysold = int(age) * 365
weeksold = int(age) * 52
monthsold = int(age) * 12

days = (365*90) - daysold
weeks = 4680 - weeksold
months = (12*90) - monthsold


print("You have " + str(days) + " days, " + str(weeks) + " weeks, and " + str(months) + " months left.")