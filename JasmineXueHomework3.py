#Jasmine Xue Homework 3

# #Part A
# waves = 'v'
# response = float(input('How many waves would you like to ride?\n<<'))
# rides = 1
# while rides < response:
#     waves += 'v'
#     rides += 1
# print(waves)
# 
# #Part B
# 
# names = ['Smith, Tommie', 'Carlos, John', 'Normen, Peter']
# for name in names:
#     comma_index = name.index(',')
#     last_name = name[:comma_index]
#     first_name = name[comma_index + 2:]
#     first_last = first_name + ' ' + last_name
#     print(first_last)

#Part C

price = 10

offer = float(input('How much are you willing to pay?\n<<'))
while offer < price:
    price += 1
    offer = float(input('Nope! Try offering more!\n<<'))
print(f'It is a deal! The price is ${offer}.')
