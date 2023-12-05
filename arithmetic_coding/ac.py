from arithmetic_compressor import AECompressor
from arithmetic_compressor.models import StaticModel






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
    return (low + high) / 2

def find_symbol(value, cumulative_probabilities):
    for symbol, (low, high) in cumulative_probabilities.items():
        if low <= value < high:
            return symbol
    # In case of rounding issues, return the last symbol
    return list(cumulative_probabilities.keys())[-1]

def decode(encoded_value, length, cumulative_probabilities):
    message = ""
    low, high = 0.0, 1.0
    for _ in range(length):
        symbol = find_symbol(encoded_value, cumulative_probabilities)
        message += symbol
        low, high = calculate_interval(symbol, low, high, cumulative_probabilities)
        encoded_value = (encoded_value - low) / (high - low)
    return message


def test_ac_coding(message,probabilities):
    cumulative_probabilities = calculate_cumulative_probabilities(probabilities)
    encoded_value = encode(message, cumulative_probabilities)
    decoded_message = decode(encoded_value, len(message), cumulative_probabilities)
    
    assert message == decoded_message, "Decoded message is not the same as the original message"


def test_ac_compressor(message,probabilities):
    model = StaticModel(probabilities)
    compressor = AECompressor(model)
    encoded_message = compressor.compress(message)
    decoded_message = compressor.decompress(encoded_message)
    
    assert message == decoded_message, "Decoded message is not the same as the original message when using ac compressor package" 
  
    if __name__ == "__main__":
    
        probabilities = {"A": 0.7, 
                        "B": 0.2, 
                        "C": 0.1}
        
        message = "ABB"
        
        test_ac_coding(message,probabilities)
        