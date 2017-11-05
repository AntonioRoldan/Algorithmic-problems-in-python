
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
    connected_sets = find_squares_in_row(nxm, colour, row)
    previous_rows[y] = connected_sets if colour_found #We ignore those rows that do not contain our colour
  end
  previous_rows
end

def find_squares_in_row(nxm, colour, row)
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
  Returns array containing arrays that store groups of adjacent rows or single independent rows 
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
  rows_ranges.uniq!
  rows_ranges = rows_ranges.each_slice(2).to_a
  all_adjacent = rows_ranges.flatten!.each_cons(2).map{|a, b| b - a}
  return [rows_ranges] if all_adjacent.all? {|difference| difference == 1}
  rows_ranges = rows_ranges.each_slice(2).to_a
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
          adjacent_rows_groups << [rows_ranges[rows_ranges.index(rows_pairs) - 1].last] #We add the previous element as an independent row
          adjacent_rows_groups << rows_pairs #and our current last row also stored as an independent row
        end
      elsif rows_pairs.length == 1 and adjacent #If we have a last row (number of rows is odd) and the previous pair of rows is adjacent we may
        if rows_pairs.first - rows_ranges[rows_ranges.index(rows_pairs) - 1].last == 1 #If our last element is part of our previous group
          adjacent_rows << rows_pairs.first
          adjacent_rows_groups << adjacent_rows
        else #If not we just add the current pair
          adjacent_rows_groups << adjacent_rows
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
            if rows_ranges.index(rows_pairs) != rows_ranges.length - 1
              adjacent_rows_groups << [rows_pairs.first, rows_pairs.last] unless rows_ranges[rows_ranges.index(rows_pairs) + 1].first - rows_pairs.last == 1
            else
              adjacent_rows_groups << [rows_pairs.first, rows_pairs.last]
            end
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
  adjacent_rows_groups
end

def assemble_rows(spot)
  <<-DOC
  Returns array containing groups of adjacent rows
  DOC
  adjacent_rows_group = Array.new([])
  begin_range = spot.keys.min
  end_range = spot.keys.max
  rows_ranges = Array.new([])
  (begin_range..end_range).each do |row_number|
    cur_row = row_number if spot.keys.include? row_number
    cur_row = false unless spot.keys.include? row_number
    prev_row = row_number - 1 if spot.keys.include? row_number - 1
    prev_row = false unless spot.keys.include? row_number - 1
    rows_ranges << prev_row << cur_row
  end
  rows_ranges = rows_ranges.select {|row| row.class == Fixnum}
  adjacent_rows_group = assemble_rows_helper(rows_ranges)
end

def single_square_to_single_square(cur_single_square_at, prev_single_square_at)
  <<-DOC
  It checks whether not there is a match between two single squares
  if so they will create a column
  DOC
  cur_single_square_at.last == prev_single_square_at.last
end

def build_connected_sets(cur_block, prev_block, connected_sets)
  new_set = true
  connected_sets.each do |sets|
    if sets.include? prev_block
      sets << cur_block
      new_set = false
    end
  end
  connected_sets << cur_block if new_set
end

def is_in_range_single_square(prev_row, cur_square, connected_sets)
  <<-DOC
  It tries to match a single square from the current row to a block or a single square 
  from the previous row
  DOC
  prev_row.each do |prev_square|
    if prev_square.length == 1 #If the previous square is of length one
      if single_square_to_single_square(cur_square, prev_square)#We check whether not there is a match between two single blocks through the rows
        build_connected_sets(cur_square, prev_square, connected_sets)
      else
        connected_sets << prev_square
      end
    else #If the previous square is greater than one
      #We check if our current single block is lying at any point contained within our range
      prev_beg = prev_square.first.last
      prev_end = prev_square.last.last
      prev_block = prev_square
      if square_against_range(cur_square, prev_beg, prev_end) #If the single square is lying at any point in between the ranges of our current square
        #we add another block to an existing connected set
        build_connected_sets(cur_square, prev_block, connected_sets)
      else
        #We add the first block to a newly created connected set
        connected_sets << cur_square
      end
    end
  end
end

