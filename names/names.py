import time
from binary_search_tree import BSTNode
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# build names list 1: **** O(n) ****
count = 0
for n in names_1:
    if count == 0:
        list_1_names = BSTNode(n)
        count += 1
    else:
        list_1_names.insert(n)
        count += 1

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# **** runtime: O(n^C), quadric (11.5 on my machine) ****
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# **** O(Log n) ****
for n in names_2:
    if list_1_names.contains(n):
        duplicates.append(n)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
