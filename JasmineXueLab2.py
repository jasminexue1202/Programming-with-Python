#Jasmine Xue Lab 2

ready = input('Are you ready to start?\n>>')
yesReady = ['y', 'yes', 'Yes', 'YES', 'Y', 'Yup', 'yup', 'sure', 'Sure']
if ready in yesReady:
    print('Ok, lets get started')
else:
    print('Well, go get ready')
    
pointsEarned = float(input('How many points have you earned?\n>>'))
pointsPossible = float(input('How many points are possible?\n>>'))

percent = pointsEarned/pointsPossible * 100

grade = 'unknown'
if percent >= 93:
    grade = 'A'
elif percent >= 90: #elif only executes if bool alove it is false
    grade = 'A-'
elif percent >=87: #elif only executes if bool alove it is false
    grade = 'B+'
elif percent >=83 : #elif only executes if bool alove it is false
    grade = 'B'
elif percent >=80 : #elif only executes if bool alove it is false
    grade = 'B-'
elif percent >=77 : #elif only executes if bool alove it is false
    grade = 'C+'
elif percent >=73 : #elif only executes if bool alove it is false
    grade = 'C'
elif percent >=70 : #elif only executes if bool alove it is false
    grade = 'C-'
elif percent >=67 : #elif only executes if bool alove it is false
    grade = 'D+'
elif percent >=63 : #elif only executes if bool alove it is false
    grade = 'D'
elif percent >=60 : #elif only executes if bool alove it is false
    grade = 'D-'
else:
    grade = 'F'

print(grade)

print('The student currently has', percent, '% with a letter grade of', grade)