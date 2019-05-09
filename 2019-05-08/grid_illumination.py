'''
Jon R. and Greg collaboration
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
