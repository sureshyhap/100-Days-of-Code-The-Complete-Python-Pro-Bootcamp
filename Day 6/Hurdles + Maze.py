def turn_around():
    turn_left()
    turn_left()
   
def turn_right():
    turn_around()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
"""
# Hurdle 1
for i in range(6):
    move()
    jump()

#x = 0
#while x != 6:
#    move()
#    jump()
#    x += 1
   
# Hurdle 2
while not at_goal():
    move()
    jump()

# Hurdle 3
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()

# Hurdle 4
def hop():
    turn_left()
    move()
    turn_right()

height = 0
while not at_goal():
    if wall_in_front():
        hop()
        height += 1
    else:
        move()
        turn_right()
        while height > 0:
            move()
            height -= 1
        turn_left()
"""

# Maze
# Move forward until found a wall.
# Needed because of a special case
# where reeborg moves in a square
# forever because has never found a
# right wall
while front_is_clear():
    move()
# Guarantees a wall at the right
turn_left()
while True:
    # While wall on the right, hug
    # the wall
    while wall_on_right():
        if front_is_clear():
            if at_goal():
                break
            move()
        # Wall on right and front
        # so try turning left
        else:
            turn_left()
    # No wall on the right so go right
    turn_right()
    if at_goal():
        break
    move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
