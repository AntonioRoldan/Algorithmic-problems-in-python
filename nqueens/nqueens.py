from string import *

################################rows and columns movement##################################

def endangered_row(position, chess_board): #Takes initial position as parameter
    letter, number = position[0], position[1]
    row_number = ascii_uppercase.index(letter)
    row = []
    for j in range(len(chess_board[0])):
        row.append(tuple(chess_board[row_number][j]))
    return tuple(row)

def endangered_column(position, chess_board):
    letter, number = position[0], position[1] - 1
    column = []
    for i in range(len(chess_board[0])):
        try:
            column.append(tuple(chess_board[i][number]))
        except:
            column.append(tuple(chess_board[i][number - 1]))
    return tuple(column)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!rows and columns movement #!!!!!!!!!!!!!!!!!!!!!!!!!!

################################diagonal movement from the corners##################################

def is_at_corner(position, n):
    letter, number = position[0], position[1]
    if (number == 1 or number == n):  # We check if queen is at either of the edge columns
        if (letter == 'A' or letter == ascii_uppercase[n - 1]):  # If so we check if it is also at the edge rows
            return True
        else:
            return False
    else:
        return False

def diagonal_from_top_left(position, n):
    letter, number = position[0], position[1]
    while(number != n): #while the program has not reached the bottom_right position
        number += 1 #We keep on drawing the diagonal all the way down
        letter = ascii_uppercase[number - 1] #Note : since our numbers range between one and zero, we subtract one for correct indexing
        yield letter, number

def diagonal_from_top_right(position):
    letter, number = position[0], position[1]
    threshold = ascii_uppercase.index(letter) #If we move from the top_right without the program knowing what the table dimensions are, we need to find them by converting the character to an integer
    while (number != 1): #while the program has not reached the bottom_left position
        number -= 1 #We keep on drawing the diagonal all the way down
        threshold += 1 #By converting the character to its corresponding index in the ascii alphabet, we can now obtained the desired values as we reach the bottom_left corner of the board
        letter = ascii_uppercase[threshold]
        yield letter, number

def diagonal_from_bottom_left(position, n):
    letter, number = position[0], position[1]
    threshold = ascii_uppercase.index(letter) #If we move from the bottom_left without the program knowing what the table dimensions are, we need to find them by converting the character to an integer
    while(number != n): #While the program has not reached the top_right position
        number += 1 #We keep on drawing the diagonal all the way up
        threshold -= 1 #By converting the character to its corresponding index in the ascii alphabet, we can now obtain the desired values as we reach the top_right corner of the board
        letter = ascii_uppercase[threshold]
        yield letter, number

def diagonal_from_bottom_right(position):
    letter, number = position[0], position[1]
    ascii_index = ascii_uppercase.index(letter)
    while(number != 1): #While the progam has not reached the top_left position
        number -= 1 #We keep on drawing the diagonal all the way up
        ascii_index -= 1
        letter = ascii_uppercase[ascii_index] #Note : since our numbers range between one and zero, we subtract one for correct indexing
        yield letter, number

def move_from_top(position, n):
    letter, number = position[0], position[1]
    is_top_left = number == 1
    if (is_top_left):
        endangered_squares = tuple(diagonal_from_top_left(position=(letter, number), n=n))
    else:  # else it will be on the right side
        endangered_squares = tuple(diagonal_from_top_right(position=(letter, number)))
    endangered_squares = move_helper(endangered_squares, position, n)
    return endangered_squares

def move_from_bottom(position, n):
    letter, number = position[0], position[1]
    is_bottom_left = number == 1
    if (is_bottom_left):
        endangered_squares = tuple(diagonal_from_bottom_left(position=(letter, number), n=n))
    else:  # else it will be on the right side
        endangered_squares= tuple(diagonal_from_bottom_right(position=(letter, number)))
    endangered_squares = move_helper(endangered_squares, position, n)
    return endangered_squares

def move_diagonal_from_corners(position, n):
    letter, number = position[0], position[1]
    is_at_top = (letter == 'A')
    if (is_at_top):
        return move_from_top(position=(letter, number), n=n)
    else:  # else it will be at the bottom
        return move_from_bottom(position=(letter, number), n=n)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!diagonal movement from the corners #!!!!!!!!!!!!!!!!!!!!!!!!!!



################################diagonal movement from the edges##################################

def is_at_edge(position, n):
    letter, number = position[0], position[1]
    right_edge = False
    left_edge = False
    top_edge = False
    bottom_edge = False
    if((number == 1 or number == n) and (letter != 'A' and letter != ascii_uppercase[n - 1])): #If it is at the right or left edge
        right_edge, left_edge = number == n, number == 1
    elif((letter == 'A' or letter == ascii_uppercase[n - 1]) and (number != 1 and number != n)):
        top_edge, bottom_edge = letter == 'A', letter == ascii_uppercase[n - 1]
    return right_edge, left_edge, top_edge, bottom_edge

