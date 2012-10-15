def print_numbers(numbers):
    print "The numbers: "
    for num in numbers:
        print num

def count(i, max_count):
    while i < max_count:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        
i = 0
max_count = 6
numbers = []
        
count(i, max_count)
print_numbers(numbers)
