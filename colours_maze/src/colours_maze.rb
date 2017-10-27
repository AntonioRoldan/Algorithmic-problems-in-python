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
  colours_in_matrix = what_numbers_in_matrix(nxm)
  dearranged_colours = collect_square_matches(nxm, colours_in_matrix)
  puts dearranged_colours
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
