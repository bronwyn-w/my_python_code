# Chapter 4, loops, continued with number manipulation

squares=[]
for value in range(1,21):
    squares.append(value**2)

#print(squares)
print(f"The sum of the squares from 1-20 is: {sum(squares)}")

# same thing using list comprehension

squares=[value**2 for value in range(1,21)]
print(f"Squares from 1-20 with list comprehension\n{squares}")

#for value in range(1,21):
#   print(value)

millions=[]
for value in range(1,1000001):
    millions.append(value)

print(f"Minimum={min(millions)}, Maximum={max(millions)}, Sum={sum(millions)}")

odd_numbers=list(range(1,10,2))

for num in odd_numbers:
    print(f"The number {num} is odd")

mult_three=list(range(3,31,3))

for num in mult_three:
    print(f"The number {num} is a multiple of 3")

cubes=[num**3 for num in range(0,11)]
#print(cubes)
for value in range(1,11):
    print(f"The cube of {value} is {cubes[value]}")

#mult_three.sort(reverse=True)
print(f"Reverse sorted multiples of 3 are: {sorted(mult_three,reverse=True)}")

    
