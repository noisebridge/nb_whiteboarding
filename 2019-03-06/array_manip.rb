require "set"

def array_manipulation n, queries
  pushes = Hash.new 0
  pops = Hash.new 0
  marks = Set.new
  best = running_total = 0

  queries.each do |a, b, k|
    pushes[a] += k
    pops[b] += k
    marks.add a
    marks.add b
  end

  marks.to_a.sort.each do |mark|
    running_total += pushes[mark]
    best = [best, running_total].max
    running_total -= pops[mark]
  end

  best
end


p array_manipulation 5, [
  [1, 2, 100],
  [2, 5, 100],
  [3, 4, 100],
]

p array_manipulation 10, [
  [1, 5, 3],
  [4, 8, 7],
  [6, 9, 1],
]

p array_manipulation 10, [
  [2, 6, 8],
  [3, 5, 7],
  [1, 8, 1],
  [5, 9, 15]
]

p array_manipulation 40, [
  [29, 40, 787],
  [9 ,26 ,219 ],
  [21, 31, 214],
  [8 ,22 ,719 ],
  [15, 23, 102],
  [11, 24, 83 ],
  [14, 22, 321],
  [5 ,22 ,300 ],
  [11, 30, 832],
  [5 ,25 ,29  ],
  [16, 24, 577],
  [3 ,10 ,905 ],
  [15, 22, 335],
  [29, 35, 254],
  [9 ,20 ,20  ],
  [33, 34, 351],
  [30, 38, 564],
  [11, 31, 969],
  [3 ,32 ,11  ],
  [29, 35, 267],
  [4 ,24 ,531 ],
  [1 ,38 ,892 ],
  [12, 18, 825],
  [25, 32, 99 ],
  [3 ,39 ,107 ],
  [12, 37, 131],
  [3 ,26 ,640 ],
  [8 ,39 ,483 ],
  [8 ,11 ,194 ],
  [12, 37, 502]
]
