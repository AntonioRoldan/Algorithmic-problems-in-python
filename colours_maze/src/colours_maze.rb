
=begin
Consider a nxm matrix, with elements decimal digits (natural numbers between 1 and 9), representing colors.
A connected set associated to an element is the set of elements that may be reached from this element,
by successive moves on a same row or column preserving the same color.
It is to determine the size and the colour of the biggest connected set. In case of multiple solutions, display them all.
=end

def what_numbers_in_matrix(nxm)
  <<-DOC
  Returns integers ranging between 0-9 that are contained in an nxm matrix
  DOC
  numbers = Array.new([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  numbers_in_matrix = Array.new([])
  nxm.each {|vector| vector.each {|coordinate| numbers_in_matrix << coordinate if numbers.include? coordinate unless numbers_in_matrix.include? coordinate}}
  numbers_in_matrix
end

def assemble_rows_sets(nxm, colour)
  <<-DOC
  Returns an array containing all x, y coordinates in the matrix where a certain colour can be found
  DOC
  previous_rows = {} #It maps the row index to the ranges (max and min values) of successive squares found in it
  #If the row does not contain any square with the given colour
  nxm.each_index do |y|
    row = Array.new([])
    colour_found = false
    nxm[y].each_index do |x|
      square = [y, x]
      if nxm[y][x] == colour
        row << square
        colour_found = true
      end
    end
    connected_sets = find_connected_sets(nxm, colour, row)
    previous_rows[y] = connected_sets if colour_found #We ignore those rows that do not contain our colour
  end
  previous_rows
end

def find_connected_sets(nxm, colour, row)
  <<-DOC
  Returns groups of adjacents squares or single adjacent squares sharing a given colour, contained in a given row 
  these will be given as ranges (stardardising the length of elements in the dicitonary to having either length one or two will make it easier
  to assemble the pieces of our connnected sets)
  DOC
  connected_sets = Array.new([])
  until row.empty?
    connected_set = Array.new([])
    pivot = row.first
    p_x, p_y = pivot[1], pivot[0]
    until nxm[p_y][p_x] != colour
      square = [p_y, p_x]
      row.delete(square)
      connected_set << square
      p_x += 1
    end
    connected_sets << [connected_set.first, connected_set.last] unless connected_set.length == 1
    connected_sets << connected_set if connected_set.length == 1 #We handle single independent squares here
  end
  connected_sets
end

def assemble_rows_helper(rows_ranges)
  <<-DOC
  Returns array containing arrays that store groups of adjacent rows 
  Upon this assumption we know that for s, r and c with s being the amount of connected sets and r the amount of connected or independent rows and c 
  the overall amount of coloured squares we can conclude that 
  s >= r and s <= c 
  In other words, the number of sets is greater or equal to the number of groups of adjacent or single rows and less or equal to the number of squares of a given colour!
  DOC
  adjacent_rows_groups = Array.new([])
  adjacent_rows = Array.new([])
  adjacent = false #Adjacent is set to true
  rows_ranges = rows_ranges.flatten!
  rows_ranges.delete(rows_ranges.first) #First element is always going to be false and so we get rid of it
  rows_ranges.uniq!
  rows_ranges = rows_ranges.each_slice(2).to_a
  if rows_ranges.length == 1
    if rows_ranges.first.length == 1 #If there is a single row with the given colour
      adjacent_rows_groups << rows_ranges.first
    else #If there are two rows then
      if rows_ranges.first[0] - rows_ranges.first[1] == 1 #If the two only rows that we have are adjacent
        adjacent_rows_groups << rows_ranges.first #We store the two connected rows
      else #We already have all connected sets stored!

      end
    end
  else #If there is more than one element
    rows_ranges.each do |rows_pairs|
      if rows_pairs.length == 1 and not adjacent #If we have a last row (number of rows is odd) and the previous pair of rows is not adjacent
        if rows_pairs.first - rows_ranges[rows_ranges.index(rows_pairs) - 1][1] == 1 #If second latter and last element are adjacent
          adjacent_rows_groups << [rows_pairs.first, rows_ranges[rows_ranges.index(rows_pairs) - 1][1]]
        else
          adjacent_rows_groups << rows_pairs #We store it as an independent set there for in an array
        end
      elsif rows_pairs.length == 1 and adjacent #If we have a last row (number of rows is odd) and the previous pair of rows is adjacent
        if rows_pairs.first - rows_ranges[rows_ranges.index(rows_pairs) - 1][1] == 1 #If second latter and last element are adjacent
          adjacent_rows << rows_ranges[rows_ranges.index(rows_pairs) - 1][1]
          adjacent_rows << rows_pairs.first
          adjacent_rows_groups << adjacent_rows
        else
          adjacent_rows_groups << rows_pairs #
        end
      elsif rows_pairs.length == 2
        if rows_pairs.last - rows_pairs.first == 1 and not adjacent #If a pair of rows is adjacent and the previous one isn't
          adjacent = true
          adjacent_rows << rows_pairs.last
          adjacent_rows << rows_pairs.first
        elsif rows_pairs.last - rows_pairs.first == 1 and adjacent
          adjacent_rows << rows_pairs.last
          adjacent_rows << rows_pairs.first
        elsif rows_pairs.last - rows_pairs.first != 1  #If a pair of rows are not adjacent and we have no previous adjacent pair
          #We first check if the first element and the last element from the previous pair are adjacent
          #If not we check if the last element and the first element of the next pair
          #Note: We have to make sure we won't repeat the case that is handled when a pair of length one is reached
          #If adjacent we set to not adjacent if not adjacent we do nothing
      end
  end
  print(rows_ranges)
  print("\n")
end

def assemble_rows(spot)
  <<-DOC
  Returns array containing groups of adjacent rows
  DOC
  adjacent_rows_group = Array.new([])
  begin_range = spot.keys.min
  end_range = spot.length
  rows_ranges = Array.new([])
  (begin_range..end_range + 1).each do |row_number|
    cur_row = row_number if spot.keys.include? row_number
    cur_row = false unless spot.keys.include? row_number
    prev_row = row_number - 1 if spot.keys.include? row_number - 1
    prev_row = false unless spot.keys.include? row_number - 1
    rows_ranges << [prev_row, cur_row]
  end
  adjacent_rows_group = assemble_rows_helper(rows_ranges)
end

def find_colour_sets_helper(spots)
  adjacent_rows_group = assemble_rows(spot) #We have the group of rows that have to be checked in the dictionary
end

def find_colour_sets(nxm)
  <<-DOC
  Returns a dictionary mapping colours to their connected sets in a nxm matrix
  DOC
  connected_spots = {} #Key: colour, values: dictionary mapping row number to the arranged adjacent or single squares in the row where colour is found
  connected_sets = {} #Key: colour values: all connected sets in the matrix of a given colour
  colours_in_matrix = what_numbers_in_matrix(nxm)
  colours_in_matrix = colours_in_matrix.sort!
  colours_in_matrix.each {|colour| connected_spots[colour] = assemble_rows_sets(nxm, colour)} #First we arranged the disassembled spots of a given colour in a dictionary
  colours_in_matrix.each {|colour| connected_sets[colour] = find_colour_sets_helper(connected_spots[colour])}
  connected_sets
end

nxm = [[1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 0]]

numbers_in_matrix = what_numbers_in_matrix(nxm)
find_colour_sets(nxm)
