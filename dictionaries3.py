# Third lesson using python dictionaries

info_1 = {
    'firstname':'bianca',
    'lastname':'wirth',
    'birthdate':'11/28/91',
    'city':'state college',
    }
info_2 = {
    'firstname':'xenia',
    'lastname':'wirth',
    'birthdate':'11/28/91',
    'city':'fullerton',
    }
info_3 = {
    'firstname':'zephyr',
    'lastname':'strosnider',
    'birthdate':'12/8/99',
    'city':'atlanta',
    }
info_4 = {
    'firstname':'bronwyn',
    'lastname':'wirth',
    'birthdate':'8/27/61',
    'city':'sandy springs',
    }
people=[info_1,info_2,info_3,info_4]

for person in people: 
    print(f"\nName: {person['firstname'].title()} {person['lastname'].title()}")
    print(f"Birthdate: {person['birthdate']}")
    print(f"Resides in: {person['city'].title()}")

#print(f"\nName: {info_2['firstname'].title()} {info_2['lastname'].title()}")
#print(f"Birthdate: {info_2['birthdate']}")
#print(f"Resides in: {info_2['city'].title()}")


favnums = {
    'bianca':5,
    'xenia':10,
    'zephyr':15,
    'gaston':20,
    'wilson':25,
    }
print(f"\n")
for name, num in favnums.items():
    print(f"{name.title()}'s favorite number is {num}")

if 17 not in favnums.values():
    print(f"What, no ones favorite number is 17?!?!")

people = ['bianca','tori','zephyr','izzy','gaston','zola']

print(f"\n")
for person in people[:]:
    if person not in favnums.keys():
        print(f"{person.title()}, what is your favorite number?")
    else:
        print(f"{person.title()}'s favorite number is {favnums[person]}")

#print(favnums.keys())
#print(favnums.values())
#print(f"Xenia's favorite number is {favnums['xenia']}")
#print(f"Zephyr's favorite number is {favnums['zephyr']}")
#print(f"Gaston's favorite number is {favnums['gaston']}")
#print(f"Wilson's favorite number is {favnums['wilson']}")


