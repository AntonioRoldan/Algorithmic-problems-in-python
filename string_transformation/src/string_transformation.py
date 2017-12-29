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

def fully_non_matching_strings(a_lst, b_lst): #If strings do not match at all
    pass #We are gonna perform full deletion and insertion, just returning the cost
    cost = 0
    for i in range(len(a_lst)):
        cost += 7
    return cost

def delete_insert(a_lst, to_be_deleted_index, match_target):
    """It changes the value to a location in the list"""
    a_lst[to_be_deleted_index] = match_target
    return a_lst

def match_comparison(a_lst, b_lst):
    """It tries converting a into b via replacement and insertion, deletion operations"""
    """Note: We are assuming they both have the same length"""
    """The main premise here is that replacement is always cheaper than our delete-insert alternative when both lengths are same.
    The reasoning behind it is the following, having a and b as sets of characters with the difference of their sets resulting in an empty set.
    Replacing a character (swapping a character by another in the same string) will always be cheaper than deleting (3) and inserting (4) which would give us a cost of seven, 
    the replacement operation here is five, apart from that, once we have made the necessary replacements if that's all we did and we are left with a single mismatch between both strings, only a delete and insert operation can be performed 
    otherwise we would be altering the result we had"""
    """In the case that the difference operation between both sets is not empty (i.e there is a character in a that doesn't exist in b or viceversa"""
    """Only deletion and insertion in accordance to b can be performed"""
    boolean_matrix = matches_at(a_lst, b_lst) #True if characters match, False if they don't
    cost = 0
    print(boolean_matrix)
    while(not all(boolean_matrix)): #Until a is b
        if not any(boolean_matrix): #If both strings have no characters in common
            return fully_non_matching_strings(a_lst, b_lst) #If they do not match at all
        if (set(a_lst) - set(b_lst)):#If there are characters in a that don't exist in b
            for i, char in enumerate(a_lst):
                if(char not in set(b_lst)):
                    match_target = b_lst[i] #Only deletion and insertion can be performed here
                    a_lst = delete_insert(a_lst, i, match_target)
                    cost += 7
        for i, char in enumerate(a_lst):
            if not boolean_matrix[i]: #If the words' characters do not match at this specific index
                match_target = b_lst[i] #We define the target to be our replacement
                if match_target not in a_lst: #If the letter from b is not contained in a no replacement can be made
                    a_lst = delete_insert(a_lst, i, match_target)
                    break
                to_be_swapped_or_deleted = a_lst[i] #The operation might be a deletion or a replacement
                print(match_target, to_be_swapped_or_deleted)
                print("index: ", i)
                temporary_a = a_lst
                a_lst = find_swap_target(a_lst, match_target, boolean_matrix, i)
                if a_lst is None:
                    cost += 7
                    a_lst = delete_insert(temporary_a, i, match_target)
                    print("delete and insert")
                    break
                else:
                    cost += 5
                    print("replace")
                    break
                    #We delete and insert
        boolean_matrix = matches_at(a_lst, b_lst)
    print(a_lst)
    return cost

def find_swap_target(a_lst, target, match_at, pivot_index):
    swap_found = False
    for i, char in enumerate(a_lst):
        if char == target and not match_at[i]:
            print("swapped by: " + char + "index: " + str(i))
            if match_at.count(False) == 1:
                return None
            a_lst[pivot_index], a_lst[i] = a_lst[i], a_lst[pivot_index]
            return a_lst

def matches_at(a_lst, b_lst):
    matches_at = [False for i in range(len(a_lst))]
    for i, (a, b) in enumerate(zip(a_lst, b_lst)):
        if a == b:
            matches_at[i] = True
        continue
    return matches_at

if __name__ == '__main__':
    print(a_to_b("abcanc", "ababab"))
