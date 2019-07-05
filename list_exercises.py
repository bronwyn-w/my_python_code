# Chapter 3 programs, lists

friends = ['kitty', 'susan', 'jen','jane']
print (friends[0],friends[1], friends[-2],friends[-1])

# getting fancy now

message0=f" I love my friend {friends[0].title()}."
message1=f"I love my friend {friends[1].title()}."
message2=f"I love my friend {friends[2].title()}."
message3=f"I love my friend {friends[3].title()}."

print (message0,'\t',message1,'\n',message2,'\t',message3)

# print (message0,'\n',message1,'\n',message2,'\n', messsage3)
# print (message1, sep='\n', message2, sep='\n', message3)

#print (message1, sep='\n', message2)

cars = ['subaru','kia','honda','toyota']
print (cars)

cars[0]='bmw'

print (cars)

cars.append('subaru')
print(cars)

cars.insert(2,'mazda')
print(cars)

msg1=f"Zephyr has a {cars[3].title()},"
msg2=f"Bianca has a {cars[2].title()},"
msg3=f"Xenia has a {cars[1].title()},"

print (msg1, msg2, msg3)
