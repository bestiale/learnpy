x = "There are %d type of people." % 10
binary = "binary"
do_not = "don't"
# String in string the first %s is for binary the 2nd is for don't
y = "Those who know %s and those who %s." % (binary, do_not)

# output from x and y
print x
print y

# output from x (string in a string)
print "I said: %r." % x
# output from y (string in string)
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# %r in the joke_evaluation string will be replaced with the value of hilarious (False)
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
