cars = [('citroen', 'xsara', 1100), ('lincoln', 'navigator', 2000),('lincoln', 'znd', 2000),('lincoln', 'yrt', 2000), ('bmw', 'x5', 1700)]

print(sorted(cars, key=lambda car: car[0]))
print(sorted(cars, key=lambda car: car[1]))
print(sorted(cars, key=lambda car: (-car[2],car[1])))
#key = lambda x: (-x[0], x[1])git