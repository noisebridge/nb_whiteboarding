# 1. In a given array of length n, find max(A[j] – A[i]) such that i < j.
# 
# 2. A person can create a flower bouquet with either 3 roses (cost of bouquet = p) or 1 rose and 1 lily (cost = q)
# In an array of flowers, the person has to select contiguous set of flowers i.e. 2 or 3 to gain maximum cost.
# 
# Input format: A string of 0(denotes rose) and 1(denotes lily).
# Output : Maximum cost.
# 
# Examples:
# 
# Input: p = 2, q = 3, s = 0001000
# Output: 5
#
# https://www.geeksforgeeks.org/flipkart-internship-interview-on-campus/

def max_profit(s, p, q)
  dp = Array.new(s.size, 0)
  
  (1...s.size).each do |i|
    dp[i] = dp[i-1]

    if ["01", "10"].include? s[i-1..i]
      dp[i] = [dp[i], i - 2 >= 0 ? q + dp[i-2] : q].max
    elsif i > 1 && s[i-2..i] == "000"
      dp[i] = [dp[i], i - 3 >= 0 ? p + dp[i-3] : p].max
    end
  end

  dp[-1]
end


p max_profit "00011000", 2, 3
p max_profit "0001000", 2, 3
p max_profit "000101000010101000", 4, 1
p max_profit "010", 2, 3
p max_profit "100", 2, 3
p max_profit "001", 2, 3
p max_profit "000", 2, 3
p max_profit "0", 2, 3
