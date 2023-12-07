import heapq
import unittest
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(text):
    return Counter(text)

def build_huffman_tree(freq_table):
    heap = [Node(char, freq) for char, freq in freq_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def encode(text, codebook):
    return ''.join(codebook[char] for char in text)

def decode(encoded_text, root):
    decoded = []
    current = root
    for bit in encoded_text:
        current = current.left if bit == '0' else current.right
        if current.char is not None:
            decoded.append(current.char)
            current = root
    return ''.join(decoded)

def test_huffman_coding():
    text = "example text for Huffman encoding"
    freq_table = build_frequency_table(text)
    root = build_huffman_tree(freq_table)
    codebook = generate_codes(root)
    encoded_text = encode(text, codebook)
    decoded_text = decode(encoded_text, root)

    assert decoded_text == text, "Decoded text does not match original"

if __name__ == "__main__":
    test_huffman_coding()
