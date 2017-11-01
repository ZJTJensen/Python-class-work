# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# for i in range (len(students)):
#     output=students[i]['first_name']
#     output+=" "
#     output+=students[i]['last_name']
#     print output

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

num = 0
print "students"
output = ''
for i in range (len(users['Students'])):
    output=''
    output+= str(num) + " - " + users['Students'][i]['first_name']
    output+=" "
    output+= users['Students'][i]['last_name'] + " - "
    output+= str(len(users['Students'][i]['last_name'])+len(users['Students'][i]['first_name']))
    print output
    num=num+1

print "Instructors"
for i in range (len(users['Instructors'])):
    output=''
    output+= str(num) + " - " + users['Instructors'][i]['first_name']
    output+=" "
    output+= users['Instructors'][i]['last_name'] + " - "
    output+= str(len(users['Instructors'][i]['last_name'])+len(users['Instructors'][i]['first_name']))
    print output
    num=num+1