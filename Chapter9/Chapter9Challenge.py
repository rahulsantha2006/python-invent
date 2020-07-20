print(' Please enter how many names you would like in your list.')

print('Enter as a number please.')
peopleWhoFarted = int(input())  # 5
names_list = []

# Collect one name per loop and add to list
for x in range(peopleWhoFarted):
    print('enter name')
    name = input()
    names_list.append(name)

# Loop through an array
y = 0
while y < peopleWhoFarted:
    print(names_list[y].upper() + ' Farted!')
    y = y + 1

# Here is another way of looping an array
# for kutty_index in range(peopleWhoFarted):
#    print(names_list[kutty_index].upper() + ' Farted big time... brrrrrrrrr...!')
