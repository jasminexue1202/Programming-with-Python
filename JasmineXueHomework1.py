#Jasmine Xue Homework 1
#Part A
pagination = 'Page 1 of 12'
numberIndex = pagination.index('12')
padIndex = pagination[numberIndex:]
indexInt = int(padIndex)
print(indexInt)

#Part B
runner1 = 300.25 #Finish time in Minutes
runner2 = 260.75
runner3 = 315.75
runner4 = 245.25
calculateAverage = (float(runner1) + float(runner2) + float(runner3) + float(runner4))/4
average = calculateAverage
print('Average:', average)


caclulateVariance = (float(runner1 - average)**2 + float(runner2 - average)**2 + float(runner3 - average)**2 + float(runner4 - average)**2) / 4
variance = caclulateVariance
print('Variance:', variance)

#Part C
p = float(input('Please enter the principal:\n<<'))
r = float(input('Please enter the annual rate as a percentage:\n<<'))
n = int(input('Please enter the number of times the interest will compound per year:\n<<'))
t = float(input('Please enter the term of the loan or the number of years before it is repaid:\n<<'))

r = r / 100

A = p * (1 + r / n) ** (n * t)

print(f'In {t} years, at the interest rate of {r * 100:.2f}% compounded {n} times per year, the initial amount of ${p:.2f} will be worth ${A:.2f}')
