#MonChefDoeuvre1237.py

# Description:
# Draws a painting without input from the user. Closes when user clicks.
# Painting inspiration "Birds and Plum" by Chinese Painter Pu Zuo (1918-2001)
# https://www.chinadaily.com.cn/culture/art/2014-09/17/content_18615995.htm

# Author:
# Marcus Ho

# Date:
# 2023-10-20

# --- Permission is given to show case this work ---

# Import modules
# import turtle module
import turtle
# import math module
import math

def drawTwig(pen, x, y, turn, length):
    """Draw a line at x,y of length with turn to right.
        "pen" - The turtle
        "x" - The starting x position of the twig's base
        "y" - The starting y position of the twig's base
        "turn" - The turn (in degrees towards the right) of the twig's direction
        "length" -  The length of the twig
    """
    #Pickup the pen
    pen.penup()
    # Move the pen to desired location
    pen.goto(x,y)
    # Put pen down
    pen.pendown()
    # Turn pen right
    pen.right(turn)
    # Draw forward to length
    pen.forward(length)
    return

def drawWave(pen,amp,freq,length,sLength,width,scale):
    """Draw a cosine wave.
        "pen" - The Turtle
        "amp" - The amplitude of the wave
        "freq" - The frequency multiplier
        "length" - The overall length of the wave
        "sLength" - The point along the length where the turtle begins drawing
       sLength may also be set to 0 to draw along the entire length of wave.
       "width" - Width of drawn wave
       "scale" - Scale multiplier of wave
    """
    # Start with pen up
    pen.penup()
    # If delayed start is specified, set bool mayDraw false
    if sLength > 0:
        mayDraw = False
    # Else, allow turtle to draw from the start
    else:
        mayDraw = True
    # Set pen width, prepare to draw from current position
    pen.width(width)
    # Draws slowly due to high step count, speed turtle up
    pen.speed(100000)
    # Loop until turtle reaches the end of the branch length:
    for currentX in range(0, length, 3):
        # Cosine wave formula (no shift) y = amp*cos(freq(x))
        # Take slope of cosine wave at current length
        # y' = (cos(freq*x)) + amp(x*-sin(freq*x))
        slope = math.cos(freq*currentX) + -amp*(freq * math.sin(freq*currentX))
        
        # Get the angle given by the slope (arctan)
        pointAngle = math.atan(slope)*3

        # point the turtle left by the point angle amount                                       
        pen.left(pointAngle)

        # If turtle is past startPoint and not able to draw, set pendown
        if not mayDraw and currentX >= sLength:
            mayDraw = True
            pen.pendown()
        # Otherwise, keep pen as it is
        
        # Move turtle forward
        pen.forward(scale*3)
    # return the turtle to a reasonable speed
    pen.speed(100)
    return

def drawTaperBranch(pen,width1,width2,length):
    """Draw a line that gradually tapers from width 1 to width 2.
        "pen" - The turtle used to draw the branch
        "width1" - The starting width 
        "width2" - The final width
        "length" - The overall length of the branch
    """
    # calculate taper: final - initial
    taper = width2 - width1
    # calculate required taper per step
    # times three to speed up animation speed
    stepTaper = 3*taper/length
    # Set current width
    currentWidth = width1
    # Set the pen down
    pen.pendown()
    # Draws slowly due to high step count, speed turtle up
    pen.speed(100000)
    #Loop until branch reaches specified length:
    for currentX in range(0, length, 3):
        # Set pen width
        pen.width(currentWidth)
        pen.forward(3)
        #adjust width value
        currentWidth += stepTaper
    # return the turtle to a reasonable speed
    pen.speed(100)
    return
        
