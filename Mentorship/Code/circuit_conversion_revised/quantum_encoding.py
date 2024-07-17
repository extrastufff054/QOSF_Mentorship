import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

def encode_character(c):
    angle = ord(c) * (2 * np.pi / 256)
    return angle

def decode_character(angle):
    char_code = int(np.round(angle * (256 / (2 * np.pi))))
    return chr(char_code) if 0 <= char_code < 256 else '?'

def create_embedding_circuit(word):
    n_qubits = len(word)
    dev = qml.device("default.qubit", wires=n_qubits)

    @qml.qnode(dev)
    def circuit():
        for i, char in enumerate(word):
            angle = encode_character(char)
            qml.RY(angle, wires=i)
        return [qml.expval(qml.PauliZ(wires=i)) for i in range(n_qubits)]

    return circuit

def embed_word(word):
    embedding_circuit = create_embedding_circuit(word)
    measured_states = embedding_circuit()

    decoded_word = ''.join(
        decode_character(np.arccos(np.clip(measured_states[i], -1, 1))) for i in range(len(measured_states))
    )
    
    return decoded_word, measured_states

word = "Bat"
retrieved_word, measured_states = embed_word(word)
print(f"Original word: {word}")
print(f"Retrieved word: {retrieved_word}")

circuit = create_embedding_circuit(word)
print("Quantum circuit:")
print(qml.draw(circuit)())

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(word)):
    bloch_vector = [np.cos(encode_character(word[i])), np.sin(encode_character(word[i])), 0]
    ax.plot([0, bloch_vector[0]], [0, bloch_vector[1]], [0, bloch_vector[2]], color='b')
    ax.text(bloch_vector[0], bloch_vector[1], bloch_vector[2], f"Qubit {i}")

    arrow = Arrow3D([0, bloch_vector[0]], [0, bloch_vector[1]], [0, bloch_vector[2]], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
    ax.add_artist(arrow)

ax.set_xlim([-1.1, 1.1])
ax.set_ylim([-1.1, 1.1])
ax.set_zlim([-1.1, 1.1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title("Bloch sphere representation of qubit states")
plt.show()
b