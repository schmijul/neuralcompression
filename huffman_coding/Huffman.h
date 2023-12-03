#ifndef HUFFMAN_H
#define HUFFMAN_H

#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
#include <string>

struct Node {
    char symbol;
    unsigned frequency;
    Node *left, *right;

    Node(char symbol, unsigned frequency);
};

struct Compare {
    bool operator()(Node* left, Node* right);
};

void encode(Node* root, std::string str, std::unordered_map<char, std::string> &huffmanCode);
void decode(Node* root, int &index, std::string str);
void buildHuffmanTree(std::string text);

#endif