def drawCurveTaperBranch(pen,x,y,curveDegree,width1,width2,stepSize,steps):
    """Draw a simple curve at x,y that gradually tapers in width.
        "pen" - The turtle
        "x" - The x position of the base of the branch
        "y" -  The y position of the base of the branch
        "curveDegree" - Curve multiplier
        "width1" - Starting width
        "width2" - Final width
        "stepSize" - Number of curve steps (resolution)
        "steps" - Effects total length, combined with stepSize
    """
    
    # If x and y are 1234, do not move pen from current position
    # Intentional feature for finishing a branch with a curved section
    if not x == 1234 and not y == 1234:
        #Pickup the pen
        pen.penup()
        # Move the pen to desired location
        pen.goto(x,y)
    # Put pen down
    pen.pendown()
    # calculate taper: final - initial
    taper = width2 - width1
    # calculate required taper per step (x2 to speed anim length)
    stepTaper = 2*taper/steps
    # Set current width
    currentWidth = width1
    # Draws slowly due to high step count, speed turtle up
    pen.speed(100000)
    # For the number of steps
    for currentPt in range(0, steps, 2):
        # Set pen width
        pen.width(currentWidth)
        #Take one step forward
        pen.forward(stepSize*2)
        #Turn right based on curve degree
        pen.right(curveDegree)
        #adjust width value
        currentWidth += stepTaper
    # return the turtle to a reasonable speed
    pen.speed(100)
    return

def drawPineCluster(pen,x,y,rays,width,scale,c1,c2):
    """Draw a cluster of pine needles
        "pen" - The turtle
        "x" - X position of center of cluster
        "y" - Y position of center of cluster
        "Rays" - Number of needles
        "Width" - Needle thickness
        "Scale" - Needle length
        "c1" - Colour 1
        "c2" - Colour 2
    """
    
    #Pickup the pen
    pen.penup()
    # Move the pen to desired location
    pen.goto(x,y)
    # Set pen thickness
    pen.width(width)
    # Get angle between each needle
    rayAngle = 360/rays
    # for the number of rays
    for x in range(0, rays, 1):
        # alternate between needle colours
        if x%2 == 0:
            pen.color(c1)
        else:
            pen.color(c2)
        # Put pen down
        pen.pendown()
        pen.forward(scale)
        # Pick up pen
        pen.penup()
        # Return to centre
        pen.backward(scale)
        # Change angle by rayAngle
        pen.right(rayAngle)
    return

def drawBud(pen,x1,y1,targetx,targety,stemColour,budColour,longMorph):
    """ Draw a small flower bud of fixed size.
        pen - Turtle
        x1 - x position of bud stem base
        y1 - y position of bud stem base
        targetx - x position of the point that bud will point towards
        targety - y position of the point that bud will point towards
        stemColour - Colour of stem
        budColour - Colour of flower bud
        longMorph - True if long variant, false if short variant
    """
    # pickup pen
    pen.penup()
    # move pen to x,y
    pen.goto(x1,y1)
    # setheading to target x and y
    pen.seth(pen.towards(targetx,targety))
    # set pen to stem colour, set width
    pen.color(stemColour)
    pen.width(2)
    # pendown, draw forward a fixed amount
    pen.pendown()
    if longMorph:
        drawTaperBranch(pen,4,2,20)
    else:
        drawTaperBranch(pen,4,2,12)
    # change pen to bud colour
    pen.color(budColour)
    # set shape size
    pen.shapesize(0.5)
    # stamp bud
    pen.stamp()
    # return pen to up state
    pen.penup()
    return

def drawFlower(pen,x,y,petals,petalDist,petalSize,cSize,petalColour,cColour):
    """Draw a cluster of pine needles
        "pen" - The turtle
        "x" - X position of center of flower
        "y" - Y position of center of flower
        "petals" - Number of petals
        "petalDist" - Distance of petals from center
        "petalSize" - Petal shapesize
        "cSize" - Center of flower shapesize
        "petalColour" - Color of flower petals
        "cColour" - Colour of center of flower
    """
    
    #Pickup the pen
    pen.penup()
    # Move the pen to desired location
    pen.goto(x,y)
    # Set petal colour, size
    pen.shapesize(petalSize)
    pen.color(petalColour)
    # Get angle between each petal
    rayAngle = 360/petals
    # for the number of petals
    for x in range(0, petals, 1):
        # Move forward by petalDist
        pen.forward(petalDist)
        # Stamp petal
        pen.stamp()
        # Return to centre
        pen.backward(petalDist)
        # Change angle by rayAngle
        pen.right(rayAngle)
        
    # Set center shapesize,colour
    pen.shapesize(cSize)
    pen.color(cColour)
    # Stamp center
    pen.stamp()
    return

