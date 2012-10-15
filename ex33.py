def print_numbers(numbers):
    print "The numbers: "
    for num in numbers:
        print num

def count(first, last):
    while first < last:
        print "At the top i is %d" % first
        numbers.append(first)
        
        first += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % first
        
i = 0
max_count = 6
numbers = []
        
count(i, max_count)
print_numbers(numbers)
