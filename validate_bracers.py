#!/usr/bin/env python3

# Write a script to validate matching closing bracers; square, curly, round

def validate_bracers(test_str):
    if len(test_str) % 2 != 0:
        # Length is not veen so something is missing
        return "band input length", len(test_str)
    # initialize parentheses dict
    par_dict = {'(':')','{':'}','[':']'}
    stack = []
    for char in test_str:
        # push opening bracket to stack
        if char in par_dict.keys():
            stack.append(char)
        else:
            # closing bracket without matching opening bracket
            if stack == []:
                return "missing open bracer", char
            # if closing bracket -> pop stack top
            open_brac = stack.pop()
            # not matching bracket -> invalid!
            if char != par_dict[open_brac]:
                return "mismatch bracer", char
    return "matching", ""

if __name__ == "__main__":
    samples = ["{}]","[{}]","[]","[]{}","[{]}","{{]}"]
    for test_str in samples:
        x, y = validate_bracers(test_str)
        if x == "matching":
            print(("{} has matching braces".format(test_str)))
        else:
            print(("{} has {}, at {}".format(test_str,x,y)))
