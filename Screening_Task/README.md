# Task 1 => less than k

Given a positive integer “k” and a list of integer numbers, look for the numbers within the list, that are less than k. Consider an appropriate number of qubits and explain why your proposal is valid for all kinds of numbers in case 


def less_than_k (int:k, list[int] ,list_n):
     “””
k : integer value that is the positive number to compare in list_n,
list_n : integer list that has positive numbers.
Return the numbers that are in list_n and are less than k 
     “””

     # use a framework that works with quantum circuits, qiskit, cirq, pennylane, etc. 

      # consider print your quantum circuit,


### Example:

A = less_than_k (7,[4,9,11,14,1,13,6,15])
print(A)

“4,1,6”

### References:

[1] Deutsch, David, and Richard Jozsa. "Rapid solution of problems by quantum computation." Proceedings of the Royal Society of London. Series A: Mathematical and Physical Sciences 439.1907 (1992): 553-558.
[2] Bernstein, Ethan, and Umesh Vazirani. "Quantum complexity theory." SIAM Journal on computing 26.5 (1997): 1411-1473.
[3] Grover, Lov K. , "A fast quantum mechanical algorithm for database search", Proceedings of the 28th Annual ACM Symposium on the Theory of Computing (1996), arXiv:quant-ph/9605043

# Task 2 => Odd to Even

Design a quantum algorithm that when given numbers of range [1,n) and are odd convert them into even numbers, and they must stay in the same range so they cannot be less than 1 nor greater than n. n = 2^k where k is the number of qubits you are going to use.


### Example:


B = odd_to_even (n = 31,list= [1,2,2,4,5,6,7,11,17,21,22,23] )
print(B)

One possible output is
 
“[2,2,2,4,4,6,8,10,18,20,22,22]”

Exist multiple solutions

### References:

[1] Deutsch, David, and Richard Jozsa. "Rapid solution of problems by quantum computation." Proceedings of the Royal Society of London. Series A: Mathematical and Physical Sciences 439.1907 (1992): 553-558.
[2] Bernstein, Ethan, and Umesh Vazirani. "Quantum complexity theory." SIAM Journal on computing 26.5 (1997): 1411-1473.
[3] Grover, Lov K. , "A fast quantum mechanical algorithm for database search", Proceedings of the 28th Annual ACM Symposium on the Theory of Computing (1996), arXiv:quant-ph/9605043

# Task 3 ZNE


Zero-noise extrapolation (ZNE) is a noise mitigation technique. It works by intentionally scaling the noise of a quantum circuit to then extrapolate the zero-noise limit of an observable of interest. In this task, you will build a simple ZNE function from scratch:

Build a simple noise model with depolarizing noise 
Create different circuits to test your noise models and choose the observable to measure 
Apply the unitary folding method. 
Apply the extrapolation method to get the zero-noise limit. Different extrapolation methods achieve different results, such as Linear, polynomial, and exponential.
Compare mitigated and unmitigated results 
Bonus: Run your ZNE function in real quantum hardware through the IBM Quantum Service

Check the Mitiq documentation for references. You are not allowed to use the functions from Mitiq or any other frameworks where ZNE is already implemented. 



# Task 4 MIS

An independent set is a set of vertices in a graph such that no two of which are connected by an edge. The problem of finding Maximum Independent Sets (MIS) is NP-hard. In this task, you will solve small instances of the MIS with gate and analog-based quantum computing: 

Create 4 graphs with 3, 5, 6, and 7 nodes. You can define the edges as you prefer. 
For each graph, find the MIS using the following methods: 
The Gate-Based QAOA  
The Quantum adiabatic algorithm using analog based quantum computing. You can check the documentation in Pulser and Blockade for references. 
Compared the results 

