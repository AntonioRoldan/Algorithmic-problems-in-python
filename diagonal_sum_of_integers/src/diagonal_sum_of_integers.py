import random
import heapq

def generate_matrix(w, h):
    return [[random.randint(1, 9) for x in range(w)] for y in range(h)]

def find_diagonal_below(matrix, starting_index, ending_index):
    diagonal = []
    i = starting_index
    j = 0
    while(j != ending_index):
        diagonal.append(matrix[i][j])
        i += 1
        j += 1
    return diagonal

def find_main_diagonal(matrix, ending_index):
    main_diagonal = []
    i = 0
    j = 0
    while(i != len(matrix)):
        main_diagonal.append(matrix[i][j])
        i += 1
        j += 1
    return main_diagonal

def find_diagonal_above(matrix, starting_index, ending_index):
    diagonal = []
    i = 0
    j = starting_index
    while(i != ending_index):
        diagonal.append(matrix[i][j])
        i += 1
        j += 1
    return diagonal

def perform_addition(diagonal, n):
    """It takes the n smallest numbers and returns them plus the addition of its elements"""
    n_smallest = []
    for i in range(n + 1):
        n_smallest = heapq.nsmallest(i, diagonal)
    return sum(n_smallest), n_smallest

def find_diagonals(matrix, n):
    m = len(matrix)
    starting_index = m - n  # We find the starting index for both diagonals, one starting from the i index, and the other from j index
    ending_index = m - starting_index
    diagonal_above = find_diagonal_above(matrix, starting_index, ending_index)
    diagonal_below = find_diagonal_below(matrix, starting_index, ending_index)
    main_diagonal = find_main_diagonal(matrix, ending_index)
    return diagonal_below, diagonal_above, main_diagonal

def sum_of_diagonals(m, n):
    addition_to_diagonal = {} #It maps the result of the addition to the diagonal it is coming from
    above_main_below = []
    #matrix = generate_matrix(m, m)
    matrix = [[3, 1, 5, 6, 9], [2, 4, 1, 9, 7], [3, 5, 2, 8, 10], [4, 2, 1, 6, 8], [1, 4, 7, 9, 1]]
    #print("Matrix: ")
    #print(matrix)
    diagonal_below, diagonal_above, main_diagonal = find_diagonals(matrix, n)
    addition_to_diagonal[perform_addition(diagonal_below, n)[0]] = perform_addition(diagonal_below, n)[1]
    addition_to_diagonal[perform_addition(diagonal_above, n)[0]] = perform_addition(diagonal_above, n)[1]
    addition_to_diagonal[perform_addition(main_diagonal, n)[0]] = perform_addition(main_diagonal, n)[1]
    result = min(addition_to_diagonal.keys())
    for addition in addition_to_diagonal.keys():
        if addition == result:
            print(str(addition) + " from the addition of ")
            print("\n")
            print(addition_to_diagonal[addition])
    #print("Diagonal below: ")
    #print(diagonal_below)
    #print("Diagonal above: ")
    #print(diagonal_above)
    #print("Main diagonal: ")
    #print(main_diagonal)

sum_of_diagonals(5, 4)

