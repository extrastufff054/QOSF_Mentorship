# Quantum Open Source Foundation Mentorship Program

### Task :
* Write a code to embed word into a quantum circuit. The code needs to be read a word, write the circuit and you should measure to retrieve the word.

### Pre-requisites :

To run this program, you should have the following pre-requisites:

1. **PennyLane Library**:
   - Install the PennyLane library, which is a cross-platform Python library for differentiable programming of quantum computers. You can install it using pip:
     ```bash
     pip install pennylane
     ```Encoded word: cab -> 010000001
Retrieved word: 
Encoded word: a -> 000
Retrieved word: 
Encoded word: b -> 001
Retrieved word: 
Encoded word: c -> 010
Retrieved word: 
Encoded word: d -> 011
Retrieved word: 

2. **Python**:
   - Ensure you have Python installed on your system. PennyLane supports Python 3.7 and above.

3. **Numpy**:
   - PennyLane uses NumPy for numerical computations. If you don't have NumPy installed, you can install it using pip:
     ```bash
     pip install numpy
     ```

4. **Quantum Circuit Definition**:
   - Define a quantum circuit using PennyLane's `@qml.qnode` decorator. This circuit should include the necessary quantum operations (gates) to perform the desired quantum computation.

5. **Device Definition**:
   - Define a device using PennyLane's `qml.device` function. This device should be a simulator or a hardware device that can execute the quantum circuit.

6. **Quantum Circuit Execution**:
   - Execute the quantum circuit using the defined device. This will generate the probabilities of the qubits being in different states.

7. **Decoding**:
   - Decode the probabilities to retrieve the original word by processing every three bits and converting them back to their original form.

8. **Print Results**:
   - Print the encoded word and the retrieved word to compare the original and encoded words.

These pre-requisites ensure that you have the necessary tools and libraries to run the program and perform quantum computations using PennyLane.

Citations:

1.  https://arxiv.org/html/2403.02512v
 2. https://docs.pennylane.ai/en/stable/introduction/circuits.ht
 3. https://www.youtube.com/watch?v=MCDHAn-Gv
 4. https://pennylane.ai/blog/2021/10/how-to-start-learning-quantum-machine-learnin
 5. https://pennylane.ai/qm

### The key steps involved in developing this program are:

1. **Importing Libraries**:
   - Import the necessary libraries, including `pennylane` and `numpy`, to create a quantum circuit and execute it.
   ```
    pip install pennylane 
    pip install numpy
    ```

2. **Defining the Word**:
   - Define the word to be encoded, which is a string of three-bit binary sequences.

3. **Creating the Quantum Circuit**:
   - Create a quantum circuit using `qml.device` and `@qml.qnode` to define the quantum operations to be performed.

4. **Defining the Quantum Circuit Function**:
   - Define a function `circuit` that takes the word as input and applies the necessary quantum gates based on the three-bit sequences.

5. **Executing the Circuit**:
   - Execute the circuit using `circuit(word)` to get the probabilities of the qubits being in different states.

6. **Decoding the Probabilities**:
   - Decode the probabilities to retrieve the original word by processing every three bits and converting them back to their original form.

7. **Printing the Results**:
   - Print the encoded word and the retrieved word to compare the original and encoded words.

  These steps demonstrate how to create a quantum circuit to encode and decode a word using different quantum gates.

