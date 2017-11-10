import random


def generate_matrix(w, h):
    return [[random.randint(1, 9) for x in range(w)] for y in range(h)]
    #print(m_rand)

#def what_numbers_in_matrix(nxm):
  #"""Returns integers ranging between 0-9 that are contained in an nxm matrix"""

  #numbers = Array.new([1, 2, 3, 4, 5, 6, 7, 8, 9])
  #numbers_in_matrix = Array.new([])
  #nxm.each {|vector| vector.each {|coordinate| numbers_in_matrix << coordinate if numbers.include? coordinate unless numbers_in_matrix.include? coordinate}}
  #numbers_in_matrix

def generate_boolean_matrix(w, h):
  visited = [[False for x in range(w + 1)] for y in range(h + 1)]
  return visited

def find_coloured_sets(w, h):
  colour = 2
  matrix = generate_matrix(w, h)
  visited = generate_boolean_matrix(w, h)
  #depth_first_search(matrix, nxm, visited, colour) TODO change this

def down(coordinate, nxm, colour):
  i = coordinate[0]
  j = coordinate[1]
  adjacent = False
  if nxm[i + 1][j] == colour: #We move towards the right
    coordinate = [i + 1, j]
    return coordinate
  else:
      return False

def up(coordinate, nxm, colour):
  i = coordinate[0]
  j = coordinate[1]
  adjacent = False
  if nxm[i - 1][j] == colour: #We move towards the right
    i -= 1 #We move in that direction
    coordinate = [i, j]
    return coordinate
  else:
      return False

def right(coordinate, nxm, colour):
  i = coordinate[0]
  j = coordinate[1]
  adjacent = False
  if nxm[i][j + 1] == colour: #and down
    j += 1
    coordinate = [i, j]
    return coordinate
  else:
      return False

def left(coordinate, nxm, colour):
  i = coordinate[0]
  j = coordinate[1]
  if nxm[i][j - 1] == colour: #We go up
    j -= 1
    coordinate = [i, j]
    return coordinate
  else:
      return False

def colours_in_matrix(nxm):
  m_colours = []
  for row in nxm:
      for colour in row:
        m_colours.append(colour)
  m_colours = list(set(m_colours))
  return m_colours

##############################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Determine position

def at_top_left_corner(nxm, coordinate):
    i = coordinate[0]
    j = coordinate[1]
    return i == 0 and j == 0

def at_top_right_corner(nxm, coordinate):
    i = coordinate[0]
    j = coordinate[1]
    w = len(nxm[0]) - 1
    return i == 0 and j == w

def at_bottom_left_corner(nxm, coordinate):
    i = coordinate[0]
    j = coordinate[1]
    h = len(nxm) - 1
    return i == h and j == 0

def at_bottom_right_corner(nxm, coordinate):
    i = coordinate[0]
    j = coordinate[1]
    w = len(nxm[0]) - 1
    h = len(nxm) - 1
    return i == h and j == w

def at_right_edge(nxm, coordinate):
    w = len(nxm[0]) - 1
    j = coordinate[1]
    return j == w

def at_left_edge(nxm, coordinate):
    j = coordinate[1]
    return j == 0

def at_bottom_edge(nxm, coordinate):
    h = len(nxm) - 1
    i = coordinate[0]
    return i == h

def at_top_edge(nxm, coordinate):
    i = coordinate[0]
    return i == 0
#####################################Determine position#############################

########################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Determine movement
def from_top_left(nxm, coordinate):
    i = coordinate[0]
    j = coordinate[1]
    colour = nxm[i][j]
    adjacent_squares = []
    adjacent_right = right(coordinate, nxm, colour)
    adjacent_down = down(coordinate, nxm, colour)
    if adjacent_right:
        adjacent_squares.append(tuple(adjacent_right))
    if adjacent_down:
        adjacent_squares.append(tuple(adjacent_down))
    return adjacent_squares

def from_top_right(nxm, coordinate):
    i = coordinate[0]
    j = coordinate[1]
    colour = nxm[i][j]
    adjacent_squares = []
    adjacent_left = left(coordinate, nxm, colour)
    adjacent_down = down(coordinate, nxm, colour)
    if adjacent_left:
        adjacent_squares.append(tuple(adjacent_left))
    if adjacent_down:
        adjacent_squares.append(tuple(adjacent_down))
    return adjacent_squares

