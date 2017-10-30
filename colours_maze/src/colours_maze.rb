
=begin
Consider a nxm matrix, with elements decimal digits (natural numbers between 1 and 9), representing colors.
A connected set associated to an element is the set of elements that may be reached from this element,
by successive moves on a same row or column preserving the same color.
It is to determine the size and the colour of the biggest connected set. In case of multiple solutions, display them all.
=end


def determine_coordinate_position(nxm, coordinate)
  at_top, at_bottom, at_right_edge, at_left_edge = false, false, false, false
  top_right, top_left, bottom_right, bottom_left = false, false, false, false
  y, x = coordinate[0], coordinate[1]
  n_dimension = nxm[0].length - 1
  m_dimension = nxm.length - 1 #This way we avoid having an ugly and necessary - 1 for the comparisons
  at_top = true if(y == 0)
  at_bottom = true if(y == m_dimension)
  at_right_edge = true if(x == n_dimension)
  at_left_edge = true if(x == 0)
  #We now proceed to find whether our coordinate lays at any of the corners
  top_right = true if(at_top and x == n_dimension)
  top_left = true if(at_top and x == 0)
  bottom_right = true if(at_bottom and x == n_dimension)
  bottom_left = true if(at_bottom and x == 0)
  coordinate_position = {:at_edge => [at_top, at_bottom, at_right_edge, at_left_edge], :at_corner => [top_right, top_left, bottom_right, bottom_left]}
end

def towards_right(nxm, position_at)
  matches = Array.new([])
  n_dimensions = nxm[0].length - 1
  x, y =  position_at[1], position_at[0]
  colour = nxm[y][x]
  loop do
    x += 1
    if nxm[y][x] != colour or x == n_dimensions
       matches << [y, x] if nxm[y][x] == colour #We make sure that we catch the last one coloured square after the condition has been met, if there is any
      return matches
    end
    matches << [y, x]
  end
end

def towards_left(nxm, position_at)
  matches = Array.new([])
  x, y = position_at[1], position_at[0]
  colour = nxm[y][x]
  loop do
    x -= 1
    if nxm[y][x] != colour or x == 0
       matches << [y, x] if nxm[y][x] == colour #We make sure that we catch the last one coloured square after the condition has been met, if there is any
      return matches
    end
    matches << [y, x]
  end
end

def upwards(nxm, position_at)
  matches = Array.new([])
  x, y = position_at[1], position_at[0]
  colour = nxm[y][x]
  loop do
    y -= 1
    if nxm[y][x] != colour or y == 0
       matches << [y, x] if nxm[y][x] == colour #We make sure that we catch the last one coloured square after the condition has been met, if there is any
       return matches
    end
    matches << [y, x]
  end
end

def downwards(nxm, position_at)
  matches = Array.new([])
  x, y = position_at[1], position_at[0]
  m_dimension = nxm.length - 1
  colour = nxm[y][x]
  loop do
    y += 1
    if nxm[y][x] != colour or y == m_dimension
       matches << [y, x] if nxm[y][x] == colour #We make sure that we catch the last one coloured square after the condition has been met, if there is any
       return matches
    end
    matches <<  [y, x]
  end
end

def top_right_diagonal(nxm, position_at)
  matches = Array.new([])
  x, y = position_at[1], position_at[0]
  n_dimension = nxm[0].length - 1
  colour = nxm[y][x]
  loop do
    y -= 1
    x += 1
    if nxm[y][x] != colour or (y == 0 or x == n_dimension)
       matches << [y, x] if nxm[y][x] == colour #We make sure that we catch the last one coloured square after the condition has been met, if there is any
       return matches
    end
    matches << [y, x]
  end
end

def top_left_diagonal(nxm, position_at)
  matches = Array.new([])
  x, y = position_at[1], position_at[0]
  colour = nxm[y][x]
  loop do
    x -= 1
    y -= 1
    if nxm[y][x] != colour or (y == 0 or x == 0)
       matches << [y, x] if nxm[y][x] == colour #We make sure that we catch the last one coloured square after the condition has been met, if there is any
       return matches
    end
    matches << [y, x]
  end
