class GameSettings:
    """
    Class for some helpful game settings

    board : List of list of int
        - Game board represented as a list of lists
    
    num_bottles : int
        - number of bottles in the game

    empty_spaces : int
        - number of empty spaces in a bottle
    
    num_balls : int
        - number of balls in a bottle
    
    num_colors : int
        - number of colors in the game
    
    ball_per_colr : int
        - number of existing balls of a certain color in the game

    """
    def __init__(self, board):
        self.board = board

        self.num_bottles = len(board)
        if self.num_bottles <= 1:
            print("You need at least two bottles")
            exit(-1)
        
        self.bottle_size = len(board[0])
        for bottle in board:
            if len(bottle) != self.bottle_size:
                print("All bottles should have the same size")
                exit(-1)

        self.empty_spaces = 0
        self.num_balls = 0
        self.num_colors = 0
        self.ball_per_color = self.bottle_size

        aux_colors = []
        for bottle in board:
            for elem in bottle:
                if elem == 0:
                    self.empty_spaces += 1
                else:
                    if elem not in aux_colors:
                        aux_colors.append(elem)
                        self.num_colors += 1
                    self.num_balls += 1

        
                

            
        