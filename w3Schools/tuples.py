# Tuple is a collection which is unchangeable

firsttuple = ('rahul', ' sibi', 'bantha')

print(firsttuple)
print(firsttuple[2])
# negative indexing means starting form the end [-1] is calling the last item and [-2] is second to last and so on
print(firsttuple[-1])

# when having a range of index the first is included while the second is not
secondtuple = ('a', 'b', 'c', 'd', 'e')
print(secondtuple[2:4])
print(secondtuple[-4:-1])

# can use tuple in for loops
thirdtuple = ('hello', 'my', 'name', 'is','Rahul')
for x in thirdtuple:
    print(x)
if 'Rahul' in thirdtuple:
    print('Rahul is in third tuple')
# to print the lenght of a tuple use the len() keyword
print(len(thirdtuple))
# tuple cannot have only 1 value you have to put a comma after the first value for
# it to be considered a tuple