# Testing purposes only
# def buttonclick(x,y):
    #print(f'Clicked at ({x},{y}')
    #return

#--------- MAIN CODE BODY -----------#
# create screen object
canvas = turtle.Screen()

# Otherwise, full animation roughly 4mins 13sec long

# create turtle objects
tt1 = turtle.Turtle()
tt2 = turtle.Turtle()
# set background colour
canvas.bgcolor("#dac6a7")
# set turtle shape
tt1.shape("circle")
tt2.shape("circle")
# Prep turtle for moving
tt1.penup()
tt2.penup()

# Testing purposes only
#turtle.onscreenclick(buttonclick,1)

# BACKGROUND FLOWERS - DARK
drawFlower(tt2,270,-107,5,15,1,0.6,"#cc3f52","#cc3f52")
drawPineCluster(tt2,270,-107,6,3,8,"#272725","#272725")

drawFlower(tt2,236,-41,5,15,1,0.6,"#cc3f52","#cc3f52")
drawPineCluster(tt2,236,-41,6,3,8,"#272725","#272725")

drawFlower(tt2,224,267,5,15,1,0.6,"#cc3f52","#cc3f52")
drawPineCluster(tt2,224,267,6,3,8,"#272725","#272725")

# BACKGROUND FLOWERS - MEDIUM

drawFlower(tt2,-305,-80,5,15,1,0.6,"#d67a7a","#d67a7a")
drawPineCluster(tt2,-305,-80,15,0.5,15,"#4a3325","#4a3325")

drawFlower(tt2,-53,-146,5,15,1,0.6,"#d67a7a","#d67a7a")
drawPineCluster(tt2,-53,-146,6,3,8,"#272725","#272725")

drawFlower(tt2,-41,-118,5,15,1,0.6,"#d67a7a","#d67a7a")
drawPineCluster(tt2,-41,-118,6,3,8,"#272725","#272725")

drawFlower(tt2,171,57,5,15,1,0.6,"#d67a7a","#d67a7a")
drawPineCluster(tt2,171,57,6,3,8,"#272725","#272725")

drawFlower(tt2,174,-68,5,15,1,0.6,"#d67a7a","#d67a7a")
drawPineCluster(tt2,174,-68,6,3,8,"#272725","#272725")

drawFlower(tt2,199,-114,5,15,1,0.6,"#d67a7a","#d67a7a")
drawPineCluster(tt2,199,-114,6,3,8,"#272725","#272725")

drawFlower(tt2,248,-86,5,15,1,0.6,"#d67a7a","#d67a7a")
drawPineCluster(tt2,248,-86,6,3,8,"#272725","#272725")

drawFlower(tt2,137,-148,5,15,1,0.6,"#d67a7a","#d67a7a")
drawPineCluster(tt2,137,-148,6,3,8,"#272725","#272725")


# MAIN BRANCH
# Set turtle orientation
tt1.seth(0)
# move turtle to position of main branch, angle towards branch
tt1.goto(400,150)
tt1.right(120)
# move turtle 2 into correct angle for relocation
tt2.seth(-161)
# Set Turtle colour
tt1.color("#272725")
tt2.color("#272725")
# Draw main branch base segment
drawCurveTaperBranch(tt2,400,70,-0.5,35,25,4,68)
# Draw main branch curved segment
drawWave(tt1,50,0.05,300,160,25,2)
# Start non-wave part of main branch
drawTaperBranch(tt1,25, 20, 20)
# Turn for 2nd segment
tt1.right(10)
# Draw 2nd segment
drawTaperBranch(tt1,20, 18, 50)
# Turn for 3rd segment
tt1.right(20)
#Draw 3rd segment
drawTaperBranch(tt1,18, 15, 100)
# Turn for 4th segment
tt1.right(25)
# Draw 4th segment
tt1.forward(185)
# Lift pen for relocation
tt1.penup()

