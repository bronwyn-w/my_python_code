# Third lesson using python dictionaries

#define a few dictionaries containing information about pets
pet_1 = {
    'ownername':'bianca',
    'petname':'nemo',
    'breed':'clownfish',
    'type':'fish',
    }
pet_2 = {
    'ownername':'xenia',
    'petname':'wilson',
    'breed':'mutt',
    'type':'dog',
    }
pet_3 = {
    'ownername':'fikret',
    'petname':'honey badger',
    'breed':'grey tabby',
    'type':'cat',
    }
pet_4 = {
    'ownername':'bronwyn',
    'petname':'gaston',
    'breed':'brittany',
    'type':'dog',
    }

pets=[pet_1,pet_2,pet_3,pet_4]

for pet in pets: 
    print(f"\n{pet['ownername'].title()} has a pet {pet['type']}. \
The breed is a {pet['breed']} and its name is {pet['petname'].title()}.")

# Example of lists within dictionaries    
vacationspots = {
        'bianca':['antarctica','morroco'],
        'xenia':['australia','new zealand', 'bahamas'],
        'zephyr':['ecuador','argentina','bahamas'],
        }

for name in vacationspots.keys():
    print(f"\n{name.title()} wants to go to:")
    for spot in vacationspots[name]:
        print(f"\t{spot.title()}")

#Example of dictionary within dictionary
cities = {
    'atlanta':{
        'state':'georgia',
        'population':'6 million',
        'growth':'increasing',
        },
    'san diego':{
        'state':'california',
        'population':'3.3 million',
        'growth':'stable',
        },
    'davenport':{
        'state':'iowa',
        'population':'100,000',
        'growth':'decreasing',
        },
    }

for city, info in cities.items():
    print(f"\n{city.title()} is located in {info['state'].title()},")
    print(f"Its population is {info['population']} and {info['growth']}.")
    


