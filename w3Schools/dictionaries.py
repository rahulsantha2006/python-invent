
firstDiction = {
    "Rahul":"Chicken Columbu",
    "sibi": "Chilli Chicken",
    "Bantha": "Badhusha"
}
print(firstDiction)
x = firstDiction["sibi"]
x = firstDiction.get("sibi")
print((x))
firstDiction["Rahul"]="Chicken Biryani"
print(firstDiction)
# using for loop to print all key names
for y in firstDiction:
    print(y)

for z in firstDiction:
    print(firstDiction[z])
# to do both keywords and values use two variables
for a,b in firstDiction.items():
     print(a,b)
# to add a value to a dictionary
firstDiction["Nandhini"] = " Samia"
print(firstDiction)
# to remove a item for a dictionary use the pop method
(firstDiction).pop("Nandhini")
print(firstDiction)
# you can created muilpe dictionaries in a dictionary
myfamily = {
  "child1" : {
    "name" : "sibi",
    "year" : 2008
  },
  "child2" : {
    "name" : "bantha",
    "year" : 1977
  },
  "child3" : {
    "name" : "rahul",
    "year" : 2006
  }
}
print(myfamily)