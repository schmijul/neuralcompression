#include "Huffman.h"

// Constructor for the Node structure
Node::Node(char symbol, unsigned frequency) 
    : symbol(symbol), frequency(frequency), left(nullptr), right(nullptr) {}

// Comparator function for the priority queue
bool Compare::operator()(Node* left, Node* right) {
    return left->frequency > right->frequency;
}

// Function to encode the symbols with their Huffman codes
void encode(Node* root, std::string str, std::unordered_map<char, std::string> &huffmanCode) {
    if (root == nullptr)
        return;

    if (root->symbol != '\0') {
        huffmanCode[root->symbol] = str;
    }

    encode(root->left, str + "0", huffmanCode);
    encode(root->right, str + "1", huffmanCode);
}




// Function to decode the encoded string
void decode(Node* root, int &index, std::string str) {
    if (root == nullptr) {
        return;
    }

    // Found a leaf node
    if (root->left == nullptr && root->right == nullptr) {
        std::cout << root->symbol;
        return;
    }

    index++;

    if (index < str.length()) {
        if (str[index] == '0') {
            decode(root->left, index, str);
        } else {
            decode(root->right, index, str);
        }
    }
}

// Function to build the Huffman tree and encode the data
void buildHuffmanTree(std::string text) {
    // Count the frequency of each character in the input string
    std::unordered_map<char, unsigned> freq;
    for (char ch : text) {
        freq[ch]++;
    }

    // Create a priority queue to store live nodes of the Huffman tree
    std::priority_queue<Node*, std::vector<Node*>, Compare> pq;

    // Create a leaf node for each character and add it to the priority queue
    for (auto pair : freq) {
        pq.push(new Node(pair.first, pair.second));
    }

    // Iterate until there is more than one node in the queue
    while (pq.size() != 1) {
        // Remove the two nodes of highest priority (lowest frequency) from the queue
        Node *left = pq.top(); pq.pop();
        Node *right = pq.top(); pq.pop();

        // Create a new internal node with these two nodes as children and with frequency equal to the sum of the two nodes' frequencies. Add the new node to the priority queue
        Node *sum = new Node('\0', left->frequency + right->frequency);
        sum->left = left;
        sum->right = right;
        pq.push(sum);
    }

    // The remaining node is the root of the Huffman tree
    Node* root = pq.top();

    // Traverse the Huffman tree and store the Huffman codes in a map
    std::unordered_map<char, std::string> huffmanCode;
    encode(root, "", huffmanCode);

    std::cout << "Huffman Codes are:\n";
    for (auto pair : huffmanCode) {
        std::cout << pair.first << " " << pair.second << "\n";
    }

    std::cout << "\nOriginal string was:\n" << text << "\n";

    // Encode the input string into a binary string according to the Huffman codes
    std::string str = "";
    for (char ch : text) {
        str += huffmanCode[ch];
    }

    std::cout << "\nEncoded string is:\n" << str << "\n";

    // Decode the binary string back into the original string
    int index = -1;
    std::cout << "\nDecoded string is: \n";
    // print empty line
    std::cout << "   ";
    while (index < (int)str.size() - 2) {
        decode(root, index, str);
    }
}