end

def bottom_left_diagonal(nxm, position_at)
  matches = Array.new([])
  x, y = position_at[1], position_at[0]
  m_dimension = nxm.length - 1
  n_dimension = nxm[0].length - 1
  colour = nxm[y][x]
  loop do
    y += 1
    x -= 1
    if nxm[y][x] != colour or (y == m_dimension or x == 0)
      matches << [y, x] if nxm[y][x] == colour #We make sure that we catch the last one coloured square after the condition has been met, if there is any
      return matches
    end
    matches << [y, x]
  end
end

def bottom_right_diagonal(nxm, position_at)
  matches = Array.new([])
  x, y = position_at[1], position_at[0]
  n_dimensions = nxm.length - 1
  m_dimensions = nxm[0].length - 1
  colour = nxm[y][x]
  loop do
    y += 1
    x += 1
    if nxm[y][x] != colour or (y == m_dimensions or x == n_dimensions)
       matches << [y, x] if nxm[y][x] == colour #We make sure that we catch the last one coloured square after the condition has been met, if there is any
       return matches
    end
    matches << [y, x]
  end
end

def compute_matches_from_corner(nxm, which_corner)
  <<-DOC
  Computes adjacent blocks with same colour/number in an nxm matrix
  We can understand the multiple directions better 
  by imagining a clock ticking but in this case we will only cover one of the quarters
  DOC
  top_right, top_left, bottom_left, bottom_right = which_corner[:at_corner][0], which_corner[:at_corner][1], which_corner[:at_corner][2], which_corner[:at_corner][3]
  x, y = nxm[0].length - 1, 0 if top_right
  x, y = 0, 0 if top_left
  x, y = nxm[0].length - 1, nxm.length - 1 if bottom_right
  x, y = 0, nxm.length - 1 if bottom_left
  position_at = y, x
  return (upwards(nxm, position_at) << top_right_diagonal(nxm, position_at) << towards_right(nxm, position_at)).flatten! if bottom_left #First try first quarter
  return (towards_right(nxm, position_at) << bottom_right_diagonal(nxm, position_at) << downwards(nxm, position_at)).flatten! if top_left #Secondly try second quarter
  return (downwards(nxm, position_at) << bottom_left_diagonal(nxm, position_at) << towards_left(nxm, position_at)).flatten! if top_right #Thirdly try third quarter
  return (towards_left(nxm, position_at) << top_left_diagonal(nxm, position_at) <<  upwards(nxm, position_at)).flatten! if bottom_right #Last, go for the fourth quarter
end

def compute_matches_from_edge(nxm, what_edge, position_at)
  <<-DOC
  Computes adjacent blocks with same colour/number in an nxm matrix 
  We can understand the mutliple directions better  
  by imagining a clock ticking except in this case we will only cover half an hour
  DOC
  top_edge, bottom_edge, right_edge, left_edge = what_edge[:at_edge][0], what_edge[:at_edge][1], what_edge[:at_edge][2], what_edge[:at_edge][3]
  return (towards_right(nxm, position_at) << bottom_right_diagonal(nxm, position_at) << downwards(nxm, position_at) << towards_left(nxm, position_at) <<
      bottom_left_diagonal(nxm, position_at)).flatten! if top_edge #Twelve o' clock
  return (upwards(nxm, position_at) << top_left_diagonal(nxm, position_at) << towards_left(nxm, position_at) <<
      bottom_left_diagonal(nxm, position_at) << downwards(nxm, position_at)).flatten! if right_edge #Three o' clock
  return (towards_left(nxm, position_at) << top_left_diagonal(nxm, position_at) <<
      upwards(nxm, position_at) << top_right_diagonal(nxm, position_at) << towards_right(nxm, position_at)).flatten! if bottom_edge #Six o' clock
  return (upwards(nxm, position_at) << top_right_diagonal(nxm, position_at) << towards_right(nxm, position_at) << bottom_right_diagonal(nxm, position_at) <<
  downwards(nxm, position_at)).flatten! if left_edge #Nine o' clock
