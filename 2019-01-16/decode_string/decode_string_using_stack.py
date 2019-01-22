"""
01/16/2019: Problem 1: Decode String

Implementation using a stack.
Assumes that the input string is well-formed
(i.e., there is no error checking!).

Author: Eugene Ma
"""

from collections import deque
import decode_string_tests

def decode_string_using_stack(s):
    stack = []

    for i in range(len(s)):
        c = s[i]
        if c.isalpha():
            if stack:
                # Try appending new letter
                # to previous string of letters built (if it exists)
                top = stack.pop()
                if isinstance(top, str) and top.isalpha():
                    top += c
                    stack.append(top)
                else:
                    stack.append(top)
                    stack.append(c)
            else:
                stack.append(c)
        elif c.isdigit():
            if stack:
                # Try appending new digit
                # to previous number built (if it exists)
                top = stack.pop()
                if isinstance(top, int):
                    top = top * 10 + int(c)
                    stack.append(top)
                else:
                    stack.append(top)
                    stack.append(int(c))
            else:
                stack.append(int(c))
        elif c == '[':
            stack.append(c)
        elif c == ']':
            # Found a closing bracket.
            # Keep poping off stack
            # to determine the contents inside the brackets.
            to_join = deque()
            while stack:
                top = stack.pop()
                if top == '[':
                    break
                else:
                    to_join.appendleft(top)
            contents = ''.join(to_join)

            num_repeat = stack.pop()

            stack.append(contents * num_repeat)
        else:
            raise ValueError('Unexpected character: ' + c)

    return ''.join(stack)

if __name__ == '__main__':
    decode_string_tests.test_decode_string_with_well_formed_input(decode_string_using_stack)
    decode_string_tests.test_decode_string_with_malformed_input(decode_string_using_stack)
