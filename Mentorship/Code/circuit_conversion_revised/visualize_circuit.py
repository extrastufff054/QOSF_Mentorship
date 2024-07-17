from quantum_encoding import create_embedding_circuit
import pennylane as qml

word = "Bat"
embedding_circuit = create_embedding_circuit(word)
qml.draw(embedding_circuit)()