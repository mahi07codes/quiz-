#text data is called string 
message ="Hello world"
print(message)
print(len(message))
print(message[0])
#len is for the lengh of the message 
print(message[1:5])
# : is from where you want to write your message
print(message.lower())
print(message.count('Hello'))
print(message.count('l'))
print(message.find('e'))
# find print whole no and find print natural no 
new_message =message.replace("world","universe")
print(new_message)
greeting ='Hello'
name ='mariya'
message = greeting + ' ' + name 
print(message)
message = greeting + ', ' + name
print(message)
#if we want space or anything between two strings use''for it 
message = '{},{}. pagal!'.format(greeting,name)
print(message)
#message = f'{greeting},{name.upper()}.pagal'
print(message)
print(dir(name))
print(help(str))
print(help(str.lower))
