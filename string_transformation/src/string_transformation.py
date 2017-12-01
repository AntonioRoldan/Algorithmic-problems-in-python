import collections

def a_to_b(a_str, b_str):
    a_lst = list(a_str) #First we convert both to a list
    b_lst = list(b_str)
    if len(a_lst) == len(b_lst):
        cost = match_comparison(a_lst, b_lst)
        return cost
    elif len(a_lst) > len(b_lst):
        pass
    else:#If len(a_lst) < len(b_lst)
        pass

def a_greater_than_b():
    pass
def check_edges(from_right, a_lst, match_target, boolean_matrix):
    swap_index = 0
    if(from_right):
        for i, char in enumerate(a_lst):
            if not i: #We ignore the first element when iterating from the left edge
                continue
            elif char == match_target and not boolean_matrix[i]:
                swap_index = i
            continue
    else: #We have our element on the left most side on the list
        for i, char in enumerate(a_lst):
            if i == len(a_lst) - 1: #We ignore the right most letter when iterating from the right edge
                continue
            elif char == match_target:
                swap_index = i
            continue
    return swap_index

def fully_non_matching_strings(a_lst, b_lst): #If strings do not match at all
    pass #We are gonna perform full deletion and insertion, just returning the cost
    cost = 0
    for i in range(len(a_lst)):
        cost += 7
    return cost

def swap_letters(a_lst, starting_swap_index, ending_swap_index):
    """It swaps two elements from within the same list"""
    a_lst[starting_swap_index], a_lst[ending_swap_index] = a_lst[ending_swap_index], a_lst[starting_swap_index]
    return a_lst #and return our resulting list

def delete_insert(a_lst, to_be_deleted_index, match_target):
    """It changes the value to a location in the list"""
    a_lst[to_be_deleted_index] = match_target
    return a_lst

def match_comparison(a_lst, b_lst):
    """It tries converting a into b via replacement and insertion, deletion operations"""
    """Note: We are assuming they both have the same length"""
    """The main premise here is that replacement is always cheaper than our delete-insert alternative when both lengths are same"""
    boolean_matrix = matches_at(a_lst, b_lst) #True if characters match, False if they don't
    cost = 0
    while(not all(boolean_matrix)): #Until a is b
        if not any(boolean_matrix): #If both strings have no characters in common
            return fully_non_matching_strings(a_lst, b_lst) #If they do not match at all
        for i, char in enumerate(a_lst):
            if not boolean_matrix[i]: #If the words' characters do not match at this specific index
                match_target = b_lst[i] #We define the target to be our replacement
                to_be_swapped_or_deleted = i #The operation might be a deletion or a replacement
                if i == 0: #If our non-matching character happens to be at the beginning
                    swap_index = check_edges(cost, from_right=True , a_lst=a_lst, match_target=match_target) #We iterate through the whole list
                    if not swap_index: #We perform a deletion insertion operation
                        delete_insert_index = swap_index #
                        delete_insert(a_lst, delete_insert_index, match_target)
                        cost += 7
                    else:
                        cost += 5
                if i == len(boolean_matrix) - 1: #If it is at the end
                    swap_index = check_edges(from_right=False, a_lst =a_lst, match_target=match_target, boolean_matrix=boolean_matrix) #We iterate through the whole list
                    if not swap_index:
                        delete_insert_index = swap_index  #
                        a_lst = delete_insert(a_lst, delete_insert_index, match_target)
                        cost += 7
                    else:
                        cost += 5
                else: #else we will have to check on both sides of the list looking for our missing character
                    left_side, right_side = chunk_list(a_lst, i)
                    swap_index = check_sides(left_side, right_side, match_target, boolean_matrix)
                if swap_index:
                    cost += 5
                    to_be_swapped_index = to_be_swapped_or_deleted
                    swap_index = swap_index
                    a_lst = swap_letters(a_lst, to_be_swapped_or_deleted, swap_index)
                else:
                    delete_insert_index = to_be_swapped_or_deleted
                    a_lst = delete_insert(a_lst, delete_insert_index, match_target)
                    cost += 7
                    #We delete and insert
        boolean_matrix = matches_at(a_lst, b_lst)
    return cost


def check_sides(left_side, right_side, match_target, match_at):
    """It will find a character that matches on both left and right and return it for the swap operation"""
    left_side.reverse()
    swap_index = 0
    found = False
    for letter, i in enumerate(left_side):
        if letter == match_target and not match_at[i]: #We also check if the character is already matching
            swap_index = i #We do not return the value yet, and use a boolean
            found = True
        continue
    for letter, i in enumerate(right_side):
        if letter == match_target and not match_at[i]:
            swap_index = i
            found = True
        continue
    if found:
        return swap_index
    else:
        return False #so that we can know whether not the program will have to replace or delete

def chunk_list(a_lst, i):
    """It chunks a list into two parts given a pivot index"""
    a_chunk = [a_lst[index] for index in range(i)]
    b_starting_point = (len(a_lst) - 1) - i
    b_ending_point = len(a_lst) - 1
    b_chunk = [a_lst[index] for index in range(b_starting_point, b_ending_point + 1)]
    return a_chunk, b_chunk

def matches_at(a_lst, b_lst):
    matches_at = [False for i in range(len(a_lst))]
    for i, (a, b) in enumerate(zip(a_lst, b_lst)):
        if a == b:
            matches_at[i] = True
        continue
    return matches_at

if __name__ == '__main__':
    print(a_to_b("abcabc", "abacab"))