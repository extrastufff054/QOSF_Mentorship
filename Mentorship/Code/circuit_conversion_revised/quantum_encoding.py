import pennylane as qml
from pennylane import numpy as np

def encode_character(c):
    """
    Encode a character into a quantum state representation.

    This function takes a single character and converts it to a corresponding
    angle that will be used for rotation in the quantum circuit.

    Args:
        c (str): A single character (e.g., 'A', 'b').

    Returns:
        float: An angle in radians, scaled to fit within the range of a qubit state.
    """
    # Calculate the angle based on the ASCII value of the character
    angle = ord(c) * (2 * np.pi / 256)
    return angle  # Angle will be between 0 and 2π

def decode_character(angle):
    """
    Decode an angle back into a character from its quantum state representation.

    This function converts the angle obtained from the quantum measurement back
    into a character.

    Args:
        angle (float): An angle in radians representing a character's state.

    Returns:
        str: The decoded character or '?' if the angle does not correspond to a valid ASCII character.
    """
    # Convert the angle back to a character code
    char_code = int(np.round(angle * (256 / (2 * np.pi))))
    return chr(char_code) if 0 <= char_code < 256 else '?'  # Ensure character is in valid range

def create_embedding_circuit(word):
    """
    Create a quantum circuit that encodes a word into qubit states.

    This function sets up a quantum circuit with one qubit for each character in the input word.
    Each character is encoded by applying an RY rotation to its corresponding qubit.

    Args:
        word (str): The input word to be encoded, consisting of characters.

    Returns:
        Callable: A quantum circuit that, when called, will return the expectation values 
        of each qubit's state after encoding the input word.
    """
    # Determine the number of qubits needed (one for each character)
    n_qubits = len(word)
    
    # Initialize a quantum device with 'n_qubits' number of qubits
    dev = qml.device("default.qubit", wires=n_qubits)

    @qml.qnode(dev)  # Define a quantum node for executing the circuit
    def circuit():
        # Iterate over each character in the word
        for i, char in enumerate(word):
            angle = encode_character(char)  # Get the angle for the character
            qml.RY(angle, wires=i)  # Apply the rotation to the corresponding qubit
        # Return the expectation values of the Pauli-Z observable for each qubit
        return [qml.expval(qml.PauliZ(wires=i)) for i in range(n_qubits)]

    return circuit  # Return the defined quantum circuit


def embed_word(word):
    """
    Encode a word into a quantum circuit and then decode it back to retrieve the original word.

    This function integrates the entire workflow: encoding the word into qubit states using
    a quantum circuit, measuring the qubits, and then decoding the resulting states back
    into characters.

    Args:
        word (str): The input word to be encoded.

    Returns:
        str: The retrieved word after encoding and decoding process.
    """
    embedding_circuit = create_embedding_circuit(word)  # Create the embedding circuit
    measured_states = embedding_circuit()  # Execute the circuit to get measured states

    # Decode the measured states back into a word
    decoded_word = ''.join(
        decode_character(np.arccos(measured_states[i])) for i in range(len(measured_states))
    )
    
    return decoded_word  # Return the reconstructed word


word = "Bat"  # Input word to encode
retrieved_word = embed_word(word)  # Encode and decode the word
print(f"Original word: {word}")  # Display the original word
print(f"Retrieved word: {retrieved_word}")  # Display the reconstructed word
