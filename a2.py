# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """ __init__:(Rat,str,int,int)->NoneType
        The first parameter represents the rat to be initialized,
        the second parameter represents the 1-character symbol for the rat,
        the third parameter represents the row where the rat is located,
        and the fourth parameter represents the column where the rat is located.

        symbol: the 1-character symbol for the rat
        row: the row where the rat is located
        col: the column where the rat is located
        num_sprouts_eaten: the number of sprouts that this rat has eaten,
                            which is initially 0.

        >>> Rat(’P’,1,4)
        >>> Rat.symbol
        'J'
        >>> Rat.row
        1
        >>> Rat.col
        4
​	    """

        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0
        self.set_location(self.row, self.col)

    def set_location(self, row, col):
        """set_location: (Rat,int,int)->NoneType
    ​	"""
        self.row = row
        self.col = col

    def eat_sprout(self):
        """eat_sprout:(Rat)->NoneType
    ​	"""
        self.num_sprouts_eaten += 1

    def __str__(self):
        """__str__:(Rat)->NoneType
​	    """
        return "{0} at ({1}, {2}) ate {3} sprouts".format(
            self.symbol, self.row, self.col, self.num_sprouts_eaten)


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = sum(maze[i].count(SPROUT)
                                    for i in range(len(self.maze)))

    def is_wall(self, row, col):
        """is_wall:(Maze,int,int)->bool
​	    """
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        """get_character:(Maze,int,int)->str
​	    """
        return\
            RAT_1_CHAR if self.rat_1.row == row and self.rat_1.col == col else \
            RAT_2_CHAR if self.rat_2.row == row and self.rat_2.col == col else \
        self.maze[row][col]

    def move(self, move_rat, vertical, horizontal):
        """move:(Maze,Rat,int,int)->bool
​	    """
        if (
                vertical == UP or vertical == DOWN or horizontal == LEFT or horizontal == RIGHT or vertical == NO_CHANGE or horizontal == NO_CHANGE):
            ##Check if wall
            if (
            self.is_wall(move_rat.row + vertical, move_rat.col + horizontal)):
                return False
            else:
                # set old location stuff
                self.maze[move_rat.row][move_rat.col] = HALL

                # if sprout
                if (self.maze[move_rat.row + vertical][
                    move_rat.col + horizontal] == SPROUT):
                    move_rat.eat_sprout()
                    self.num_sprouts_left = self.num_sprouts_left - 1

                # move rat
                self.maze[move_rat.row + vertical][
                    move_rat.col + horizontal] = move_rat.symbol
                move_rat.set_location(move_rat.row + vertical,
                                       move_rat.col + horizontal)
                return True
            
    def __str__(self):
        """__str__:(Maze)->str
​	    """
        result = ""
        for i in self.maze:
            result += str(i) + '\n'
        # result += sum(str(i) + '\n' for i in self.maze)
        return result + str(self.rat_1) + '\n' + str(self.rat_2)


if __name__ == "__main__":

    Maze1 = Maze([['#', '#', '#', '#', '#', '#', '#'],
                  ['#', '.', '.', '.', '.', '.', '#'],
                  ['#', '.', '#', '#', '#', '.', '#'],
                  ['#', '.', '.', '@', '#', '.', '#'],
                  ['#', '@', '#', '.', '@', '.', '#'],
                  ['#', '#', '#', '#', '#', '#', '#']], Rat('J', 1, 1),
                 Rat('P', 1, 4)
                 )