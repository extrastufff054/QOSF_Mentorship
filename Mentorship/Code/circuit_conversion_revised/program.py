import pennylane as qml
from pennylane import numpy as np

def encode_character(c):
    """Encode a character into a quantum state."""
    angle = ord(c) * (2 * np.pi / 256)
    return angle

def decode_character(angle):
    """Decode a quantum state angle into a character."""
    char_code = int(np.round(angle * (256 / (2 * np.pi))))
    return chr(char_code) if 0 <= char_code < 256 else '?'  # Handle out-of-range

def create_embedding_circuit(word):
    """Create a quantum circuit that encodes a word."""
    n_qubits = len(word)
    dev = qml.device("default.qubit", wires=n_qubits)

    @qml.qnode(dev)
    def circuit():
        for i, char in enumerate(word):
            angle = encode_character(char)
            qml.RY(angle, wires=i)
        return [qml.state() for _ in range(n_qubits)]

    return circuit

def embed_word(word):
    """Encode a word into a quantum circuit and then decode it."""
    embedding_circuit = create_embedding_circuit(word)
    measured_states = embedding_circuit()
    
    decoded_word = ''.join(
        decode_character(np.angle(measured_states[i][1]) if np.abs(measured_states[i][1]) > 0 else np.angle(measured_states[i][0]))
        for i in range(len(measured_states))
    )
    
    return decoded_word

# Example usage
word = "Hello"
retrieved_word = embed_word(word)
print(f"Original word: {word}")
print(f"Retrieved word: {retrieved_word}")
