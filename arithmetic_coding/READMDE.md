# Arithmetic Coding - A Mathematical and Algorithmic Overview

## Introduction

Arithmetic coding is an advanced technique used in data compression. Unlike traditional methods that compress data symbol by symbol, arithmetic coding encodes an entire message into a single number, a fraction between 0 and 1. 

## Mathematical Description

Arithmetic coding operates by narrowing down the range of possible values based on the input symbols and their probabilities. Initially, the range is [0,1). As each symbol is processed, the range is narrowed based on the cumulative probability distribution. The final output is a number within the last range calculated, uniquely identifying the sequence of symbols.



## Algorithm Summary

### Encoding Steps:

1. **Initialization:** Set the initial range as [0,1).
2. **For Each Symbol:**
   - Determine the current symbol's probability range.
   - Narrow the current range based on this interval.
   - Update the range for the next symbol.
3. **Finalization:** After processing all symbols, output the final range as the encoded value.

### Decoding Steps:

1. **Initialization:** Read the encoded value and set the initial range as [0,1).
2. **For Each Symbol:**
   - Determine which symbol's range contains the encoded value.
   - Output this symbol.
   - Narrow the range to that of the output symbol.
   - Repeat until the entire message is decoded.

## Example

message :"ABAA" with symbol probabilities: A=0.7, B=0.3. 

The encoding steps :

1. **Initial Range:** [0,1)
2. **Process 'A':** New range [0, 0.7)
3. **Process 'B':** New range [0.49, 0.7)
4. **Process 'A':** New range [0.49, 0.644)
5. **Process 'A':** Final range [0.49, 0.5978)

The encoded number for "ABAA" can be any number within [0.49, 0.5978), e.g., 0.55.

Decoding :

1. **Initial Range:** [0,1), Encoded Value: 0.55
2. **Determine Symbol for 0.55:**
   - 0.55 falls in the range of 'A' ([0, 0.7)), so output 'A'.
   - Narrow range to [0, 0.7).
3. **Update Encoded Value:**
   - Adjust 0.55 to fit the new range: 0.55.
4. **Determine Next Symbol for 0.55:**
   - 0.55 falls in the range of 'B' ([0.49, 0.7)), so output 'B'.
   - Narrow range to [0.49, 0.7).
5. **Update Encoded Value:**
   - Adjust 0.55 to fit the new range: 0.55.
6. **Determine Next Symbol for 0.55:**
   - 0.55 falls in the range of 'A' ([0.49, 0.644)), so output 'A'.
   - Narrow range to [0.49, 0.644).
7. **Update Encoded Value:**
   - Adjust 0.55 to fit the new range: 0.55.
8. **Determine Next Symbol for 0.55:**
   - 0.55 falls in the range of 'A' ([0.49, 0.5978)), so output 'A'.
   - Final range is [0.49, 0.5978).