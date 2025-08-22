# 1. We are creating an empty list namely my_list. This can be done in two primary ways:

my_list = list()

# or my_list = []

# 2.We are Appending the following list elements to my_list:10, 20, 30, 40

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# output
# my_list = [10, 20, 30, 40]

# 3. Inserting the value 15 at the second position in the list (index 1)

my_list.insert(1, 15)

# Output
# my_list = [10, 15, 20, 30, 40]

# 4. We are extending my_list with another list: [50, 60, 70]

my_list.extend([50, 60, 70])

# Output
# my_list = [10, 15, 20, 30, 40, 50, 60, 70]

# 5. We Remove the last element from my_list. Pop method removes the last element from the list

my_list.pop()

# Output
# my_list = [10, 15, 20, 30, 40, 50, 60]
# Element on index[7], which is the value 70 is removed from my_list

# 6. We are Sorting my_list in ascending order. By default sort() arranges elemets in an ascending order.

my_list.sort()

# Output
# my_list = [10, 15, 20, 30, 40, 50, 60]

# 7. We are finding and printing the index of the value 30 in my_list. The value 30 is stored in index 3.

index_30 = my_list.index(30)

print("Index of value 30:", index_30)

# Output
# Index of value 30: 3



