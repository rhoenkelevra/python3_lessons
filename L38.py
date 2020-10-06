ten_things =  "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while len(stuff) != 10:
#     next_one = more_stuff.pop() # next_one = pop(more_stuff)
#     print("Adding: ", next_one)
#     stuff.append(next_one) # append(stuff to next_one)
#     print(f"There are {len(stuff)} items now.")

for i in stuff:
    if len(stuff) < 10:
        next_one = more_stuff.pop()
        print("Add: ", next_one)
        stuff.append(next_one)
        print(f"There are {len(stuff)} items now")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) # -> Oranges
print(stuff[-1]) # -> Corn
print(stuff.pop()) # -> Corn
print(' '.join(stuff)) # -> Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
print('#'.join(stuff[3:5])) # -> Telephone#Light . Position 3 and 4, because 3:5 does not include the fifth

print('#'.join(stuff[0:2])) # -> Apples#Oranges, slices the first two

