# Conditional tests exercise

car='bmw'

print("Is car=='mazda'? Probably not")

print("Is car=='bmw'? I think so")

cars=[]
cars.append('bmw')
cars.append('subaru')
cars.append('toyota')

print(cars)

if car in cars:
    print(car)

car='lexus'
if car not in cars:
    cars.append(car)

if car != 'subaru':
    print(f"Lame car: {car}")

if car=='toyota' or car=='lexus':
    print(f"same parent firm")
    
print(cars)

for num in range(0,8):
    for num2 in range(1,16,2):
        if num>4 and num2<10:
            print(f"num={num} and num2={num2}")
        if num==4:
            print(f"wild and crazy num=4")
        if num <4 and num2>10:
            print(f"num={num} and num2={num2}")

      

