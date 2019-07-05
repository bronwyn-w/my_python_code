# Conditional tests exercise

#car='bmw'
#print("Is car=='mazda'? Probably not")
#print("Is car=='bmw'? I think so")

cars=[]
cars.append('bmw')
cars.append('subaru')
cars.append('toyota')
cars.append('mazda')
cars.append('mercedes')
cars.append('kia')
cars.append('honda')
print(cars)

for car in cars[:]:
    if car == 'kia':
        print(f"{car.title()} is Korean")
    elif car == 'bmw':
        print(f"{car.upper()} is German")
    elif car == 'mercedes':
        print(f"{car.title()} is German")
    else:
        print(f"{car.title()} is Japanese")

for car in cars[:]:
    if car != 'subaru':
        print(f"A {car} is not as cool as a subaru")
    
for age in range(0,30,4):
    if age < 2:
      print(f"The {age} year old is a baby")
    elif age >= 2 and age < 5:
        print(f"The {age} year old is a toddler")
    elif age >= 5 and age < 13:
        print(f"The {age} year old is a child")
    elif age >= 13 and age < 18:
        print(f"The {age} year old is a teenager")
    elif age >= 18:
        print(f"The {age} year old is an adult")

