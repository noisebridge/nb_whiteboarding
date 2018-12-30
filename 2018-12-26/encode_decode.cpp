/**
 * http://buttercola.blogspot.com/2015/09/leetcode-encode-and-decode-strings.html
*/
#include <iostream>
#include <sstream>
#include <string>
#include <vector>


std::string encode(std::vector<std::string> strs) {
    std::stringstream ss;

    for (auto &s : strs) {
        for (auto &c : s) {
            ss << std::to_string(int(c)) << ',';
        }

        ss << '$';
    }

    return ss.str();
}

std::vector<std::string> decode(std::string s, char delim) {
    std::vector<std::string> strs;
    
    for (int i = 0; i < s.length(); i++) {
        std::stringstream str;

        for (; i < s.length() && s[i] != delim; i++) {
            std::stringstream num;
            
            while (i < s.length() && isdigit(s[i])) {
                num << s[i++];;
            }

            char c;
            sprintf(&c, "%c", stoi(num.str()));
            str << c;
        }

        strs.push_back(str.str());
    }

    return strs;
}

int main() {
    std::vector<std::string> strs = {"abc", "def", "uk,$\"a"};
    std::string encoded_string = encode(strs);

    std::cout << "Encoded: \n\"" << encoded_string << '"' << std::endl << std::endl;
    std::cout << "Decoded:" << std::endl;

    for (auto &s : decode(encoded_string, '$')) {
        std::cout << s << std::endl;
    }

    return 0;
}
