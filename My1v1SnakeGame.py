import turtle
import random 
import time 


delay = 0.05






#Screen settings
wn = turtle.Screen()
wn.title("Snake Wars")
wn.bgcolor("cyan")
wn.setup(width=1920,height = 1080)
wn.tracer(0)



#player1 head
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("red")
p1.penup()
p1.setpos(-750,0)
p1.direction = "stop"


#player2 head
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("circle")
p2.color("green")
p2.penup()
p2.setpos(750,0)
p2.direction = "stop"


#---------------------------------------------------------------------------------------
#food1
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.penup()
food.setpos(random.randint(-940,940),random.randint(-500,500))

#food2
food2 = turtle.Turtle()
food2.speed(0)
food2.shape("turtle")
food2.color("purple")
food2.penup()
food2.setpos(random.randint(-940,940),random.randint(-500,500))
#-----------------------------------------------------------------------------------------


#-----------------------------------------------------
#veriables that belongs to player1 and player2
p1tails = []
p2tails = []

p1score = 0
p2score = 0
#------------------------------------------




#General Pen >> Actually it is gonna keep score table
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("pink")
pen.penup()
pen.hideturtle()
pen.goto(0,400)
pen.write("Get 300 Points to Win",align="center",font=("Arial",30,"normal"))



#P1pen >> This veriable show score of player 1
p1pen = turtle.Turtle()
p1pen.speed(0)
p1pen.shape("square")
p1pen.color("grey")
p1pen.penup()
p1pen.hideturtle()
p1pen.goto(-800,450)
p1pen.write("Player1 Score : 0 ",align="left",font=("Arial",24,"normal"))

#P2pen >> This veriable show score of player 2
p2pen = turtle.Turtle()
p2pen.speed(0)
p2pen.shape("square")
p2pen.color("grey")
p2pen.penup()
p2pen.hideturtle()
p2pen.goto(800,450)
p2pen.write("Player2 Score : 0 ",align="right",font=("Arial",24,"normal"))







#-----------------------------------------------------------------------------------------------------
#FUNCTIONS

def resetP1nP2Score(): #Main task of this function is reset scores after winning,collisions
    p1score = 0
    p2score = 0 
    p1pen.clear()
    p2pen.clear()
    p1pen.write("Player1 Score : 0 ",align="left",font=("Arial",24,"normal"))
    p2pen.write("Player2 Score : 0 ",align="right",font=("Arial",24,"normal"))



def whoIsGet400():  #This function shows whoever has reached to 100 points it has won
    global p1score
    global p2score
    if p1score == 300:
        p2score = 0
        p1score = 0
        tellThePlwon()
        p1.goto(-750,0)
        p2.goto(750,0)
        p1.direction = "stop"
        p2.direction = "stop"
        p1pen.clear()
        p2pen.clear()
        p1pen.write("Player1 Score : 0 ",align="left",font=("Arial",24,"normal"))
        p2pen.write("Player2 Score : 0 ",align="right",font=("Arial",24,"normal"))

        #removing the tails
        remove_tails()



    elif p2score == 300:
        p2score = 0
        p1score = 0
        tellTheP2won()
        p1.goto(-750,0)
        p2.goto(750,0)
        p1.direction = "stop"
        p2.direction = "stop"
        p1pen.clear()
        p2pen.clear()
        p1pen.write("Player1 Score : 0 ",align="left",font=("Arial",24,"normal"))
        p2pen.write("Player2 Score : 0 ",align="right",font=("Arial",24,"normal"))

        #removing the tails
        remove_tails()





def tellThePlwon(): #This func show player 1 won also this func will be used in whoIsGet400()(u can see this func above)
    pen1winner = turtle.Turtle()
    pen1winner.speed(0)
    pen1winner.shape("square")
    pen1winner.color("black")
    pen1winner.penup()
    pen1winner.hideturtle()
    pen1winner.goto(0,300)
    pen1winner.write("PLAYER 1 WON",align="center",font=("Arial",30,"normal"))
    time.sleep(1)
    pen1winner.clear()




def tellTheP2won(): #This func show player 2 won also this func will be used in whoIsGet400()(u can see this func above)
    pen2winner = turtle.Turtle()
    pen2winner.speed(0)
    pen2winner.shape("square")
    pen2winner.color("black")
    pen2winner.penup()
    pen2winner.hideturtle()
    pen2winner.goto(0,300)
    pen2winner.write("PLAYER 2 WON",align="center",font=("Arial",30,"normal"))
    time.sleep(1)
    pen2winner.clear()







#removing the tails
#it removes tails after collision with boder or own
def remove_tails():
    for tail in p1tails:
        tail.goto(2000,2000)

    for tail2 in p2tails:
        tail2.goto(2000,2000)

    p1tails.clear()
    p2tails.clear()




def foodLoc(): #This func allows food1 to be shown in a random place
    food.setpos(random.randint(-940,940),random.randint(-500,500))

def foodLoc2(): #This func allows food2 to be shown in a random place
    food2.setpos(random.randint(-940,940),random.randint(-500,500))




#for player1
def p1_go_up():
    if p1.direction != "down":
        p1.direction = "up"


def p1_go_down():
    if p1.direction != "up":
        p1.direction = "down"


def p1_go_left():
    if p1.direction != "right":
        p1.direction = "left"


def p1_go_right():
    if p1.direction != "left":
        p1.direction = "right"



#for player2
def p2_go_up():
    if p2.direction != "down":
        p2.direction = "up"

