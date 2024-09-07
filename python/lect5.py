#*************dictionaries*************

student = {'name': 'jhon','age':25, 'courses': ['math', 'compsci']}
print(student)
print(student['courses'])
print(student.get('phone'))

#we can set default value that dosent exist

print(student.get('phone', 'not found'))

#add new key in the string

student['phone'] = '5555-66666'
student['name'] = 'Jane'
print(student)

#updating or adding new key 

student.update({'name':'jane', 'age': 27, 'phone':'5555-66666'})
print(student)

#we can delete key with del and pop also

#del student['age']
print(student)
ab = student.pop('age')
print(student)
print(ab)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
for key in student:
    print(key)
    for key , value in student.items():
        print(key,value)