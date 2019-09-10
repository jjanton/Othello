from othello_functions import draw_board
from othello_functions import draw_lines
from othello_functions import get_vertex
from othello_functions import get_grid
from othello_classes import Board
import turtle

# Each square on the board is square X square in size
SQUARE = 50
# Board dimensions, a board object is dimension X dimension in size
DIMENSION = 4

def main():

    draw_board(DIMENSION)
    board = Board(DIMENSION)
    board.draw_initial_tiles()
    turtle.onscreenclick(board.clicked)

main()
