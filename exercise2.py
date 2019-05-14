names = ["Corey" , "Josh" , "Rachel"]

def greeting():
    print("What is your name?")
    enter_your_name = input()
    if enter_your_name == names[0]:
        return("Hello Corey!")
    elif enter_your_name == names[1]:
        return("Hello Josh!")
    elif enter_your_name == names[2]:
        return("Hello Rachel!")
    else:
        return("Who goes there?")

print(greeting())
