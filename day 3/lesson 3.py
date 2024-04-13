from turtle import*

#we want to paint a house 

#step 1: draw a square
shape("turtle")
#speed(30)
width(7)
color("purple")
forward(100)
left(90)

forward(100)
left(90)

forward(100)
left(90)

forward(100)
left(90)
#end of square

#drawing a door

forward(40)
color("yellow")
begin_fill()
left(90)
forward(50)
right(90)
forward(20)
right(90)
forward(50)
end_fill()

penup()
goto(100, 100)
pendown()


color("red")
forward(100)
bgcolor("green")
penup()
goto(-1000,-50)
pendown()
color("skyblue")
begin_fill()