my_set = {1, 2, 3, 4, 5}
print(my_set)

empty_set = set()
print(empty_set)

# Add element.

my_set.add(6)
print(my_set)

# Delete an element.

my_set.remove(4) # KeyError if the element is not found
my_set.discard(4)
print(my_set)

my_set.clear()
print(my_set)

# Check if subset or superset.

my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False, because not all the elements of "your_set" are in "my_set".
print(my_set.issuperset(your_set)) # False, because "my_set" does not have all the elements of "your_set".

# Disjoint method.

print(my_set.isdisjoint(your_set)) # False, because 2, 3 and 4 are common elements.

# Union operator.

union_set = my_set | your_set
print(union_set) # {1, 2, 3, 4, 5, 6}

# Intersection operator.

inter_set = my_set & your_set
print(inter_set) # {2, 3, 4}

# Difference operator.

difference_set = my_set - your_set
print(difference_set) # {1, 5}

# Symmetric difference operator.

symmetric_set = my_set ^ your_set
print(symmetric_set) # {1, 5, 6}

# Check if an element is in a set.

print(5 in my_set) # True
