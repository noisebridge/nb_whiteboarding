"""
01/16/2019: Problem 1: Decode String

Implementation using recursive pattern matching.
The input string does not have to be well-formed
(i.e., error checking is done).

How it works is that there are a bunch of functions
(with names of the form "try_eat_something")
that try to eat a substring that matches some pattern.
They take the string ("s") and an index ("start") in the string
to start the attempt to "eat", so the form of the function is like this:
  try_eat_something(s, start)

If the eating was successful (i.e., the substring eaten matches the pattern),
it returns a pair of values.
The first of the pair is the result of the eating,
and the second of the pair is the index in the string
that the function ate up to.
(This index is the "end" of a half-open range,
so the range [start, end) is the span of the string that the function ate.)
This index could then be used as the start index
for further attempts to eat subsequent parts of the string.

If the eating was not successful, the same pair of values is returned,
but this time, it reflects that nothing was eaten.
That is, the first of the pair is None because there was no result,
and the second of the pair is just the start
because the index was not advanced.

Notice that these functions try to eat
the whole thing that it is trying to match, or none of it.
That is, there is nothing half-eaten.
Thus, error-checking is done.

Author: Eugene Ma
"""

import decode_string_tests

def decode_string_using_recursive_pattern_matching(s):
    def try_eat_char(s, start, char):
        """
        Tries to eat the single character given.

        Returns (target char to match, end index)
        """

        if start < len(s) and s[start] == char:
            return (char, start + 1)
        else:
            return (None, start)

    def try_eat_letters(s, start):
        """
        Tries to eat a series of letters.

        Returns (letters, end index)
        """

        i = start
        while i < len(s) and s[i].isalpha():
            i += 1

        if start < i:
            return (s[start:i], i)
        else:
            return (None, start)

    def try_eat_number(s, start):
        """
        Tries to eat a series of digits that represent an integer.

        Returns (actual number, end index)
        """

        i = start
        while i < len(s) and s[i].isdigit():
            i += 1

        if start < i:
            return (int(s[start:i]), i)
        else:
            return (None, i)

    def try_eat_repetition(s, start):
        """
        Tries to eat a substring with this pattern:
        numberToRepeat[contentsToRepeat]

        Returns (repeated contents, end index).
        """

        number, number_end = try_eat_number(s, start)
        if start == number_end:
            return (None, start)

        open_bracket, open_bracket_end = try_eat_char(s, number_end, '[')
        if number_end == open_bracket_end:
            return (None, start)

        contents, contents_end = try_eat_contents(s, open_bracket_end)
        if contents_end == open_bracket_end:
            return (None, start)

        close_bracket, close_bracket_end = try_eat_char(s, contents_end, ']')
        if contents_end == close_bracket_end:
            return (None, start)

        return (contents * number, close_bracket_end)

    def try_eat_contents(s, start):
        """
        Tries to eat a sequence of items
        that can respectively be "letters" or a "repetition".

        For example:
        letters letters repetition letters repetition

        Returns (full string, end index).
        """

        chunks = []

        i = start
        while i < len(s):
            ateSomething = False

            letters, end = try_eat_letters(s, i)
            if i < end:
                chunks.append(letters)
                i = end

                ateSomething = True

            repetition, end = try_eat_repetition(s, i)
            if i < end:
                chunks.append(repetition)
                i = end

                ateSomething = True

            if not ateSomething:
                break

        if start < i:
            return (''.join(chunks), i)
        else:
            return (None, start)

    def try_eat_all(s):
        expanded, end = try_eat_contents(s, 0)
        if end == len(s):
            return expanded
        else:
            return None

    return try_eat_all(s)

if __name__ == '__main__':
    decode_string_tests.test_decode_string_with_well_formed_input(decode_string_using_recursive_pattern_matching)
    decode_string_tests.test_decode_string_with_malformed_input(decode_string_using_recursive_pattern_matching)
