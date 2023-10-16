# Implement the function unique_in_order which takes as argument a string and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

def unique_in_order(sequence):
    filtered = []
    string_position = 0
    if len(sequence) == 0 or len(sequence)==1:
        return sequence
    while string_position+1 != len(sequence):
        if sequence[string_position] == sequence[string_position+1]:
            string_position += 1
        else:
            filtered.append(string_position)
    filtered.append(sequence[0])
    return filtered
