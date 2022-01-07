import turtle
import time
import random

pospone = 0.1

#Score
score = 0
high_score = 0

window = turtle.Screen() #Create screen
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

#head of snake
shead = turtle.Turtle()
shead.speed(0)
shead.shape("square")
shead.color("white")
shead.penup()#quitar rastro
shead.goto(0,0)
shead.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()#quitar rastro
food.goto(0,100)

#snake body
segment = []

#Text
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0   High Score: 0", align="center", font=("Courier", 24, "normal"))

#FUNCIONES
def arriba():
    shead.direction = "up"
def abajo():
    shead.direction = "down"
def izquiera():
    shead.direction = "left"
def derecha():
    shead.direction = "right"

def mov():#movimientos
    if shead.direction == "up":
        y = shead.ycor()
        shead.sety(y + 20)
    
    if shead.direction == "down":
        y = shead.ycor()
        shead.sety(y - 20)

    if shead.direction == "left":
        x = shead.xcor()
        shead.setx(x - 20)

    if shead.direction == "right":
        x = shead.xcor()
        shead.setx(x + 20)

#Keyboard
window.listen()
window.onkeypress(arriba, "Up")
window.onkeypress(abajo, "Down")
window.onkeypress(izquiera, "Left")
window.onkeypress(derecha, "Right")   

while True:
    window.update()

    #crash walls
    if shead.xcor() > 280 or shead.xcor() < -280 or shead.ycor() > 280 or shead.ycor() < -280:
        time.sleep(1)
        shead.goto(0,0)
        shead.direction = "stop"

        #hide the segments
        for seg in segment:
            seg.goto(1000,1000)

        #clean segment list
        segment.clear()

        #Reset Score
        score = 0
        texto.clear()
        texto.write("Score: {}      High Score: {}".format(score, high_score), 
                    align="center", font=("Courier", 24, "normal"))

    #get food
    if shead.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)

        #increase score
        score += 10

        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score: {}   High Score: {}".format(score, high_score), 
                    align="center", font=("Courier", 24, "normal"))

    #move the body of snake    
    totalSeg = len(segment)
    for index in range(totalSeg -1, 0, -1):
        x = segment[index - 1].xcor()
        y = segment[index - 1].ycor()
        segment[index].goto(x,y)


    if totalSeg > 0:
        x = shead.xcor()
        y = shead.ycor()
        segment[0].goto(x,y)

    mov()

    #body collisions
    for seg in segment:
        if seg.distance(shead) < 20:
            time.sleep(1)
            shead.goto(0,0)
            shead.direction = "stop"

            #hide the segments
            for seg in segment:
                seg.goto(1000,1000)

            #clean segment list
            segment.clear()

            #Reset Score
            score = 0
            texto.clear()
            texto.write("Score: {}      High Score: {}".format(score, high_score), 
                        align="center", font=("Courier", 24, "normal"))

    
    time.sleep(pospone)

turtle.mainloop()