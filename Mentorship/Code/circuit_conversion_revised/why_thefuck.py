import pennylane as qml
from pennylane import numpy as np

# Function to convert a character to its ASCII value and then to a quantum angle
def char_to_angle(c):
    return ord(c) * (2 * np.pi / 128)

# Function to convert a quantum angle back to a character
def angle_to_char(angle):
    return chr(int(np.round(angle * (128 / (2 * np.pi))) % 128))

# Function to encode a word into a quantum circuit
def embed_word(word):
    n_qubits = len(word)
    dev = qml.device("default.qubit", wires=n_qubits)

    @qml.qnode(dev)
    def quantum_embedding():
        # Encode each character into a qubit
        for i, char in enumerate(word):
            angle = char_to_angle(char)
            qml.RY(angle, wires=i)
        
        return qml.state()

    # Execute the quantum circuit and measure the state
    state = quantum_embedding()
    
    # Decode the measured values back to characters
    angles = np.angle(state[np.where(state != 0)])
    decoded_word = ''.join([angle_to_char(angle) for angle in angles[:n_qubits]])

    return decoded_word

# Example usage
word = "Hello"
retrieved_word = embed_word(word)
print(f"Original word: {word}")
print(f"Retrieved word: {retrieved_word}")
