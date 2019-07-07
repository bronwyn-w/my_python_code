# First lesson using python dictionaries

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
print(f"\nName: {info_1['firstname'].title()} {info_1['lastname'].title()}")
print(f"Birthdate: {info_1['birthdate']}")
print(f"Resides in: {info_1['city'].title()}")

print(f"\nName: {info_2['firstname'].title()} {info_2['lastname'].title()}")
print(f"Birthdate: {info_2['birthdate']}")
print(f"Resides in: {info_2['city'].title()}")


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

pythonterms = {
    'if':'if statements are used to check conditions',
    'for':'for loops are used to repeat actions',
    'list':'lists are one dimensional arrays',
    'dictionary':'dictionaries are multi-dimensional arrays',
    }

pythonterms['print'] = 'print statements produce output'

print(f"\nNew python terms I learned:")
for term,description in pythonterms.items():
    print(f"\t{term}: {description}")
      
