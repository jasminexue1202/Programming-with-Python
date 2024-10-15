#Jasmine Xue Homework 5

#Part A

def findFibonacci(n):
    i = 0
    numberA = 0
    numberB = 1
    while i < n:
        nextNumber = numberA + numberB
        numberA = numberB
        numberB = nextNumber
        i += 1
    return numberA #First set of ??'s

response = int(input('Which number would you like to find?:\n>>'))
result = findFibonacci(response)   #Second set of ??'s
print(result)


# #Part B
name = input('What is your name?\n<<')

def birthdaySong(name):
    print("Happy Bithday to you")
    print("Happy Birthday to you")
    print("Happy Birthday, dear " + name )
    print("Happy Birthday to you!")
    
    return

birthdaySong(name)

#Part C
    
#Should be parameters
p = '$5,000'    #Principle
r = '%7.9'      #Annual Interest Rate
t = 5         #Term of the loan
n = 365           #Compounding per year

def futureValue(p, r, t, n = 365):
    pFloat = float(p.replace('$', '').replace(',', ''))
    rFloat = float(r.replace('%', ''))*.01
    
    a = pFloat*(1 + rFloat/n)**(n*t)
    return a

loan1 = futureValue('$5,000', '7.9%', 5)
loan2 = futureValue('$12,000', '%3.2', 10)
loan3 = futureValue('$1,700,000', '%4.8', 30, 4)


print(loan1)
print(loan2)
print(loan3)

