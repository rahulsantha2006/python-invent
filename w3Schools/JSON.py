import json

x = '{"name":"Rahul", "age":"14"}'

y = json.loads(x)

print(y["name"])

a = {
    "name":"Sibi",
    "age":"10"
}
b = json.dumps(a)
print(b)
# you can convert the following into json strings
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None
