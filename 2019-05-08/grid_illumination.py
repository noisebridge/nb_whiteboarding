'''
Jon R. and Greg collaboration

With N of 10^9, the naive approaches of creating a grid of numbers
or iterating over lamps to determine lightedness is intractable. 
The approach we used involves four dict data structures and one set:

- x: col numbers => count of lamps located on the col
- y: row numbers => count of lamps located on the row
- l_d: diagonal index => count of lamps located on the diagonal
- r_d: diagonal index => count of lamps located on the diagonal
- lamps: a set of coordinates for lamps

After building these structures in O(len(lamps)), we answer queries 
in O(1) by indexing into each of the data structures to check 
lightedness. Next, we turn off lamps by iterating over the 9 neighbor 
cells surrounding the query. For each lamp located in one of these 
cells, we delete it from the lamp set and decrement its count from 
each of the four structures, deleting any keys that reach 0, which 
indicates no lights shine on this row/column/diagonal.

The last detail is how diagonals are computed: for the top left to
bottom right diagonal, we can get a unique index by subtracting the 
column from the row location of a lamp. For the bottom left to top 
right diagonal, we can get a unique index by adding the column and 
row for that lamp.
'''

from collections import defaultdict

def grid_illumination(N, lamp_locs, queries):
    res = []
    x = defaultdict(lambda: 0)
    y = defaultdict(lambda: 0)
    l_d = defaultdict(lambda: 0)
    r_d = defaultdict(lambda: 0)
    lamps = set()
    
    for lamp in lamp_locs:
        x[lamp[0]] += 1
        y[lamp[1]] += 1
        l_d[lamp[1]-lamp[0]] += 1
        r_d[lamp[1]+lamp[0]] += 1
        lamps.add(tuple(lamp))
    
    for query in queries:
        if query[1] - query[0] in l_d or sum(query) in r_d or \
           query[0] in x or query[1] in y:
            for row in range(-1, 2):
                for col in range(-1, 2):
                    x_prime = query[0] + col
                    y_prime = query[1] + row
                    
                    if (x_prime, y_prime) in lamps:
                        x[x_prime] -= 1
                        y[y_prime] -= 1
                        l_d[y_prime-x_prime] -= 1
                        r_d[x_prime+y_prime] -= 1
                        lamps.remove((x_prime, y_prime))

                        if x[x_prime] <= 0:
                            del x[x_prime]
                        
                        if y[y_prime] <= 0:
                            del y[y_prime]
                            
                        if l_d[y_prime-x_prime] <= 0:
                            del l_d[y_prime-x_prime]
                            
                        if r_d[x_prime+y_prime] <= 0:
                            del r_d[x_prime+y_prime]
                                                    
            res.append(1)
        else:
            res.append(0)
            
    return res


if __name__ == "__main__":
    print(grid_illumination(5, [[0,0],[4,4]], [[1,1],[1,0]]))
