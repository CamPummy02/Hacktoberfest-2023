""" 

Make your own list, calculate the product
 of all the numbers excluding the duplicates.
"""
a = [1, 4, 5, 6, 6]
b = []
for i in a:
    if i not in b:
        b.append(i)

product = 1
for i in b:
    product *= i

print("Product of all elements is", product)
