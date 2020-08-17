
import turtle 
t = turtle.Turtle()
t.pensize(5)

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

# ashok chakra
t.color("#054188")
for i in range(24):
    t.forward(80)
    t.backward(80)
    t.left(15)
move(0,-80)
t.circle(80, 360)


# In[4]:


# for green part
t.begin_fill()
t.color("green")
t.forward(350)
t.backward(700)
t.right(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.end_fill()

# orange part
move(-350, 80)
t.right(180)
t.begin_fill()
t.color('orange')
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.end_fill()




