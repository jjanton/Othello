import turtle 
SQUARE = 50
        
def draw_board(n):
    ''' Function: draw_board
        Parameters: n, an int for # of squares
        Returns: nothing
        Does: Draws an nxn board with a green background
    '''

    turtle.setup(n * SQUARE + SQUARE, n * SQUARE + SQUARE)
    turtle.screensize(n * SQUARE, n * SQUARE)
    turtle.bgcolor('white')

    # Create the turtle to draw the board
    othello = turtle.Turtle()
    othello.penup()
    othello.speed(0)
    othello.hideturtle()

     # Line color is black, fill color is green
    othello.color("black", "forest green")
    
    # Move the turtle to the upper left corner
    corner = -n * SQUARE / 2
    othello.setposition(corner, corner)
  
    # Draw the green background
    othello.begin_fill()
    for i in range(4):
        othello.pendown()
        othello.forward(SQUARE * n)
        othello.left(90)
    othello.end_fill()

    # Draw the horizontal lines
    for i in range(n + 1):
        othello.setposition(corner, SQUARE * i + corner)
        draw_lines(othello, n)

    # Draw the vertical lines
    othello.left(90)
    for i in range(n + 1):
        othello.setposition(SQUARE * i + corner, corner)
        draw_lines(othello, n)


def draw_lines(turt, n):
    turt.pendown()
    turt.forward(SQUARE * n)
    turt.penup()


def get_vertex(x,y):

    '''
        Parameters: x and y coordinates (int)
        Returns: The square's vertex (list)
        Does: Takes the x and y vertex 
    '''

    
    xvertex = int(x / SQUARE) * SQUARE
    yvertex = int(y / SQUARE) * SQUARE

    if x < 0:
        xvertex -= SQUARE
    if y > 0:
        yvertex += SQUARE
        

    xvertex = int(xvertex + (SQUARE / 2))
    yvertex = int(yvertex - (SQUARE / 2))
    return [xvertex, yvertex]


    
def get_grid(n):
    '''
        Parameters: length of board (int)
        Returns: Nested list
        Does: takes the lenght of the board, and creates a nested list
              representing individual squares
    '''

    lst = [[i for i in range(n)] for i in range(n)]
    return lst



