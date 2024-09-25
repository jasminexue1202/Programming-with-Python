#Jasmine Xue Lab 3
#Part A
urlList = ['https://www.yelp.com/biz/levain-bakery-new-york-13']
url = 'https://www.yelp.com/biz/levain-bakery-new-york-13'
i = 0
x = 10
while i < 5:
    nextUrl = url + '?start=' + str(x)
    x += 10
    urlList.append(nextUrl)
    i += 1
print(urlList)

#Part B
charList = ['!', ',', ' ', '.', '~', '-', '?']
attempt = input('Enter a word or a phrase:\n>>')
while attempt != '':
    cleanedAttempt = attempt
    for char in charList:
        cleanedAttempt = cleanedAttempt.replace(char, '')
    reverseAttempt = cleanedAttempt[::-1]

    if cleanedAttempt.lower() == reverseAttempt.lower():
        print('Yes', attempt, 'is a palindrome')
    else:
        print('No', attempt, 'is not a palindrome')
    attempt = input('Enter a word or a phrase:\n>>')
print('Thank you for using the palindrome finder')