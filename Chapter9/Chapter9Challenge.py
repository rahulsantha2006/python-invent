print('Please enter how many names you would like in your list.')

print('Enter as a number please.')

peopleWhoFarted = int(input())  # 5
names_list = []

for x in range(peopleWhoFarted):
    print('enter name')
    name = input()
    names_list.append(name)

y = 0
while y < peopleWhoFarted:
    print(names_list[y].upper() + ' Farted!')
    y = y + 1
