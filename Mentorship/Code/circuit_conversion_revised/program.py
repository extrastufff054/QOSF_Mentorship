import pennylane as qml
from pennylane import numpy as np

def char_to_angle(c):
    return ord(c) * (2 * np.pi / 256)  # Use a larger range for the angles

def angle_to_char(angle):
    return chr(int(np.round(angle * (256 / (2 * np.pi)))))  # Use a larger range for the characters

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
                qml.RX(np.pi / 2, wires=i)  # Apply an additional RX gate
            
            # Measure the chosen Pauli operator
            return [qml.expval(measurement(wires=i)) for i in range(n_qubits)]
        
        return circuit

    return quantum_embedding_circuit

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