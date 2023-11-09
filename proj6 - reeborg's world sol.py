# 6/100 days of coding, here are 2 different maps solutions to Reeborg's world


# solution to Hardle 1-4
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()

while not at_goal():
    if wall_in_front():
        jump()
        turn_right()
        if front_is_clear():
            move()
            turn_right()
            while front_is_clear():
                move()
            turn_left()
    if at_goal():
        break
    if front_is_clear():
        move()


#solution for maze map
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not is_facing_north():
        turn_left()    
turn_right()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif not front_is_clear() and right_is_clear():
        turn_right()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
        