def move_diagonal_down_left(position, n): #Moving up letter determines direction, number determines orientation, + letter, + - number
    """It finds the threatened squares by the queen all the way up if it is located at one of the right or left edges"""
    letter, number = position[0], position[1]
    ascii_index = ascii_uppercase.index(letter)
    while(letter != ascii_uppercase[n - 1]):
        ascii_index += 1  #We increase the index at the beginning of the loop, since we do not need to store the square where our queen is located
        letter = ascii_uppercase[ascii_index]
        number -= 1
        yield letter, number

def move_diagonal_down_right(position, n): #Moving down letter determines direction, number determines orientation, - letter, + - number
    """It finds the threatened squares by the queen all the way down if it is located at one of the right or left edges"""
    letter, number = position[0], position[1]
    ascii_index = ascii_uppercase.index(letter)
    while(letter != ascii_uppercase[n - 1]):
        ascii_index += 1 #We decrease the index at the beginning of the loop, since we do not need to store the square where our queen is located
        letter = ascii_uppercase[ascii_index]
        number += 1
        yield letter, number

def move_diagonal_up_right(position):
    """It finds the threatened squares by the queen all the way to the right if it is located at one of the top or bottom edges"""
    letter, number = position[0], position[1]
    ascii_index = ascii_uppercase.index(letter)
    while(letter != 'A'):
        ascii_index -= 1
        letter = ascii_uppercase[ascii_index]
        number += 1
        yield letter, number

def move_diagonal_up_left(position):
    """It finds the threatened squares by the queen all the way to the left if it is located at one of the top or bottom edges"""
    letter, number = position[0], position[1]
    ascii_index = ascii_uppercase.index(letter)
    while(letter != 'A'):
        ascii_index -= 1
        letter = ascii_uppercase[ascii_index]
        number -= 1
        yield letter, number

def move_from_top_edge(position, n):
    letter, number = position[0], position[1]
    endangered_squares = tuple(move_diagonal_down_left(position=(letter, number), n=n)) + tuple(move_diagonal_down_right(position=(letter, number), n=n))
    endangered_squares = move_helper(endangered_squares, position, n)
    return endangered_squares

def move_from_bottom_edge(position, n):
    letter, number = position[0], position[1]
    endangered_squares = tuple(move_diagonal_up_right(position=(letter, number))) + tuple(move_diagonal_up_left(position=(letter, number)))
    endangered_squares = move_helper(endangered_squares, position, n)
    return endangered_squares

def move_from_left_edge(position, n):
    letter, number = position[0], position[1]
    endangered_squares = tuple(move_diagonal_up_right(position=(letter, number))) + tuple(move_diagonal_down_right(position=(letter, number), n=n))
    endangered_squares = move_helper(endangered_squares, position, n)
    return endangered_squares

def move_from_right_edge(position, n):
    letter, number = position[0], position[1]
    endangered_squares = tuple(move_diagonal_up_left(position=(letter, number))) + tuple(move_diagonal_down_left(position=(letter, number), n=n))
    endangered_squares = move_helper(endangered_squares, position, n)
    return endangered_squares

def move_diagonal_from_edges(position, is_at_edge, n):
    letter, number = position[0], position[1]
    right_edge = is_at_edge[0]
    left_edge = is_at_edge[1]
    top_edge = is_at_edge[2]
    bottom_edge = is_at_edge[3]
    endangered_squares = ()
    if(right_edge):
        endangered_squares = move_from_right_edge(position=(letter, number), n=n)
    elif(left_edge):
        endangered_squares = move_from_left_edge(position=(letter, number), n=n)
    elif(top_edge):
        endangered_squares = move_from_top_edge(position=(letter, number), n=n)
    elif(bottom_edge):
        endangered_squares = move_from_bottom_edge(position=(letter, number), n=n)
    return endangered_squares + move_helper(endangered_squares, position, n)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!diagonal movement from the edges #!!!!!!!!!!!!!!!!!!!!!!!!!!


################################movement from inside the board##################################

def move_from_inside_board(position, chess_board):
    letter, number = position[0], position[1]
    n = len(chess_board[0])
    endangered_squares = tuple(move_diagonal_up_right(position=(letter, number))) + tuple(move_diagonal_up_left(position=(letter, number))) \
           + tuple(move_diagonal_down_left(position=(letter, number), n=n)) + tuple(move_diagonal_down_right(position=(letter, number), n=n)) \
           + tuple(endangered_column(position=(letter, number), chess_board=chess_board)) + tuple(endangered_row(position=(letter, number), chess_board=chess_board))
    endangered_squares = move_helper(endangered_squares, position=(letter, number), n=n)
    return endangered_squares

def move_helper(endangered_squares, position, n):
    return tuple(square for square in endangered_squares if square[1] > 0 and square[1] < n + 1) #TODO: Fix that (indices and duplicates)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!movement from inside the board#!!!!!!!!!!!!!!!!!!!!!!!!!!

def get_endangered_squares(position, chess_board):
    letter, number = position[0], position[1]
    n = len(chess_board[0])
    if (is_at_corner(position=(letter, number), n=n)):
        return move_diagonal_from_corners(position=(letter, number), n=n) + endangered_row(position=(letter,number), chess_board=chess_board) + endangered_column(position=(letter, number), chess_board=chess_board)
    elif (not all(is_at_edge(position=(letter, number), n=n)) and not any(is_at_edge(position=(letter, number), n=n))):  # If queen is within the square
        return move_from_inside_board(position=(letter, number), chess_board=chess_board)
    else:
        return move_diagonal_from_edges(position, is_at_edge(position=(letter, number), n=n), n=n) + endangered_row(position, chess_board) + endangered_column(position, chess_board)

