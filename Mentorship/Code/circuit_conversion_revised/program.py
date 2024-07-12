import pennylane as qml
from pennylane import numpy as np

# Function to convert a character to its ASCII value and then to a quantum angle
def char_to_angle(c):
    return ord(c) * (2 * np.pi / 128)

# Function to convert a quantum angle back to a character
def angle_to_char(angle):
    return chr(int(np.round(angle * (128 / (2 * np.pi))) % 128))

# Function to create a quantum circuit that encodes a word
def create_embedding_circuit(word):
    n_qubits = len(word)
    dev = qml.device("default.qubit", wires=n_qubits)

    def quantum_embedding_circuit(measurement):
        @qml.qnode(dev)
        def circuit():
            # Encode each character into a qubit
            for i, char in enumerate(word):
                angle = char_to_angle(char)
                qml.RY(angle, wires=i)
            
            # Measure the chosen Pauli operator
            return [qml.expval(measurement(wires=i)) for i in range(n_qubits)]
        
        return circuit

    return quantum_embedding_circuit

# Function to encode a word into a quantum circuit and then decode it
def embed_word(word):
    n_qubits = len(word)
    embedding_circuit = create_embedding_circuit(word)

    # Measure the expectation values of PauliX and PauliY
    x_results = embedding_circuit(qml.PauliX)()
    y_results = embedding_circuit(qml.PauliY)()
    
    # Compute angles from the expectation values
    angles = np.arctan2(y_results, x_results)
    
    # Convert angles back to characters
    decoded_word = ''.join([angle_to_char(angle) for angle in angles])

    return decoded_word

# Example usage
word = "Hello"
retrieved_word = embed_word(word)
print(f"Original word: {word}")
print(f"Retrieved word: {retrieved_word}")
