#Jasmine Xue HW 2

#Part A
shortActing = ['Humulin', 'Novolin']
rapidActing = ['NovoLog', 'FlexPen', 'Fiasp', 'Apidra']
prescribed = input('What medication has the patient been prescribed \n>>')
if prescribed in shortActing or prescribed in rapidActing:
    print('The patient is a diabetic')
else:
    print('The patient is not a diabetic')
    
#Part B
spend = 500
price = float(input('How much are you asking?\n>>'))
if price > spend:
    print('Sorry, that price is too high for me.')
if price <= spend:
    print('Ok, I would like to purchase it.')

#Part C
print('Welcome to the currency calculator!')
amount = float(input('Enter the amount:\n>>'))
start = input('Enter the original currency:\n>>')
end = input('Enter the new currency:\n>>')

if start == 'y' and end == 'd':
    currency = amount * 0.0071
    print(f'{amount} Yen is worth {currency} dollar(s)')
elif start == 'y' and end == 'e':
    currency = amount * 0.0064
    print(f'{amount} Yen is worth {currency} Euro(s)')
elif start == 'y' and end == 'p':
    currency = amount * 0.0054
    print(f'{amount} Yen is worth {currency} Peso(s)')
elif start == 'd' and end == 'y':
    currency = amount * 141.39
    print(f' {amount} Dollar(s) is worth {currency} Yen')
elif start == 'd' and end == 'e':
    currency = amount * 0.90
    print(f' {amount} Dollar(s) is worth {currency} Euro(s)')
elif start == 'd' and end == 'p':
    currency = amount * 0.76
    print(f' {amount} Dollar(s) is worth {currency} Peso(s)')
elif start == 'e' and end == 'y':
    currency = amount * 157.35
    print(f' {amount} Euro(s) is worth {currency} Yen')
elif start == 'e' and end == 'p':
    currency = amount * 0.85
    print(f' {amount} Euro(s) is worth {currency} Peso(s)' )
elif start == 'p' and end == 'd':
    currency = amount * 1.32
    print(f' {amount} Peso(s) is worth {currency} Dollar(s)')
elif start == 'p' and end == 'y':
    currency = amount * 186.15
    print(f' {amount} Peso(s) is worth {currency} Yen')
elif start == 'p' and end == 'e':
    currency = amount * 1.18
    print(f' {amount} Peso(s) is worth {currency} Euro(s)')