def create_board(n):
    chess_board = []
    row = []
    for letter in range(n):
        for number in range(n):
            row.append((ascii_uppercase[letter], number + 1))
        chess_board.append(row)
        row = []
    for row in chess_board:
        print(row)
    return tuple(chess_board)

def move_down_column(position):
    """It moves the queen down the columnby one square"""
    letter, number = position[0], position[1]
    ascii_index = ascii_uppercase.index(letter)
    letter = ascii_uppercase[ascii_index + 1]
    return letter, number

def move_left_row(position):
    letter, number = position[0], position[1]
    number += 1
    return letter, number

def queens(n):
    """We will name the queens this way Q0... QN - 1"""
    for i in range(n):
        yield 'Q%s' % str(i)

def generate_permutations(endangered_squares, endangered_square_copy, column_square, chess_board):
    for previous_column_square in endangered_squares:
        if (column_square in endangered_squares[previous_column_square]):
            pass
        else:  # Endangered squares are refilled with the free squares being left by the possible combinations that result from this iteration
            endangered_squares_copy = endangered_squares.copy()
            endangered_squares_copy[
                str(previous_column_square) + str(column_square[0]) + str(column_square[1])] = get_endangered_squares(
                column_square, chess_board) + endangered_squares[previous_column_square]
            continue

def nqueens(chess_board):
    endangered_squares = {} #Free squares is a temporary container, it contains the squares that are available with every permutation
    endangered_squares_copy = {}
    possible_permutations = ()
    right_most_column = False
    down_most_row = False
    first_square = False
    digit_increased = False
    ascii_index = 0
    iterations = 0
    digit_length_increase = 0
    column_number = 1
    row_letter = "A"
    column = []
    while (not right_most_column):
        #A function called get column will move towards the right
        if (len(str(column_number)) != len(str(column_number - 1)) and not digit_increased or iterations == 100 or iterations == 90): #If we increase the amount of digits for the first nine numbers up until the 90 decimals we have before one hundred and so on
            iterations = 0
            digit_length_increase += 1
            digit_increased = True
        column_number =  column_number + 1 if down_most_row else column_number
        right_most_column = True if column_number == len(chess_board[0]) + 1 else False
        if(down_most_row):
            column_number -= 1
            row_letter = 'A'
            endangered_squares = endangered_squares_copy
            down_most_row = False
            if (digit_increased):
                iterations += 1
                endangered_squares = {permutation: square for permutation, square in endangered_squares.items() if
                                      len(permutation) == column_number * 2 + digit_length_increase * iterations}
            else:
                endangered_squares = {permutation: square for permutation, square in endangered_squares.items() if
                                      len(permutation) == column_number * 2}
            column_number += 1
        if (not endangered_squares):
             endangered_squares = {str(column_square[0]) + str(column_square[1]): get_endangered_squares(column_square, chess_board) for column_square in endangered_column(('A', 1), chess_board)}
             #Permutation maps the column number in this case one to each column_square along with the available squares it leaves
        else:
            #Here permutation should be set to A1A2, A1,B2, AN$N, B1A2, B1B2, $N$N
            column_square = (row_letter, column_number)
            if(column_square[0] == 'A' and first_square or column_square[0] != 'A'):
                column_square = move_down_column(column_square)
                row_letter, column_number = column_square[0], column_square[1]
                first_square = False
            else:
                endangered_squares_copy = endangered_squares.copy()
                first_square = True
            for previous_column_square in endangered_squares:
                if (column_square in endangered_squares[previous_column_square]):
                    pass
                else:  # Endangered squares are refilled with the free squares being left by the possible combinations that result from this iteration
                    endangered_squares_copy[previous_column_square + str(column_square[0]) + str(
                            column_square[1])] = get_endangered_squares(
                        column_square, chess_board) + endangered_squares[previous_column_square]
                    continue
            ascii_index = ascii_uppercase.index(row_letter)
            down_most_row = True if ascii_index + 1 == len(chess_board[0]) else False
            possible_permutations = tuple(endangered_squares_copy.keys())
    column_number -= 1 #After the last iteration, column number needs to be readjusted
    possible_permutations = [permutation for permutation in possible_permutations if len(permutation) == (column_number * 2) + digit_length_increase * iterations]
    return possible_permutations

def main():
    n = int(input("Give a number for the board dimensions"))
    chess_board = create_board(n) #We create an nxn dimensions board
    #position = ('H', 8)
    #print(get_endangered_squares(position, chess_board))
    permutations = nqueens(chess_board)
    print(permutations)
    #letter, number = 'A', 2
    #print(get_endangered_squares(position=(letter, number), chess_board=chess_board))
    #Beyond D level to reach the top edge
    #below E level to reach the bottom edge

if __name__ == '__main__':
    main()
