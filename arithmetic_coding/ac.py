import math 
import binascii
def calculate_cumulative_probabilities(probabilities):
    cumulative_probabilities = {}
    cumulative = 0.0
    for symbol, prob in probabilities.items():
        cumulative_probabilities[symbol] = (cumulative, cumulative + prob)
        cumulative += prob
    return cumulative_probabilities

def calculate_interval(symbol, low, high, cumulative_probabilities):
    range = high - low
    symbol_low, symbol_high = cumulative_probabilities[symbol]
    new_high = low + range * symbol_high
    new_low = low + range * symbol_low
    return new_low, new_high

def encode(message, cumulative_probabilities):
    low, high = 0.0, 1.0
    for symbol in message:
        low, high = calculate_interval(symbol, low, high, cumulative_probabilities)
    return low, high

def decode(encoded_value, length, cumulative_probabilities):
    message = ""
    low, high = 0.0, 1.0
    for _ in range(length):
        for symbol, (symbol_low, symbol_high) in cumulative_probabilities.items():
            new_low, new_high = calculate_interval(symbol, low, high, cumulative_probabilities)
            if new_low <= encoded_value < new_high:
                message += symbol
                low, high = new_low, new_high
                break
    return message

def calc_msg_size_in_bits(message:str):
    binary_msg = "".join(map(bin,bytearray(message,'utf8')))
    return len(binary_msg) - 2 

def test_arithmetic_coding(messages, probabilities):
    cumulative_probabilities = calculate_cumulative_probabilities(probabilities)
    
    for message in messages:
        encoded_low, encoded_high = encode(message, cumulative_probabilities)
        decoded_message = decode((encoded_low + encoded_high) / 2, len(message), cumulative_probabilities)

        assert message == decoded_message, f"Test failed for message: '{message}'. Expected: '{message}', got: '{decoded_message}'"
        print(f"Test passed for message: '{message}'. Encoded: {encoded_low}, {encoded_high}")

def test_compression_efficiency(message, probabilities):
    cumulative_probabilities = calculate_cumulative_probabilities(probabilities)
    encoded_low, encoded_high = encode(message, cumulative_probabilities)
    decoded_message = decode((encoded_low + encoded_high) / 2, len(message), cumulative_probabilities)
    
    original_size = calc_msg_size_in_bits(message)
    
    compressed_size = calc_msg_size_in_bits(str(encoded_low)) + calc_msg_size_in_bits(str(encoded_high))

    assert message == decoded_message, f"Decoding failed for message: '{message}'"
    return compressed_size, original_size

def get_symbol_propability_of_msg(message):
    
    symbol_propability_of_msg = {}
    for symbol in message:
        if symbol not in symbol_propability_of_msg:
            symbol_propability_of_msg[symbol] = 1
        else:
            symbol_propability_of_msg[symbol] += 1
    
    for symbol in symbol_propability_of_msg:
        symbol_propability_of_msg[symbol] = symbol_propability_of_msg[symbol] / len(message)
    
    return symbol_propability_of_msg

def time_fct_runtime(fct, *args):
    import time
    start = time.time()
    fct(*args)
    end = time.time()
    return end - start
    
    
    
if __name__ == "__main__":
    
    TESTMESSAGES = ["A", "B", "C","ARBITRARYMESSAGE", ]

    
    for message in TESTMESSAGES:
        
        symbol_propability_of_msg = get_symbol_propability_of_msg(message)
        
        compression_Time = time_fct_runtime(test_compression_efficiency, message, symbol_propability_of_msg)
        len_compressed_msg, len_original_msg = test_compression_efficiency(message, symbol_propability_of_msg)
        
        print(f"msg = '{message}' \ncompr-time = {compression_Time*1000}ms\nlen-msg = {len_original_msg} bits \nlen-compr-msg = {len_compressed_msg} bits\n")
        
        
        
        
    print(calc_msg_size_in_bits("B"))