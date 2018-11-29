# 17.18 Shortest Supersequence:
#
# You are given two arrays, one shorter (with all distinct elements) and one
# longer. Find the shortest subarray in the longer array that contains all the elements in the shorter
# array. The items can appear in any order.
#
# EXAMPLE
# Input: {1, 5, 9} | {7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7}
#                                          ^^^^^^^^^^
# Output: [7, 10] (the underlined portion above)

def shortest_supersequence shorter, longer
  lo = hi = unique_count = 0
  counts = Hash[shorter.map {|i| [i, 0]}]
  best = [0, Float::INFINITY]
  
  while hi < longer.size do
    while hi < longer.size && unique_count < counts.size
      if counts.include? longer[hi]
        counts[longer[hi]] += 1
        unique_count += 1 if counts[longer[hi]] == 1
      end
      
      hi += 1
    end

    while lo < hi && unique_count == counts.size do
       best = [lo, hi - 1] if hi - 1 - lo < best[1] - best[0]

      if counts.include? longer[lo]
        counts[longer[lo]] -= 1
        unique_count -= 1 if counts[longer[lo]] == 0
      end

      lo += 1
    end
  end

  best
end


[
  [[9], [9,2]],
  [[9], [2,9]],
  [[1], [1]],
  [[1,5,9], [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]],
  [[1,5,9], [1,4,5,6,5,2,4,2,5,9,9,2]]
].each {|shorter, longer| p shortest_supersequence shorter, longer}

3.times do 
  longer = 12.times.map {rand(1..10)}
  shorter = 4.times.map {longer.sample}.uniq
  puts "\nshorter: #{shorter}"
  puts "longer:  #{longer}"
  res = shortest_supersequence(shorter, longer)
  puts "shortest supersequence: #{res}"
end
