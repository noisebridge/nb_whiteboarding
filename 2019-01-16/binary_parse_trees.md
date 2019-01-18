Consider the following context-free grammar:

X -> X X | w

This grammar says that, starting with a single X,
you can turn an X into two X's (i.e., X -> X X),
or you can turn an X into a word w (i.e., X -> w).
You keep doing this until all the X's are turned into words,
which constitutes a sentence.

For example, starting with a single X, a four-word sentence
can be generated like so:

```
Step 1:     X
Step 2:  X      X     (The X in step 1 was turned into two X's.)
Step 3:  X    X   X   (The right X in step 2 was turned into two X's.)
Step 4:  X   X X  X   (The middle X in step 3 was turned into two X's.)
Step 5:  w1 w2 w3 w4  (All the X's are turned into words.)
```

You can visualize what generated what with a parse tree.
For example, the parse tree for the generation process
just described is as follows:

```
      X
     / \
    /   X
   /   / \
  /   X   \
 /   / \   \
X   X   X   X
|   |   |   |
w1  w2  w3  w4
```

(Note that the parse tree is a binary tree.)

Given a sentence S = (w1 w2 ... wn) with n words,

1. Design an algorithm that gives the number of possible parse trees
for the sentence.
2. Design an algorithm that generates all possible parse trees
for the sentence.
3. (BONUS) Instead of generating all possible parse trees,
generate a single parse tree that is selected uniformly at random
from the set of all possible parse trees for the sentence.