# MAIN BRANCH - TWIGS
# Set turtle orientation
tt1.seth(150)
# Set turtle width for all twigs
tt1.width(10)
# Draw left uppermost twig and extend
drawTwig(tt1, -310, -150, 50, 70)
tt1.left(5)
drawTaperBranch(tt1,10, 5, 40)
tt1.width(10)
# Draw left lower twig and extend
tt1.right(-100)
drawCurveTaperBranch(tt1,-275,-185,2,10,3,6,22)
# Draw minor branch fork 1
tt1.width(10)
drawTwig(tt1, -20, -155, 25, 10)
drawTaperBranch(tt1,10,5,20)
# Draw minor branch fork 2
tt1.width(10)
tt1.right(45)
drawCurveTaperBranch(tt1,-23,-151,-2,10,2,3,24)

# MAIN BRANCH - CURVED TWIGS
# Turn and Draw leftmost curved twig
tt1.left(20)
drawCurveTaperBranch(tt1,0,-135,-4,10,3,6,36)


# -------- BIRD #1 ------------
# Draw bird wing
# Turn For bird 1 wing
tt2.seth(220)
# Set bird wing colour
tt2.color("#928874")
# Draw bird wing
drawCurveTaperBranch(tt2,90,140,-3.8,22,5,3,36)
# Set wingtip colour
tt2.color("#302921")
# Point wingtip, draw
tt2.seth(-105)
drawCurveTaperBranch(tt2,62,110,-2,12,5,3,15)

# Draw nape
# Set bird nape colour
tt2.color("#c4ac92")
# Set turtle point direction
tt2.seth(70)
# Draw nape
drawCurveTaperBranch(tt2,140,116,-4.5,15,10,2,38)
# Point to fill in ear region
tt2.seth(90)
# Draw
drawCurveTaperBranch(tt2,130,146,-4,15,5,1,16)

# Draw face pattern
# Set under layer cheek fill
tt2.color("#d5ccc6")
# move to under layer of cheek
tt2.penup()
tt2.goto(102,162)
# set width and stamp
tt2.width(45)
tt2.stamp()
# Set colour to darker mask
tt2.color("#302921")
# Set turtle point direction
tt2.seth(180)
# Draw
drawCurveTaperBranch(tt2,110,180,-6.2,15,7,1,40)
# Add forehead
# Set turtle point direction
tt2.seth(180)
# Draw
drawCurveTaperBranch(tt2,110,180,-2,15,7,1,40)

# Draw bird cheek
# Move to head position of bird 1
tt2.penup()
tt2.goto(105,170)
# Set pen size, put pen down
tt2.shapesize(1)
tt2.pendown()
# Set pen heading
tt2.seth(220)
# Set bird cheek fill and outline colour
tt2.color("#d5ccc6")
tt2.fillcolor("#d5ccc6")
tt2.begin_fill()
tt2.circle(13)
tt2.end_fill()

# Draw bird body
# Turn For bird 1 body
tt2.seth(-125)
# Set bird belly colour
tt2.color("#c4ac92")
# Draw bird body
drawCurveTaperBranch(tt2,110,115,0,75,5,3,30)

# Draw bird beak
# Turn for beak
tt2.seth(-170)
# Set bird beak colour
tt2.color("#d99c41")
# Draw bird beak
drawCurveTaperBranch(tt2,84,168,-3,20,5,1,22)

# Draw bird eye
# Lift pen, move to eye position
tt2.penup()
tt2.goto(101,176)
# Set eye colour
tt2.color("#b07361")
#Set stamp size, Stamp eye
tt2.shapesize(0.5)
tt2.stamp()
# Set to pupil color
tt2.color("#000000")
#Set stamp size, Stamp pupil
tt2.shapesize(0.2)
tt2.stamp()
# BIRD 1 DONE ---------


# NEARGROUND PINE NEEDLES
# Draw rightmost cluster
drawPineCluster(tt2,315,180,30,2,25,"PaleGreen4","DarkSlateGray")
# Draw next cluster
drawPineCluster(tt2,310,140,30,2,35,"PaleGreen4","DarkSlateGray")
# Draw next cluster
drawPineCluster(tt2,295,95,30,2,35,"PaleGreen4","DarkSlateGray")

