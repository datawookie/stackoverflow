#include <iostream>
#include <cstdlib>

// This has a memory leak!

int main() {
    int *ptr = new int; // Allocate memory without deallocating it.
    *ptr = 10;
    std::cout << "Value: " << *ptr << std::endl;
    // delete ptr; // Uncomment this line to fix the memory leak
    return 0;
}
