# Guides: http://cayetanoguerra.github.io/

print "hola"

a = 1
b = 2
a, b = b, a
print a, b

# List of integers
nums = range(5)
print nums
print nums[2:4]
print nums[2:]
print nums[:2]
print nums[:]
print nums[:-1]
nums[2:4] = [8, 9]
print nums

# "For" loop example
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print squares

# Simplified "for" loop
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print squares

# Simplified loop with a condition
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print even_squares

# Dictionaries
d={'cat':'cute', 'dog':'furry'}
print d['cat']
print 'cat' in d # Boolean: checks if a key is contained.
print d.get('monkey','N/A')

# Dictionary iteration
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print 'A %s has %d legs' % (animal, legs)