end

def compute_matches_from_center(nxm, position_at)
  <<-DOC
  Computes adjacent blocks with same colour/number in an nxm matrix 
  We can understand the multiple directions better 
  by imagining a clock ticking except in this case we will cover the whole hour
  DOC
  matches = (upwards(nxm, position_at) << top_right_diagonal(nxm, position_at) << towards_right(nxm, position_at) <<
      bottom_right_diagonal(nxm, position_at) << downwards(nxm, position_at) << top_left_diagonal(nxm, position_at) <<
      bottom_left_diagonal(nxm, position_at) << towards_left(nxm, position_at)).flatten!
  matches
end

def find_adjacent_matches(nxm, coordinate)
  matches = Array.new([])
  at_center = true #We assume from the beginning that the coordinate is going to be located at the center of the board
  coordinate_at = determine_coordinate_position(nxm, coordinate)
  x, y = coordinate[1], coordinate[0]
  at_center = false unless ((x != 0 and x != nxm[0].length - 1) and (y != 0 and y != nxm.length - 1))
  at_corner = coordinate_at[:at_corner].any?
  only_at_edge = !at_corner && !at_center
  if at_center
    matches = compute_matches_from_center(nxm, coordinate)
  else
    matches = compute_matches_from_edge(nxm, coordinate_at, coordinate) if only_at_edge
    matches = compute_matches_from_corner(nxm, coordinate_at) if at_corner
  end
  matches = matches.each_slice(2).to_a if matches.length > 2
  matches
end

