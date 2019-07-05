# Page 46, lists continued. Sorting and ordering

places=['rouen','dunkirk','rennes','bron','lyon']

#print(f"Places I want to visit in France: {places}\n")
#print(f"Places I want to visit in France: {sorted(places)}\n")
#print(f"Places I want to visit in France: {sorted(places,reverse=True)}\n")
#print(f"Places I want to visit in France: {places}\n")

places.reverse()

print(f"Reverse 1,Places I want to visit in France: {places}\n")

places.reverse()

print(f"Reverse 2,Places I want to visit in France: {places}\n")

places.sort()

print(f"After perm Sort,Places I want to visit in France: {places}\n")

places.sort(reverse=True)

print(f"After reverse perm Sort,Places I want to visit in France: {places}\n")

numplaces=len(places)

print(f"I want to visit {numplaces} places in France, {sorted(places)}.\n")
      
dogs=['brittany','golden retriever','pug','mutt','german shephard','welsh corgi']

print(f"Cool dogs are: {sorted(dogs)}\n")

print(f"I have {len(dogs)} favorite dogs, in reverse order they are:")

dogs.sort(reverse=True)
print(dogs)

dogs.append('australian shepherd')
print(dogs)
dogs.insert(3,'bernese mountain dog')

print(dogs)
dogs.sort()
print(dogs)

current_dog=dogs.pop(2)
print(f"My current dog is a {current_dog.title()}")
      

