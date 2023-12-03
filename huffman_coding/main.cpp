#include "Huffman.h"
#include <iostream>

int main() {
    std::string text;

    std::cout << "Enter the string for Huffman encoding: ";
    std::getline(std::cin, text);  // Use getline to read the entire line including spaces

    if (!text.empty()) {
        buildHuffmanTree(text);
    } else {
        std::cout << "No input provided. Exiting program." << std::endl;
    }

    return 0;
}
