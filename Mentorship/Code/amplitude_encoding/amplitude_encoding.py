# 1. Amplitude Encoding
# Amplitude encoding represents data using the amplitudes of quantum states. It can encode multiple bits of information into a single qubit but requires careful preparation and manipulation of the quantum state.

# Pros:
# Can encode 
# n^2
#   bits of information into 
# 𝑛
# n qubits.
# Cons:
# State preparation can be complex.
# Requires precise amplitude control.

import pennylane as qml
from pennylane import numpy as np

def encode_string_amplitude(word):
    """Encode a string using amplitude encoding."""
    # Convert characters to their ASCII values
    ascii_values = [ord(c) for c in word]
    norm = np.linalg.norm(ascii_values)
    state_vector = np.array(ascii_values) / norm  # Normalize to get state vector

    # Pad to the nearest power of 2
    size = 2**int(np.ceil(np.log2(len(state_vector))))
    state_vector = np.pad(state_vector, (0, size - len(state_vector)), mode='constant')

    n_qubits = int(np.log2(len(state_vector)))
    dev = qml.device("default.qubit", wires=n_qubits)

    @qml.qnode(dev)
    def circuit():
        qml.AmplitudeEmbedding(state_vector, wires=range(n_qubits), normalize=True)
        return qml.state()

    return circuit()

def decode_amplitude(state_vector):
    """Decode a state vector to a string."""
    probabilities = np.abs(state_vector)**2
    indices = np.argmax(probabilities, axis=1)
    characters = [chr(int(i)) for i in indices]
    return ''.join(characters)

# Example usage
word = "Cat"
encoded_state = encode_string_amplitude(word)
retrieved_word = decode_amplitude(encoded_state)
print(f"Original word: {word}")
print(f"Retrieved word: {retrieved_word}")
