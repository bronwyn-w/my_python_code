# Chapter 4, starting to use loops with lists

pizzas=['veggie','sausage','anchovy','sun-dried tomato']

# Copy the list of pizza's using the slice function
# which creates a new, identical list
newpizzas=pizzas[:]

pizzas.append('olive')
newpizzas.append('pepperoni')
newpizzas.insert(2,'cheese')
newpizzas.remove('anchovy')

print(pizzas)
for pizza in pizzas:
    print(f"I love {pizza} pizza!")

print(newpizzas)
for pizza in newpizzas:
    print(f"I want {pizza.title()} pizza for lunch.")

print(f"Enough about pizza!\n")

animals=[]
animals.append('tiger')
animals.append('lion')
animals.append('jaguar')
animals.append('bobcat')
animals.append('lynx')
animals.append('leopard')
animals.append('cheetah')

print(animals)
#animals.sort()

print(f"The first 3 animals are: ")
for animal in animals[:3]:
    print(f"{animal.title()}")

for animal in animals[2:5]:
    print(f"A {animal.title()} is a big cat.")
#    print(f"Cats like {animal}s belong in the wild.")

print(f"The last 3 animals are: ")
for animal in animals[-3:]:
    print(f"{animal.title()}")

#print(sorted(animals,reverse=True))

print(f"Moving on to tuples...")
desserts=('cake','creme brulee','pie')

for dessert in desserts:
    print(f"{dessert} is yummy")

# This fails because you can't change tuples
#desserts.remove('cookies')

# But you can redefine them completely
desserts=('cobbler','pudding','mousse')

for dessert in desserts:
    print(f"{dessert} is yummy")
