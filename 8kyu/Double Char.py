# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

def double_char(s):
    last_digit = len(s) + 1
    n = 0
    final_char = ""
    for i in s[0:last_digit]:
        final_char = final_char + s[n]*2
        n = n + 1
    return final_char
    pass