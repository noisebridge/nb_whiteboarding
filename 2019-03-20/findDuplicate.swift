
func findDuplicate(_ nums: [Int]) -> Int {
    var slow = nums[0]
    var fast = nums[0]
    repeat {
        slow = nums[slow]
        fast = nums[nums[fast]]
    } while slow != fast
    
    slow = nums[0]
    while slow != fast {
        slow = nums[slow]
        fast = nums[fast]
    }
    
    return slow
}


print("\(findDuplicate([1,4,4,2,4]))")
print("\(findDuplicate([1,3,4,2,2]))")
print("\(findDuplicate([2,2,2,2]))")

