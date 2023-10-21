# Implement the function unique_in_order which takes as argument a string and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

def unique_in_order(sequence):
    unique_sequence = []
    if len(sequence) != 0:
        string_position = 0
        unique_sequence = [sequence[0]]
        for char in sequence[1:]:
            if sequence[string_position] != char:
                unique_sequence.append(char)
            string_position += 1
    return unique_sequence
