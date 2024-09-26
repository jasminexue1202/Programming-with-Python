print('Welcome to the currency calculator!')
amount = float(input('Enter the amount:\n>>'))
start = input('Enter the original currency: (CAD = Canadian Dollar, y = Yen, d = Dollar, p = Peso) \n>>')
end = input('Enter the new currency: (CAD = Canadian Dollar, y = Yen, d = Dollar, p = Peso)\n>>')

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
elif start == 'e' and end == 'd':
    currency = amount * 1.12
    print(f' {amount} Euro(s) is worth {currency} Dollar(s)' )
elif start == 'p' and end == 'd':
    currency = amount * 1.32
    print(f' {amount} Peso(s) is worth {currency} Dollar(s)')
elif start == 'p' and end == 'y':
    currency = amount * 186.15
    print(f' {amount} Peso(s) is worth {currency} Yen')
elif start == 'p' and end == 'e':
    currency = amount * 1.18
    print(f' {amount} Peso(s) is worth {currency} Euro(s)')
elif start == 'CAD' and end == 'd':
    currency = amount * .74
    print(f' {amount} Canadian Dollar(s) is worth {currency} Dollar(s)')
elif start == 'd' and end == 'CAD':
    currency = amount * 1.35
    print(f' {amount} Dollar(s) is worth {currency} Canadian Dollar(s)')
elif start == 'y' and end == 'CAD':
    currency = amount * 0.0093
    print(f' {amount} Yen(s) is worth {currency} Canadian Dollar(s)')
elif start == 'CAD' and end == 'y':
    currency = amount * 107.38
    print(f' {amount} Canadian Dollar(s) is worth {currency} Yen(s)')
elif start == 'e' and end == 'CAD':
    currency = amount * 1.51
    print(f' {amount} Euro(s) is worth {currency} Canadian Dollar(s)')
elif start == 'CAD' and end == 'e':
    currency = amount * 0.66
    print(f' {amount} Canadian Dollar(s) is worth {currency} Euro(s)')
elif start == 'CAD' and end == 'p':
    currency = amount * 14.60
    print(f' {amount} Canadian Dollar(s) is worth {currency} Peso(s)')
elif start == 'p' and end == 'CAD':
    currency = amount * 0.069
    print(f' {amount} Peso(s) is worth {currency} Canadian Dollar(s)')
    