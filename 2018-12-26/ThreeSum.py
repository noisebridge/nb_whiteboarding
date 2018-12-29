
#https://leetcode.com/problems/3sum/

# Find all triplets in an array that sum to a target
# O(n^2) runtime, O(1) space method
def threeSum(array, tgt):
    array.sort()
    triplets = []

    for i in range(0,len(array)-3):
        j = i+1
        k = len(array)-1

        if i > 0 and array[i] == array[i-1]: #Prevent duplicates
          continue

        # Minor improvement
        if array[i] > tgt:
            break

        while j < k:
            triplet = array[i] + array[j] + array[k]
            if triplet == tgt:
                triplets.append([array[i], array[j], array[k]])
                j += 1
                k -= 1
            elif triplet < tgt:
                j += 1
            else:
                k -= 1

    return triplets


print(threeSum([-1, 0, 1, 2, -1, -4], 0)) # Expected [[-1, 0, 1], [-1, -1, 2]]

print(threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0],0)) # Expected: [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]

print(threeSum([-2,0,0,2,2],0)) # Expected: [[-2,0,2]]