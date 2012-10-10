print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "\nI give you the Result of two added numbers\n"
print "Give me a number: \n",
first = int(raw_input())
print "Give me a second number: \n",
second = int(raw_input())

result = first + second

print "%d + %d = %d" % (first, second, result)