def do_ranges_overlap(cur_block, begin_range, end_range, prev_row, connected_sets)
  <<-DOC
  It tries to match a block of squares found at current row to another block or single square contained in the previous row
  DOC
  prev_row.each do |prev_square|
    print("prev_square: ")
    print(prev_square)
    print("\n")
    if prev_square.length == 1 #We are going to check if the previous row contains a square that lies withing the range of the block we found at the current row
      if square_against_range(prev_square, begin_range, end_range)
        #We add a new block to an already created connected set
        build_connected_sets(cur_block, prev_square, connected_sets)
      else
        #We add the first block to a newly created connected set
        connected_sets << cur_block
      end
    else #We are going to check whether not there exists an overlap between two blocks lying at cur and prev row respectively
      prev_beg = prev_square.last.first
      prev_end = prev_square.last.last
      prev_block = prev_square
      if do_blocks_match(begin_range, end_range, prev_beg, prev_end)
        #We add a new block to an existing connected set
        build_connected_sets(cur_block, prev_block, connected_sets)
      else
        #We create a new connected set and add its first block to it
        connected_sets << cur_block
      end
    end
  end
end

def square_against_range(square, beg_range, end_range)
  square_at = square.first.last
  if square_at >= beg_range and square_at <= end_range
    true
  else
    false
  end
end

def do_blocks_match(begin_range, end_range, prev_beg, prev_end)
  <<-DOC
  It returns a boolean to indicate if a set of squares found in pivot and another found in our current row are connected
  DOC
  if (begin_range >= prev_beg and begin_range <= end_range) or (end_range <= prev_end and end_range >= prev_beg)
    true
  else
    false
  end
end

def compare_pivot_row(prev_row, cur_row, connected_sets)
  <<-DOC
  The fact that there are n adjacent squares in our current row with n being the amount of connected squares in the previous row 
  is a prerequisite for there to be a connected set that spreads throughout these two rows however that in itself does not guarantee 
  that there is in effect a connected set, the relation between the ranges will give us this fact, it is also possible that there are
  more than n connected squares in our row, so we can determine that c_n a variable representing the amount of connected squares in our current row 
  must meet the following condition
  c_n >= p_n with p_n representing the same value for the previous row if these numbers are not equal we know that at least one of the connected sets that we 
  started to create is over at this point and so we have the condition that if c_n < p_n the amount of connected sets that end at this point which we will 
  call e_s (ended sets) is equal to the difference between c_n and p_n if and only if c_n <= p_n 
  At the same time if c_n >= p_n we know that new connected sets are started at this point with the number of new sets n_s being equal to c_n - p_n if and only if 
  c_n < p_n now if both are equal c_n = p_n that doesn't necessarily mean that the connected sets continue. 
  Therefore the conditions stated before are only a proof that at the very least c_n - p_n new sets are starting or ending, there might be more with
  DOC
  #print(cur_row)
  #print("\n")
  #print(prev_row)
  #print("\n")
  cur_row.each do |cur_square|
    print("Cur_square: ")
    print(cur_square)
    print("\n")
    if cur_square.length == 1
      #print(cur_square)
      #print("\n")
      #print(prev_row)
      #print("\n")
      is_in_range_single_square(prev_row, cur_square, connected_sets)
    else
      begin_range = cur_square.first.last
      end_range = cur_square.last.last
      cur_block = cur_square
      #print("Ranges: ")
      #print(begin_range, " ", end_range)
      #print("\n")
      #print("Cur block: ")
      #print(cur_block)
      #print("\n")
      do_ranges_overlap(cur_block, begin_range, end_range, prev_row, connected_sets)
    end
  end
end

def find_connected_sets(spots, adjacent_rows)
  <<-DOC
  It will return an array containing all connected sets by row and column of a given colour
  that can be created a cluster of adjacent rows
  DOC
  connected_sets = Array.new([])
  #print(adjacent_rows)
  #print("\n")
  if adjacent_rows.length == 1 #If the length is one that means we have a group but not necessarily a single independent row !
    spots[adjacent_rows.first].each {|adjacent_squares| connected_sets << adjacent_squares}
    cur_row = adjacent_rows.first
  else
    adjacent_rows.each_index do |i|
      if i == adjacent_rows.length - 1
        break
      else
        prev_row = spots[adjacent_rows[i]]
        cur_row = spots[adjacent_rows[i + 1]]
        prev_row.sort!
        cur_row.sort!
      end
      compare_pivot_row(prev_row, cur_row, connected_sets) unless i == adjacent_rows.length - 1 and adjacent_rows.length == 1
      #print(prev_row, "", cur_row)
      #print("\n")
    end
  end
end

def find_colour_sets_helper(spots)
  connected_sets = Array.new([])
  adjacent_rows_groups = assemble_rows(spots) #We have the group of rows that have to be checked in the dictionary
  adjacent_rows_groups.each do |adjacent_rows|
    find_connected_sets(spots, adjacent_rows)
  end
  connected_sets
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

nxm = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

find_colour_sets(nxm)
