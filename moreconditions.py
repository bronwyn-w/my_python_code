# Exercises on page 89

users=['FALCON','eagle','Hawk','cardinal','admin','bluejay','sparrow']
newusers=['wilson','gaston','Hawk','Zephyr','falcon']
print(users)

lowercaseusers=[]
for user in users[:]:
    lowercaseusers.append(user.lower())
#print(lowercaseusers)

if users == []:
        print("We need to find some users!")
else:
        for newuser in newusers[:]:
            if newuser.lower() in lowercaseusers:
                print(f"Sorry, {newuser} is already taken")
            else:
                users.append(newuser)
                print(f"Welcome {newuser}!")
       

#print(users)

for num in range(1,10):
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")

    