def what_numbers_in_matrix(nxm)
  <<-DOC
  Returns integers ranging between 0-9 that are contained in an nxm matrix
  DOC
  numbers = Array.new([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  numbers_in_matrix = Array.new([])
  nxm.each {|vector| vector.each {|coordinate| numbers_in_matrix << coordinate if numbers.include? coordinate unless numbers_in_matrix.include? coordinate}}
  numbers_in_matrix
end

def collect_square_matches(nxm, colours_in_matrix)
  <<-DOC
  Gets a dictionary of dictionaries mapping colours to a dictionary containing their corresponding 
  coordinates along with their adjacents, by colour we mean a number ranging between 0-9
  DOC
  colour_spots = {}
  colours_in_matrix.each {|colour| colour_spots[colour] = find_colour_spots(nxm, colour)}
  colour_spots
end

def find_largest_connected_set(nxm)
  arranged_colour_spots = {}
  colour_spots = Array.new([]) #A 2D array containing
  colours_in_matrix = what_numbers_in_matrix(nxm)
  dearranged_colours = collect_square_matches(nxm, colours_in_matrix)
  colours_in_matrix.each do |colour|
    colour_spots[colour] = find_connected_sets(dearranged_colours[colour])
  end
end

def get_random_key(dearranged_squares, visited_squares)
  if visited_squares.empty?
    random_key = dearranged_squares.keys.sample(1)
  else
    random_key = (dearranged_squares.keys - visited_squares.flatten!.slice(2).to_a).sample(1)
  end
  random_key
end

def at_which_corner(cur, square)
  <<-DOC
  It tells whether not a square is attached to another (cur in this case) by its corners 
  if so it gives the corner at which it is attached, the data is stored in a hash
  DOC
  at_which_corner = Array.new([])
  c_x, c_y = cur[1], cur[0]
  s_x, s_y = square[1], square[0]
  at_top_left, at_top_right, at_bottom_right, at_bottom_left = false, false, false, false
  at_top_right = true if(s_x - c_x == 1 and c_y - s_y == 1) #We find it by subtracting coordinates
  at_top_left = true if (c_x - s_x == 1 and c_y - s_y == 1)
  at_bottom_right = true if (s_x - c_x == 1 and s_y - c_y == 1)
  at_bottom_left = true if(c_x - s_x == 1 and s_y - c_y == 1)
  at_which_corner << at_top_right << at_top_left << at_bottom_right << at_bottom_left
  at_which_corner if at_which_corner.any? else false
end

def squares_attached_to_corner(dearranged_colours, cur)
  <<-DOC
  It returns a dictionary with each square adjacent to a given colour by its corners along with the point at which they are (top_left, top_right...)
  Returns false if there are none
  DOC
  squares_at_corners = {} #Dictionary containing the squares which are attached at the corner and the corner at which the are attached
  adjacent_squares = dearranged_colours[cur]
  adjacent_squares.each {|square| squares_at_corners[square] = at_which_corner(cur, square) if at_which_corner(cur, square)}
  adjacent_squares = false if adjacent_squares.empty? #If the square has no squares at any of the corners return a false boolean
  adjacent_squares
end

def succesive_diagonal_squares(square, dearranged_colours, at_which_corner )
  <<-DOC
  It handles the possible case where there are several squares 
  only connected by their corners until it reaches a fully connected set or any of the board's edges
  DOC
  
end

def filter_corner_squares_helper(dearranged_colours, cur, at_which_corner)
  <<-DOC
  It will tell us whether not the given square is in turn connected to a whole different connected set 
  if so it will check if it is connected only diagonally which would mean it is an individual set consisting of 
  a single square otherwise it will tell us whether it is part of a whole connected set (in which case we will ignore it
  for it to be processed later on)
  It should also handle the case where the square is part of a succesion of diagonally connected squares
  DOC
  top_right, top_left, bottom_right, bottom_left = at_which_corner[0], at_which_corner[1], at_which_corner[2], at_which_corner[3]
  at_top, at_bottom, on_right, on_left = false, false, false, false
  x, y = cur[1], cur[0]
  dearranged_colours[cur].each do |adjacent|
    x_a, y_a = adjacent[1], adjacent[0]
    if top_right
        if x_a == x and y - y_a == 1 #If there is a sqaure attached to it in the same column
          at_top = true
        end
        if x_a - x == 1 and y == y_a #If there is a square attached to it in the same row
          on_right = true
        end
        if at_top or on_right #If there is a square attached to it in the same row or column
          next #We ignore it for it to be processed later on as another independent fully connected set
        else #If not we know it is connected by its corners to either another fully connected set or another independent square
          succesive_diagonal_squares(adjacent, dearranged_colours, at_which_corner)
        end
    elsif top_left
      if x_a == x and y - y_a == 1
        at_top = true
      end
      if x - x_a == 1 and y == y_a
        on_left = true
      end
      if at_top or on_left #If there is a square attached to it in the same row or column
        next #We ignore it for it to be processed later on as another independent fully connected set
      else #If not we know it is connected by its corners to either another fully connected set or another independent square
        succesive_diagonal_squares(adjacent, dearranged_colours, at_which_corner)
      end
    elsif bottom_right
      if x_a - x == 1 and y == y_a #If there is a square attached to it in the same row
        on_right = true
      end
      if y_a - x == 1 and x == x_a #If there is a square attached to it in the same column
        at_bottom =  true
      end
      if on_right or at_bottom #If there is a square attached to it in the same row or column
        next #We ignore it for it to be processed later on as another independent fully connected set
      else #If not we know it is connected by its corners to either another fully connected set or another independent square
        succesive_diagonal_squares(adjacent, dearranged_colours, at_which_corner)
      end
    elsif bottom_left
      if x - x_a == 1 and y == y_a #If there is a square attached to it in the same row
        on_left = true
      end
      if y_a - x == 1 and x == x_a #If there is a square attached to it in the same column
        at_bottom =  true
      end
      if on_left or at_bottom #If there is a square attached to it in teh same row or column
        next #We ignore it for it to be processed later on as another independent fully connected set
      else #If not we know it is connected by its corners to either another fully connected set or another independent square
        succesive_diagonal_squares(adjacent, dearranged_colours, at_which_corner)
      end
    end
end

def filter_corner_squares(colour_spots, adjacent_squares, dearranged_colours)
  adjacent_squares.each do |square|
    squares_at_each_corner = squares_attached_to_corner(dearranged_colours[square], square)
    if squares_at_each_corner.any?
      squares_at_each_corner.each_pair do |adjacent, at_which_corner|
        if dearranged_colours[adjacent].length == 1 #If it is connected to the corner and the length of squares connected to it is one we can delete it
            colour_spots << adjacent #We consider it a unique set consisting of a single square
            dearranged_colours.delete(adjacent) #We delete the element from the dictionary
            dearranged_colours[square].delete(adjacent) #and from the squares contained there
        elsif (dearranged_colours[square] & dearranged_colours[adjacent]).empty? #If there is no intersection between these
            #We will have two possible cases

        else #If despite being at the corner

          end
      end
    else #In this case we may have
      next
  end
end

def find_connected_sets(dearranged_squares) #P1: dictionary of key: square value: square of same colour P2: Return value, 2D array with connected colour sets
  <<-DOC
  Finds connected sets of a given colour
  DOC
  colour_spot = Array.new([]) #It stores a connected set
  colour_spots = Array.new([]) #It stores all connnected sets of a given colour
  adjacent_to_adjacent = Array.new([]) #Adjacent to adjacent is going to store the connections that squares that are connected to our current square have
  dearranged_squares.each_key do |square|
    if dearranged_squares[square].empty? #Those elements that are not connected to any other
      colour_spots << square #Will be considered individual connected sets consisting of a single square
      dearranged_squares.delete(square) #We delete them from dearranged_squares
    end
  end
  until dearranged_squares.empty? do
    cur = get_random_key(dearranged_squares, colour_spot) #First we pick up a random square which we know has not already been spotted
    adjacent_squares = dearranged_squares[cur]
    colour_spots.push(colour_spot) unless colour_spot.empty?
    colour_spot.clear
    loop do
      filter_corner_squares(colour_spots, adjacent_squares, dearranged_colours)
      adjacent_squares.each {|square| dearranged_squares[square].each {|adjacent_square| adjacent_to_adjacent << adjacent_square}}
      if colour_spot.empty?
        colour_spot << adjacent_squares & adjacent_to_adjacent
        adjacent_squares = adjacent_to_adjacent - adjacent_squares
      else #if colour spot is not empty we know that adjacent squares has already been filled
        adjacent_squares = adjacent_to_adjacent - adjacent_squares
        colour_spot << (adjacent_to_adjacent & adjacent_squares) & colour_spot
        if ((adjacent_to_adjacent - adjacent_squares) - colour_spot).empty? #If the difference operation between the sets of squares not visited yet and the ones we already visited is empty
          colour_spots << colour_spot #We already found our main colour spot
          break #and so we can stop our subroutine
        end
      end
      adjacent_to_adjacent.clear #We empty adjacent to adjacent but not colour_spot since we will need it to get our random key
    end
  end
  colour_spots #And return our value
end

def find_squares_with_colour(nxm, colour)
  <<-DOC
  Returns an array containing all x, y coordinates in the matrix where a certain colour can be found
  DOC
  colour_found_at = Array.new([]) #Contains all coordinates where a certain colour can be found
  nxm.each_index do |y|
    nxm[y].each_index do |x|
      colour_found_at << [y, x] if nxm[y][x] == colour
    end
  end
  colour_found_at
end

def find_colour_spots(nxm, colour)
  squares_adjacents = {}
  coloured_squares = find_squares_with_colour(nxm, colour)
  coloured_squares.each {|square| squares_adjacents[square] = find_adjacent_matches(nxm, square)}
  squares_adjacents
end


nxm = [[2, 2, 7], [9, 5, 5], [5, 9, 9]]

numbers_in_matrix = what_numbers_in_matrix(nxm)
squares_with_colour_5 = find_squares_with_colour(nxm, 5)
adjacent_matches_for_5 = find_adjacent_matches(nxm, [1, 1])
puts find_largest_connected_set(nxm)

