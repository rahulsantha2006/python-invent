# a set in python is a collection which is unordered and unindexed. It is written with curly braces

firstset = {"biriyani","chilli chicken","kesari"}
print(firstset)
# can be used in for loops
for x in firstset:
    print(x)
print('chilli chicken' in firstset)
# once a set is created you can alter it, but can add new items to it
firstset.add("Porrta")
print(firstset)
# to add multiple items to a set use update
firstset.update(["Mutton columbu", "Mysoorpa,", "Dosa"]) # you need the ([]) inside
print(firstset)

secondset = {'1','2','3','4','5','6'}
print(len(secondset))
# to remove an item from the set use the remove or discard function
# if the item being removed is not there it will have and error for the remove but not discard
secondset.remove('3')
print(secondset)

# to combine two sets use the union function
thirdset = firstset.union(secondset)
print(thirdset)