# Noisebridge Whiteboarding Workshop

This is an archive of whiteboarding problems discussed at weekly whiteboarding meetups at [Noisebridge](https://www.meetup.com/noisebridge/). Make a [PR](https://help.github.com/articles/creating-a-pull-request/) if you've written a solution. To pose an algorithm problem to the group, open an issue in this repository.

## Starting out

If you're new to whiteboarding, here's a miniature prerequisite roadmap to help prepare you for the experience:

1. Learn [programming fundamentals](https://greenteapress.com/wp/think-python-2e/) (variables, functions, loops, arrays, etc). [Python](https://www.python.org/about/gettingstarted/) is a popular language choice; however, most algorithm books use Java, C or C++, so exposure to one of those is recommended.
2. Explore the [basics of data structures and algorithms](http://interactivepython.org/runestone/static/pythonds/index.html) (big-O, stacks, queues, graphs, hashing, sorting, searching, etc).
3. Grab a copy of [Cracking the Coding Interview](http://ahmed-badawy.com/blog/wp-content/uploads/2018/10/Cracking-the-Coding-Interview-6th-Edition-189-Programming-Questions-and-Solutions.pdf), read a few chapters and try some problems.
4. Sign up for [LeetCode](https://leetcode.com/ggorlen/) and [other coding challenge sites](https://medium.com/coderbyte/the-10-best-coding-challenge-websites-for-2018-12b57645b654) and keep solving!

## Pull request guidelines

- Please adhere to your language's typical style guidelines for indentation, whitespace and casing.
- Focus on realistic solutions to whiteboarding problems (cap lines of code at a reasonable amount but feel free to subtract lines used to write larger helper functions that an interviewer would typically allow to be abbreviated, like a [disjoint-set](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)).
- Add a simple test suite or driver code.

## Past problems

### 11/07/2018

1. [Longest path in DAG](/2018-11-07/longest_path_in_dag.py)
2. [BST to linked list](/2018-11-07/bst_to_linked_list.py)
3. [K smallest numbers in array](/2018-11-07/smallest_k.py)

### 11/14/2018

1. [Rotate array](https://leetcode.com/problems/rotate-array/)
2. [Detect cycle in undirected graph](https://www.geeksforgeeks.org/union-find/)
3. [Roads and Libraries](https://www.hackerrank.com/challenges/torque-and-development/problem)
4. [New Year Chaos](https://www.hackerrank.com/challenges/new-year-chaos/problem)

### 11/21/2018

1. [Bouquet of flowers](https://www.geeksforgeeks.org/flipkart-internship-interview-on-campus/)
2. [First missing positive](https://leetcode.com/problems/first-missing-positive/description/)
3. [Median of two sorted arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)

### 11/28/2018

1. [Find the duplicate number](https://leetcode.com/problems/find-the-duplicate-number/)
2. [N-th Fibonacci Number](https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/)
3. [Shortest Supersequence](/2018-11-28/shortest_supersequence.rb)
4. [Design a spreadsheet](https://www.careercup.com/question?id=14949056)

### 12/05/2018

1. [Collect maximum points in a grid using two traversals](https://www.geeksforgeeks.org/collect-maximum-points-in-a-grid-using-two-traversals/) (similar: [Cherry Pickup](https://leetcode.com/problems/cherry-pickup/description/))
2. [Largest time for given digits](https://leetcode.com/problems/largest-time-for-given-digits/description/)
3. [Reveal cards in increasing order](https://leetcode.com/problems/reveal-cards-in-increasing-order/description/)
4. [Flip equivalent binary trees](https://leetcode.com/problems/flip-equivalent-binary-trees/description/)
5. [Design an elevator](https://stackoverflow.com/questions/493276/modelling-an-elevator-using-object-oriented-analysis-and-design)
6. Given a sequence of points where consecutive points are connected by line segments to make a path, return the point along the path that corresponds to a given percentage along the path.

### 12/12/2018

1. [Longest file path](2018-12-12/longest_file_path.md)
2. Write the most efficient data structure that stores the last N records of orders to a company that supports two operations: (1) Return the record for the ith last order and (2) add a new record for a new order.
3. [Write a post-order traversal of a binary tree using iteration](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)
4. [Concurrent sum](2018-12-12/concurrent_sum.py)
5. [Force order in concurrency](2018-12-12/force_order_in_concurrency.py) ([Similar](https://www.careercup.com/question?id=4783236498587648))
6. [Select a random number from a stream with O(1) space](https://www.geeksforgeeks.org/select-a-random-number-from-stream-with-o1-space/)
7. Find missing number in an array of N-1 elements where number from 1 to N is missing. ([Similar](https://leetcode.com/problems/missing-number/))
8. CTCI 17.24, Max Submatrix: Given an NxN matrix of positive and negative integers, write code to find the submatrix with the largest possible sum. Variant: submatrix is not necessarily square.

### 12/19/2018

1. [Dependency resolution](https://www.electricmonk.nl/log/2008/08/07/dependency-resolving-algorithm/) (Similar to CTCI 4.7)
2. [CTCI 2.5: Add two numbers stored in linked lists](https://leetcode.com/problems/add-two-numbers/description/)
3. [CTCI 2.3: Delete a node in the middle of a singly linked list, given only access to that node](http://sw-engineers.com/wiki/index.php/Cracking_The_Coding_Interview/Q_2.3)
4. [Regions cut by slashes](https://leetcode.com/problems/regions-cut-by-slashes/)

### 12/26/2018

1. [Generate all binary strings of length n with k bits set](https://stackoverflow.com/questions/1851134/generate-all-binary-strings-of-length-n-with-k-bits-set)
2. [Print all paths from top left to bottom right of an n by m matrix moving only right and down](https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/)
3. [2-sum, 3-sum, 4-sum and variants](https://www.reddit.com/r/dailyprogrammer/comments/6melen/20170710_challenge_323_easy_3sum/)
4. [Encode and decode strings](http://buttercola.blogspot.com/2015/09/leetcode-encode-and-decode-strings.html)

### 01/02/2019

1. CTCI 1.1: Is unique
2. CTCI 1.2: Check permutations
3. CTCI 1.3: URLify
4. CTCI 1.5: One away
5. CTCI 1.6: String compression
6. [All possible full BSTs](https://leetcode.com/problems/all-possible-full-binary-trees/)
7. [Range sum of BST](https://leetcode.com/problems/range-sum-of-bst/)
8. [Find itinerary (variant: return origin city)](https://www.geeksforgeeks.org/find-itinerary-from-a-given-list-of-tickets/)
9. [LRU cache](https://leetcode.com/problems/lru-cache/)
10. CTCI 15.7: Multithreaded FizzBuzz

### 01/09/2019

1. CTCI 4.1: Routes between nodes
2. [Save the Queen!](https://www.hackerrank.com/contests/hourrank-31/challenges/save-the-queen)
3. [Balanced parenthesis](http://interactivepython.org/courselib/static/pythonds/BasicDS/SimpleBalancedParentheses.html)
4. [Combine fruits](https://www.codewars.com/kata/kata-2019-combine-fruits/)
5. [Find and replace in string](https://leetcode.com/problems/find-and-replace-in-string/)
6. [Word break](https://leetcode.com/problems/word-break/description/)
7. [Best time to buy and sell stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

### 01/16/2019

1. [Decode String](https://leetcode.com/problems/decode-string/description/)
2. [Binary parse trees](2019-01-16/binary_parse_trees.md)
3. [Reverse Vowels in a String](https://www.codewars.com/kata/reverse-vowels-in-a-string)
4. [Valid parenthesis string](https://leetcode.com/problems/valid-parenthesis-string/)
5. [Connected Cell in a Grid](https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem)
6. [Longest palindromic substring](https://leetcode.com/problems/longest-palindromic-substring/description/)

### 01/23/2019

1. [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)
2. [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
3. [Almost Sorted](https://www.hackerrank.com/challenges/almost-sorted/problem)
4. [Find Peak Element](https://leetcode.com/problems/find-peak-element/)
5. [CTCI 8.14 Boolean Evaluation](https://stackoverflow.com/questions/47341496/)

### 1/30/2019

1. [Larry's Array](https://www.hackerrank.com/challenges/larrys-array/problem)
2. Given a number `k` and an array of numbers, return an array of the `k` largest elements in the array in any order.
3. [String without AAA or BBB](https://leetcode.com/problems/string-without-aaa-or-bbb/description/)
4. [Shortest palindrome](https://leetcode.com/problems/shortest-palindrome/)

### 2/6/2019

1. Find leftmost `1` in linear time in a matrix of `1` and `0` where each row is sorted ascending (all `0`s are left of the `1`s).
2. [Write `rand5()` using only `rand7()`](https://stackoverflow.com/questions/137783/expand-a-random-range-from-1-5-to-1-7)
3. [House Robber](https://leetcode.com/problems/house-robber/description/)
4. [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
5. [Remove nth node in linked list](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

### 2/13/2019

1. Return deepest node in a binary tree
2. [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/description/)
3. [Roll a string](https://www.geeksforgeeks.org/roll-characters-string/)
4. [Hungry Rabbit in Garden of Carrots](https://medium.com/@internetross/a-particularly-wascally-wabbit-lessons-from-my-annals-of-software-eng-interviews-7fd7574f009b)

### 2/20/2019

1. [Median of binary search tree](https://www.geeksforgeeks.org/find-median-bst-time-o1-space/)
2. Find a path from top left to bottom right of a matrix
3. [Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/description/)
4. [Word Ladder](https://leetcode.com/problems/word-ladder/description/)
5. Sort floating point numbers by decimal portion of the number only
6. [Perfectly Balanced](https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/) (follow-up: with wildcards)

### 2/27/2019

1. [Time complexity of the harmonic series](https://stackoverflow.com/questions/25905118/finding-big-o-of-the-harmonic-series)

### 3/6/2019

1. [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
2. [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/description/)
3. [Array Manipulation](https://www.hackerrank.com/challenges/crush/problem)
4. [Train of Dominoes](https://www.codewars.com/kata/train-of-dominoes)
5. CTCI 16.14 Best Line

### 3/13/2019

1. [CTCI 16.19 Pond Sizes](https://github.com/myyk/cracking-the-coding-interview-6th/blob/master/src/main/java/com/github/myyk/cracking/Chapter16Solutions.java#L1021)
2. [Score bowling](http://codingdojo.org/kata/Bowling/)
3. Split a common address into parts
4. [Name matching](https://www.glassdoor.com/Interview/-Name-Matching-At-Checkr-one-of-the-most-important-aspects-of-our-work-is-accurately-matching-records-to-candi-QTN_2629768.htm)

### 3/20/2019

1. CTCI 16.21 Sum Swap: Given two arrays of integers, find a pair of values (one value from each array) that you can swap to give the two arrays the same sum.
2. Can you hop through an array of numbers from beginning to end? Each `a[i]` is the max potential step size. `[1,2,0,1] => true`, `[2,1,0,1] => false`.
3. [Find a duplicate in an array containing numbers 1..N in O(n) time and O(1) space](https://www.jasondavies.com/duplicates/)
4. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/)
5. Determine if a graph is a tree, and if it isn't, delete edges to make it into one.
6. Magic list: longest consecutive list of words made by changing one letter, given a word list and a start letter.
7. Make a bunch of separate API calls and return the results in an array.

### 3/27/2019

1. [Partition array into three parts with equal sum](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/)
2. [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/description/)
3. Find all anagrams of string `b` in string `a` in O(n) time and O(1) space.
4. [Minimum size subarray sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

### 4/3/2019

1. [Balanced binary tree](https://leetcode.com/problems/balanced-binary-tree/description/)
2. [Invert binary tree](https://leetcode.com/problems/invert-binary-tree/description/)
3. [Longest common prefix](https://leetcode.com/problems/longest-common-prefix/)
4. [Cycle in linked list](https://leetcode.com/problems/linked-list-cycle/)
5. [Desert crossing](https://stackoverflow.com/questions/52023569/bfs-traversing-a-desert-graph-under-certain-rules/)

### 4/10/2019

1. [Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/)
2. [Repair HTML Brackets](https://stackoverflow.com/questions/55602620/repair-html-tag-brackets-using-python/)
3. [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)
4. [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/description/)
5. [Count vowels in all substrings of a string](https://www.geeksforgeeks.org/count-the-number-of-vowels-occurred-in-the-substrings-of-given-string/)
6. [Waffle Choppers](https://codejam.withgoogle.com/2018/challenges/0000000000007883/dashboard)

### 4/17/2019

1. [Egg drop problem](https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/)
2. maximum sum of any subsequence of non-adjacent numbers in array
3. [Binary tree right side view](https://leetcode.com/problems/binary-tree-right-side-view/description/)
4. [Online election](https://leetcode.com/articles/online-election/)

### 4/24/2019

1. [Merge strings with common last and first word](https://stackoverflow.com/questions/55779390/merge-strings-with-common-last-and-first-word)
2. Count primes between 1 and `n` (both exclusive).
3. [Sort array of 0s, 1s and 2s in O(n)](https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/)

### 5/1/2019

1. Code [insertion sort](https://en.wikipedia.org/wiki/Insertion_sort).
2. Design and code <a href="https://en.wikipedia.org/wiki/Minesweeper_(video_game)">Minesweeper</a>.
