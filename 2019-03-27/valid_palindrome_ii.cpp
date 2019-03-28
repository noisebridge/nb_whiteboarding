#include <array>
#include <iostream>
#include <string>

bool valid_palindrome(std::string s) {
    int half = s.length() / 2;
    int errors = 0;
    
    for (unsigned int i = 0, j = s.length() - 1; i < half; i++, j--) {
        if (s[i] != s[j]) {
            if (errors++) { 
                return false; 
            }
            else if (s[i+1] == s[j] && s[i+2] == s[j-1]) { 
                j++; 
            }
            else { 
                i--; 
            }
        }
    }
    
    return true;
}

int main() {
    std::array<std::string, 6> tests = {
        "racecar", "racecadr", "rdacecar", 
        "radcecddar", "racecard", "raddcecadr"
    };

    for (auto &test : tests) {
        std::cout << valid_palindrome(test) << std::endl;
    }

    return 0;
}
