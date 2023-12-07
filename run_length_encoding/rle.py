def encode_rle(data):
    if not data:
        return ""

    encoded = []
    prev_char = data[0]
    count = 1

    for char in data[1:]:
        if char == prev_char:
            count += 1
        else:
            encoded.append((prev_char, count))
            prev_char = char
            count = 1

    encoded.append((prev_char, count))  # Don't forget the last set of characters
    return encoded

def decode_rle(encoded_data):
    decoded = []

    for char, count in encoded_data:
        decoded.append(char * count)

    return ''.join(decoded)

def test_rle():
    test_data = "AAAABBBCCDAA"
    encoded = encode_rle(test_data)
    decoded = decode_rle(encoded)

    assert test_data == decoded, "RLE encoding/decoding failed"

if __name__ == "__main__":
    test_rle()

