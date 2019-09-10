import othello_functions
import turtle 
SQUARE = 50

class Board:
    def __init__(self, dimension):
        '''
            Parameters: Self, and the lenght of a side of the board (int),
                        creates a dimension X dimension sized board
            Returns: A board object 
            Does: Instantiates a board object with attributes 
        '''
        self.dimension = dimension
        corner = dimension * SQUARE / 2
        self.xcorner = -corner
        self.ycorner = corner
        self.limit = corner
        self.tiles = []
        self.color = 'black'

    
    def get_square(self, xcoord, ycoord):
        x = abs(int((xcoord - self.xcorner) / SQUARE))
        y = abs(int((ycoord - self.ycorner) / SQUARE))
        #lst = othello_functions.get_grid(self.dimension)
        return[x,y]


    def draw_initial_tiles(self):
        '''
            Parameters: Self
            Returns: Nothing  
            Does: Draws 4 initial tiles, 2 of each color, to the center of the
                  board 
        '''
        center_x = 0
        center_y = 0
        self.add_tile('white', center_x - 25, center_y + 25)
        self.add_tile('black', center_x + 25, center_y + 25)
        self.add_tile('black', center_x - 25, center_y - 25)
        self.add_tile('white', center_x + 25, center_y - 25)
        

    def tile_doesnt_exists(self, tile):

        '''
            Parameters: Self, and a tile (object)
            Returns: Boolean 
            Does: Checks if the tile already exists on the board 
        '''
        # Loop through each existing tile on board
        for t in self.tiles:
            if tile == t:
                return False
        return True

       
    def add_tile(self, color, x, y):
        '''
            Parameters: Self, color (string), x and y coordinates (int)
            Returns: Nothing  
            Does: Creaates a tile object, implements tile_doesnt_exist, and
                  adds tile to board if appropriate 
        '''
        tile = Tile(color, x, y)

        # Check if clicked location is within the confines of the board
        if tile.vertex_x > (self.limit) or tile.vertex_x < (-self.limit):
            return
        elif tile.vertex_y > (self.limit) or tile.vertex_y < (-self.limit):
            return

        # Add tile to board 
        if self.tile_doesnt_exists(tile):
            
            self.tiles.append(tile)
            tile.draw()
            print(self.get_square(x,y))

            # Change color for next tile 
            if self.color == 'black':
                self.color = 'white'
            else:
                self.color = 'black'

        # Check if board is full
        if self.is_board_full():
            self.winner()





    def is_legal_move(self):
        


    

    def clicked(self, x, y):
        '''
            Parameters: Self, x and y coordinates (int)
            Returns: Nothing  
            Does: Gets and passes x y coordinates
        '''
        self.add_tile(self.color, x, y)        


    def is_board_full(self):
        '''
            Parameters: Self
            Returns: Boolean  
            Does: Checks if every square on the board contains a tile
        '''
        return len(self.tiles) == self.dimension * self.dimension


    def winner(self):
        '''
            Parameters: Self
            Returns: Nothing  
            Does: Counts number of black and white tiles on the board, and
                  calculates winner or tie
        '''
        print('Game over!')
        black_tiles = 0
        white_tiles = 0
        
        # Loop through tiles list, increment black/white tile count
        for tile in self.tiles:
            if tile.get_color() == 'black':
                black_tiles += 1
            else:
                white_tiles += 1
                
        # Determine winner 
        if black_tiles > white_tiles:
            print('Black wins with %d tiles!' % black_tiles)
        elif white_tiles > black_tiles:
            print('White wins with %d tiles!' % white_tiles)
        else:
            print('Tie with %d tiles each!' % black_tiles)

        turtle.bye()        





    def __str__(self):
        '''
            Parameters: Self
            Returns: string 
            Does: Returns a string containing the board's dimension attribute
        '''
        board_str = "Board dimensions: %d X %d" % \
                    (self.dimension, self.dimension)
        return board_str


    def __eq__(self, other):
        ''' 
        Parameters: Self, and another board (both objects)
        Returns: Boolean 
        Does: Compares the list of tile objects in two board objects
        '''
        return self.tiles == other.tiles


class Tile:
    RADIUS = 20
    
    def __init__(self, color, x, y):
        '''
            Parameters: Self, tile color (string), x and y coordinates (int)
            Returns: A tile object 
            Does: Instantiates a tile object with attributes 
        '''
        self.color = color
        vertex = othello_functions.get_vertex(x, y)
        self.vertex_x = vertex[0]
        self.vertex_y = vertex[1]
        

    def draw(self):
        '''
            Parameters: Self
            Returns: Nothing 
            Does: Draws a circle at the selected square's vertex 
        '''
        turtle.hideturtle()
        turtle.speed(0)
        turtle.color(self.color)
        turtle.penup()
        turtle.goto(self.vertex_x, self.vertex_y-20)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.RADIUS)
        turtle.end_fill()


    def get_vertices(self):
        '''
            Parameters: Self
            Returns: x and y vertex coordinates (list) 
            Does: Gets the coordinates for a square's vertex 
        '''
        return [self.vertex_x, self.vertex_y]


    def get_color(self):
        '''
            Parameters: Self
            Returns: the object's color (string)
            Does: gets the color of the tile object  
        '''
        return self.color


    def __eq__(self, other):
        '''
            Parameters: Self, and another tile (both objects)
            Returns: Boolean 
            Does: Compares the vertex coordinates of two tile objects 
        '''
        return self.vertex_x == other.vertex_x and \
               self.vertex_y==other.vertex_y

    def __str__(self):
        '''
            Parameters: Self
            Returns: string 
            Does: Returns a string containing the tile's color and vertex
                  coordinates 
        '''
        tile_str = "Color: %s \n Vertex: %d, %d" % \
                   (self.color, self.vertex_x, self.vertex_y)
        return tile_str 
                                                    

    
