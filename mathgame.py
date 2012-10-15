def intro():
    print "Type your name pls.."
    name = raw_input("> ")
    print "Welcome %s to the MathGame!" % name
    print "Let's start.."

def check_result(userres, realres):
    if userres == realres:
        print "That's right.. go on!"
        return True
    else:
        print "You lost! Game Over!"
        return False

start = 1

name = intro()
check = True

while check == True:
    print "How much is %d * %d ?" % (start, start)
    rightres = start * start
    res = raw_input("> ")
    if res.isdigit():
        res = int(res)
        check = check_result(res, rightres)
        start += 1
    else:
        print "Type a number pls"
