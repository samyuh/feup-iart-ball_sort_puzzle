class GameSettings:
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

        
                

            
        