def from_bottom_left(nxm, coordinate):
    i = coordinate[0]
    j = coordinate[1]
    colour = nxm[i][j]
    adjacent_squares = []
    adjacent_right = right(coordinate, nxm, colour)
    adjacent_up = up(coordinate, nxm, colour)
    if adjacent_right:
        adjacent_squares.append(tuple(adjacent_right))
    if adjacent_up:
        adjacent_squares.append(tuple(adjacent_up))
    return adjacent_squares

def from_bottom_right(nxm, coordinate):
    i = coordinate[0]
    j = coordinate[1]
    colour = nxm[i][j]
    adjacent_squares = []
    adjacent_up = up(coordinate, nxm, colour)
    adjacent_left = left(coordinate, nxm, colour)
    if adjacent_up:
        adjacent_squares.append(tuple(adjacent_up))
    if adjacent_left:
        adjacent_squares.append(tuple(adjacent_left))
    return adjacent_squares

def from_right_edge(nxm, coordinate):
    i = coordinate[0]
    j = coordinate[1]
    colour = nxm[i][j]
    adjacent_squares = []
    adjacent_up = up(coordinate, nxm, colour)
    adjacent_down = down(coordinate, nxm, colour)
    adjacent_left = left(coordinate, nxm, colour)
    if adjacent_up:
        adjacent_squares.append(tuple(adjacent_up))
    if adjacent_down:
        adjacent_squares.append(tuple(adjacent_down))
    if adjacent_left:
        adjacent_squares.append(tuple(adjacent_left))
    return adjacent_squares

def from_left_edge(nxm, coordinate):
    i = coordinate[0]
    j = coordinate[1]
    colour = nxm[i][j]
    adjacent_squares = []
    adjacent_right = right(coordinate, nxm, colour)
    adjacent_up = up(coordinate, nxm, colour)
    adjacent_down = down(coordinate, nxm, colour)
    if adjacent_up:
        adjacent_squares.append(tuple(adjacent_up))
    if adjacent_down:
        adjacent_squares.append(tuple(adjacent_down))
    if adjacent_right:
        adjacent_squares.append(tuple(adjacent_right))
    return adjacent_squares

def from_top_edge(nxm, coordinate):
    i = coordinate[0]
    j = coordinate[1]
    colour = nxm[i][j]
    adjacent_squares = []
    adjacent_right = right(coordinate, nxm, colour)
    adjacent_left = left(coordinate, nxm, colour)
    adjacent_down = down(coordinate, nxm, colour)
    if adjacent_right:
        adjacent_squares.append(tuple(adjacent_right))
    if adjacent_left:
        adjacent_squares.append(tuple(adjacent_left))
    if adjacent_down:
        adjacent_squares.append(tuple(adjacent_down))
    return adjacent_squares

def from_bottom_edge(nxm, coordinate):
    i = coordinate[0]
    j = coordinate[1]
    colour = nxm[i][j]
    adjacent_squares = []
    adjacent_right = right(coordinate, nxm, colour)
    adjacent_left = left(coordinate, nxm, colour)
    adjacent_up = up(coordinate, nxm, colour)
    if adjacent_right:
        adjacent_squares.append(tuple(adjacent_right))
    if adjacent_left:
        adjacent_squares.append(tuple(adjacent_left))
    if adjacent_up:
        adjacent_squares.append(tuple(adjacent_up))
    return adjacent_squares

def from_center(nxm, coordinate):
    i = coordinate[0]
    j = coordinate[1]
    colour = nxm[i][j]
    adjacent_squares = []
    adjacent_right = right(coordinate, nxm, colour)
    adjacent_left = left(coordinate, nxm, colour)
    adjacent_up = up(coordinate, nxm, colour)
    adjacent_down = down(coordinate, nxm, colour)
    if adjacent_up:
        adjacent_squares.append(tuple(adjacent_up))
    if adjacent_down:
        adjacent_squares.append(tuple(adjacent_down))
    if adjacent_right:
        adjacent_squares.append(tuple(adjacent_right))
    if adjacent_left:
        adjacent_squares.append(tuple(adjacent_left))
    return adjacent_squares

#####################################Determine movement#############################

