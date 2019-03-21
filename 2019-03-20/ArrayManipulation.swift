

func arrayManipulation(n: Int, queries: [[Int]]) -> Int {
    var arr = Array(repeating: 0, count: n+1)
    for q in queries {
        arr[q[0]-1] += q[2]
        arr[q[1]] -= q[2]
    }

    var maxValue = 0
    var curValue = 0
    for i in 0..<arr.count {
        curValue += arr[i]
        if curValue > maxValue {
            maxValue = curValue
        }
    }

    return maxValue
}

let query = [[1, 5 ,3], [4, 8, 7], [6, 9,1]]
arrayManipulation(n: 9, queries: query)
