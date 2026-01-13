data = [1,2,3,4,5,6,2,4]

cubes = {i: i*i*i for i in data}
cubes01 = {i: i**3 for i in data}
print(cubes)
print(cubes01)