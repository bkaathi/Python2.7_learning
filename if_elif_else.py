first_name = raw_input("Enter you first name: ")

if first_name == "Karthik":
    last_name = raw_input("Enter your last name: ")
    if last_name == "Balasubramani":
        print "Hey Karthik Balasubramani, welcome to Python 2.7"
    else:
        print "Sorry " + first_name + " " + last_name + " we cannot identify your last name. Bye! "

else:
    print "Sorry " + first_name + " I cannot identify you. Bye!"