def p2_go_down():
    if p2.direction != "up":
        p2.direction = "down"
        
def p2_go_left():
    if p2.direction != "right":
        p2.direction = "left"

def p2_go_right():
    if p2.direction != "left":
        p2.direction = "right"


#Keyboard bindings settings
wn.listen() 
#p1 player
wn.onkeypress(p1_go_up,"w") 
wn.onkeypress(p1_go_down,"s")
wn.onkeypress(p1_go_right,"d")
wn.onkeypress(p1_go_left,"a")

#p2 player
wn.onkeypress(p2_go_up,"Up")
wn.onkeypress(p2_go_down,"Down")
wn.onkeypress(p2_go_right,"Right")
wn.onkeypress(p2_go_left,"Left")






def move():
    if p1.direction == "up":
        p1.sety(p1.ycor()+20)


    if p1.direction == "down":
        p1.sety(p1.ycor()-20)


    if p1.direction == "right":
        p1.setx(p1.xcor()+20)


    if p1.direction == "left":
        p1.setx(p1.xcor()-20)



def move2():
    if p2.direction == "up":
        p2.sety(p2.ycor()+20)


    if p2.direction == "down":
        p2.sety(p2.ycor()-20)


    if p2.direction == "right":
        p2.setx(p2.xcor()+20)


    if p2.direction == "left":
        p2.setx(p2.xcor()-20)






#gameloop
while True:
    wn.update()


    #if player 1 hits the board
    if p1.xcor() > 950 or p1.xcor() < -950 or p1.ycor() > 530 or p1.ycor() < -530:
        time.sleep(1)
        p1.goto(-750,0)
        p2.goto(750,0)
        p1.direction = "stop"
        p2.direction = "stop"

        #removing the tails
        remove_tails()

        tellTheP2won()



    #if player 2 hits the board
    if p2.xcor() > 950 or p2.xcor() < -950 or p2.ycor() > 530 or p2.ycor() < -530:
        time.sleep(1)
        p1.goto(-750,0)
        p2.goto(750,0)
        p1.direction = "stop"
        p2.direction = "stop"

        #removing the tails
        remove_tails()

        tellThePlwon()



    #growing p1 player
    if p1.distance(food)<20 or p1.distance(food2) < 20:
        foodLoc()
        foodLoc2()

        #Add tail to p1
        p1tail = turtle.Turtle()
        p1tail.speed()
        p1tail.shape("square")
        p1tail.color("yellow")
        p1tail.penup()
        p1tails.append(p1tail)

        p1score = p1score + 10
        p1pen.clear()
        p1pen.write("Player1 Score : {} ".format(p1score),align="left",font=("Arial",24,"normal"))

        whoIsGet400()





    #Adding tail to player1 
    for index in range(len(p1tails)-1,0,-1):
        x = p1tails[index - 1].xcor()
        y = p1tails[index - 1].ycor()
        p1tails[index].goto(x,y)


    #Move tail 0 to where the head is
    if len(p1tails) > 0 :
        x = p1.xcor()
        y = p1.ycor()
        p1tails[0].goto(x,y)




    #growing p2 player
    if p2.distance(food)<20 or p2.distance(food2) < 20:
        foodLoc()
        foodLoc2()

        #Add tail to p1
        p2tail = turtle.Turtle()
        p2tail.speed()
        p2tail.shape("circle")
        p2tail.color("orange")
        p2tail.penup()
        p2tails.append(p2tail)

        p2score = p2score + 10
        p2pen.clear()
        p2pen.write("Player2 Score : {} ".format(p2score),align="right",font=("Arial",24,"normal"))

        whoIsGet400()







    #Adding tail to player1 
    for index in range(len(p2tails)-1,0,-1):
        x = p2tails[index - 1].xcor()
        y = p2tails[index - 1].ycor()
        p2tails[index].goto(x,y)


    #Move segment 0 to where the head is
    if len(p2tails) > 0 :
        x = p2.xcor()
        y = p2.ycor()
        p2tails[0].goto(x,y)



    move()
    move2()


    #if player 1 hits its own body
    for tail in p1tails:
        if tail.distance(p1) < 20:
            time.sleep(1)
            p1.goto(-750,0)
            p2.goto(750,0)
            p1.direction = "stop"
            p2.direction = "stop"

            remove_tails()

            tellTheP2won()

            resetP1nP2Score()





    #if player 2 hits its own bodu
    for tail2 in p2tails:
        if tail2.distance(p2) < 20:
            time.sleep(1)
            p1.goto(-750,0)
            p2.goto(750,0)
            p1.direction = "stop"
            p2.direction = "stop"

            remove_tails()

            tellThePlwon()

            resetP1nP2Score()

    #if player2's head hits player1's body
    for tail in p1tails:
        if p2.distance(tail) < 20:
            time.sleep(1)
            p1.goto(-750,0)
            p2.goto(750,0)
            p1.direction = "stop"
            p2.direction = "stop"

            remove_tails()

            tellThePlwon()

            resetP1nP2Score()
 

    #if player1's head hits player2's body
    for tail2 in p2tails:
        if p1.distance(tail2) < 20:
            time.sleep(1)
            p1.goto(-750,0)
            p2.goto(750,0)
            p1.direction = "stop"
            p2.direction = "stop"

            remove_tails()

            tellTheP2won()

            resetP1nP2Score()



        

    time.sleep(delay)

wn.mainloop()



