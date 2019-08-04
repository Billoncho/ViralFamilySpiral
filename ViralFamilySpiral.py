# ViralSpiral.py
# Billy Ridgeway
# Demostrates nested loops by creating a spiral of names.

import turtle               # Imports the turtle library
t = turtle.Pen()            # Creates a new turtle called t.
t.speed(0)                  # Sets the speed of writing to fast.
t.penup()                   # Begins the program with the pen up to prevent accidently writing lines.
turtle.bgcolor("black")     # Sets the background to black.
family = []                 # Sets up an empty list for family names.

# Ask for the first family member's name.
name = turtle.textinput("My family",
                        "Enter a name, or just hit {ENTER] to end:")

# Keep asking for names until ENTER is pressed without an entry.
while name != "":
    family.append(name)                                                 # Add their name to the family list.
    name = turtle.textinput("My family",
                        "Enter a name, or just hit {ENTER] to end:")    # Ask for another name, or end the program.

colors = ["red", "yellow", "blue", "green", "purple", "orange", "white", "brown",
          "gray", "pink"]

# Our outter spiral loop.
for m in range(100):
    t.forward(m*4)              # Move forward the number contained in 'm' times 4.
    position = t.position()     # Remember this corner of the spiral.
    heading = t.heading()       # Remember the direction we were heading.

    # Draw a spiral of the names on the screen.
    for n in range(len(family)):                                                    # Calculate the number of names to be written.
        t.pendown()                                                                 # Allows the pen to write on the screen.
        t.pencolor(colors[n%len(family)%10])                                        # Cycle through the colors based upon the number of family members.                           
        t.write(family[n%len(family)], font = ("Arial", int((m+4)/4), "bold"))      # Writes the name contained in that location of the string.
        t.right(360/len(family))                                                    # Turn the spiral right by 360 degrees divided by the number of family members.
        t.penup()                                                                   # Lifts the pen until the program is ready to write the next name.
        t.forward(m//2)                                                             # Calculate how far to move by using only the quotient of 'm' divided by 2.

    t.setposition(position)         # Resets the 'x' and 'y' position to that stored in the outter loop.
    t.setheading(heading)           # Resets the heading to that stored in the outter loop.
    t.left(360/len(family) + 3)     # Sets the pen to a position calculated by dividing 360 degree by the number of family members plus 3.

