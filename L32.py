the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

for number in the_count:
    print(f"This is count {number}")
    
for fruit in fruits:
    print(f"A fruit of type: {fruit}")
    
for i in change:
    print(f"I got {i}")
    
# Build Lists, first start with an empty one
elements = []

# the use the range function to do 0 to 5 counts
#for i in range(0, 6):
#    print(f"Adding {i} to the list.")
#    elements.append(i)
 
elements = range(0, 6)
              
for i in elements:
    print(f"Element was: {i}")
