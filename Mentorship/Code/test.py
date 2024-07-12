import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

# Encoding dictionary
encoding = {
    'a': '000', 'b': '001', 'c': '010', 'd': '011', 'e': '100', 'f': '101', 'g': '110', 'h': '111',
    'i': '000', 'j': '001', 'k': '010', 'l': '011', 'm': '100', 'n': '101', 'o': '110', 'p': '111',
    'q': '000', 'r': '001', 's': '010', 't': '011', 'u': '100', 'v': '101', 'w': '110', 'x': '111',
    'y': '000', 'z': '001'
}

def encode(input_string):
    output_string = ''
    for char in input_string.lower():
        output_string += encoding.get(char, '000')
    return output_string

# Example usage
word = "cab"
binary_word = encode(word)
print(f"Encoded word: {word} -> {binary_word}")

dev = qml.device("default.qubit", wires=len(binary_word))

@qml.qnode(dev)
def circuit(binary_word):
    for i in range(0, len(binary_word), 3):
        bit_sequence = binary_word[i:i+3]
        value = int(bit_sequence, 2)

        if value == 0:
            qml.PauliX(wires=i)
        elif value == 1:
            qml.PauliX(wires=i)
        elif value == 2:
            qml.PauliY(wires=i)
        elif value == 3:
            qml.PauliZ(wires=i)
        elif value == 4:
            qml.Hadamard(wires=i)
        elif value == 5:
            qml.S(wires=i)
        elif value == 6:
            qml.T(wires=i)
        elif value == 7:
            qml.CZ(wires=(i, (i+1) % len(binary_word)))

    return [qml.probs(wires=i) for i in range(len(binary_word))]

probabilities = circuit(binary_word)

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

retrieved_word = decode_word(probabilities)
print(f"Retrieved word: {retrieved_word}")

# Testing the circuit with different words
words = ["a", "b", "c", "d"]
for word in words:
    binary_word = encode(word)
    print(f"Encoded word: {word} -> {binary_word}")
    probabilities = circuit(binary_word)
    print(f"Retrieved word: {decode_word(probabilities)}")
    
    # Visualize the circuit
    fig = qml.draw(circuit)(binary_word)
    plt.figure(figsize=(12, 4))
    plt.savefig(f"{word}_circuit.png")
    plt.close()