#Jasmine Xue Lab 1
#A
fullName = 'Xue, Jasmine'
commaIndex = fullName.index(',')
lastName = fullName[:commaIndex]
firstName = fullName[commaIndex+2:]
modifiedFullName = firstName + ' ' + lastName
print(modifiedFullName)

#B
originalBill = input('Please enter the bill amount:\n>>')
tipInput = input('Please enter the percent you would like to tip:\n>>')
billFloat = float(originalBill)
tipFloat = float(tipInput)
total = billFloat + (billFloat * tipFloat * 0.1)
print('Your total bill with a', tipInput, 'percent tip is:', '${0:,.2f}'.format(total))
