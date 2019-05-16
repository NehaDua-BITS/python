pointspossible = 100
score = 70
studentname = "Neha"

'''
A : 100-90%
B : 89 - 80%
C : 79 -70%
D: 69 - 60%
F : 59 - 0%
'''


#print the name and grade he/she got

percentage = float(score) / pointspossible * 100
print(percentage)
grade = "ERROR"
if percentage>=90 and percentage<=100:
    grade = 'A'
elif percentage>=80 and percentage<=89:
    grade = 'B'
elif percentage>=70 and percentage<=79:
    grade = 'C'
elif percentage>=60 and percentage<=69:
    grade = 'D'
elif percentage>=0 and percentage<=59:
    grade = 'F'

print(studentname + " : " + grade)


'''other way to do using between'''

if 90<=percentage<=100:
    grade = 'A'
elif 80<=percentage<=89:
    grade = 'B'
elif 70<=percentage<=79:
    grade = 'C'
elif 60<=percentage<=69:
    grade = 'D'
elif 0<=percentage<=59:
    grade = 'F'

print(studentname + " : " + grade)
