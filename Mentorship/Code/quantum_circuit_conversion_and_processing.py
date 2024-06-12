import pennylane as qml
from pennylane import numpy as np

# Example word with three bits per character
word = "cab"  # Example word to encode

# Convert the word into a binary representation
binary_word = ''.join(format(ord(char), '08b') for char in word)

# Create the quantum circuit
dev = qml.device("default.qubit", wires=len(binary_word))
@qml.qnode(dev)
def circuit(binary_word):
    for i in range(0, len(binary_word), 3):  # Iterate over the word in steps of three bits
        bit_sequence = binary_word[i:i+3]
        # Convert the three-bit sequence to an integer between 0 and 7
        value = int(bit_sequence, 2)
        # Use the integer value to determine which gates to apply
        if value == 0:
            qml.PauliX(i)  # Apply X gate for '000'                 # Replace this by loop
        elif value == 1:                                            # Check the value of the bit sequence and apply the corresponding gate - 1 or 0
            qml.PauliX(i)  # Apply X gate for '001'
        elif value == 2:
            qml.PauliY(i)  # Apply Y gate for '010'
        elif value == 3:
            qml.PauliZ(i)  # Apply Z gate for '011'
        elif value == 4:
            qml.Hadamard(i)  # Apply Hadamard gate for '100'
        elif value == 5:
            qml.S(i)  # Apply S gate for '101'
        elif value == 6:
            qml.T(i)  # Apply T gate for '110'
        elif value == 7:
            qml.CZ((i, (i+1)%len(binary_word)))  # Apply CZ gate for '111'

    return [qml.probs(wires=i) for i in range(len(binary_word))]

# Execute the circuit to get probabilities
probabilities = circuit(binary_word)

# Decode the probabilities to retrieve the original word
retrieved_word = ''
for i in range(0, len(binary_word), 3):  # Process every three bits
    bit_sequence = binary_word[i:i+3]
    # Convert the three-bit sequence back to its original form
    qubit_probabilities = [p[1] for p in probabilities[i:i+3]]  # Calculate the probabilities for each qubit
    # Determine the most likely outcome for each qubit
    for qubit_probability in qubit_probabilities:
        if qubit_probability > 0.5:
            bit_sequence += '1'
        else:
            bit_sequence += '0'
    retrieved_word += chr(int(bit_sequence, 2))
    print(f"Bit Sequence: {bit_sequence}, Probabilities: {qubit_probabilities}, Determined Bits: {bit_sequence}")

# Add a new function to decode the word from the output probabilities
def decode_word(probabilities):
    decoded_word = ''
    for i in range(0, len(probabilities), 3):
        qubit_probabilities = [p[1] for p in probabilities[i:i+3]]
        bit_sequence = ''
        for qubit_probability in qubit_probabilities:
            if qubit_probability > 0.5:
                bit_sequence += '1'
            else:
                bit_sequence += '0'
        decoded_word += chr(int(bit_sequence, 2))
    return decoded_word

# Retrieve the original word from the output probabilities
retrieved_word_probabilities = decode_word(probabilities)

print(f"Encoded Word: {word}")
print(f"Retrieved Word: {retrieved_word_probabilities}")
