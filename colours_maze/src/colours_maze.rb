
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
  We have s, r and c with s being the amount of connected sets, r the amount of adjacent or single rows and c the overall amount 
  of coloured squares contained in r and s 
  Having these variables the following condition is then satisfied 
  r <= s <= c 
  In other words, the number of sets is greater or equal than the number of groups of adjacent or single rows 
  and less or equal than the number of squares of a given colour!
  DOC
  adjacent_rows_groups = Array.new([])
  adjacent_rows = Array.new([])
  adjacent = false #Adjacent defines whether two elements contained, it merely determines the pre format in which we are going to store our data
  rows_ranges = rows_ranges.flatten!
  rows_ranges.delete(rows_ranges.first) #First element is always going to be false and so we get rid of it
  rows_ranges.uniq!
  rows_ranges = rows_ranges.each_slice(2).to_a
  all_adjacent = rows_ranges.flatten!.each_cons(2).map{|a, b| b - a}
  print([rows_ranges]) if all_adjacent.all? {|difference| difference == 1}
  print("\n")
  return [rows_ranges] if all_adjacent.all? {|difference| difference == 1}
  rows_ranges = rows_ranges.each_slice(2).to_a
  print(rows_ranges)
  print("\n")
  if rows_ranges.length == 1
    if rows_ranges.first.length == 1 #If there is a single row with the given colour
      adjacent_rows_groups << rows_ranges.first
    else #If there are two rows then
      if rows_ranges.first[0] - rows_ranges.first[1] == 1 #If the two only rows that we have are adjacent
        adjacent_rows_groups << rows_ranges.first #We store the two connected rows
      else #If there two only rows we have are not adjacent
        #We already have all connected sets stored!
      end
    end
  else #If there is more than one element
    rows_ranges.each do |rows_pairs|
      if rows_pairs.length == 1 and not adjacent #If we have a last row (number of rows is odd) and the previous pair of rows is not adjacent
        if rows_pairs.first - rows_ranges[rows_ranges.index(rows_pairs) - 1].last == 1 #If second latter and last element are adjacent
          adjacent_rows_groups << [rows_pairs.first, rows_ranges[rows_ranges.index(rows_pairs) - 1].last]
        else
          adjacent_rows_groups << [rows_ranges[rows_ranges.index(rows_pairs) - 1].last]
          adjacent_rows_groups << rows_pairs #We store it as an independent set there for in an array
        end
      elsif rows_pairs.length == 1 and adjacent #If we have a last row (number of rows is odd) and the previous pair of rows is adjacent we may
        if rows_pairs.first - rows_ranges[rows_ranges.index(rows_pairs) - 1].last == 1 #If our last element is part of our previous group
          adjacent_rows << rows_pairs.first
          adjacent_rows_groups << adjacent_rows
        else #If not we just add the current pair
          adjacent_rows_groups << rows_pairs
        end
      else #We have elements of length 2 only before we get to the end of the list (assuming our list has an odd number of elements)
        if rows_pairs.last - rows_pairs.first == 1 and not adjacent #If a pair of rows is adjacent and the previous one isn't
          if rows_ranges.index(rows_pairs) == 0 #We must check if this is the first element in the array or not, if so we don't need to check adjacency between last row of previous pair and first row of current pair
            adjacent_rows << rows_pairs.first
            adjacent_rows << rows_pairs.last
          elsif rows_pairs.first - rows_ranges[rows_ranges.index(rows_pairs) - 1].last == 1 #If the connection goes on we just add these next two elements
            adjacent_rows << rows_ranges[rows_ranges.index(rows_pairs) - 1].last
            adjacent_rows << rows_pairs.first
            adjacent_rows << rows_pairs.last
            adjacent_rows_groups << adjacent_rows
          elsif rows_pairs.first - rows_ranges[rows_ranges.index(rows_pairs) - 1][1] != 1
            adjacent_rows_groups << [rows_ranges[rows_ranges.index(rows_pairs) - 1][1]] #We only store adjacent rows at the point where we know for sure the connection has been put an end
            adjacent_rows.clear
            adjacent_rows << rows_pairs.first
            adjacent_rows << rows_pairs.last
          end
          adjacent = true
        elsif rows_pairs.last - rows_pairs.first == 1 and adjacent #adjacent can only be set to true after at least one pair has been checked therefore we don't need to check for the pair's position
          if rows_pairs.first - rows_ranges[rows_ranges.index(rows_pairs) - 1].last == 1 #If the connection goes on we just add these next two elements
            adjacent_rows << rows_pairs.first
            adjacent_rows << rows_pairs.last
          else
            adjacent_rows_groups << adjacent_rows
            adjacent_rows_groups << [rows_pairs.first, rows_pairs.last] unless rows_ranges[rows_ranges.index(rows_pairs) + 1].first - rows_pairs.last == 1
            adjacent_rows = Array.new([])
          end
          adjacent_rows << rows_pairs.last
          adjacent_rows << rows_pairs.first
        elsif rows_pairs.last - rows_pairs.first != 1 and not adjacent #If a pair of rows are not adjacent and we have no previous adjacent pair
          if rows_ranges.index(rows_pairs) == 0 #We must check if this is the first element in the array or not, if so we don't need to check adjacency between last row of previous pair and first row of current pair
            adjacent_rows_groups << [rows_pairs.first]
          elsif rows_pairs.first - rows_ranges[rows_ranges.index(rows_pairs) - 1].last == 1 #At this point we have an intermediate connection between two rows
            adjacent_rows_groups << [rows_ranges[rows_ranges.index(rows_pairs) - 1].last, rows_pairs.first] #and so we store it
            adjacent_rows_groups << [rows_pairs.last] if rows_ranges.index(rows_pairs) == rows_ranges.length - 1
          else
            adjacent_rows_groups << [rows_ranges[rows_ranges.index(rows_pairs) - 1].last]
            adjacent_rows_groups << [rows_pairs.first]
            adjacent_rows_groups << [rows_pairs.last] if rows_ranges.index(rows_pairs) == rows_ranges.length - 1
          end
        else #if rows_pairs.last - rows_pairs.first != 1 and adjacent
          if rows_pairs.first - rows_ranges[rows_ranges.index(rows_pairs) - 1].last == 1
            adjacent_rows_groups << [rows_pairs.first]
            adjacent_rows_groups << [rows_pairs.last] if rows_ranges.index(rows_pairs) == rows_ranges.length - 1
            #print(adjacent_rows)
            #print("\n")
          else
            print("b")
            adjacent_rows_groups << adjacent_rows
          end
          adjacent = false
          adjacent_rows = Array.new([])
        end
      end
    end
  end
  adjacent_rows_groups.each {|adjacent_rows| adjacent_rows.sort!}
  adjacent_rows_groups.uniq!
  adjacent_rows_groups.each {|adjacent_rows| adjacent_rows.uniq!}
  print(adjacent_rows_groups)
  print("\n")
end

def assemble_rows(spot)
  <<-DOC
  Returns array containing groups of adjacent rows
  DOC
  adjacent_rows_group = Array.new([])
  begin_range = spot.keys.min
  end_range = spot.length + 1
  rows_ranges = Array.new([])
  (begin_range..end_range + 1).each do |row_number|
    cur_row = row_number if spot.keys.include? row_number
    cur_row = false unless spot.keys.include? row_number
    prev_row = row_number - 1 if spot.keys.include? row_number - 1
    prev_row = false unless spot.keys.include? row_number - 1
    rows_ranges << [prev_row, cur_row]
    #print([prev_row, cur_row])
    #print("\n")
  end
  adjacent_rows_group = assemble_rows_helper(rows_ranges)
end

def find_colour_sets_helper(spots)
  adjacent_rows_group = assemble_rows(spots) #We have the group of rows that have to be checked in the dictionary
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

nxm = [[1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0]]

numbers_in_matrix = what_numbers_in_matrix(nxm)
find_colour_sets(nxm)
