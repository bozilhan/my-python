workHours = [int(x) for x in input('enter hours per day in entire week, separated by space').split()]

wage = int(input('enter hourly wage'))

total = sum(workHours) * wage