from qiskit import QuantumCircuit, transpile, assemble
from qiskit.providers.aer import Aer
from qiskit.execute import execute
from qiskit.visualization import plot_histogram
from math import pi, sqrt


def oracle(circuit, k, n):
    """
    Implements the oracle for Grover's algorithm.
    The oracle marks the states that represent numbers less than k.
    """
    for i in range(n):
        if i < k:
            circuit.x(i)
    circuit.h(n)
    circuit.mct([i for i in range(n)], n)
    circuit.h(n)
    for i in range(n):
        if i < k:
            circuit.x(i)

def grover_operator(circuit, n):
    """
    Implements the Grover operator for amplification.
    """
    circuit.h(n)
    oracle(circuit, k, n)
    circuit.h(n)
    circuit.z(n)
    oracle(circuit, k, n)
    circuit.h(n)

def less_than_k(k, list_n):
    n = len(list_n)
    # Determine the number of qubits needed
    num_qubits = int(sqrt(n)) + 1
    
    # Create a quantum circuit
    circuit = QuantumCircuit(num_qubits, num_qubits)
    
    # Initialize the circuit
    for i in range(num_qubits - 1):
        circuit.h(i)
    
    # Apply Grover's operator
    for _ in range(int(pi / 4 * sqrt(n))):
        grover_operator(circuit, num_qubits - 1)
    
    # Measure the circuit
    circuit.measure(range(num_qubits - 1), range(num_qubits - 1))
    
    # Execute the circuit on a simulator
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=1024)
    result = job.result()
    counts = result.get_counts(circuit)
    
    # Extract the numbers less than k
    numbers_less_than_k = []
    for state, count in counts.items():
        number = int(state, 2)
        if number < k:
            numbers_less_than_k.append(number)
    
    return numbers_less_than_k

# Example usage
k = 7
list_n = [4, 9, 11, 14, 1, 13, 6, 15]
result = less_than_k(k, list_n)
print(result)
