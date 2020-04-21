// not available for python so used C++14 language to solve this. used others solution
#include <iostream>
#include <vector>
#include <string>
#include <iterator>

using namespace std;

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
template <typename, typename Cont>
void printArray(const Cont& container) {
    std::copy(std::cbegin(container), std::cend(container),
        std::ostream_iterator<typename Cont::value_type>(
            std::cout, "\n"));
}

int main() {
	int n;
	
	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}
	
	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}