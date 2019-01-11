/**
 * Save the Queen!
 * Problem description: https://www.hackerrank.com/contests/hourrank-31/challenges/save-the-queen/
 * Explanation of my solution: https://www.hackerrank.com/contests/hourrank-31/challenges/save-the-queen/forum/comments/533792
*/

#include <algorithm>
#include <iostream>
#include <vector>

double save_the_queen(int n, std::vector<int> a) {
    unsigned long long total = 0;
    std::sort(a.begin(), a.end());
    
    for (auto &i : a) {
        total += i;
    }
    
    double avg = (double)total / n;
    std::vector<int>::iterator it = std::lower_bound(a.begin(), a.end(), avg);
    
    int j = it - a.begin();
    
    for (; it != a.end(); n--, it++) {
        total -= *it;
    }
    
    double left_avg = (double)total / n;
    
    for (j--; j >= 0 && a[j] > left_avg; j--) {
        n--;
        total -= a[j];
        left_avg = (double)total / n;
    }
    
    return n <= 0 ? avg : left_avg;
}

int main() {
    std::vector<int>troops {1000, 100, 1, 2000, 79, 125};
    std::cout << std::fixed << save_the_queen(3, troops) << std::endl;
    return 0;
}
