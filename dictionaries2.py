# Second lesson using python dictionaries

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
      
