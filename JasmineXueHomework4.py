#Jasmine Xue Homework 4

#Part A
print('KPH\tMPH')

speedsKPH = [60, 70, 80, 90, 100, 110, 120, 130]


for speed in speedsKPH:
    speedsMPH = speed * 0.6214
    print(f'{speed}\t{speedsMPH}')


#Part B
secretWord = 'heart'
guess = input('Guess a letter:\n<<')
i = 1
while i < 5:
    if guess in secretWord:
        print(f' Yes, {guess} is in the word')
        i += 1
        guess = input('Guess a letter:\n<<')
    else:
        print(f'No, {guess} is NOT in the word')
        i+=1
        guess = input('Guess a letter:\n<<')

answer = input('Can you guess the word?\n<<')
if answer != secretWord:
    print(f'The secret word was {secretWord}')
else:
    print('Winner Winner, Chicken Dinner! That is correct!')
    

#Part C
password = 'password'
attempt = input('Please enter the password:\n<<')
i = 1
while attempt != password and i < 3:
    attempt = input('Please try again:\n<<')
    i += 1
if attempt == password:
    print('Access granted')
else:
    print('Access denied')