from functools import reduce
a = (1,2,3,4,5,6,7,8,9)

even= list(filter(lambda x:x%2==0,a))
print (even)

square= list(map(lambda y:y**2,even))
print (square)

sum=reduce(lambda b,c:b+c,square)
print (sum)

for index, value in enumerate(square, start=1):
    print (index,value)