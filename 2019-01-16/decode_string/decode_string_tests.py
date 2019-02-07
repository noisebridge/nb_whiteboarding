"""
01/16/2019: Problem 1: Decode String

Test cases for some implementation of the solution.

Test sets include one with well-formed inputs and one with malformed inputs.

Author: Eugene Ma
"""

def test_decode_string(decode_string, test_cases):
    num_passed = 0
    for i, test_case in enumerate(test_cases):
        input, gold_output = test_case

        output = decode_string(input)
        if output == gold_output:
            num_passed += 1
        else:
            print("Failed test case {}: {}", i + 1, input)

    print("{} of {} tests passed".format(num_passed, len(test_cases)))

def test_decode_string_with_well_formed_input(decode_string):
    test_cases = [
        ("x2[y]3[z]", "xyyzzz"),
        ("xy12[2[a]3[b]z]c", "xyaabbbzaabbbzaabbbzaabbbzaabbbzaabbbzaabbbzaabbbzaabbbzaabbbzaabbbzaabbbzc")
    ]

    print("Testing with well-formed input:")

    test_decode_string(decode_string, test_cases)

def test_decode_string_with_malformed_input(decode_string):
    test_cases = [
        ("a[b]", None),
        ("a4[b", None)
    ]

    print("Testing with malformed input:")

    test_decode_string(decode_string, test_cases)