def get_adjacent_squares(nxm, coordinate):
    adjacent_squares = []
    if at_top_right_corner(nxm, coordinate):
        adjacent_squares = from_top_right(nxm, coordinate)
        return adjacent_squares
    if at_top_left_corner(nxm, coordinate):
        adjacent_squares = from_top_left(nxm, coordinate)
        return adjacent_squares
    if at_bottom_right_corner(nxm, coordinate):
        adjacent_squares = from_bottom_right(nxm, coordinate)
        return adjacent_squares
    if at_bottom_left_corner(nxm, coordinate):
        adjacent_squares = from_bottom_left(nxm, coordinate)
        return adjacent_squares
    if at_top_edge(nxm, coordinate):
        adjacent_squares = from_top_edge(nxm, coordinate)
        return adjacent_squares
    if at_right_edge(nxm, coordinate):
        adjacent_squares = from_right_edge(nxm, coordinate)
        return adjacent_squares
    if at_left_edge(nxm, coordinate):
        adjacent_squares = from_left_edge(nxm, coordinate)
        return adjacent_squares
    if at_bottom_edge(nxm, coordinate):
        adjacent_squares = from_bottom_edge(nxm, coordinate)
        return adjacent_squares
    else:
        adjacent_squares = from_center(nxm, coordinate)
        return adjacent_squares

def find_connected_sets(coordinates, nxm):
    sets = []
    w = len(nxm)
    h = len(nxm[0])
    bool_matrix = generate_boolean_matrix(w, h)
    for i in range(h):
        for j in range(w):
            if (i, j) in coordinates.keys() and not bool_matrix[i][j]:
                start = (i, j)
                bool_matrix[i][j] = True
                sets.append(list(dfs(coordinates, start, bool_matrix)))
    return sets

def dfs(graph, start, bool_matrix):
    visited, stack = set(), [start]
    while stack:
        square = stack.pop()
        if square not in visited:
            i = square[0]
            j = square[1]
            bool_matrix[i][j] = True
            visited.add(square)
            stack.extend(graph[square] - visited)
    return visited

def test(nxm):
    connected_sets = []
    adjacency_dictionary = collect_adjacent_squares(nxm, connected_sets)
    set = adjacency_dictionary[8]
    start = (1, 1)
    print(dfs(set, start))

def get_connected_sets(nxm):
    colour_to_sets = {}
    connected_sets = []
    adjacency_dictionary = collect_adjacent_squares(nxm, connected_sets)
    for colour in adjacency_dictionary.keys():
        if adjacency_dictionary[colour]:
            colour_to_sets[colour] =  find_connected_sets(adjacency_dictionary[colour], nxm)
        continue
    return colour_to_sets

def get_colour_squares_helper(nxm, colour):
    colour_squares = []
    for i in range(len(nxm)):
        for j in range(len(nxm[0])):
            if nxm[i][j] == colour:
                colour_squares.append([i, j])
    return colour_squares

def collect_adjacent_squares_helper(nxm, squares_of_colour, connected_sets):
    square_to_adjacent = {}
    for square in squares_of_colour:
        if get_adjacent_squares(nxm, square):
            square_to_adjacent[tuple(square)] = set(get_adjacent_squares(nxm, square))
        else:
            connected_sets.append(list(square)) #We store the coordinate as a connected set in itself
    return square_to_adjacent

def collect_adjacent_squares(nxm, connected_sets):
    squares_with_colour = get_colour_squares(nxm)
    colour_to_squares_to_adjacent = {}
    for colour in squares_with_colour.keys():
        temporary_container = squares_with_colour[colour]
        colour_to_squares_to_adjacent[colour] = collect_adjacent_squares_helper(nxm, temporary_container, connected_sets)
    return colour_to_squares_to_adjacent

def get_colour_squares(nxm):
    squares_with_colour = {}
    colours = colours_in_matrix(nxm)
    for colour in colours:
        squares_with_colour[colour] = get_colour_squares_helper(nxm, colour)
    return squares_with_colour

def find_largest_connected_set(w, h):
    nxm = generate_matrix(w, h)
    largest_sets = {}
    largest_set_colours = []
    connected_sets = get_connected_sets(nxm)
    for colour in connected_sets.keys():
        largest_sets[colour] = max(connected_sets[colour], key=len)
    maximum_length = len(max(largest_sets.values(), key=len))
    for colour in largest_sets.keys():
        if len(largest_sets[colour]) == maximum_length:
            largest_set_colours.append(colour)
    for colour in largest_set_colours:
        print(colour)
n = 5
m = 6

#nxm = generate_matrix(3, 5)

nxm = [[1, 3, 5, 6, 6, 6], [8, 8, 5, 2, 2, 2], [2, 8, 8, 3, 4, 1], [7, 1, 8, 5, 9, 9], [9, 8, 3, 4, 2, 2]]

colours_in_matrix(nxm)
connected_sets = []

find_largest_connected_set(nxm)