# NEARGROUND PINE BRANCH NEEDLES
# Draw upper cluster
drawPineCluster(tt2,225,145,30,2,35,"PaleGreen4","DarkSlateGray")
# Draw lower cluster
drawPineCluster(tt2,225,120,30,2,25,"PaleGreen4","DarkSlateGray")
# Draw lowerer cluster
drawPineCluster(tt2,155,15,30,2,30,"PaleGreen4","DarkSlateGray")
# Draw lowest cluster
drawPineCluster(tt2,130,-5,30,2,35,"PaleGreen4","DarkSlateGray")

# NEARGROUND FLOWERS - DARK
drawFlower(tt2,304,154,5,15,1,0.6,"#cc3f52","#cc3f52")
drawPineCluster(tt2,304,154,6,3,8,"#272725","#272725")

drawFlower(tt2,280,4,5,15,1,0.6,"#cc3f52","#cc3f52")
drawPineCluster(tt2,280,4,6,3,8,"#272725","#272725")

drawFlower(tt2,312,30,5,15,1,0.6,"#cc3f52","#cc3f52")
drawPineCluster(tt2,312,30,6,3,8,"#272725","#272725")

# NEARGROUND FLOWERS - MEDIUM
drawFlower(tt2,253,192,5,15,1,0.6,"#d67a7a","#d67a7a")
drawPineCluster(tt2,253,192,6,3,8,"#272725","#272725")

drawFlower(tt2,350,114,5,15,1,0.6,"#d67a7a","#d67a7a")
drawPineCluster(tt2,350,114,6,3,8,"#272725","#272725")

drawFlower(tt2,269,-28,5,15,1,0.6,"#d67a7a","#d67a7a")
drawPineCluster(tt2,269,-28,6,3,8,"#272725","#272725")

# SECONDARY BRANCH
# Rotate turtle accordingly and draw
tt1.right(10)
drawCurveTaperBranch(tt1,400,210,-2,35,25,6,40)
# Turn and draw straight segment
tt1.right(20)
drawTaperBranch(tt1,25,10,115)
# Finish this branch
tt1.right(30)
drawCurveTaperBranch(tt1,1234,1234,-3,14,3,6,34)
# Add additional fork
tt1.left(65)
drawCurveTaperBranch(tt1,225,-70,3,10,3,6,28)

# UPPER TWIGS
# Turn and Draw leftmost curved twig
tt1.right(170)
drawCurveTaperBranch(tt1,400,80,-2,15,5,6,60)
# Turn and draw second leftmost curved twig
tt1.right(50)
drawCurveTaperBranch(tt1,380,70,-2,15,10,6,30)

# PINE TWIG
# Pickup pen
tt1.penup()
# Turn and move to pine twig base
tt1.left(60)
tt1.goto(400,240)
# draw twig base
drawTaperBranch(tt1,15,12,160)
# draw bend in twig
drawCurveTaperBranch(tt1,1234,1234,-2.5,12,12,2,20)
# extend pine twig
drawTaperBranch(tt1,12,5,175)

# BIRD PERCH BRANCH
# Pickup pen
tt1.penup()
# Turn and move to perch twig base
tt1.right(85)
tt1.goto(225,0)
# draw twig base
drawTaperBranch(tt1,20,15,160)
# turn for final segment
tt1.left(80)
drawCurveTaperBranch(tt1,1234,1234,2,15,5,3,66)


# ------------- BIRD #2 ---------------

# Draw right wing
# Set bird wing
tt2.color("#928874")
# Turn For bird 2 wing
tt2.seth(-30)
# Draw bird wing
drawCurveTaperBranch(tt2,25,108,5.5,15,5,3,30)
# Draw right wingtip
# Set wingtip colour
tt2.color("#302921")
# Point wingtip, draw
tt2.seth(-70)
drawCurveTaperBranch(tt2,51,81,2.2,12,5,3,12)

# Draw belly
# Turn For bird 2 belly
tt2.seth(-120)
# Set bird belly colour
tt2.color("#c4ac92")
# Draw bird belly
drawCurveTaperBranch(tt2,-25,135,-5,25,10,3,45)

