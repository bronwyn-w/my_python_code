# Exercises on page 42, creating and manipulating lists

guestlist=[]

guestlist.append('gaston')
guestlist.append('wilson')
guestlist.append('xenia')
guestlist.append('bianca')
guestlist.append('zephyr')

print(f"Guest list: {guestlist}")

invite0=f"Dear {guestlist[0].title()}, please come to dinner."
invite1=f"Dear {guestlist[1].title()}, please come to dinner."
invite2=f"Dear {guestlist[2].title()}, please come to dinner."
invite3=f"Dear {guestlist[3].title()}, please come to dinner."
invite4=f"Dear {guestlist[4].title()}, please come to dinner."
print(invite0)
print(invite1)
print(invite2)
print(invite3)
print(invite4)

print(f"Oops, looks like {guestlist[1].title()} can't make it!")

del guestlist[1]

print(f"Guest list: {guestlist}")

invite0=f"Dear {guestlist[0].title()}, please come to dinner."
invite1=f"Dear {guestlist[1].title()}, please come to dinner."
invite2=f"Dear {guestlist[2].title()}, please come to dinner."
invite3=f"Dear {guestlist[3].title()}, please come to dinner."
print(invite0)
print(invite1)
print(invite2)
print(invite3)

guestlist.insert(0,'jane')
guestlist.insert(3,'bill')
guestlist.append('sophie')
print(f"Guest list: {guestlist}")

print(f"Oops, not enough food for a crowd, gotta shrink the list!\n")
poppedguest=guestlist.pop()
print(f"Guest list: {guestlist}")
print(f"sorry {poppedguest.title()}, you're uninvited")
print(f"Oops, not enough food for a crowd, gotta shrink the list!\n")
poppedguest=guestlist.pop()
print(f"Guest list: {guestlist}")
print(f"sorry {poppedguest.title()}, you're uninvited")
print(f"Oops, not enough food for a crowd, gotta shrink the list!\n")
poppedguest=guestlist.pop()
print(f"Guest list: {guestlist}")
print(f"sorry {poppedguest.title()}, you're uninvited")

del guestlist[0]
del guestlist[0]
del guestlist[0]
del guestlist[0]
print(f"Guest list: {guestlist}")



