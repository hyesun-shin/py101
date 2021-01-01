def print_message():
    print("CS101 is fantastic!")
    print("Programming is fun!")

def repeat_message():
    print_message()
    print_message()

repeat_message()

from cs1robots import *
create_world()
hubo = Robot(beepers=1)

hubo.move()
hubo.