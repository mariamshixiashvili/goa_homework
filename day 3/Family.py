mother  = "nino"
father = "gio"
grandma = "leila"

print(mother + " " + father + " " + grandma)
print(mother)
print(father)
print(grandma)



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
left(90)
forward(50)
right(90)
forward(20)
right(90)
forward(50)