# O(2^n) top-down
def fib n
  n < 2 ? n : fib(n - 1) + fib(n - 2)
end  

# O(n) top-down DP
@memo = {}
def fib n
  return n if n < 2
  @memo[n] = fib(n - 1) + fib(n - 2) if !@memo.include? n
  @memo[n]
end

# O(n) bottom-up DP
def fib n
  a, b = 0, 1
  n.times {b, a = a + b, b}
  a
end


35.times {|i| puts "fib #{i}:\t#{fib i}"}
