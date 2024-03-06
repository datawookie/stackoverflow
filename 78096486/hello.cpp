#include <iostream>
#include <filesystem>

int main() {
    // Print "Hello, World!"
    std::cout << "Hello, World!" << std::endl;

    // Example filesystem operations
    std::filesystem::path currentPath = std::filesystem::current_path();
    std::cout << "Current path: " << currentPath << std::endl;
    return 0;
}
