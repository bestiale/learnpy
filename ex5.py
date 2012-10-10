name = 'Ricky'
age = 25
# in inches
height = 67.5
# in pounds
weight = 157.0
eyes = 'Brown'
hair = 'Brown'

print "Let's talk about %s." % name
# output in cm %.2f
print "He's %.2f cm tall" % (height * 2.54)
# output in kg
print "He's %d kg heavy." % (weight / 2.2)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)



# tricky line
print "If i add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
