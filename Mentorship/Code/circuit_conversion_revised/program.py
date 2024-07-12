import pennylane as qml
from pennylane import numpy as np

def encode_character(c):
    """Encode a character into a quantum state."""
    angle = ord(c) * (2 * np.pi / 256)
    return [np.cos(angle / 2), 1j * np.sin(angle / 2)]

def decode_character(state):
    """Decode a quantum state into a character."""
    angle = 2 * np.arctan2(np.abs(state[1]), np.abs(state[0]))

    # Ensure the angle is within the valid range for a character
    angle = (angle + 2 * np.pi) % (2 * np.pi)
    char_code = int(np.round(angle * (256 / (2 * np.pi))))
    if 0 <= char_code < 256:
        return chr(char_code)
    else:
        return '?'  # Return a placeholder character if the angle is out of range

def create_embedding_circuit(word):
    """Create a quantum circuit that encodes a word."""
    n_qubits = len(word)
    dev = qml.device("default.qubit", wires=n_qubits)

    @qml.qnode(dev)
    def circuit():
        # Encode each character into a qubit
        for i, char in enumerate(word):
            state = encode_character(char)
            qml.QubitStateVector(state, wires=i)

        # Measure the expectation values of the qubits
        return [qml.state() for i in range(n_qubits)]

    return circuit

def embed_word(word):
    """Encode a word into a quantum circuit and then decode it."""
    embedding_circuit = create_embedding_circuit(word)
    measured_states = embedding_circuit()
    decoded_word = ''.join(decode_character(state) for state in measured_states)
    return decoded_word

# Example usage
word = "Hello"
retrieved_word = embed_word(word)
print(f"Original word: {word}")
print(f"Retrieved word: {retrieved_word}")
