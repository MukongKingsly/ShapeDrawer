# Create variables with shapes
print ("Rectangle = 1 \n Square = 2 \n Circle = 3 \n Triangle = 4\
\n Rhombus = 5 \n Parallelogram = 6  \n Trapezium = 7")

while True:
    try:
        # Choose shape to draw
        shape = int(input("Type number of shape to draw: "))
        # Choose color
        col = input("Type color: red, blue, green, yellow etc:  ")

        if shape < 8:
            # Draw using turtle graphics  
            import turtle as t
            # If user choses a Rectangle and whatever color
            if shape == 1:
                t.fillcolor(col)
                t.begin_fill()
                t.forward(300)
                t.right(90)
                t.forward(150)
                t.right(90)
                t.forward(300)
                t.right(90)
                t.forward(150)
                t.end_fill()
                t.done()
               
            # If user choses a Square and whatever color
            elif shape == 2:
                t.fillcolor(col)
                t.begin_fill()
                t.forward(300)
                t.right(90)
                t.forward(300)
                t.right(90)
                t.forward(300)
                t.right(90)
                t.forward(300)
                t.end_fill()
                t.done()
                
            # If user choses a Circle and whatever color
            elif shape == 3:
                t.fillcolor(col)
                t.begin_fill()
                t.circle(200, extent = 360)
                t.end_fill()
                t.done()

            # If user choses a triangle and whatever color
            elif shape == 4:
                t.fillcolor(col)
                t.begin_fill()
                t.circle(100, steps=3)
                t.end_fill()
                t.done()

            # If user choses a Rombus and whatever color  
            elif shape == 5:
                t.fillcolor(col)
                t.begin_fill()
                t.forward(150)
                t.right(135)
                t.forward(150)
                t.right(45)
                t.forward(150)
                t.right(135)
                t.forward(150)
                t.end_fill()
                t.done()

            # If user choses Parallelogram and whatever color   
            elif shape == 6:
                t.fillcolor(col)
                t.begin_fill()
                t.forward(300)
                t.right(120)
                t.forward(150)
                t.right(60)
                t.forward(300)
                t.right(120)
                t.forward(150)
                t.end_fill()
                t.done()

            # If user choses Trapezium and whatever color
            elif shape == 7:
                t.fillcolor(col)
                t.begin_fill()
                t.forward(200)
                t.right(60)
                t.forward(100)
                t.right(120)
                t.forward(300)
                t.right(120)
                t.forward(100)
                t.end_fill()
                t.done()
                
            else:
                print ("Choose a number from 1 to 7")
    except:
        print ("Input should be a number")
    else:
        print ("Choose a number from 1 to 7 and also check spelling of your colors!!!")
