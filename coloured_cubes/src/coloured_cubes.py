import operator
from collections import Counter
import unittest

#Cubes is a dictionary mapping

def get_colours(cubes):
    colour = ""
    for cube in cubes:
        colour = cubes[cube][0]
        yield colour

def get_colours_list(cubes):
    colours = list(get_colours(cubes))  # We store all colours in a list
    colours = Counter(
        colours)  # We create a temporary dictionary containing colours along with their amount of occurrences
    return colours

def update_colours(cubes_by_colour):
    return set(cubes_by_colour.keys())

def arrange_cubes_by_colour(cubes):
    colours = get_colours_list(cubes) #We need this method before we have arranged the cubes by colour after which we will simply get the colours from cubes_by_colour.keys()
    sorted_colours = {} #Stores sorted repetitions of colours by length, key: colour, values: increasing lengths
    for colour in colours:
        sorted_colours[colour] = sorted([(cube, colour_length[1]) for cube, colour_length in cubes.items() if colour_length[0] == colour], key=operator.itemgetter(1))  # We fill a map containing a sorted  list of all cube lengths of a given colour, using the colour as its key
    return sorted_colours, colours

def alternative_cubes_maximum_lengths(cur_colour,  cubes_by_colour, colours):
    """It will take into a account the current colour, to make sure that only the other cube colours are gonna be taken into account in the next iteration"""
    for cube_by_colour in colours:
        if(cube_by_colour == cur_colour): #We ignore the current colour since no adjacent cubes of the same colour can be added
            pass
        else:
            yield max(cubes_by_colour[cube_by_colour]) #We get the cube of maximum length out of those of a given colour
        continue

def cubes_maximum_lengths(colours, cubes_by_colour):
    """It gets a list of the cubes maximum lengths"""
    for colour in colours:
        yield max(cubes_by_colour[colour])

def delete_cube(cubes_by_colour, deleted_cube): #It deletes a given cube from our group of cubes as it has already been added to the pile
    for cubes_by_colour_list in cubes_by_colour.values():
        if(deleted_cube in cubes_by_colour_list):
            cubes_by_colour_list.remove(deleted_cube)
        continue

def delete_colour_if_its_over(cubes_by_colour, cur_colour):
    if(not cubes_by_colour[cur_colour]):
        del cubes_by_colour[cur_colour]
    pass

def display_solution(cubes, pile_of_blocks):
    pile_height = sum([length[1] for length in pile_of_blocks])
    print(str(pile_height) + ' ' + 'maximum height corresponding to ')
    for block in pile_of_blocks:
        cube_name = block[0]
        cube_height = block[1]
        print(cube_name + ' of colour ' + cubes[cube_name][0] + ' and length ' + str(cube_height))

def recursive_build_pile(first_block, cubes, cubes_by_colour, colours, pile_of_blocks):
    colours = set(colours) if(first_block) else update_colours(cubes_by_colour)
    maximum_length_cubes = list(cubes_maximum_lengths(colours, cubes_by_colour))
    cur_colour = ""
    if(len(colours) == 1 and first_block):
        return sorted(cubes_by_colour[colours.pop()], key=operator.itemgetter(1))[-1]
    elif(len(colours) == 1): #Recursion continues until we have only one colour left
        cur_colour = colours.pop()
        max_block = max(cubes_by_colour[cur_colour])
        pile_of_blocks.append(max_block)
        return tuple(reversed(pile_of_blocks))
    if(first_block):
        max_block = max(maximum_length_cubes, key=operator.itemgetter(1))
        cur_colour = cubes[max_block[0]][0]
        first_block = False
    else:
        max_block = max(alternative_cubes_maximum_lengths(cur_colour, cubes_by_colour, colours), key=operator.itemgetter(1))
        cur_colour = cubes[max_block[0]][0]
    delete_cube(cubes_by_colour, max_block)
    delete_colour_if_its_over(cubes_by_colour, cur_colour)
    pile_of_blocks.append(max_block)
    pile_of_blocks = recursive_build_pile(first_block, cubes, cubes_by_colour, colours, pile_of_blocks)
    return pile_of_blocks

def iterative_build_pile(cubes, cubes_by_colour, colours):
    pile_of_blocks = []
    cubes_by_colour, colours = arrange_cubes_by_colour(
        cubes)  # We get a dictionary as follows keys: colours, values: cubes' names, cubes' lengths and a set containing our available colours
    first_block = True
    while (len(colours) > 1):  # As we place one block upon the other we will eventually have a single colour left
        colours = set(colours) if (first_block) else update_colours(
            cubes_by_colour)  # We update the colours to make sure deleted colours are not going to be taken into account
        maximum_length_cubes = list(cubes_maximum_lengths(colours, cubes_by_colour))
        if (first_block):
            max_block = max(maximum_length_cubes, key=operator.itemgetter(1))
            cur_colour = cubes[max_block[0]][
                0]  # We make sure the set is not going to split the string into characters by wrapping it with another iterable object
            first_block = False
        else:
            max_block = max(alternative_cubes_maximum_lengths(cur_colour, cubes_by_colour, colours), key=operator.itemgetter(1))
            cur_colour = cubes[max_block[0]][0]
        delete_cube(cubes_by_colour, max_block)
        delete_colour_if_its_over(cubes_by_colour, cur_colour)  # If we don't have any more cubes of that colour, we delete it from the dictionary
        pile_of_blocks.append(max_block)
    return tuple(reversed(pile_of_blocks))
    # Since we have already chose the maximum element from the previously available colours and the their next cubes will always have a larger length
    # by the time we get to the only colour we have left, its value will always be lower than its predecessors and so we can discard it

def colour_cubes(n, cubes):
    pile_of_blocks = []
    cubes_by_colour, colours = arrange_cubes_by_colour(cubes) #We get a dictionary with colours as keys and cubes' names and lengths as values
    first_block = True
    pile_of_blocks = recursive_build_pile(first_block, cubes, cubes_by_colour, colours, pile_of_blocks)
    #pile_of_blocks = iterative_build_pile(cubes, cubes_by_colour, colours)
    display_solution(cubes, pile_of_blocks)
    #print(max_block)
    #print(maximum_length_cubes)
    #print(cubes_by_colour)

colour_cubes(3, {'cube 1' : ('red', 5) , 'cube 2' : ('red', 6), 'cube 3' : ('blue', 5), 'cube 4' : ('blue', 7), 'cube 5' : ('yellow', 3), 'cube 6' : ('green', 6)})