# Draw bird 2 body
# Set bird back colour
tt2.color("#928874")
# Turn For bird 2 body
tt2.seth(-50)
# Draw bird body
drawCurveTaperBranch(tt2,5,84,0,75,5,3,30)
# Draw nape
# Set turtle point direction
tt2.seth(170)
# Draw nape
drawCurveTaperBranch(tt2,-6,111,5,26,10,1,80)
# finish nape
# draw
# setwidth, direction
tt2.width(15)
tt2.seth(90)
drawTwig(tt2,-24,100,0,30)

# Draw left wing
tt2.seth(-85)
drawCurveTaperBranch(tt2,-27,90,-2,26,10,1,80)
# Draw left wingtip
# Set wingtip colour, width
tt2.color("#302921")
tt2.width(10)
# Set direction, draw straight border
tt2.seth(20)
drawTwig(tt2,-13,68,0,30)
# Draw primary feathers
tt2.seth(-70)
drawCurveTaperBranch(tt2,-10,60,-1,26,10,1,80)
# Draw secondary feathers
tt2.seth(-80)
drawCurveTaperBranch(tt2,10,67,-1,26,10,1,60)
# Draw wingspot
# Set colour
tt2.color("#d5ccc6")
# set direction, draw
tt2.seth(-50)
drawTwig(tt2,0,34,3,10)

# Draw tail
# Pickup pen
tt1.penup()
# Angle move to position, angle to tail upper left corner
tt1.goto(45,22)
# Point and draw to upper right corner
tt1.seth(tt1.towards(65,29))
tt1.pendown()
#start fill
tt1.begin_fill()
# Set fill and outline colour, begin drawing
tt1.width(1)
tt1.color("#302921")
tt1.fillcolor("#302921")
tt1.forward(17)
# Angle for lower right corner, draw
tt1.seth(tt1.towards(81,-22))
tt1.forward(65)
# Angle to lower left corner
tt1.seth(tt1.towards(50,-18))
tt1.forward(30)
# Angle to original corner and fill shape
tt1.seth(tt1.towards(45,22))
tt1.forward(40)
tt1.end_fill()
# Finish tail detail
# Prep size and lift pen for relocation
tt1.penup()
tt1.shapesize(0.5)
tt1.goto(62,-19)
tt1.stamp()
tt1.goto(70,-25)
tt1.stamp()
tt1.goto(78,-27)
tt1.stamp()

# Draw face pattern
# Set colour to darker mask
tt2.color("#302921")
# Set turtle point direction
tt2.seth(-10)
# Draw
drawCurveTaperBranch(tt2,-3,154,6.1,15,8,1,38)
# Add forehead
# Set turtle point direction
tt2.seth(-5)
# Draw
drawCurveTaperBranch(tt2,0,154,2,15,7,1,20)

# Draw bird cheek
# Move to head position of bird 2
tt2.penup()
tt2.goto(-6,120)
# Set pen width, put pen down
tt2.width(0)
tt2.pendown()
# Set pen heading
tt2.seth(0)
# Set bird cheek fill and outline colour
tt2.color("#d5ccc6")
tt2.fillcolor("#d5ccc6")
tt2.begin_fill()
tt2.circle(13)
tt2.end_fill()

# Draw bird beak
# Turn for beak
tt2.seth(-10)
# Set bird beak colour
tt2.color("#d99c41")
# Draw bird beak
drawCurveTaperBranch(tt2,18,142,3,20,4,1,22)

# Draw bird #2 eye
# Lift pen, move to eye position
tt2.penup()
tt2.goto(4,151)
# Set eye colour
tt2.color("#b07361")
#Set stamp size, Stamp eye
tt2.shapesize(0.5)
tt2.stamp()
# Set to pupil color
tt2.color("#000000")
#Set stamp size, Stamp pupil
tt2.shapesize(0.2)
tt2.stamp()
# BIRD 2 DONE --------------

# FOREGROUND PINE NEEDLES
# Draw uppermost cluster
drawPineCluster(tt2,335,265,30,2,35,"PaleGreen4","DarkSlateGray")
# Draw rightmost cluster
drawPineCluster(tt2,355,220,30,2,30,"PaleGreen4","DarkSlateGray")

