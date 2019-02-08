# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

def largest_rectangle_area heights
  start_idx = []
  height = []
  best = 0

  heights.each_with_index do |e, i|
    if height.empty? || height[-1] < e
      height << e
      start_idx << i
    elsif height[-1] > e
      while !height.empty? && height[-1] > e
        best = [height.pop * (i - start_idx[-1]), best].max
        last_popped = start_idx.pop
      end
      
      if height[-1] != e
        height << e
        start_idx << last_popped
      end
    end
  end

  while !height.empty?
    best = [height.pop * (heights.size - start_idx.pop), best].max
  end

  best
end

def largest_rectangle_area_with_location heights
  start_idx = []
  height = []
  best = 0
  best_location = [0, 0, 0]

  heights.each_with_index do |e, i|
    if height.empty? || height[-1] < e
      height << e
      start_idx << i
    elsif height[-1] > e
      while !height.empty? && height[-1] > e
        y = height.pop
        x = start_idx[-1]
        size = y * (i - x)

        if size > best
          best = size
          best_location = [x, y, i - x]
        end  

        last_popped = start_idx.pop
      end
      
      if height[-1] != e
        height << e
        start_idx << last_popped
      end
    end
  end

  while !height.empty?
    y = height.pop
    x = start_idx.pop
    size = y * (heights.size - x)

    if size > best
      best = size
      best_location = [x, y, heights.size - x]
    end  
  end

  best_location
end


heights = (rand(20) + 1).times.map {|e| rand(10)}
hist = heights.max.times.map {|e| []}

hist.size.times do |i|
  heights.each {|h| hist[i] << (h > i ? "@" : ".")}
end

x, y, w = largest_rectangle_area_with_location heights

y.times do |i|
  w.times {|j| hist[i][x+j] = "%"}
end

puts "\n +#{"-" * (heights.size * 2 - 1)}+\n"
hist.reverse.each {|row| puts " |#{row.join " "}|"}
puts " +#{"-" * (heights.size * 2 - 1)}+\n\n [#{heights.join ","}]"
puts " largest rect area: #{largest_rectangle_area heights}\n\n"
