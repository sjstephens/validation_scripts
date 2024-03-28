#!/usr/bin/env python3

# Write a script to validate matching closing bracers; square, curly, round

def validate_bracers(test_str):
    if (len(test_str) % 2 != 0) or (len(test_str) == 0):
        # Length is not even, bad input string
        return "bad input length", len(test_str)
    # initialize braces  dict
    # could also build dict with all braces (closes set to blah)
    # then do a dict.get on closes. code below will be infficient for large dicts.
    par_dict = {'(':')','{':'}','[':']'}
    stack = []
    for char in test_str:
        # push opening braces on to stack
        if char in par_dict.keys():
            stack.append(char)
            continue
        # check for closing braces
        if char in par_dict.values():
            # closing bracket without matching opening bracket
            if stack == []:
                return "missing open bracer", char
            # if closing bracket -> pop last open brace
            open_brac = stack.pop()
            # check if close matches the value of the opened key
            if char != par_dict[open_brac]:
                return "mismatch bracer", char
        else:
            # Not a bracer
            continue
    return "matching", ""

if __name__ == "__main__":
    samples = ["{}]","[{}]","[]","[]{}","[{]}","{{]}","{ab}",""]
    for test_str in samples:
        x, y = validate_bracers(test_str)
        if x == "matching":
            print(("{} has matching braces".format(test_str)))
        else:
            print(("{} has {}, for {}".format(test_str,x,y)))