# FLOWER BUDS
# Draw buds from left to right
# Main branch buds
drawBud(tt2,-330,-66,-350,-58,"#272725","#cc3f52",True)
drawBud(tt2,-328,-51,-320,-40,"#272725","#cc3f52",True)
drawBud(tt2,-293,-157,-281,-138,"#272725","#cc3f52",True)
drawBud(tt2,-352,-208,-357,-191,"#272725","#cc3f52",True)
drawBud(tt2,-292,-195,-294,-210,"#272725","#cc3f52",True)

# Curved twig buds
drawBud(tt2,-168,-144,-192,-138,"#272725","#cc3f52",True)
drawBud(tt2,-112,-125,-116,-136,"#272725","#cc3f52",False)
drawBud(tt2,-94,-117,-113,-100,"#272725","#cc3f52",True)

# Secondary branch buds
drawBud(tt2,115,-197,116,-218,"#272725","#cc3f52",True)
drawBud(tt2,119,-184,102,-177,"#272725","#cc3f52",False)
drawBud(tt2,309,-173,295,-190,"#272725","#cc3f52",False)

# Upper buds
drawBud(tt2,163,284,153,271,"#272725","#cc3f52",False)
drawBud(tt2,181,282,181,300,"#272725","#cc3f52",False)
drawBud(tt2,201,271,191,261,"#272725","#cc3f52",False)

# FOREGROUND FLOWERS (IN BLOOM)
# Draw flowers left to right
# Draw leftmost flowers
# Flowers - MEDIUM
drawFlower(tt2,202,15,5,15,1,0.6,"#d67a7a","#d67a7a")
drawPineCluster(tt2,202,15,6,3,8,"#272725","#272725")

# Flowers - LIGHT
drawFlower(tt2,-315,-100,5,15,1,0.6,"#dda194","#dda194")
drawPineCluster(tt2,-315,-100,15,0.5,15,"#4a3325","#4a3325")

drawFlower(tt2,-322,-201,5,15,1,0.6,"#dda194","#dda194")
drawPineCluster(tt2,-322,-201,15,0.5,15,"#4a3325","#4a3325")

drawFlower(tt2,219,298,5,15,1,0.6,"#dda194","#dda194")
drawPineCluster(tt2,219,298,15,0.5,15,"#4a3325","#4a3325")

drawFlower(tt2,310,67,5,15,1,0.6,"#dda194","#dda194")
drawPineCluster(tt2,310,67,15,0.5,15,"#4a3325","#4a3325")

drawFlower(tt2,296,-10,5,15,1,0.6,"#dda194","#dda194")
drawPineCluster(tt2,296,-10,15,0.5,15,"#4a3325","#4a3325")

drawFlower(tt2,184,88,5,15,1,0.6,"#dda194","#dda194")
drawPineCluster(tt2,184,88,15,0.5,15,"#4a3325","#4a3325")

drawFlower(tt2,112,37,5,15,1,0.6,"#dda194","#dda194")
drawPineCluster(tt2,112,37,15,0.5,15,"#4a3325","#4a3325")

drawFlower(tt2,-77,-115,5,15,1,0.6,"#dda194","#dda194")
drawPineCluster(tt2,-77,-115,15,0.5,15,"#4a3325","#4a3325")

drawFlower(tt2,278,-122,5,15,1,0.6,"#dda194","#dda194")
drawPineCluster(tt2,278,-122,15,0.5,15,"#4a3325","#4a3325")

drawFlower(tt2,182,-129,5,15,1,0.6,"#dda194","#dda194")
drawPineCluster(tt2,182,-129,15,0.5,15,"#4a3325","#4a3325")

drawFlower(tt2,252,-32,5,15,1,0.6,"#dda194","#dda194")
drawPineCluster(tt2,252,-32,15,0.5,15,"#4a3325","#4a3325")

drawFlower(tt2,275,-59,5,15,1,0.6,"#dda194","#dda194")
drawPineCluster(tt2,275,-59,15,0.5,15,"#4a3325","#4a3325")

drawFlower(tt2,234,35,5,15,1,0.6,"#dda194","#dda194")
drawPineCluster(tt2,234,35,15,0.5,15,"#4a3325","#4a3325")

# Hide turtle
tt1.hideturtle()
tt2.hideturtle()

# exit on click
canvas.exitonclick()

