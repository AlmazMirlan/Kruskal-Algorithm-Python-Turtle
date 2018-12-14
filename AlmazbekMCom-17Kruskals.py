import turtle
import time
turtle.title("Kruskal's Algorithm")


turtle.bgcolor("#FFD700")

    #FIRST PART

turtle.shape("turtle")
turtle.shapesize(2)
turtle.pensize(5)
turtle.hideturtle();
#turtle.home()

turtle.speed(1)
turtle.penup();
turtle.left(90);turtle.fd(250);
turtle.left(90);turtle.fd(50)
turtle.left(180)
turtle.color("purple")
turtle.write("Kruskal's Algorithm",align="center",font=("Freestyle Script",50,"normal"))
turtle.home()
turtle.right(135)
turtle.fd(400)
turtle.right(45)
turtle.fd(50)
turtle.write("Almazbek Mirlan uulu Com-17",align="center",font=("Freestyle Script",50,"normal"))


turtle.home()
turtle.left(90)
turtle.fd(200)
turtle.left(90)
turtle.fd(35)
turtle.write("Kruskal's Algorithm is one of the greedy algorithm to find the minimum spanning tree of a graph. " ,align="center",font=("Freestyle Script",23,"normal"))
turtle.home()
turtle.left(90)
turtle.fd(170)
turtle.left(90)
turtle.fd(35)
turtle.write("A spanning tree is a subgraph that contains all the vertices of the original graph. ",align="center",font=("Freestyle Script",23,"normal"))
turtle.home()
turtle.left(90)
turtle.fd(140)
turtle.left(90)
turtle.fd(350)
turtle.write("The steps for implementing Kruskal's algorithm are as follows:",align="center",font=("Freestyle Script",25,"normal"))
turtle.home()
turtle.left(90)
turtle.fd(110)
turtle.left(90)
turtle.fd(350)
turtle.write("1.Sort all the edges from low weight to high",align="center",font=("Freestyle Script",25,"normal"))
turtle.home()
turtle.left(90)
turtle.fd(90)
turtle.left(90)
turtle.fd(350)
turtle.write("2.Take the edge with the lowest weight and add it to the spanning tree. ",align="center",font=("Freestyle Script",25,"normal"))
turtle.home()
turtle.left(90)
turtle.fd(70)
turtle.left(90)
turtle.fd(350)
turtle.write("     If adding the edge created a cycle, then reject this edge.",align="center",font=("Freestyle Script",25,"normal"))
turtle.home()
turtle.left(90)
turtle.fd(50)
turtle.left(90)
turtle.fd(350)
turtle.write("3.Keep adding edges until we reach all vertices.",align="center",font=("Freestyle Script",25,"normal"))

#draw
turtle.home()


turtle.color("black")
turtle.left(135)
turtle.fd(40)
turtle.right(135)
turtle.left(180)

turtle.write("A",align="center",font=("Freestyle Script",20,"normal"))
turtle.left(180)
turtle.fd(210)
turtle.write("B",align="center",font=("Freestyle Script",20,"normal"))
#turtle.left(180)
turtle.fd(215)
turtle.write("C",align="center",font=("Freestyle Script",20,"normal"))
turtle.left(270)
turtle.fd(90)
turtle.write("D",align="center",font=("Freestyle Script",20,"normal"))
turtle.fd(90)
turtle.write("E",align="center",font=("Freestyle Script",20,"normal"))
turtle.left(270)
turtle.fd(200)
turtle.write("F",align="center",font=("Freestyle Script",20,"normal"))

turtle.fd(225)
turtle.write("G",align="center",font=("Freestyle Script",20,"normal"))
turtle.left(270)
turtle.fd(90)
turtle.write("H",align="center",font=("Freestyle Script",20,"normal"))
turtle.left(270)
turtle.fd(220)

turtle.write("I",align="center",font=("Freestyle Script",20,"normal"))




turtle.home()
turtle.left(135)
turtle.fd(20)
turtle.right(135)

turtle.pd()
turtle.showturtle()
turtle.dot(20, "green");
turtle.fd(50)
turtle.fd(75); 
turtle.write ("8",font=("Arial", 16, "normal"))
turtle.fd(75); turtle.dot(20, "green"); turtle.fd(75)
turtle.write ("11",font=("Arial", 16, "normal"))
turtle.fd(75); 
turtle.fd(50); turtle.dot(20, "green");


turtle.right(90);turtle.dot(20, "green");turtle.fd(40)
turtle.write ("   2",font=("Arial", 16, "normal"))
turtle.fd(40)
turtle.dot(20, "green");turtle.fd(40);
turtle.write("   2",font=("Arial", 16, "normal"))
turtle.fd(40);turtle.dot(20, "green")

turtle.right(90);turtle.dot(20, "green");turtle.fd(100)
turtle.write ("4",font=("Arial", 16, "normal"))
turtle.fd(100)

turtle.dot(20,"green");turtle.fd(100)
turtle.write("5",font=("Arial", 16, "normal"))

turtle.fd(100)

turtle.right(90);turtle.dot(20,"green")
turtle.fd(40);turtle.write("   6",font=("Arial", 16, "normal"))
turtle.fd(40);turtle.dot(20,"green");turtle.fd(40)

turtle.write("   7",font=("Arial", 16, "normal"))

turtle.fd(40);turtle.right(90)

turtle.right(90);turtle.fd(80);turtle.dot(20, "green");turtle.left(90);turtle.fd(100);
turtle.write("15",font=("Arial", 16, "normal"))
turtle.fd(100);turtle.dot(20,"green");turtle.fd(100);
turtle.write("12",font=("Arial", 16, "normal"))
turtle.fd(100)

turtle.right(180);turtle.fd(200);turtle.dot(20,"green")


turtle.left(90);turtle.fd(40);turtle.write("   18",font=("Arial", 16, "normal"))
turtle.fd(40);turtle.dot(20,"green")


turtle.right(180);turtle.fd(100);turtle.write("   9",font=("Arial", 16, "normal"))
turtle.fd(60);turtle.dot(20,"green")



# table part
turtle.up()
turtle.hideturtle()
turtle.home()
turtle.left(90)
turtle.fd(20)
turtle.left(90)
turtle.fd(400)
turtle.color("green")
turtle.write("  СD=2   DE=2   EF=4  FG=5   GH=6  HA=7   AB=8   BI=9  ",align="center",font=("Freestyle Script",23,"normal"))  
turtle.home()
turtle.right(90)
turtle.fd(15)
turtle.right(90)
turtle.fd(400)
turtle.color("green")
turtle.write("  BC= 11    ID=12   IH=15   IF=18",align="center",font=("Freestyle Script",23,"normal"))  




turtle.home()
turtle.left(135)
turtle.fd(20)
turtle.right(135)
turtle.fd(403);turtle.dot(20,"green")
turtle.showturtle()
turtle.pd()

#SECOND PART

time.sleep(10)
turtle.pensize(15)
turtle.fillcolor("red")

turtle.color("red")



turtle.right(90);turtle.fd(163);turtle.dot(10,"red")
turtle.right(90);turtle.fd(203);turtle.dot(10,"red")
turtle.fd(203);turtle.dot(10,"red")
turtle.right(90);turtle.fd(85);turtle.dot(10,"red")
turtle.fd(83);turtle.dot(10,"red")
turtle.right(90);turtle.fd(203);turtle.dot(10,"red")
turtle.right(90);turtle.fd(80);turtle.dot(10,"red")

turtle.exitonclick()
 


