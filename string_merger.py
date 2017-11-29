rom itertools import zip_longest
from math import *

def string_merger(str_1, str_2):
    output_string = ""
    index = 0
    for char1, char2 in zip_longest(list(str_1), list(str_2)):
        index += 1
        output_string += (char1 + char2 if index <= len(str_1) - 1 else char1) if len(str_1) > len(str_2) else (char1 + char2 if index <= len(str_2) - 1 else char2)
    return output_string

print(string_merger("day", "time"))
